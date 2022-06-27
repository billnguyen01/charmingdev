# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)


class MrpWorkOrderSubcontract(models.Model):
    _inherit = 'mrp.workorder'

    bill_of_material = fields.Many2one('mrp.bom', string='Bill Of Material')

    def button_subcontract(self):
        _logger.info('Click subcontract')
