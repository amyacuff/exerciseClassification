import sys
import tensorflow as tf
import tensorboard
from datetime import datetime
from tensorflow.keras.preprocessing import sequence
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import LSTM, Dense, Bidirectional
import numpy as np
import tensorflow.keras as keras
import pandas as pd
from os import listdir
import glob
import code

# train.py
# invoke with python3 train.py [log_file]
# python3 train.py # Runs until reaches training threshold
# python3 train.py training_notes # Runs until epochs end, logging stats for Tensorboard visualization

# Enables verbose printing and interactive console
DEBUG = False

# Logs to Tensorboard for Analysis
TUNE = False

# % of dataset to allocate to training
TRAINING_SPLIT = 0.6

JOINTS_OF_INTEREST = [
'root',
'hips_joint',
'left_upLeg_joint',
'left_leg_joint',
'left_foot_joint',
'right_upLeg_joint',
'right_leg_joint',
'right_foot_joint',
'spine_1_joint',
'spine_2_joint',
'spine_3_joint',
'spine_4_joint',
'spine_5_joint',
'spine_6_joint',
'spine_7_joint',
'left_shoulder_1_joint',
'left_arm_joint',
'left_forearm_joint',
'neck_1_joint',
'neck_2_joint',
'neck_3_joint',
'neck_4_joint',
'head_joint',
'nose_joint',
'right_shoulder_1_joint',
'right_arm_joint',
'right_forearm_joint',
'right_forearm_joint'
]

# Number of exercises in the `captured` folder
NUM_EXERCISES = 3
# Number of csv per exercise
CAPTURES_PER_EXERCISE = 10

CAPTURED_DATA_DIR = "./captured/*/*.csv"

LABEL_DATA_DIR = "./captured/*/*_label.txt"

# This is the longest data capture (highest number of rows in all the csv's)
# TODO When seeking to improve performance, shrink the datasets
MAX_CAPTURED_SEQUENCE = 328

# Stop training when loss drops below this threshold
TRAINING_STOP_LOSS = 0.01

def genColumnsOfInterestWith(joints):
	# The columns of interest are, for each joint of interest, 
	# the 3x3 submatrix below extracted from the 4x4
	# 1  5  9 -
	# 2  6 10 -
	# 3  7 11 -
	# -  -  - -
	matrixIndices = [1,2,3,5,6,7,9,10,11]
	output = []
	for j in joints:
		for i in matrixIndices:
			output.append(j+str(i))
	return output

# selected 3x3 submatrix values range from -1,1, so normalize to 0,1
def normalize(csv):
	csv += 1
	csv /= 2
	return csv

def loadCapturedData():
	all_files = glob.glob(CAPTURED_DATA_DIR)
	x = []
	for f in all_files:
		csv = pd.read_csv(f, header=0)[COLUMNS_OF_INTEREST]
		normalized = normalize(csv)
		x.append(normalized)
	if DEBUG: 
		print(x)
	return x

def loadLabelData():
	all_files = sorted(glob.glob(LABEL_DATA_DIR))
	y = []
	for f in all_files:
		with open(f, 'r') as file:
			label = int(file.read().replace('\n',''))
			# Create 10 labels for each exercise
			for i in range(CAPTURES_PER_EXERCISE):
				y.append(label)
	if DEBUG: 
		print(y)
	return y

class StopAtLossThreshold(tf.keras.callbacks.Callback):
	def on_epoch_end(self, epoch, logs={}):
		if(logs.get('loss')<TRAINING_STOP_LOSS):
			print("\nReached end of useful training")
			self.model.stop_training=True

LOG_DIR="logs/fit/" + datetime.now().strftime("%Y%m%d-%H%M%S")

if len(sys.argv) >= 2:
	name=sys.argv[1]		
	LOG_DIR="logs/fit/"+name	

logBehavior = keras.callbacks.TensorBoard(log_dir=LOG_DIR)

if TUNE:
	callbacks=[logBehavior]
else:
	callbacks=[StopAtLossThreshold()]

COLUMNS_OF_INTEREST = genColumnsOfInterestWith(JOINTS_OF_INTEREST)

print("Filtering on the following columns: \n", "\n".join(COLUMNS_OF_INTEREST))

x = loadCapturedData()
y = loadLabelData()

# TODO Center padding
x = sequence.pad_sequences(x, maxlen=MAX_CAPTURED_SEQUENCE, dtype=float)
y = np.array(y,dtype=int)

if DEBUG:
	code.interact(local=locals())

# TODO Add shuffle
x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=TRAINING_SPLIT, test_size = 1-TRAINING_SPLIT)


layer1 = Bidirectional(LSTM(256, return_sequences=True))
layer2 = Bidirectional(LSTM(256))
layer3 = Dense(3, activation='softmax')

model = keras.models.Sequential([layer1, layer2, layer3])

model.compile(optimizer = tf.optimizers.Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train,epochs=100, callbacks=callbacks)

model.evaluate(x_test, y_test)
