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

Layer 1: First LSTM, default 128 Nodes. Returns Hidden sequence layer to be utilized by Second layer
Layer 2: Second LSTM reduces spikes in inaccuracy during training
Layer 3: Selects the exercise

## Training

- The training is configured to stop once the `loss` reaches a very low 0.05. This value represents end of useful training.

## Tuning

- Including all joints significantly improves performance, compared to using a subset of joints
- Unidirectional LSTM's seem to work best with this data
- Dropout increased training duration and was not utilized. When have more data, may be worth revisiting.
- Adding additional LSTM nodes increases noise and decreases accuracy