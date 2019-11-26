from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.mod_dummy.forms import LoginForm
from app.mod_dummy.forms import CreateForm
from app.mod_dummy.models import User

mod_dummy = Blueprint('dummy', __name__, url_prefix='/dummy')

@mod_dummy.route('/login/', methods=['GET', 'POST'])
def signin():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Welcome %s' % user.name)
            return redirect(url_for('dummy.home'))

        flash('Wrong email or password', 'error-message')

    return render_template("dummy/signin.html", form=form)

@mod_dummy.route('/create/', methods=['GET', 'POST'])
def create():
    form = CreateForm(request.form)

    if form.validate_on_submit():
        user = User(
            form.name.data,
            form.email.data,
            generate_password_hash(form.password.data),
            form.role.data,
            form.status.data) 
        db.session.add(user)
        db.session.commit()
        
    return render_template("dummy/create.html", form=form)