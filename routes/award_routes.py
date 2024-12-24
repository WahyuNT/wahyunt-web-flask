from flask import Blueprint
from controllers.AwardController import get_award,get_award_detail

award_bp = Blueprint('award', __name__, url_prefix='/api/award')

award_bp.route('/',methods=['GET'])(get_award)
award_bp.route('/detail/<slug>', methods=['GET'])(get_award_detail)