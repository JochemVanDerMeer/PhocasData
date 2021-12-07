from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/results.db'
db = SQLAlchemy(app)


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match = db.Column(db.String(120))
    year = db.Column(db.String(120))
    field = db.Column(db.String(120))
    totalTime = db.Column(db.String(120))

    def __repr__(self):
        return f'id: {self.id}, match: {self.match}, year: {self.year}, field: {self.field}, total time: {self.totalTime}'

#when database is empty
@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def main():
  return render_template("index.html")

if __name__ == "__main__":
  app.run()