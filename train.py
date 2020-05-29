import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM #, CuDNNLSTM
from numpy import array
import numpy as np
import sklearn.model_selection as model_selection
import pandas as pd
from matplotlib import pyplot

def convert_to_float(x):
    try:
        return np.float(x)
    except:
        return np.nan


data = pd.read_csv("activityRecording.csv")
#print(data.head())
print("data.shape")
print(data.shape)

#select columns
#reshape
#split data

#each of the 27 selected body parts has a 4x4 matrix with 16 floats, 27x16 = 432
features = 432 #float numbers between -1 and 1
num_samples = 12 # acitivty recording sessions of 300 frames (rows)
num_classes = 3 #number of activity classifications (jumping jacks, boxing, jogging in place)
#labels must be 0,1,2
timesteps = 300 #frame LSTM’s prefer 200-400 time steps, 5 sec of video at 60fps

#convert all values to float
#data = data.iloc[:,:].apply(convert_to_float)

#data.dropna(axis=0, how='any', inplace=True)
#data.head(20)

# Round numbers to normalize
#data = data.iloc[:,1:].round(4)


x = data.iloc[:,2:] #all columns except the first and second, all rows



#print(y)

print("x.shape")
print(x.shape)

#print(x.head())

#x = x.values.reshape((num_samples, timesteps, features)) #samples, time steps, features
#y= np.asarray(y)

#take labels off csv file

#pyplot.plot(data)
#pyplot.show()

x = x.values.reshape((num_samples, timesteps, features)) #samples, time steps, features


#need to split train/test based on sessionID with test = 10,11,12
#film 3 activities 9 sessionIDs, make sure not short one row

##x_test = x[x.iloc[:,1] > 9] #data[data.iloc[:,1] > 9]
##x_train = x[x.iloc[:,1] <= 9] #data[data.iloc[:,1] <= 9]



#need one activity label per recording, not 300, get first and last row only of first column
#make dataframe of labels 0,0,0,1,1,1,2,2,2,0,0,0
#y = data.iloc[[0, -1],[0]] #first and last row, first column
#y = data.iloc[:,0] # the first column, and all of the rows for the column.
y = data.iloc[[0,302,602,902,1202,1502,1802,2102,2402,2702,3002,3302],[1]]
y= np.asarray(y)

##y_train = data.iloc[[0,302,602,902,1202,1502,1802,2102,2402],[0]]
##y_train= np.asarray(y_train)
##y_test = data.iloc[[2702,3002,3302],[0]]
##y_test= np.asarray(y_test)

#print("y_train.shape")
#print(y_train.shape)

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, train_size=0.75,test_size=0.25, random_state=101, shuffle=False)

model = Sequential()
#model.add(LSTM(128, input_shape=(x_train.shape[1:]), activation='relu', return_sequences=True))
#we need to “flatten” the data for our input layer into the neural network. Instead of feeding a matrix of shape 300x432 we will feed in a list of 129,600 values.
#x_train = x_train.reshape(x_train.shape[0], input_shape)
##x_train = x_train.astype('float32')
#y_train = y_train.astype('float32')

#y_train_hot = np_utils.to_categorical(y_train, num_classes)
#print('New y_train shape: ', y_train_hot.shape)

model.add(LSTM(128, input_shape=(timesteps, features), activation='relu', return_sequences=True))
#model.add(CuDNNLSTM(128, input_shape=(timesteps, features), return_sequences=True) #input_shape= time steps, features, assumes one or more samples
model.add(Dropout(0.2))

model.add(LSTM(128, activation='relu'))
#model.add(CuDNNLSTM(128))
model.add(Dropout(0.2))

model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(num_classes, activation='softmax'))

opt = tf.keras.optimizers.Adam(lr=1e-3, decay=1e-5)
model.compile(loss='sparse_categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3, validation_split=0.5)

model.evaluate(x_test, y_test)
