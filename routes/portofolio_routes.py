from flask import Blueprint
from controllers.PortofolioController import get_portofolio,get_portofolio_detail,get_portofolio_list

portofolio_bp = Blueprint('portofolio', __name__, url_prefix='/api/portofolio')

portofolio_bp.route('/',methods=['GET'])(get_portofolio)
portofolio_bp.route('/detail/<slug>',methods=['GET'])(get_portofolio_detail)
portofolio_bp.route('/image/list/<oid>', methods=['GET'])(get_portofolio_list)