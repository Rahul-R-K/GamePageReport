from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def launchpage():
  return render_template('home.html', Welcomemsg='Welcome To Automation World')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
