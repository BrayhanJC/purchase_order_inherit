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

class PurchaseOrderLineInherit(models.Model):
	_inherit = 'purchase.order.line'

	volumen = fields.Float(string='volumen(m³)', compute='_compute_volumen', store=True)
	box = fields.Float(string='Total Box', compute='_compute_box', store=True)

	@api.one
	@api.depends('product_id', 'product_qty')
	def _compute_box(self):

		for line in self:
			total_box = 0
			if line.product_id and line.product_id.master:
				total_box += (line.product_qty/line.product_id.master) or 0
			
		self.box = total_box


	@api.one
	@api.depends('product_id', 'product_qty')
	def _compute_volumen(self):

		for line in self:
			volumen = 0
			if line.product_id and line.product_id.volume:
				volumen += (line.product_id.volume * line.box)
			
		self.volumen = volumen


PurchaseOrderLineInherit()