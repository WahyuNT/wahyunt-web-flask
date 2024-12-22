from flask import Blueprint
from controllers.AboutController import get_about

about_bp = Blueprint('about', __name__, url_prefix='/about')

about_bp.route('/',methods=['GET'])(get_about)