from keras.models import load_model
import pickle

import struct,socket

model = load_model('botnet2.h5')
file = open('last.pickle', 'rb')
sd = pickle.load(file)
X,XT = sd[0], sd[2]
n_features = 1
X = X.reshape((X.shape[0], X.shape[1], n_features))

predictions = model.predict_classes(X)
sia = []
dia = []
together = []

# summarize the first 5 cases
for i in range(len(predictions)):
	if predictions[i] == 1:
		inputs = X[i].tolist()
		sp = inputs[4]
		sia.append(sp)
v=sia[0]
m=v[0]
print(type(m))
		
		
		
			
		
	
	

