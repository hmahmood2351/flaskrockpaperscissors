from markupsafe import Markup
from application import app, db
from application.models import Winlose
import random
from flask import render_template

@app.route('/home')
def home():
    msg = []
    msg.append("Welcome to the rock paper scissors game.")
    msg.append("View past results: /game/viewresults")
    msg.append("Play the game: /game/'MOVE' ")
    msg.append("Delete an entry in the database: /game/delete.'NUMBER'")
    msg.append("Return the number of matches in the database: /game/count")
    msg.append("Access the index.html file: /home/layout")
    msg.append("Access the squid.html file: /home/squid")
    return Markup("<br>".join(msg))

@app.route('/home/layout')
def homelayout():
    return render_template('layout.html')

@app.route('/home/squid')
def homesquid():
    return render_template('squid.html')

@app.route('/game/viewresults')
def viewresults():
    results = ""
    all_games = Winlose.query.all()
    for i in all_games:
        results = results + str(i.matchid) + " " + str(i.player) + " " + str(i.opponent) + " " + str(i.result) + "<br>"
    return results

@app.route('/game/<move>')
def playgame(move):
    moves = ['ROCK', 'PAPER', 'SCISSORS']
    opponent = random.choice(moves)
    if move not in moves:
        return "Error."
    elif move == 'ROCK':
        if opponent == 'ROCK':
            new_game = Winlose(player=move, opponent=opponent, result='DRAW')
            db.session.add(new_game)
            db.session.commit()
            return "View results to see your latest match."
        elif opponent == 'PAPER':
            new_game = Winlose(player=move, opponent=opponent, result='LOSE')
            db.session.add(new_game)
            db.session.commit()
            return "View results to see your latest match."
        elif opponent == 'SCISSORS':    
            new_game = Winlose(player=move, opponent=opponent, result='WIN')
            db.session.add(new_game)
            db.session.commit()
            return "View results to see your latest match."
    elif move == 'PAPER':
        if opponent == 'ROCK':
            new_game = Winlose(player=move, opponent=opponent, result='WIN')
            db.session.add(new_game)
            db.session.commit()
            return "View results to see your latest match."
        elif opponent == 'PAPER':
            new_game = Winlose(player=move, opponent=opponent, result='DRAW')
            db.session.add(new_game)
            db.session.commit()
            return "View results to see your latest match."
        elif opponent == 'SCISSORS':    
            new_game = Winlose(player=move, opponent=opponent, result='LOSE')
            db.session.add(new_game)
            db.session.commit()
            return "View results to see your latest match."
    elif move == 'SCISSORS':
        if opponent == 'ROCK':
            new_game = Winlose(player=move, opponent=opponent, result='LOSE')
            db.session.add(new_game)
            db.session.commit()
            return "View results to see your latest match."
        elif opponent == 'PAPER':
            new_game = Winlose(player=move, opponent=opponent, result='WIN')
            db.session.add(new_game)
            db.session.commit()
            return "View results to see your latest match."
        elif opponent == 'SCISSORS':    
            new_game = Winlose(player=move, opponent=opponent, result='DRAW')
            db.session.add(new_game)
            db.session.commit()
            return "View results to see your latest match."

@app.route('/game/delete.<int:matchid>')
def deletematch(matchid):
    match = Winlose.query.get(matchid)
    db.session.delete(match)
    db.session.commit()
    return "Deleted match: " + str(matchid)

@app.route('/game/count')
def count():
    nmatches = Winlose.query.count()
    return "There are: " + str(nmatches) + " games within the database."