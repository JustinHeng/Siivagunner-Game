from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import pandas as pd
import random

df = pd.read_csv('Siivagunner.csv')
games_list = list(df['Game Name'])
jokes_list = list(df['Joke Name'])

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        return redirect(url_for('views.play'))
    return render_template("home.html", user=current_user)

@views.route('/play', methods=['GET', 'POST'])
@login_required
def play():
    rand = random.randint(0, len(df.index)-1)
    video = df['Link'][rand]
    if request.method == 'POST':
        last_video = int(request.form.get('video_id'))
        gameans = df['Game Name'][last_video]
        jokeans = df['Joke Name'][last_video]
        game = request.form.get('game')
        joke = request.form.get('joke')
        if game.lower() == gameans.lower() and joke.lower() == jokeans.lower():
            flash("Correct! You get 2 points. Game: " + str(gameans) + " Joke: " + str(jokeans), category='success')
        elif game.lower() != gameans.lower() and joke.lower() != jokeans.lower():
            flash("Incorrect! Game: " + str(gameans) + " Joke: " + str(jokeans), category='error')
        else:
            flash("Partially correct. You get 1 point. Game: " + str(gameans) + " Joke: " + str(jokeans), category='success')

        return render_template('play-results.html', user=current_user, video=df['Link'][last_video], id=rand, games_list=games_list,
                               jokes_list=jokes_list)
        # note = request.form.get('note')
        #
        # if len(note) < 1:
        #     flash('Cannot be empty!', category='error')
        # else:
        #     new_note = Note(data=note, user_id=current_user.id)
        #     db.session.add(new_note)
        #     db.session.commit()
        #     flash('Note added!', category='success')
    #return render_template("play.html", user=current_user, video=video, id=rand, games_list=games_list, jokes_list=jokes_list)
    return render_template('play.html', user=current_user, video=video, id=rand, games_list=games_list, jokes_list=jokes_list)

# @views.route('/play-results', methods=['GET', 'POST'])
# @login_required
# def play_results():
#     rand = int(request.form.get('video_id'))
#     video = df['Link'][rand]
#     count = int(request.form.get('count'))
#     return render_template("play.html", user=current_user, video=video, id=rand, games_list=games_list, jokes_list=jokes_list)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})