import flask
import os


app = flask.Flask(__name__)
print("wow this app will ")


@app.route("/")
def hello_world():
    return flask.render_template('index.html')


if __name__ =="__main__":
  app.run(
    host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", "8080")),
)