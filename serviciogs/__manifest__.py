{
    'name': 'Servicio Rutas',
    'version': '17.0.0.0',
    'author': 'GSerrano Lagos de Moreno',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        "industry_fsm",
        "sale_management",
        "project",
        "fleet",
        "account",
        "contacts",
        "product",
    ],
    'data': [
        'views/proyecto_ruta.xml',
        'views/servicio_externo_proyecto.xml',
        'views/ruta_view_tree.xml',
        'report/reports.xml',
        'report/ticket_viaje.xml',
        'report/ticket_cliente.xml',
        'report/proceso_lavado.xml',
        'report/cp_vertical.xml',
        'report/inspeccion_trans.xml',
        'report/report_cost.xml'
    ],
}