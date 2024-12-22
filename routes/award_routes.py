from flask import Blueprint
from controllers.AwardController import get_award

award_bp = Blueprint('award', __name__, url_prefix='/api/award')

award_bp.route('/',methods=['GET'])(get_award)