from flask import Flask, request, redirect, abort
from flask import send_file
import ts3

users = {
	'lantrix': ['VZDUWHRwVQlaAnLc+oum0TnnGR0=', 'wy5YOXZYwc6dpWEr+TdU1Frs4xU=', 'ykR5DGyS9C2ICKrr8MfB5xBVDdg='],
	'ginger': ['uvh9fIQruJDpgScU7zxhmW6biy8='],
	'both': ['uvh9fIQruJDpgScU7zxhmW6biy8=', 'VZDUWHRwVQlaAnLc+oum0TnnGR0=', 'wy5YOXZYwc6dpWEr+TdU1Frs4xU=', 'ykR5DGyS9C2ICKrr8MfB5xBVDdg=']
}

app = Flask(__name__)

@app.route("/")
def hello():
	return ("<!DOCTYPE html>"
			"<style>form{ text-align: center; vertical-align: middle;} input{ padding: 10px; margin: 10px}</style>"
			"<form action=\"/bantrix\" "
			"enctype=\"multipart/form-data\" method=\"post\"><br>"
			"<input type=\"text\" name=\"username\" size=\"40\">"
			"<input type=\"password\" name=\"password\" size=\"40\"><br>"
			"<input type=\"submit\" name=\"action\" value=\"Kick\" size=\"40\">"
			"<input type=\"submit\" name=\"action\" value=\"Ban\" size=\"40\"><br>"
			"<input type=\"radio\" name=\"target\" value=\"lantrix\" checked> Lantrix<br>"
			"<input type=\"radio\" name=\"target\" value=\"ginger\"> Ginger<br>"
			"<input type=\"radio\" name=\"target\" value=\"both\"> Both<br>"
			"</form>")


@app.route("/bantrix", methods=['POST'])
def ts3memes():
	if request.method == "POST":
		ts = ts3.query.TS3Connection("127.0.0.1")
		try:
			ts.login(client_login_name=request.form['username'], client_login_password=request.form['password'])
			ts.use(sid=1)
			ts.clientupdate(client_nickname='Roboi')
		except ts3.query.TS3QueryError as err:
			print("login failed", err)
			return('failed to login')
		except AttribueError as err:
			print('attrerr', err)
			return(err)
	
		for i in users[request.form['target']]:
			try:
				lantrix=ts.clientgetids(cluid=i).parsed
				if request.form['action'] == 'Ban':
					for user in lantrix:
						ts.banclient(clid=user['clid'], time=1, banreason="Everyone hates you not just me")
					return ("BANNED!")
				elif request.form['action'] == 'Kick':
					for user in lantrix:
						ts.clientkick(reasonid=4, reasonmsg="Everyone hates you not just me", clid=user['clid'])
					return ("KICKED!")
			except ts3.query.TS3QueryError as err:
				print('Unreturned statement')
		return("somehow we fucked up or he's offline")

	
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
