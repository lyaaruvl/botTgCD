from flask import Flask, render_template, url_for, request, redirect


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

app = Flask(__name__, template_folder='templates')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///date.db"
db = SQLAlchemy(app)


class Base(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	full_name = db.Column(db.String(100), nullable=False)
	number = db.Column(db.Integer)
	date_r = db.Column(db.Integer)
	uslugi = db.Column(db.String(200), nullable=False)
	vrachi = db.Column(db.String(200))
	date_zapisi = db.Column(db.Integer, unique =True)
	time = db.Column(db.Integer)

	def __repr__(self):
		return '<Base %r>' % self.id


def check():
	u = Base(date_zapisi = 'date_zapisi')
	inspection = inspect(u)
	inspection.pending

	db.session.add(u)
	inspection.pending

	db.session.commit()
	inspection.pending



@app.route("/")
def base():
	return render_template("index.html")



@app.route("/index", methods=["POST", "GET"])
def index():
	if request.method == "POST":
		username = request.form['username']
		number = request.form['number']
		date = request.form['date']
		exampleFormControlSelect1 = request.form['exampleFormControlSelect1']
		exampleFormControlSelect2 = request.form['exampleFormControlSelect2']
		date1 = request.form['date1']
		time = request.form['time']

		base = Base(full_name=username, number=number, date_r=date,uslugi=exampleFormControlSelect1,vrachi=exampleFormControlSelect2,date_zapisi=date1, time=time)

		try:
			db.session.add(base)
			db.session.commit()
			#check()
			success = ""
			return render_template("result.html", success=success)
		except:
			return render_template("result_false.html")
	else:
		return render_template("index.html")



if __name__ == "__main__":
	app.run(debug = True)