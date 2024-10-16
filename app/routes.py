from flask import render_template,request,redirect,url_for
from app import app

users=[]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        hobbi = request.form.get('hobbi')
        age = request.form.get('age')
        if name and city and hobbi and age:
            users.append({'name': name, 'city': city, 'hobbi':hobbi, 'age': age})
            return redirect(url_for('index'))
    return render_template('anketa.html', users=users)