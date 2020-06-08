# Exercise Classification

## How to add new Exercises

1. Update `NUM_EXERCISES = 3` to the updated number

2. File Format:

Format:
`/captured/<EXERCISE_NAME>/<EXERCISE_ID>_<CAPTURE_ID>.csv`

Ex:
`/captured/Exercise1/01/01.csv`
`/captured/Exercise1/01/02.csv`

3. Note, mp4s are not used by Tensorflow. Only by developer during debug.

## Model Configuration

Layer 1: First LSTM, 256 Nodes to compute with the 252 Data Inputs. Returned Hidden sequence layer to be utilized by Second layer
Layer 2: Second LSTM reduces spikes in inaccuracy during training
Layer 3: Selects the exercise

## Tuning

- Using all joints makes a considerable increase in accuracy
- LSTM's are unidirectional
- 