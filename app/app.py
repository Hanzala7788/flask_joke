from flask import Flask, render_template
import pyjokes

app = Flask(__name__)

@app.route('/')
def joke():
    joke_text = pyjokes.get_joke()
    return render_template('index.html', joke=joke_text)

@app.route('/multiple_jokes')
def multiple_jokes():
    jokes = pyjokes.get_jokes()
    return render_template('index.html', joke=jokes)

if __name__ == '__main__':
    app.run(debug=True)