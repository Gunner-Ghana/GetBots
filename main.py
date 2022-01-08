from flask import Flask,request, render_template
import pickle

from dataset_grab import loaddata
from predictor import predictors

app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def hello_world():
	if request.method == 'POST':
		f = request.files['file']
		if '.binetflow' in f.filename:
			f.save('bot1')
			loaddata('bot1')
			file = open('come.pickle', 'rb')
			sd = pickle.load(file)
			X,XT = sd[0], sd[2]
			n_features = 1
			X = X.reshape((X.shape[0], X.shape[1], n_features))
			all_ips= predictors(X)
			S_ips = all_ips[0]
			D_ips = all_ips[1]
		else:
			return render_template('index.html')
		return render_template('prediction.html', sourceips = S_ips, destips = D_ips)
		
	return render_template('index.html')
		

if __name__ == "__main__" :
	app.run()
