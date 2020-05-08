from flask import Blueprint

from .main.controller.service_controller import api as service_bp

# blueprint = Blueprint('api', __name__)
#
# api = Api(blueprint,
#           title='FLASK TEST PROJECT',
#           version='1.0',
#           description='flask web service'
#           )
#
# api.add_namespace(service_ns)
