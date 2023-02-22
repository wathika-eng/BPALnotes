from flask import Flask, website, app, 
from flask import routes, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Submit
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea, TextField




@app.context_processor
def base():
	form = Searchform()
	return dict(form=form)

# Create Search Function
@app.route('/search, methods=["POST"]')
def search():
    form = SearchForm()
    if form.validate_on_submit():
        post.searched = form.searched.data
        return redirect(url_for('views.search', search=form.search.data))
    return render_template('search.html', form=form, searched = post.searched)