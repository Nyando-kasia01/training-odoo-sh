
from odoo import models,fields


class NoteSubject(models.Model):
    _name = 'note.subject'
    _description = 'Note subject'

    name = fields.Char(string='Name')
    teacher = fields.Many2one('res.partner', string='Teacher')