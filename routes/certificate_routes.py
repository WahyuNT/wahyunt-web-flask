from flask import Blueprint
from controllers.CertificateController import get_certificate

certificate_bp = Blueprint('certificate', __name__, url_prefix='/api/certificate')

certificate_bp.route('/',methods=['GET'])(get_certificate)