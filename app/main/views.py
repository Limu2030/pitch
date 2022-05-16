
from flask import render_template,url_for,redirect,flash
from . import main
from .forms import RegistrationForm,LoginForm,PitchForm,CommentForm
from .models import Pitch, User,Comments
from app import db
from flask_login import login_required, login_user,current_user


@main.route('/')
def home():
    comment_form=CommentForm()
    get_pitches=Pitch.query.all()
    for pitch in get_pitches:
        pitch.user=User.query.filter_by(id=pitch.author).first()
    return render_template('home.html',title='home',pitches=get_pitches, comment_form=comment_form)


@main.route('/about')
def about():
    return render_template('about.html',title='about')




@main.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    user_exist=User.query.filter_by(email=form.email.data).first() 
    if form.validate_on_submit() and user_exist is None: 
   
        user = User(username=form.username.data, email=form.email.data,
                password=form.password.data)

        print(form.username)
        db.session.add(user)
        db.session.commit()
        
        flash('Yaaaay! Thanks for registering!')

        return redirect(url_for('main.login'))
    flash('Username is taken')
    
    print(form.username.data,form.email.data,form.password.data,form.confirm_password.data)
    return render_template('register.html',title='register',form=form)


@main.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user != None and user.verify_password(form.password.data):
            login_user(user)
            flash('Thanks for logging in!')
        return redirect(url_for('main.pitch'))
    return render_template('login.html',title = 'login',form = form)


@main.route('/pitch',methods=['GET','POST'])
@login_required
def pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(title=form.title.data, content=form.content.data,
                author=current_user.id,category=form.category.data)

        db.session.add(pitch)
        db.session.commit()

        flash('Thanks for your pitch!')
        return redirect(url_for('main.home'))
    return render_template('pitch.html',title = 'pitch',form = form)
    

@main.route('/comment/<int:user_id>/<int:pitch_id>',methods=['POST'])
@login_required
def comment(user_id,pitch_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comments(content=form.content.data,user_id=user_id,pitch_id=pitch_id)

        db.session.add(comment)
        db.session.commit()
    return redirect(url_for('main.home'))


        
    





