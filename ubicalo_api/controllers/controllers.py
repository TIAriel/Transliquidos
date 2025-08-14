from odoo import http
from odoo.http import request
from werkzeug.utils import redirect  # Importa la función de werkzeug

class controllersUbicaloApi(http.Controller):
    @http.route('/endpoint/ubicalo', type='http', auth='public', methods=['GET'], csrf=False)
    def ubicalo_response(self, **post):
        data = {
            "Latitud": 21.0832583,
            "Longitud": -101.624985
        }
        url = f"https://www.google.com/maps/search/?api=1&query={data['Latitud']},{data['Longitud']}"
        
        # Redirige directamente a la URL de Google Maps
        return redirect(url)
