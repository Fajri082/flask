from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
	navigasi = [
		('/', 'home'),
		('/perhitungan', 'perhitungan'),
	]
	return render_template('index.html', navigasi=navigasi)


@application.route('/perhitungan')
def hitung():

	s = 2
	t = 3
	u = s+t

	cerita1 = 'Lutung Kasarung Cerita rakyat Lutung Kasarung menceritakan seorang putri cantik bernama Purbasari yang diusir dari istana. Sang kakak iri Purbasari ditunjuk menjadi ratu dan bukan dirinya. Purbasari yang hidup di luar istana pun bertemu dengan seekor lutung. Ternyata lutung tersebut adalah jelmaan pangeran dari istana dari khayangan. Lutung turun ke bumi untuk mencari istri yang cantik. Mereka berdua pun bersama-sama mencari keadilan dengan merebut tahta kerajaan dari kakak Purbasari yang jahat.'

	cerita2 = 'Batu Menangis Cerita rakyat Batu Menangis berasal dari Kalimantan Barat. Kisah ini menceritakan seorang ibu yang memiliki anak perempuan berparas cantik. Namun sayang, sifat sang anak sangat lah angkuh dan pemalas. Suatu hari ibu mengajak sang ajak pergi ke pasar dan betapa kagetnya karena sang anak mengatakan bahwa ibunya merupakan seorang pembantu. Ibunya pun sedih dan berdoa agar sang anak dihukum karena telah durhaka. Sang anak pun berubah menjadi batu dan menangis memohon ampun kepada ibunya.Namun hal itu sudah terlambat. Kisah ini pun dikenal dengan batu menangis'
	
	return render_template('hitung.html',
		cerita1=cerita1,
		cerita2=cerita2,
		s=s, t=t, u=u)
		
if __name__ == '__main__':
	application.run(debug=True)