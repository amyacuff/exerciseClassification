# Exercise Classification

## How to add new Exercises

1. Update `NUM_EXERCISES = 3` to the updated number

2. File Format:

Format:
`/captured/<EXERCISE_NAME>/<EXERCISE_ID>_<CAPTURE_ID>.csv`

Ex:
`/captured/Exercise1/01/01.csv`
`/captured/Exercise1/01/02.csv`

3. Add `/captured/<EXERCISE_NAME>/<EXERCISE_ID>_label.txt`

The contents should be <EXERCISE_ID>

## Model Configuration

Layer 1: First LSTM 256 Nodes to accompany the 252 input dimensions. Returns Hidden sequence layer to be utilized by Second layer
Layer 2: Second LSTM reduces spikes in inaccuracy during training
Layer 3: Selects the exercise

## Training

- The training is configured to stop once the `loss` reaches a very low 0.01. This value represents end of useful training.

## Tuning

- Including all joints significantly improves performance, compared to using a subset of joints
- Biidirectional LSTM's seem to work best with this data
- Dropout increased training duration and was not utilized. When have more data, may be worth revisiting.
- Adding >256 LSTM nodes increases noise and decreases accuracy