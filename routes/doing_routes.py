from flask import Blueprint
from controllers.DoingController import get_doing

doing_bp = Blueprint('doing', __name__, url_prefix='/api/doings')

doing_bp.route('/',methods=['GET'])(get_doing)