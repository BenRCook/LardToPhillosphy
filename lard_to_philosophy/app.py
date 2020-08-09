from flask import Flask, render_template, make_response

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/hello")
def hello():
    return make_response("Hello World", 200)


if __name__ == "__main__":
    app.run()
