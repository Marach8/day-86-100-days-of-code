from flask import Flask, redirect, session, request
from replit import db
import os

marach = Flask(__name__, static_url_path='/static')

@marach.route('/')
def home():
  page = ''
  but = open('button.html', 'r')
  button = but.read()
  but.close()
  page += button
  data = """"""
  if db.keys():
    for i, j in db.items():
      a = f'''<hr>
      <p>{i}</p>
      <p>{j['date']}</p>
      <p>{j['text']}</p>
      '''
      data += a
  page += data
  file = open('home.html', 'r')
  page += file.read()
  file.close()
  return page

@marach.route('/login')
def login1():
  page = """
  <form method='post' action='/checklogin'>
  <p>Username <input type='text' name='username'></p>
  <p>Password <input type='password' name='password'></p>
  <button type='submit'>Login</button>
  </form>
  """
  return page

@marach.route('/checklogin', methods=['POST'])
def checklogin1():
  if request.form['username'] == 'Marach' and request.form['password'] == 'MaRaCh':
    return redirect ('/admin')
  else:
    return redirect ('/login')

@marach.route('/admin')
def admin1():
  a = open('admin.html', 'r')
  b = a.read()
  a.close()
  data = """"""
  if db.keys():
    for i, j in db.items():
      a = f'''<hr>
      <p>{i}</p>
      <p>{j['date']}</p>
      <p>{j['text']}</p>
      '''
      data += a
  
  c = open('home.html', 'r')
  d = c.read()
  c.close()
  d += b
  d += data
  return d

@marach.route('/database', methods=['POST'])
def datab():
  db[request.form['title']] = {'date':request.form['date'], 'text': request.form['text']}
  return redirect('/admin')     


marach.run(host='0.0.0.0', port=81)