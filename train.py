from tensorflow.keras.preprocessing import sequence
from sklearn.model_selection import train_test_split
import pandas as pd
from os import listdir
import glob
import code

DEBUG = True

# % of dataset to allocate to training
TRAINING_SPLIT = 0.6

# The columns of interest are, for each joint of interest, 
# the 3x3 submatrix below extracted from the 4x4
# 1  5  9 -
# 2  6 10 -
# 3  7 11 -
# -  -  - -
# TODO Add more columns to this over time
COLUMNS_OF_INTEREST = ['hips_joint1','hips_joint2','hips_joint3','hips_joint5','hips_joint6','hips_joint7','hips_joint9','hips_joint10','hips_joint11']

# This is the longest data capture, aka highest number of rows in all the csvs
# TODO When tuning, reduce
MAX_CAPTURED_SEQUENCE = 328

CAPTURES_PER_EXERCISE = 10

CAPTURED_DATA_DIR = "./captured/*/*.csv"

# TODO Ensure captured matches label
LABEL_DATA_DIR = "./captured/*/*_label.txt"

# selected 3x3 submatrix, COLUMNS_OF_INTEREST, range from -1,1, so normalize to 0,1
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
			label = file.read().replace('\n','')
			for i in range(CAPTURES_PER_EXERCISE):
				y.append(label)
	if DEBUG: 
		print(y)
	return y

print("Filtering on the following columns: \n", "\n".join(COLUMNS_OF_INTEREST))

x = loadCapturedData()
y = loadLabelData()

x = sequence.pad_sequences(x, maxlen=MAX_CAPTURED_SEQUENCE)


# TODO Add shuffle
x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=TRAINING_SPLIT)

print(x)

if DEBUG:
	code.interact(local=locals())
