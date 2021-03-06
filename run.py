from flask import Flask,render_template,request,redirect,url_for
import config
from models import User
from exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		pass

@app.route('/regist/',methods=['GET','POST'])
def regist():
	if request.method == 'GET':
		return render_template('regist.html')
	else:
		telephone = request.form.get('telephone')
		username = request.form.get('username')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')

		user = User.query.filter(User.telephone == telephone).first()
		if user:
			return '该手机号码已被注册，请更换手机号码！'
		else:
			if password1 != password2:
				return '两次密码不相等，请核对后再填写！'
			else:
				user = User(telephone = telephone,username = username,password = password1)
				db.session.add(user)
				db.session.commit()

				return redirect(url_for('login'))
		

if __name__ == '__main__':
	app.run()