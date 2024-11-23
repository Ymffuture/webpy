from flask import Blueprint ,render_template, request # type: ignore

views = Blueprint(__name__ ,'views'   )

@views.route('/' )
def home():
    return render_template('Terms.html' ,heading_h1='Terms and Conditions')
@views.route('/base' )
def base():
    return render_template('base.html' )

@views.route('/Privacy-Policy')
def PrivacyPolicy():
    return render_template('Privacy-Policy.html' , heading='Privacy Policy')

@views.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Handle form submission (e.g., send an email or save to a database)
        return render_template('contact.html', success=True)
    return render_template('contact.html', success=False)