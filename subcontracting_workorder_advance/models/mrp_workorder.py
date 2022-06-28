# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)


class MrpWorkOrderSubcontract(models.Model):
    _inherit = 'mrp.workorder'

    def button_subcontract(self):
        self.create_po()
        self.create_transfer_go()
        self.create_transfer_arrive()

    def create_po(self):
        _logger.info('create_po')

    def create_transfer_go(self):
        _logger.info('create_po')

    def create_transfer_arrive(self):
        _logger.info('create_po')
