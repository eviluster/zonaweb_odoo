# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)


class ZonawebWebsite(http.Controller):

    # NOTA: La ruta '/' NO se define aquí.
    # Al ser un tema con is_homepage=True en website.page,
    # Odoo gestiona automáticamente la homepage al activar el tema.

    @http.route('/licencias', type='http', auth='public', website=True)
    def bidding(self, **kwargs):
        """Página de licitaciones"""
        return request.render('zonaweb_website.bidding_page')

    @http.route('/submit-bidding', type='http', auth='public',
                methods=['POST'], website=True, csrf=True)
    def submit_bidding(self, **kwargs):
        """Procesar formulario de licitación"""
        try:
            estimated_budget = kwargs.get('estimated_budget')
            bidding_request = request.env['zonaweb.bidding.request'].sudo().create({
                'company_name':         kwargs.get('company_name'),
                'contact_name':         kwargs.get('contact_name'),
                'email':                kwargs.get('email'),
                'phone':                kwargs.get('phone'),
                'service_type':         kwargs.get('service_type'),
                'project_description':  kwargs.get('project_description'),
                'estimated_budget':     float(estimated_budget) if estimated_budget else 0.0,
                'estimated_timeline':   kwargs.get('estimated_timeline') or False,
                'company_sector':       kwargs.get('company_sector') or False,
                'specific_requirements': kwargs.get('specific_requirements'),
            })

            try:
                template = request.env.ref(
                    'zonaweb_website.email_template_bidding_confirmation'
                )
                template.sudo().send_mail(bidding_request.id, force_send=True)
            except Exception as mail_error:
                _logger.warning("No se pudo enviar email de confirmación: %s", mail_error)

            return request.render('zonaweb_website.bidding_thankyou', {
                'bidding_id': bidding_request.name,
            })

        except Exception as e:
            _logger.error("Error al procesar solicitud de licitación: %s", str(e))
            return request.render('website.http_error', {
                'error_message': 'Error al procesar tu solicitud. Por favor, inténtalo de nuevo.',
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
            'status':      bidding.state,
            'last_update': bidding.write_date.strftime('%Y-%m-%d %H:%M:%S'),
        }