# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    Autor: Brayhan Andres Jaramillo Castaño
#    Correo: brayhanjaramillo@hotmail.com
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

import logging
_logger = logging.getLogger(__name__)
class PurchaseOrderInherit(models.Model):
	_inherit = "purchase.order"

	origin_port = fields.Char(string='Origin Port')
	destination_port = fields.Char(string='Destination Port')
	origin_port_id = fields.Many2one('purchase.port', string='Origin Port')
	destination_port_id = fields.Many2one('purchase.port', string='Destination Port')
	total_volumen = fields.Float(string='Total Volumen(m³)', compute='_compute_volumen_total')
	total_box= fields.Float(string='Total Box', compute='_compute_box_total')
	engrave= fields.Char('Engrave')
	testing= fields.Char('Testing')
	inspection= fields.Char(u'Inspección')
	check_currency =  fields.Boolean('Validar Moneda')



	def _compute_volumen_total(self):
		for purchase in self:
			vol_total = 0
			for line in purchase.order_line:
				if line.product_id:
					vol_total += line.volumen or 0.0
					
			purchase.total_volumen = vol_total


	def _compute_box_total(self):
		for purchase in self:
			box_total = 0
			for line in purchase.order_line:
				if line.product_id:
					box_total += line.box or 0.0
					
		self.total_box = box_total


	@api.model
	def create(self, vals):
		company_id = vals.get('company_id', self.env.user.company_id.id)
		if vals.get('check_currency') == False:
			raise UserError(_("Por Favor Validar la Tasa de Cambio del día."))

		res = super(PurchaseOrderInherit, self).create(vals)

		return res
		
PurchaseOrderInherit()