# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime


class BiddingRequest(models.Model):
    _name = 'zonaweb.bidding.request'
    _description = 'Solicitud de Licitación Zonaweb'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    name = fields.Char(
        string='Referencia',
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _('Nuevo')
    )
    company_name = fields.Char(
        string='Nombre de la Empresa',
        required=True,
        tracking=True
    )
    contact_name = fields.Char(
        string='Nombre de Contacto',
        required=True,
        tracking=True
    )
    email = fields.Char(
        string='Correo Electrónico',
        required=True,
        tracking=True
    )
    phone = fields.Char(
        string='Teléfono'
    )
    service_type = fields.Selection([
        ('software', 'Desarrollo de Software'),
        ('infrastructure', 'Infraestructura de Redes'),
        ('support', 'Soporte Técnico'),
        ('security', 'Seguridad Informática'),
        ('consulting', 'Consultoría'),
        ('other', 'Otro'),
    ], string='Tipo de Servicio', required=True)
    project_description = fields.Text(
        string='Descripción del Proyecto',
        required=True
    )
    specific_requirements = fields.Text(
        string='Requerimientos Específicos'
    )
    estimated_budget = fields.Float(
        string='Presupuesto Estimado'
    )
    estimated_timeline = fields.Selection([
        ('flexible', 'Flexible'),
        ('normal', 'Normal'),
        ('urgent', 'Urgente'),
    ], string='Cronograma Estimado')
    company_sector = fields.Selection([
        ('retail', 'Retail'),
        ('manufacturing', 'Manufactura'),
        ('services', 'Servicios'),
        ('technology', 'Tecnología'),
        ('healthcare', 'Salud'),
        ('education', 'Educación'),
        ('finance', 'Finanzas'),
        ('other', 'Otro'),
    ], string='Sector de la Empresa')
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmado'),
        ('approved', 'Aprobado'),
        ('rejected', 'Rechazado'),
    ], string='Estado', default='draft', tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('Nuevo')) == _('Nuevo'):
                vals['name'] = self.env['ir.sequence'].next_by_code('zonaweb.bidding.request')
        return super().create(vals_list)

    def action_confirm(self):
        self.write({'state': 'confirmed'})
        return True

    def action_approve(self):
        self.write({'state': 'approved'})
        return True

    def action_reject(self):
        self.write({'state': 'rejected'})
        return True