from flask import Flask, render_template
from game import print_game, BOARD
app = Flask(__name__)



@app.route('/')
def index():
	data = BOARD
	return render_template("index.html", res=data)
	



if __name__ == "__main__":
    app.run(debug=True)