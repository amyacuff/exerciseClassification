import pandas as pd

ACTIVITY_FILEPATH = "captured/Exercise1/backSquat_1.0_.csv"

csv = pd.read_csv(ACTIVITY_FILEPATH)

# TODO Add more columns to this over time
columnsOfInterest = csv[['hips_joint1','hips_joint2','hips_joint3','hips_joint5','hips_joint6','hips_joint7','hips_joint9','hips_joint10','hips_joint11']]

columnsOfInterest += 1
columnsOfInterest /= 2

print(columnsOfInterest)

import code
code.interact(local=locals())
