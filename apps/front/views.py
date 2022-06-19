# front/views.py

from flask import Blueprint, render_template, views

bp = Blueprint("front", __name__)


@bp.route('/')
def index():
    return 'front index'


class SignupView(views.MethodView):
    def get(self):
        return render_template('front/signup.html')


bp.add_url_rule('/signup/', view_func=SignupView.as_view('signup'))
