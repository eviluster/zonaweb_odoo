# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
import logging

_logger = logging.getLogger(__name__)


class ZonawebWebsite(http.Controller):
    
    @http.route('/', type='http', auth='public', website=True)
    def index(self, **kwargs):
        """Página de inicio"""
        return request.render('zonaweb_website.zonaweb_homepage')
    
    @http.route('/services', type='http', auth='public', website=True)
    def services(self, **kwargs):
        """Página de servicios"""
        return request.render('zonaweb_website.zonaweb_homepage')
    
    @http.route('/portfolio', type='http', auth='public', website=True)
    def portfolio(self, **kwargs):
        """Página de portafolio"""
        return request.render('zonaweb_website.zonaweb_homepage')
    
    @http.route('/about', type='http', auth='public', website=True)
    def about(self, **kwargs):
        """Página sobre nosotros"""
        return request.render('zonaweb_website.zonaweb_homepage')
    
    @http.route('/licencias', type='http', auth='public', website=True)
    def bidding(self, **kwargs):
        """Página de licitaciones"""
        return request.render('zonaweb_website.bidding_page')
    
    @http.route('/submit-bidding', type='http', auth='public', methods=['POST'], website=True, csrf=True)
    def submit_bidding(self, **kwargs):
        """Procesar formulario de licitación"""
        try:
            # Crear registro de solicitud de licitación
            bidding_request = request.env['zonaweb.bidding.request'].sudo().create({
                'company_name': kwargs.get('company_name'),
                'contact_name': kwargs.get('contact_name'),
                'email': kwargs.get('email'),
                'phone': kwargs.get('phone'),
                'service_type': kwargs.get('service_type'),
                'project_description': kwargs.get('project_description'),
                'estimated_budget': kwargs.get('estimated_budget'),
                'estimated_timeline': kwargs.get('estimated_timeline'),
                'company_sector': kwargs.get('company_sector'),
                'specific_requirements': kwargs.get('specific_requirements'),
            })
            
            # Enviar email de confirmación
            template = request.env.ref('zonaweb_website.email_template_bidding_confirmation')
            if template:
                template.sudo().send_mail(bidding_request.id, force_send=True)
            
            # Redirigir a página de agradecimiento
            return request.render('zonaweb_website.bidding_thankyou', {
                'bidding_id': bidding_request.name,
            })
            
        except Exception as e:
            _logger.error("Error al procesar solicitud de licitación: %s", str(e))
            return request.render('website.http_error', {
                'error_message': 'Ha ocurrido un error al procesar tu solicitud. Por favor, inténtalo de nuevo.',
            })
    
    @http.route('/api/bidding-status', type='json', auth='public', methods=['POST'])
    def bidding_status(self, **kwargs):
        """API para verificar estado de licitación"""
        bidding_id = kwargs.get('bidding_id')
        if not bidding_id:
            return {'error': 'Se requiere ID de licitación'}
        
        bidding = request.env['zonaweb.bidding.request'].sudo().search([
            ('name', '=', bidding_id)
        ], limit=1)
        
        if not bidding:
            return {'error': 'Licitación no encontrada'}
        
        return {
            'status': bidding.state,
            'last_update': bidding.write_date.strftime('%Y-%m-%d %H:%M:%S'),
        }