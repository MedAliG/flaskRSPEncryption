from flask import Flask,render_template ,flash ,request ,redirect ,url_for ,session ,logging
from data import articles
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
import rsp_final

#import requests


app = Flask(__name__)

articles = articles()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/articles')
def articles():
	return render_template('/retVals.html', articles = articles)

@app.route('/article/<string:id>/')
def article(id):
	return render_template('article.html',)


class rsp_form(Form):
	cle = StringField('cle' ,validators=[validators.Length(min=1,max=36)])
	x = StringField('x' ,validators=[validators.Length(min=1,max=16)])
	nbRonds = StringField('nbRonds' ,validators=[validators.Length(min=1,max=16)])


@app.route('/rsp' ,methods=['GET', 'POST'])
def rsp_calc():
	form = rsp_form(request.form)
	if request.method == 'POST' and form.validate():
		flash('Encrypting Successfully ','success')
		cle = form.cle.data
		x = form.x.data
		nbRonds = int(form.nbRonds.data)
		keys = []
		#cle = "00111010100101001101011000111111"
		#x = "0010011010110111"
		#nbRonds = 4
		keys,y  = rsp_final.rsp(x,nbRonds,cle)
		print(keys)
		print(y)
		return render_template('rsp_result.html', result = y,keys = keys)
	return render_template('rsp.html', form=form)	



if __name__=='__main__':
	app.secret_key="123"
	app.run(debug = True)	