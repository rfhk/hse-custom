# -*- coding: utf-8 -*-
#    OpenERP, Open Source Management Solution
#    Copyright (c) Rooms For (Hong Kong) Limited T/A OSCG. All Rights Reserved.
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
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from openerp import models, api, _, fields


class SuppPayJournalDefault(models.Model):
    _name = 'supp.pay.journal.default'

    @api.onchange('currency_id')
    def _onchange_currency_id(self):
#         self.supplier_payment_journal_id = self.env['account.journal'].search([('type','=','bank'),('currency','=',self.currency_id.id)], limit=1) or False
        self.journal_id = False

    currency_id = fields.Many2one('res.currency', required=True, string='Currency')
    journal_id = fields.Many2one('account.journal', required=True, string='Supplier Payment Journal')

    _sql_constraints = [
        ('name_currency_uniq', 'unique(currency_id)', 'Currencies must be unique !'),
    ]

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: