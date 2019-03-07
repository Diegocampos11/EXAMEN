# -*- coding: utf-8 -*-

from odoo import models, fields, api

class academia_curso(models.Model):
    _name = 'academia.curso'
    identificador = fields.Integer( string = 'Identificador', required=True )
    nivel = fields.Selection( [ ('0','A2'), ('1','B1'), ('2','B2'), ('3','C1') ] )
    profesor = fields.Many2one( 'academia.alumnoprofesor', string='Profesor', ondelete='cascade' )
    alumnos = fields.One2many( 'academia.alumnoprofesor', 'curso', string='Alumnos' )

class academia_alumnoprofesor(models.Model):
    _name = 'academia.alumnoprofesor'
    dni = fields.Char( string = 'DNI', required=True )
    nombre = fields.Char( string = 'Nombre', required=True)
    primerApellido = fields.Char( string = 'Primer apellido', required=True)
    segundoApellido = fields.Char( string = 'Segundo apellido', required=True)
    fechaNacimiento = fields.Date( string='Fecha de nacimiento' )
    profesor = fields.Boolean( string= 'Profesor' )
    curso = fields.Many2one( 'academia.curso', string='Curso', ondelete='cascade' )
    notaSpeaking = fields.Float( string='Nota speaking' )
    notaListening = fields.Float( string='Nota listening' )
    notaReading = fields.Float( string='Nota reading' )
    notaWriting = fields.Float( string='Nota writing' )
    #campo calculado
    notaMedia = fields.Float( string='Nota media', compute='_notaMedia', store=True )

    #@api.depends('notaSpeaking', 'notaListening', 'notaReading', 'notaWriting')
    #def _notaMedia( self ):
    #    for r in self:
    #        r.notaMedia = ( r.notaSpeaking + r.notaListening + r.notaReading + r.notaWriting ) / 4
