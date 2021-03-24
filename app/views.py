"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app,db
from flask import render_template, request, redirect, url_for
from app.forms import PropertyForm
from app.models import Properties
from werkzeug.utils import secure_filename


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Jelani Hanlan")



@app.route('/property',  methods = ['GET','POST'])
def add_property():

    form = PropertyForm()

    if (request.method == 'POST'):
        if form.validate_on_submit() == True:

            title = request.form["title"]
            propertyDescription = request.form["propertyDescription"]
            Bedrooms = request.form["Bedrooms"]
            Bathrooms = request.form["Bathrooms"]
            price = request.form["price"]
            propertytype = request.form["propertytype"]
            location = request.form["location"]

            photo = form.photo.data
            filename = secure_filename(form.photo.data)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            prop = Properties(title,propertyDescription, Bedrooms, Bathrooms, price, propertytype, location, secureImageString)

            db.session.add(Property)
            db.session.commit()

            flash('Property added')
        else:
            flash('Property not Added')
        return redirect(url_for("properties"))
    return render_template("add_property.html", form=form )
    





@app.route('/properties',  methods = ['GET','POST'])
def properties():
    propert=db.session.query(Properties).all()
    return render_template("display_properties.html", properties=propert)






@app.route('/property/<propertyid>')
def property(propertyid):
    propert = db.session.query(Properties).filter_by(id=propertyid).first()

    return render_template('display_property.html', propert=propert)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
