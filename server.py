from flask import Flask, redirect, render_template, session, request
from random import randint

app = Flask(__name__)
app.secret_key = 'hushhush'

def takeAction(a, b, loc):
	num = randint(a, b)
	text = "Earned {} golds from the {}!".format(num, loc)
	session['total'] += num
	session['actionList'].insert(0, text)

def addtoListCasino():
	num = randint(-50, 50)
	session['total'] += num
	if (num < 0):
		text = "Entered a casino and lost " + str(abs(num)) + " golds... Ouch.."
	elif (num > 0):
		text = "Entered a casino and gained " + str(abs(num)) + " golds! You lucky duck!"
	else :
		text = "Entered a casino and came out even."
	session['actionList'].insert(0, text)

@app.route('/')
def display():
	if 'total' not in session:
		session['total'] = 0
	if 'actionList' not in session:
		session['actionList'] = []
	return render_template('index.html', total = session['total'], actionList = session['actionList'])

@app.route('/process_money', methods=['POST'])
def decision():
	if request.form['building'] == 'farm': 
		takeAction(10, 20, 'farm')
		print('actionList')
		return redirect('/')
	elif request.form['building'] == 'cave':
		takeAction(5, 10, 'cave')
		print('actionList')
		return redirect('/')
	elif request.form['building'] == 'house':
		takeAction(2, 5, 'house')
		print('actionList')
		return redirect('/')
	elif request.form['building'] == 'casino':
		addtoListCasino()
		print('actionList')
		return redirect('/')


app.run(debug=True)