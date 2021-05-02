from flask import Flask
from flask import Blueprint, render_template
from user.models import User


second = Blueprint("second", __name__, static_folder="static", template_folder="templates")

@second.route("/signup", methods=['POST'])
def signup():
  return User().signup()
  #return "hello"

@second.route("/test")
def test():
  return "test!!!!!"