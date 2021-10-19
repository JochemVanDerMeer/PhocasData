from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/results.db'
db = SQLAlchemy(app)

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match = db.Column(db.String(120))
    team = db.Column(db.String(120))
    time = db.Column(db.String(120))

    def __repr__(self):
        return f'id: {self.id}, match: {self.match}, team: {self.team}, time: {self.time}'

@app.route("/")
def hello():
  return "test"

if __name__ == "__main__":
  app.run()