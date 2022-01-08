from keras.models import load_model

import struct,socket

model = load_model('botnet2.h5')
def predictors(X):
	predictions = model.predict_classes(X)
	sia = []
	dia = []
	together = []
# summarize the first 5 cases
	for i in range(len(predictions)):
		if predictions[i] == 1:
			inputs = X[i].tolist()
			sp = inputs[4]
			sp=sp[0]
			dp = inputs[5]
			dp=dp[0]
			sp=int(sp)
			dp=int(dp)
			#getting the real source ip address
			sip = struct.pack('!L',sp)
			ssp = socket.inet_ntoa(sip)
			sia.append(ssp)
			sia = list( dict.fromkeys(sia) )
			
		
			#getting the real destination ip addresses
			dip = struct.pack('!L',dp)
			ddp = socket.inet_ntoa(dip)
			dia.append(ddp)
			dia = list( dict.fromkeys(dia) )
		
	together.append(sia)
	together.append(dia)
	
	return together
		
	
	
