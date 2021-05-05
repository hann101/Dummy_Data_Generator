from flask import Blueprint
from .models import User
bp = Blueprint('user', __name__, url_prefix='/user')
@bp.route("/")
def nonde():
    return "hello"

@bp.route("/signup", methods=['POST'])
def signup():
  return User().signup()