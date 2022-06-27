# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)


class MrpWorkOrderSubcontract(models.Model):
    _inherit = 'mrp.workorder'

    def button_subcontract(self):
        _logger.info('Click subcontract')
