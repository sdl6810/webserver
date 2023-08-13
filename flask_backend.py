from flask import Flask
from flask import render_template
import random as r
import vlc
from flask import session, request
import time

app = Flask(__name__)
app.secret_key="random nonsense"

songPlaylist = []

#create a boilerplate header and background for overall web application or website
def generateBoilerplate():
    return None

#player is a python-vlc object currently playing the music
def pickNextSong(player):
    if player.getPosition == player.get_length():
        #pick the next song randomly from the songs stored in either the RPi's memory or in an external hard drive attached to the Raspberry Pi

        #Add this song to the playlist AT THE END
        #print each of the elements of the playlist in the ordered list of the recentlyPlayed.html file

        #Refresh this page with the latest song that just finished playing.  Users should see this change if they refresh their browsers

@app.route('/')
def goToWelcomePage():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] = session["count"] + 1
    return render_template("welcomePage.html",session=session)

@app.route('/recently-played/')
def goToRecentSongs():
    return render_template("recentlyPlayed.html",session=session)

@app.route('/request-a-song/')
def songRequest():
    return render_template("songRequests.html",session=session)


# @app.route('/rollTheDice/')
# def rollTheDice():
#     # msg = "The numbers you rolled are the following: "
#     # die = []
#     # for i in range(0,15):
#     #     die.append(r.randint(1,6))
#     #     msg = msg + "2 " + session["die3"] + session["die4"] + session["die5"] + str(die[i])

#     if "count" not in session:
#         session["count"] = 0
#     else:
#         session["count"] = session["count"] + 1

#     if "diceAvg" not in session:
#         session["diceAvg"] = 0

#     if "die1" not in session or "die2" not in session or "die3" not in session or "die4" not in session or "die5" not in session:
#         session["die1"] = 0
#         session["die2"] = 0
#         session["die3"] = 0
#         session["die4"] = 0
#         session["die5"] = 0
#     else:
#         session["die1"] = r.randint(1,6)
#         session["die2"] = r.randint(1,6)
#         session["die3"] = r.randint(1,6)
#         session["die4"] = r.randint(1,6)
#         session["die5"] = r.randint(1,6)

#         session["diceAvg"] = (session["die1"] + session["die2"] + session["die3"] + session["die4"] + session["die5"])/5
        
#     return render_template("diceSimulation.html",session=session)
app.run(host='0.0.0.0', port=5000)