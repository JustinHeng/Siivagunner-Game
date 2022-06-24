from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
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

# @views.route('/lobby', methods=['GET', 'POST'])
# @login_required
# def lobby():
#     messages = History.query.filter_by(user_id=str(current_user))
#     if request.method == 'POST':
#         messages = History.query.filter_by(user_id=str(current_user)).delete()
#         db.session.commit()
#         return redirect(url_for('views.play'))
#     return render_template("lobby.html", user=current_user, messages=messages)
#
# @views.route('/final-results', methods=['GET', 'POST'])
# @login_required
# def final_results():
#     messages = History.query.filter_by(user_id=str(current_user))
#     if request.method == 'POST':
#         return redirect(url_for('views.lobby'))
#     return render_template("final-results.html", user=current_user, messages=messages)

@views.route('/play', methods=['GET', 'POST'])
@login_required
def play():
    messages = History.query.filter_by(user_id=str(current_user))
    video = list(df['Link'])
    gameans = list(df['Game Name'])
    jokeans = list(df['Joke Name'])
    # # for x in range(3):
    # #     rand = random.randint(0, len(df.index) - 1)
    # #     video.append(df['Link'][rand])
    # #     gameans.append(df['Game Name'][rand])
    # #     jokeans.append(df['Joke Name'][rand])
    #
    # #video = df['Link'][rand]
    # # Display results screen
    # if request.method == 'POST':
    #     if request.form.get('page') == "pr":
    #         last_video = int(request.form.get('video_id'))
    #         gameans = df['Game Name'][last_video]
    #         jokeans = df['Joke Name'][last_video]
    #         game = request.form.get('game')
    #         joke = request.form.get('joke')
    #         if game.lower() == gameans.lower() and joke.lower() == jokeans.lower():
    #             flash("Correct! You get 2 points. Game: " + str(gameans) + " Joke: " + str(jokeans), category='success')
    #             message = History(message=str(current_user.first_name) + " got 2 points!", user_id=str(current_user))
    #             db.session.add(message)
    #             db.session.commit()
    #             score = 2
    #         elif game.lower() != gameans.lower() and joke.lower() != jokeans.lower():
    #             flash("Incorrect! Game: " + str(gameans) + " Joke: " + str(jokeans), category='error')
    #         else:
    #             flash("Partially correct. You get 1 point. Game: " + str(gameans) + " Joke: " + str(jokeans), category='success')
    #             message = History(message=str(current_user.first_name) + " got 1 point.", user_id=str(current_user))
    #             db.session.add(message)
    #             db.session.commit()
    #             score = 1
    #         return render_template('play-results.html', user=current_user, video=df['Link'][last_video], id=rand, games_list=games_list, jokes_list=jokes_list, score=score, messages=messages)

    return render_template('play.html', user=current_user, video=video, gameans=gameans, jokeans=jokeans, games_list=games_list, jokes_list=jokes_list, messages=messages)

# @views.route('/delete-note', methods=['POST'])
# def delete_note():
#     note = json.loads(request.data)
#     noteId = note['noteId']
#     note = Note.query.get(noteId)
#     if note:
#         if note.user_id == current_user.id:
#             db.session.delete(note)
#             db.session.commit()
#     return jsonify({})