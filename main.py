from flask import Flask, request, redirect, render_template
import cgi
import os



app = Flask(__name__)

app.config['DEBUG'] = True  

@app.route("/")
def index():   
        return render_template('input_form.html', title='Sign-up')
    


@app.route('/', methods=['POST'])
def display_input_form():
    if request.method == 'GET':
        return render_template('input_form.html')
    




@app.route('/validate-input' , methods=['POST'])
def validate_input():
        username = request.form['username']
        password = request.form['password']
        verify_password = request.form['verify']
        email = request.form['email']

        username_error = ''
        password_error = ''
        verify_error = ''
        email_error = ''

        def empty(x):
            if x == '':
                return True
        if empty(username) or len(username) not in range(3, 20) or " " in username:
            username_error = 'please enter a valid username' 
        if not empty(email):
            if "@" not in email or "." not in email or len(email) not in range(3, 20) or " " in email:
                email_error = 'please enter a valid email address'
        if empty(password):
            password_error = 'Must be between 3 and 20 characters'
        elif len(password) not in range(3, 20) or " " in password:
            password_error = 'Must be 3 and 20 characters long with no spaces'
        elif password != verify_error:
            confirmation_error = 'passwords must match'
        if not email_error and not username_error and not password_error and not verify_error:
            return render_template('welcome_greeting.html', username=username)
        else: 
            return render_template('input_form.html',
        username_error=username_error,
        password_error=password_error,
        email_error=email_error,
        username=username,
        password=password, email=email)
    
    











app.run()