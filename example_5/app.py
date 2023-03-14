from flask import Flask, render_template
from models import Model25

application = Flask(__name__)

content = 'ini adalah berita baru, akan tetapi berasal dari orang lama.'

@application.route('/')
def index():
	# membuat objek dari kelas model25
	model = Model25()

	# mengisi nilai ke dalam model
	model.setTitle('Berita Terkini!')
	model.setDate('18/08/2019')
	model.setContent(content)

	#mengirim nilai ke view 
	return render_template('berita.html', judul=model.getTitle(), tanggal=model.getDate(), isi=model.getContent())

if __name__ == '__main__' :
	application.run(debug=True)