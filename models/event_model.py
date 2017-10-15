# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.osv import osv
import logging
_logger = logging.getLogger(__name__)
from openerp.tools.translate import _

#External imports
from random import randint

class EventColor(models.Model):
    _inherit = 'calendar.event'

    def _get_default_status(self):
        agenda_status_obj = self.env['agenda.status']
        status_open = agenda_status_obj.search([('key', '=', 'open')])
        for rec in status_open:
            status_open_id = rec
            continue
        return status_open_id

    agenda_status = fields.Many2one(
        'agenda.status',
        'Agenda status',
        default=_get_default_status
    )
    hex_value = fields.Char(
        string="Hex Value",
        related="agenda_status.color",
        store=False,
        size=7
    )

class AgendaStatus(models.Model):
    _name = 'agenda.status'

    name = fields.Char(
        String='Description'
    )
    key = fields.Char(
        String='Key'
    )
    color = fields.Char(
        string="Color",
        help="Choose your color",
        size=7
    )
