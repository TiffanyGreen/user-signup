from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route ("/")
def index():
    return render_template('input.html')

gl_username= []

@app.route ('/success', methods = ['POST' , 'GET'])
def success():
    username = request.args.get('username')
    return render_template ('welcome.html', username= username)


@app.route ("/error", methods=['POST'])
def user():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']


    username_error = ''
    password_error = ''
    verify_error = ''
    empty_error= ''
    invalid_email_error=''


    if username.strip()=='' or password.strip()=='' or verify.strip()=='':
        empty_error = 'You forgot to tell us information! Try again.'
    
    if (len(username) < 3) or (len(username) > 19) and username.isalpha() == False:
        password_error = 'Your username is too long or too short. Between 3 and 20 characters is best.'

    if (len(password) < 3) or (len(password) > 19) and password.isalpha() == False:
        password_error = 'Your password is too long or too short. Between 3 and 20 characters is best.'

    if password != verify:
        verify_error= 'Oops! Your passwords must match.'
    
    if email != "" and ((len(email) < 2) or (len(email) > 19) or (email.count ("@") > 1) or (email.count("@") <1) or (email.count (".") > 1) or (email.count(".") <1) or (email.count(" ")>=1)):
        invalid_email_error= 'If you want to enter an email, at least give me one that works!'
    
    if (not empty_error) and (not username_error) and (not password_error) and (not verify_error) and (not invalid_email_error):
        gl_username = username
        return redirect ('/success?username={0}'.format(gl_username))

    else:
        return render_template ('input.html', empty_error = empty_error, username = username, username_error = username_error, password_error = password_error, verify_error = verify_error, invalid_email_error = invalid_email_error)

app.run()