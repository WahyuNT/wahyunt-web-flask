from flask import Blueprint
from controllers.SkillController import get_skill

skill_bp = Blueprint('skill', __name__, url_prefix='/api/skills')

skill_bp.route('/',methods=['GET'])(get_skill)