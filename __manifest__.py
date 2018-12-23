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

{
    'name' : 'Purchase Order Inherit',
    'version' : '11',
    'summary': 'Purchase Order',
    'sequence': 10,
    'license':'LGPL-3',
    'description': """
        
        The follow module allow add several products at once on inventory, also calculate the number of boxes per purchase

    """,
    'category': 'Purchase',
    'author' : 'Brayhan Jaramillo',
    'website' : 'brayhanjaramillo@hotmail.com',
    'images': ['static/description/banner.jpg'],
    'depends' : ['sale_management'],
    'data': [
        'views/puerchase_order_inherit_views.xml',
        'views/product_template_inherit_view.xml',
        'views/purchase_port_view.xml',
        'report/purchase_order_templates_inherit.xml',
        'report/sale_order_template_inherit.xml',
        'report/report_stockpicking_operations_inherit.xml',
        'report/report_invoice_inherit.xml'
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
