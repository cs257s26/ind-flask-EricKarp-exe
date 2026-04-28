'''Replace me with your flask app'''

from flask import Flask, abort
from ProductionCode import command_line

app = Flask(__name__)

@app.route("/")
def main_page():
    return "<p> /country_origin/ <p> \n <p> /artist_name/ <p>"

@app.route("/country_origin/<string:origin>")
def web_origin_count(origin: str):
    tbr = command_line.origin_count(origin)

    if tbr != None:
        return tbr
    else:
        abort(500)

@app.route("/artist_name/<string:name_of_creator>")
def web_find_artwork(name_of_creator: str):

    print(name_of_creator)

    tbr = command_line.count_stolen_by_artist(name_of_creator)

    if tbr != None:
        return str(tbr)
    else:
        abort(500)
    

if __name__ == '__main__':
    app.run()