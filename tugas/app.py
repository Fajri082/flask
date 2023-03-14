from flask import Flask, render_template
from models import Model25

application = Flask(__name__)



@application.route('/')
def index():
	# membuat objek dari kelas model25
	model = Model25()

	# mengisi nilai ke dalam model
	model.setTitle1('udin')
	model.setText1('sumatra selatan')
	model.setContent1('08122232365')
	model.setTitle2('awan')
	model.setText2('banten')
	model.setContent2('08432234123')
	model.setTitle3('Rama')
	model.setText3('solo')
	model.setContent3('08194323423')

	#mengirim nilai ke view 
	return render_template('tabel.html', 
		name1=model.getTitle1(), address1=model.getText1(), phone1=model.getContent1(), 
		name2=model.getTitle2(), address2=model.getText2(), phone2=model.getContent2(), 
		name3=model.getTitle3(), address3=model.getText3(), phone3=model.getContent3())

if __name__ == '__main__' :
	application.run(debug=True)