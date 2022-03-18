from flask import Flask, render_template, url_for, flash, redirect

# self py
from forms import LoginForm, RegistrationForm


app = Flask(__name__)

app.config['SECRET_KEY'] = '83b764cd7f3156f9ea40d7a60f6cc998'

posts = [
    {
        'author': 'Kimtee eiei',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 20, 2022'
    },
    
    {
        'author': 'Rambo eiei',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 22, 2022'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts= posts)


@app.route("/about")
def about():
    return render_template('about.html', title= 'About')



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # home is name of function to route not route
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'test@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
    
    
## run by activate env and python flaskblog.py