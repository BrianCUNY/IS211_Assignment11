#! /usr/bin/env python3

#IS211 Assignment 11 - Web Development with Flask Week: (1/2)

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todo = []

@app.route('/')
def index():
	return render_template('index.html', todo=todo)

@app.route('/submit', methods=['POST'])
def submit():
	task = request.form['Task name']
	priority = request.form['Priority']
	email = request.form['Email address']
	if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
		return redirect('/')
	elif not task:
		return redirect('/')
	elif priority == 'Priority level':
		return redirect('/')
	else:
		todo.append((task, priority, email))
	print(todo)
	return redirect('/')
	
@app.route('/clear', methods=['POST'])
def clear():
	del todo[:]
	return redirect('/')
	
	
if __name__ == '__main__':
	app.run()
