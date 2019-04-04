#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
#!/usr/bin/env python3
from flask import Flask, render_template, request, send_file, render_template_string
from flask_wtf.csrf import CSRFProtect
from flask_wtf.csrf import CSRFError
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
import os

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
csrf = CSRFProtect()
csrf.init_app(app)
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    #return render_template('pages/placeholder.home.html')
    return render_template('pages/placeholder.form.html')

@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')

@app.route('/template-injection')
def hello_ssti():
    person = {'name':'world', 'secret': ", your third flag is hidden in /test"}
    if request.args.get('name'):
        person['name'] = request.args.get('name')
    template = '''<h2> Hello %s </h2>''' %person['name']
    return render_template_string(template, person=person)

@app.route('/test')
def test():
	return render_template('pages/placeholder.test.html')

@app.route('/return-files/')
def return_files():
	try: 
		return send_file('plaintext.pdf', attachment_filename = 'plaintext.pdf')
	except Exception as e:
		return str(e)
		
@app.route('/login')
def login():
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)
    # return render_template_string("Hello World")
    # return


@app.route('/register')
def register():
    # form = RegisterForm(request.form)
    # return render_template('forms/register.html', form=form)
    return render_template_string('Did you really think you could register? HAHAHAHA')


@app.route('/forgot')
def forgot():
    # form = ForgotForm(request.form)
    # return render_template('forms/forgot.html', form=form)
    return render_template_string('sorry, I kind of forgot about this page XD')

# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(CSRFError)
def handle_csrf_error(error):
    return render_template('errors/404.html', reason=error.description), 400


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')


#app.jinja_env.globals['get_user_file'] = get_user_file # Allows for use in Jinja2 templates
#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
