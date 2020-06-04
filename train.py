import pandas as pd

ACTIVITY_FILEPATH = "captured/Exercise1/backSquat_1.0_.csv"
COLUMNS_OF_INTEREST = ['hips_joint1','hips_joint2','hips_joint3','hips_joint5','hips_joint6','hips_joint7','hips_joint9','hips_joint10','hips_joint11']
csv = pd.read_csv(ACTIVITY_FILEPATH)

# TODO Add more columns to this over time
columnsOfInterest = csv[COLUMNS_OF_INTEREST]

columnsOfInterest += 1
columnsOfInterest /= 2

print(columnsOfInterest)

# This is the longest data capture
max_captured_sequence = 328




import code
code.interact(local=locals())
