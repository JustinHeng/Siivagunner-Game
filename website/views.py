from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import History
from . import db
import pandas as pd

df = pd.read_csv('Siivagunner.csv')
games_list = list(df['Game Name'].drop_duplicates())
jokes_list = list(df['Joke Name'].drop_duplicates())

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    messages = History.query.filter_by(user_id=str(current_user)).delete()
    db.session.commit()
    if request.method == 'POST':
        return redirect(url_for('views.play'))
    return render_template("home.html", user=current_user)

@views.route('/play', methods=['GET', 'POST'])
@login_required
def play():
    messages = History.query.filter_by(user_id=str(current_user))
    video = list(df['Link'])
    gameans = list(df['Game Name'])
    jokeans = list(df['Joke Name'])
    return render_template('play.html', user=current_user, video=video, gameans=gameans, jokeans=jokeans, games_list=games_list, jokes_list=jokes_list, messages=messages)
