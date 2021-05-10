import requests
import json
from datetime import datetime
import PySimpleGUI as ui
import isConnected as conn
""" 
Simple welcome application using REST API, Data-time and PySimpleGUI
"""

def getJoke():
    try:
        url = 'https://v2.jokeapi.dev/joke/Any?blacklistFlags=racist,sexist,explicit'  # URL + params
    except Exception as err:
        print(err)
    if not conn.is_connected(conn.REMOTE_SERVER):
        return "Internet connection not found"
    response = requests.request("GET", url)  # Request joke from Joke REst API
    # print(response.text)   # print response
    dict = json.loads(response.text)  # convert json to dict
    if dict["type"] == "twopart":  # print two part and one part joke separately
        # print(dict["setup"])
        # print(".\n.\n.\n.\n.\n.\n.")
        # print(dict["delivery"])
        return dict["setup"] + ".\n.\n.\n.\n.\n.\n" + dict["delivery"]
    else:
        # print(dict["joke"])
        return dict["joke"]


# getJoke()

# Get date and time
def getDateAndTime():
    """ Get date and time"""
    now = datetime.now()
    # print(now)
    # extract date and time from $now
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%m/%d/%Y")
    return ("Date:{} \nCurrent Time ={}".format(current_date, current_time))

def createAndDisplayUI():
    """ Create a GUI layout and get read events till window is closed"""
    ui.theme('DarkAmber')
    # Layout inside the window

    layout = [[ui.Text("Welcome", size=(60, 3), justification="center", text_color='RED', font=25)],
              [ui.Text(getDateAndTime(), size=(60, 3), justification="center", text_color='GREEN', font=20)],
              [ui.Button(button_text="Get Joke", font=20, tooltip="Get a new Joke", size=(60, 1))],
              [ui.Text("", size=(60, 10), justification="center", key="-JokeText-", font=20)]
              ]
    # Create the window
    window = ui.Window("", layout, margins=(120, 50))
    while True:
        event, values = window.read()
        if event == ui.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        elif event == "Get Joke":
            joke = getJoke()
            window["-JokeText-"].update(joke)

    window.close()

createAndDisplayUI()