from flask import Flask, render_template, redirect, url_for, request, session
import os


app = Flask(__name__)
app.config["SECRET_KEY"] = "inisecretkey"

@app.route("/question/<username>",methods=['GET','POST'])
def question(username):
	if os.path.exists(os.path.join(f"../ForumDb/DataBase/{username}")):
		session["useSesi"] =  username
		return render_template("Card.html",username=username)
		
	else:
		return 'Data tidak ada'
	
	
@app.route('/hal/<name>') 
def  hal(name) :
	data = session["userSesi"]
	return render_template("Card2.html",name=data)
	
	
	
@app.route("/pros",methods=['GET','POST'])
def inpt():
	#username = request.args.get('username')
	if request.method=="POST":
		name=request.form['name']
		forum=request.form['forum']
		username = session["useSesi"]
		
		ab=open(f"/storage/emulated/0/MYPROJECTNOW/ForumDb/DataBase/{username}/data.txt", "a+")
		ab.write(f"\nnama :{name}\nsomeone said :{forum}\n")
		session["userSesi"] = name
		return redirect(url_for('hal',name=name))
		
	
	else :
		name=request.args.get('name')
		forum=request.args.get('forum')
		return redirect(url_for('hal',name=name))
if __name__ =="__main__":
	app.run(port="5009",debug=True)
	

