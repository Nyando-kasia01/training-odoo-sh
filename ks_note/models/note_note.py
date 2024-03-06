from datetime import date

from odoo import models, fields, api


class NoteNote(models.Model):
    _name = 'note.note'
    _description = 'Note'

    date = fields.Date(string='Date')
    subject = fields.Many2one('note.subject', string='Subject')
    student = fields.Many2one('note.student', string='Student')
    note = fields.Integer(string='Note')

    @api.onchange('date')
    def _onchange_date(self):
        for note in self:
            note.date = date.today()