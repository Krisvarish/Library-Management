from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from module import ssign_in, tsign_in, lsign_in, search_, lendd, lilen, given_, lile_, stu, clas
import datetime

auth = Blueprint('auth', __name__)

@auth.route('/Student-Login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        s_username = request.form.get('s_username')
        s_password = request.form.get('s_password')
        if ssign_in(s_username, s_password) == True:
            session[ 'username' ] = s_username
            flash('Logged in', category = 'success')
            return redirect(url_for('auth.lib'))
        else:
            flash("Failed to login, Username or Password is incorrect", category = 'error')
    return render_template('student_login.html')

@auth.route('/logout')
def logout():
    session.pop('username')
    session['search'] = ''
    flash('Logged out', category = 'success')
    return redirect(url_for('views.home'))

@auth.route('/Teacher-Login', methods=['GET', 'POST'])
def teacher_login():
    if request.method == 'POST':
        t_username = request.form.get('t_username')
        t_password = request.form.get('t_password')
        if tsign_in(t_username, t_password) == True:
            session[ 'username' ] = t_username
            flash('Logged in', category = 'success')
            return redirect(url_for('auth.lib'))
        else:
            flash("Failed to login, Username or Password is incorrect", category = 'error')
    return render_template('teacher_login.html')

@auth.route('/Librarian-Login', methods=['GET', 'POST'])
def librarian_login():
    if request.method == 'POST':
        l_username = request.form.get('l_username')
        l_password = request.form.get('l_password')
        if lsign_in(l_username, l_password) == True:
            session[ 'username' ] = l_username
            flash('Logged in', category = 'success')
            return redirect(url_for('auth.change'))
        else:
            flash("Failed to login, Username or Password is incorrect", category = 'error')
    return render_template('librarian_login.html')

@auth.route('/lib')
def lib():
    if 'username' in session:
        user = session['username']
        if 'search' in session:
            m = session['search']
        else:
            m = ''
        return render_template('library.html', username=user, books = m)
    else:
        flash("You are not logged in", category = 'error')
        return render_template('home.html')
    

@auth.route('/change')
def change():
    if 'username' in session:
        user = session['username']
        n = lilen()
        session['change'] = n
        return render_template('lichange.html', username=user, boo = n)
    else:
        flash("You are not logged in", category = 'error')
        return render_template('home.html')

@auth.route('/search', methods=['POST'])
def search():
    if 'username' in session:
        if request.method == 'POST':
            search = request.form.get('search')
            m = search_(search)
            session['search'] = m
            return redirect(url_for('auth.lib'))
    else:
        flash("You are not logged in", category = 'error')
        return render_template('home.html')

@auth.route('/lend', methods=['POST', 'GET'])
def _lend():
    if 'username' in session:
        if request.method == 'POST':
            user = session['username']
            n= request.form.get('lend')
            session['lend'] = n
            date = datetime.datetime.now()
            lendd(n, user, date)
            flash("Book lent successfully", category = 'success')
            return render_template("library.html", username=user)
    else:
        flash("You are not logged in", category = 'error')
        return render_template('home.html')

@auth.route('/show', methods=['GET', 'POST'])
def show():
    if 'username' in session:
        user = session['username']
        b = lile_()
        session['show'] = b
        y = stu()
        n = clas()
        return render_template('lilend.html', username=user, bot = b, st = y, cla = n)
    else:
        flash("You are not logged in", category = 'error')
        return render_template('home.html')

@auth.route('/boinle', methods = ['GET', 'POST'])
def boinle():
    if 'username' in session:
        if request.method == 'POST':
            u = request.form.get('given')
            session['given'] = u
            given_(u)
            flash("Updated successfully", category = 'success')
            return redirect(url_for('auth.show'))
    else:
        flash("You are not logged in", category = 'error')
        return render_template('home.html')





    







