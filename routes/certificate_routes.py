from flask import Blueprint
from controllers.CertificateController import get_certificate,get_certificate_detail

certificate_bp = Blueprint('certificate', __name__, url_prefix='/api/certificate')

certificate_bp.route('/',methods=['GET'])(get_certificate)
certificate_bp.route('/detail/<slug>',methods=['GET'])(get_certificate_detail)
