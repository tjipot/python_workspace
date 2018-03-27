# MVC: model, view, control;
# 可以理解为: model->数据机构, view->html模板, control->处理(逻辑的)代码;
from flask import Flask, request, render_template

app = Flask(__name__)

# Flask 通过render_template()实现模板的渲染;
# Flask 默认支持的模板是 jinja2;
@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
	return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
	username = request.form['username']
	password = request.form['password']
	if username=='admin' and password=='password':
		return render_template('signin-ok.html', username=username)
	return render_template('form.html', message='Bad Username Or Passoword', username=username)

if __name__ == '__main__':
	app.run()