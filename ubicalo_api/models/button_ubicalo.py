from odoo import fields, models

class button_ubicalo(models.Model):
    _inherit = 'fleet.vehicle'
    
    def button_ubicalo(self):
        # Esto llamará al endpoint del controlador
        return {
            'type': 'ir.actions.act_url',
            'url': '/endpoint/ubicalo',
            'target': 'new'  # Esto abrirá en una nueva pestaña
        }
