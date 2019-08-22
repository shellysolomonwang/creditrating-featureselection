
#from Data_setup_lstm import data_clean_lstm
from Data_setup_image import data_clean_image
import numpy as np 
import pandas as pd 
import keras
from keras.models import Sequential
from keras.optimizers import SGD
from keras.layers import Dense, Dropout, Activation, Conv1D, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers import LSTM
import datetime
from sklearn.metrics import classification_report
from keras.layers import TimeDistributed

def training(sector, epochs_num = 100, MASK = False, difference =False, shuffle =False):
	'''
	if difference:
		from Data_setup2 import data_clean
	else:
		from Data_setup import data_clean

	

	def mlp():
		
		model.add(Dense(128, activation='relu', input_dim=x_train.shape[1]))
		#model.add(Dropout(0.5))
		model.add(Dense(128, activation='relu'))
		#model.add(Dropout(0.5))
		model.add(Dense(y_train.shape[1], activation='softmax'))
		
	def lstm():
		
		#global x_train, y_train, x_test, y_test
		time_step = 4
		train_x, train_y, test_x, test_y = data_clean_lstm(sector, tyear, 
                                                       MASK = False, time_step = time_step, 
                                                       difference = difference, shuffle =shuffle)

		#print(train_x.shape, train_y.shape)
		model.add(LSTM(32, return_sequences=True, input_shape=(time_step, train_x.shape[2])))
		model.add(LSTM(64,return_sequences=False))
		model.add(Dense(128, activation='relu'))
		model.add(Dense(128, activation='relu'))
		model.add(Dense(train_y.shape[1], activation='softmax'))
		print (model.summary())
		return train_x, train_y, test_x, test_y

	def cnn():
		
		global x_train, y_train, x_test, y_test
		row, col = x_train.shape
		x_train = x_train[:,:,None]
		#y_train = y_train[:,:,None]
		x_test = x_test[:,:,None]
		#y_test = y_test[:,:,None]
		print(x_train.shape, y_train.shape)
		model.add(Conv1D(64, kernel_size=3, activation='relu', input_shape=(col, 1)))
		model.add(Conv1D(32, kernel_size=3, activation='relu'))
		model.add(Dense(128, activation='relu'))
		model.add(Dense(128, activation='relu'))
		model.add(Flatten())
		model.add(Dense(y_train.shape[1], activation='softmax'))

	def cnn2d():
		
		time_step = 4
		train_x, train_y, test_x, test_y = data_clean_lstm(sector, tyear, 
                                                       MASK = False, time_step = time_step, 
                                                       difference = difference, shuffle =shuffle)
		train_x = train_x[:,:,:,None]
		test_x = test_x[:,:,:,None]
		print(train_x.shape, train_y.shape)

		model.add(Conv2D(32, kernel_size=(3, 3), padding="same", activation="relu", 
			input_shape=(train_x.shape[1],train_x.shape[2],1)))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		model.add(Dense(64, activation='relu'))
		model.add(Dense(128, activation='relu'))
		model.add(Flatten())
		model.add(Dense(y_train.shape[1], activation='softmax'))

		print (model.summary())
		return train_x, train_y, test_x, test_y


	def cnnlstm():
		
		time_step = 4
		train_x, train_y, test_x, test_y = data_clean_lstm(sector, tyear, 
                                                       MASK = False, time_step = time_step, 
                                                       difference = difference, shuffle =shuffle)
		train_x = train_x[:,:,:,None]
		test_x = test_x[:,:,:,None] 
		#train_x = train_x.reshape((291, 2, 4, 362, 1))
		#test_x = test_x.reshape((56, 2, 4, 362, 1))
		#train_y = train_y.reshape((291,2,12))
		#test_y = test_y.reshape((56,2,12))
		train_x, train_y, test_x, test_y = datashape(train_x, train_y, test_x, test_y, 3)
		print(train_x.shape, train_y.shape)
		
		model.add(TimeDistributed(Conv2D(32, kernel_size=(3, 3), padding="same", activation="relu", 
			input_shape=(train_x.shape[1:]))))
		model.add(TimeDistributed(MaxPooling2D(pool_size=(2, 2))))
		model.add(TimeDistributed(Flatten()))
		model.add(LSTM(32,return_sequences=False))
		model.add(Dense(64, activation='relu'))
		model.add(Dense(128, activation='relu'))
		model.add(Dense(train_y.shape[1], activation='softmax'))

		#print (model.summary())
		return train_x, train_y, test_x, test_y

	def datashape(train_x, train_y, test_x, test_y, time):
		num_sample = train_x.shape[0]
		num_sample1 = test_x.shape[0]
		i = 0
		Train_x= train_x[i:i+time,:,:,:]
		Train_y= train_y[i+time,:][None,:]
		Test_x= test_x[i:i+time,:,:,:]
		Test_y = test_y[i+time,:][None,:]
		print (Train_y.shape)
		for i in range(1,num_sample - time ):
			Train_x = np.concatenate([Train_x, train_x[i:i+time,:,:,:]], axis = 0)
			Train_y = np.concatenate([Train_y ,train_y[i+time,:][None,:]], axis = 0)
		for i in range(1,num_sample1 - time ):
			Test_x = np.concatenate([Test_x,test_x[i:i+time,:,:,:]], axis = 0)
			Test_y = np.concatenate([Test_y,test_y[i+time,:][None,:]], axis = 0)
		Train_x = Train_x.reshape((int(Train_x.shape[0]/time), time,Train_x.shape[1],Train_x.shape[2],Train_x.shape[3]))
		Test_x = Test_x.reshape((int(Test_x.shape[0]/time), time,Test_x.shape[1],Test_x.shape[2],Test_x.shape[3]))
		#Train_y = Train_y.reshape((Train_y.shape[]))
		return Train_x, Train_y,Test_x, Test_y

	'''
	def cnn2d_image():	
		time_step = 4
		train_x, train_y, test_x, test_y = data_clean_image('Energy', tyear=2015, MASK = False, shuffle = False)
		
		train_x = train_x[:,:,:,None]
		test_x = test_x[:,:,:,None]
		print(train_x.shape, train_y.shape)

		model.add(Conv2D(32, kernel_size=(3, 3), padding="same", activation="relu", 
			input_shape=(train_x.shape[1],train_x.shape[2],1)))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		model.add(Dense(64, activation='relu'))
		model.add(Dense(128, activation='relu'))
		model.add(Flatten())
		model.add(Dense(train_y.shape[1], activation='softmax'))

		print (model.summary())
		return train_x, train_y, test_x, test_y



	#models = ['mlp', 'cnn', 'lstm','cnn2d', 'cnnlstm']
	models = ['cnn2d_image']
	results = pd.DataFrame()
	Testyear1 = [2000, 2001,2002,2003,2004,2005,2006,2007,2008, 2009, 2010, 2011, 2012, 2013,2014,2015,2016]	
	Testyear2 = [2010, 2011, 2012, 2013,2014,2015,2016]
	if sector == 'Energy':
		Testyear = Testyear2
	else:
		Testyear = Testyear1
	if shuffle == True:
		Testyear = [0]*1
	for tyear in Testyear:
		for i in models:
			global x_train, y_train, x_test, y_test
			#x_train, y_train, x_test, y_test = data_clean(sector, tyear, MASK, shuffle = shuffle)

			# if i == 'mlp':
			# 	x_train, y_train, x_test, y_test = data_clean(sector, tyear, MASK, shuffle = shuffle)
			# 	model = Sequential()
			# 	mlp()
			# if i == 'lstm':
			# 	model = Sequential()
			# 	x_train, y_train, x_test, y_test = lstm()
			# if i == 'cnn':
			# 	x_train, y_train, x_test, y_test = data_clean(sector, tyear, MASK, shuffle = shuffle)
			# 	model = Sequential()
			# 	cnn()
			# if i == 'cnn2d':
			# 	model = Sequential()
			# 	x_train, y_train, x_test, y_test = cnn2d()
			if i == 'cnn2d_image':
				model = Sequential()
				x_train, y_train, x_test, y_test = cnn2d_image()
			# if i == 'cnnlstm':
			# 	model = Sequential()
			# 	x_train, y_train, x_test, y_test = cnnlstm()
			print('test: ', x_test.shape, y_test.shape)
			#print (model.summary())
			sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
			#model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
			model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
			model.fit(x_train, y_train, epochs=epochs_num, batch_size=128)
			test_score, test_acc = model.evaluate(x_test, y_test)
			train_score, train_acc = model.evaluate(x_train, y_train) 
			y_pred = model.predict(x_test)
			#print (np.argmax(y_pred, axis = 1), np.argmax(y_test, axis = 1))
			#print (np.argmax(y_test, axis = 1))
			print (i, 'train: ', train_acc, 'test: ', test_acc)
			#print(classification_report(np.argmax(y_test, axis = 1), np.argmax(y_pred, axis = 1)))
			results = results.append( pd.DataFrame({'train':train_acc,'test': test_acc}, index = [i]))

		results.to_csv('Result/'+ str(epochs_num) + sector + 'Diff' +str(difference)[0] + 'Suff'+ str(shuffle)[0]+ '.csv')
	print (results)


if __name__ == "__main__":
	epochs_num = 301
	Difference = [False]
	Shuffle = [True]
	start = (datetime.datetime.now())
	for difference in Difference:
		for shuffle in Shuffle:	
			training('Energy', epochs_num , MASK = False, difference =difference, shuffle =shuffle)
			training('Financial', epochs_num , MASK = False, difference =difference, shuffle =shuffle)
			training('Healthcare', epochs_num , MASK = False, difference =difference, shuffle =shuffle)
	print(datetime.datetime.now())
	print (datetime.datetime.now() - start)
