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

class PurchasePort(models.Model):
	_name = "purchase.port"

	name = fields.Char(string='Name Port', required=True)
	code = fields.Integer(string='Code', required=True)

PurchasePort()

class StockPicking(models.Model):

	_inherit = 'stock.picking'


	check_currency =  fields.Boolean('Validar Moneda')

	@api.model
	def create(self, vals):
		
		type_operation_id= vals.get('picking_type_id')

		picking_type_currecy= self.env['stock.picking.type'].search([('id', '=', type_operation_id)]).check_currency

		currency_actual= self.env['res.currency'].search([('name', '=', 'COP')]).rate

		if (vals.get('check_currency') == False) and (picking_type_currecy):
			raise UserError(_("Por Favor Validar la Tasa de Cambio del día. La tasa actual es %s") %(currency_actual))

		res = super(StockPicking, self).create(vals)

		return res
		
StockPicking()

class StockPickingType(models.Model):

	_inherit = 'stock.picking.type'

	check_currency =  fields.Boolean('Validar Moneda')

		
StockPickingType()