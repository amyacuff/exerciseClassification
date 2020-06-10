# Exercise Classification

**Version**:1.0.0

## How to add new Exercises

1. Update `NUM_EXERCISES = 3` to the updated number

2. File Format:

Format:
`/captured/<EXERCISE_ID>/<EXERCISE_ID>_<CAPTURE_ID>.csv`

Ex:
`/captured/01/01/01.csv`
`/captured/01/01/02.csv`

3. Add `/captured/<EXERCISE_ID>/<EXERCISE_ID>_label.txt`

The contents should be `<EXERCISE_ID>`

Ex:
`/captured/01/01_label.txt` contains the text `01`



## Model Configuration

Layer 1: First LSTM 256 Nodes to accompany the 252 input dimensions. Returns Hidden sequence layer to be utilized by Second layer
Layer 2: Second LSTM reduces spikes in inaccuracy during training
Layer 3: Selects the exercise

```
1/1 [==============================] - 0s 358us/step - loss: 5.2434e-04 - accuracy: 1.0000
```

## Training

Accuracy of v1.0.0
![](/Users/r/Documents/Projects/MADE/exerciseClassification/s1.png)

Loss of v1.0.0
![](/Users/r/Documents/Projects/MADE/exerciseClassification/s2.png)

- The training is configured to stop once the `loss` reaches a very low 0.01. This value represents end of useful training.

## Tuning

- Including all joints significantly improves performance, compared to using a subset of joints
- Biidirectional LSTM's seem to work best with this data
- Dropout increased training duration and was not utilized. When have more data, may be worth revisiting.
- Adding >256 LSTM nodes increases noise and decreases accuracy

## Next Steps

#### 1. Add exercises

- Performance Metrics

When given new data, how close to real-time can this model be executed?

#### 2. Performance Optimization

As necessary, there are available steps to improve performanc:

#### 3. Smooth Data

Smoothing data will reduce noise and increase accuracy

#### 4. Reducing sequence size of input data

Currently takes MAX_CAPTURED_SEQUENCE datapoints for each joints. Lowering fidelity to 50%, 25% wil improve performance.

#### 5. Using a subset of joints
- Reducing the input data size, by removing less useful joints. For example, wrist position is not as useful as knee joint.

#### 6. Capture same exercises from more viewpoints

#### 7. Capture same exercise with different athletes

#### 8. Capture more than 10 repetitions per exercise

## Appendix

Logs:

```
1/1 [==============================] - 0s 1ms/step - loss: 0.9095 - accuracy: 0.7778
Epoch 3/100
1/1 [==============================] - 0s 1ms/step - loss: 1.1506 - accuracy: 0.2778
Epoch 4/100
1/1 [==============================] - 0s 980us/step - loss: 0.7383 - accuracy: 0.6111
Epoch 5/100
1/1 [==============================] - 0s 990us/step - loss: 0.7369 - accuracy: 0.5556
Epoch 6/100
1/1 [==============================] - 0s 983us/step - loss: 0.5876 - accuracy: 0.9444
Epoch 7/100
1/1 [==============================] - 0s 999us/step - loss: 0.6728 - accuracy: 0.6111
Epoch 8/100
1/1 [==============================] - 0s 979us/step - loss: 0.5805 - accuracy: 0.6667
Epoch 9/100
1/1 [==============================] - 0s 1ms/step - loss: 0.5745 - accuracy: 0.5556
Epoch 10/100
1/1 [==============================] - 0s 1ms/step - loss: 0.4920 - accuracy: 0.9444
Epoch 11/100
1/1 [==============================] - 0s 996us/step - loss: 0.4623 - accuracy: 0.7222
Epoch 12/100
1/1 [==============================] - 0s 1ms/step - loss: 0.3174 - accuracy: 0.9444
Epoch 13/100
1/1 [==============================] - 0s 1ms/step - loss: 0.4952 - accuracy: 0.7222
Epoch 14/100
1/1 [==============================] - 0s 1ms/step - loss: 0.4817 - accuracy: 0.6667
Epoch 15/100
1/1 [==============================] - 0s 970us/step - loss: 0.1818 - accuracy: 0.9444
Epoch 16/100
1/1 [==============================] - 0s 1ms/step - loss: 0.2371 - accuracy: 0.9444
Epoch 17/100
1/1 [==============================] - 0s 1ms/step - loss: 0.1225 - accuracy: 0.9444
Epoch 18/100
1/1 [==============================] - 0s 1ms/step - loss: 0.0900 - accuracy: 0.9444
Epoch 19/100
1/1 [==============================] - 0s 1ms/step - loss: 0.0871 - accuracy: 0.9444
Epoch 20/100
1/1 [==============================] - 0s 980us/step - loss: 0.0677 - accuracy: 0.9444
Epoch 21/100
1/1 [==============================] - 0s 989us/step - loss: 0.0388 - accuracy: 1.0000
Epoch 22/100
1/1 [==============================] - 0s 2ms/step - loss: 0.0257 - accuracy: 1.0000
Epoch 23/100
1/1 [==============================] - 0s 1ms/step - loss: 0.0208 - accuracy: 1.0000
Epoch 24/100
1/1 [==============================] - 0s 1ms/step - loss: 0.0182 - accuracy: 1.0000
Epoch 25/100
1/1 [==============================] - 0s 1ms/step - loss: 0.0154 - accuracy: 1.0000
Epoch 26/100
1/1 [==============================] - 0s 1ms/step - loss: 0.0123 - accuracy: 1.0000
Epoch 27/100
1/1 [==============================] - 0s 2ms/step - loss: 0.0094 - accuracy: 1.0000
Epoch 28/100
1/1 [==============================] - 0s 2ms/step - loss: 0.0070 - accuracy: 1.0000
Epoch 29/100
1/1 [==============================] - 0s 1ms/step - loss: 0.0053 - accuracy: 1.0000
Epoch 30/100
1/1 [==============================] - 0s 1ms/step - loss: 0.0040 - accuracy: 1.0000
Epoch 31/100
1/1 [==============================] - 0s 1ms/step - loss: 0.0032 - accuracy: 1.0000
Epoch 32/100
1/1 [==============================] - 0s 2ms/step - loss: 0.0026 - accuracy: 1.0000
Epoch 33/100
1/1 [==============================] - 0s 1ms/step - loss: 0.0022 - accuracy: 1.0000
Epoch 34/100
1/1 [==============================] - 0s 2ms/step - loss: 0.0020 - accuracy: 1.0000
Epoch 35/100
1/1 [==============================] - 0s 1ms/step - loss: 0.0017 - accuracy: 1.0000
Epoch 36/100
1/1 [==============================] - 0s 1ms/step - loss: 0.0016 - accuracy: 1.0000
Epoch 37/100
1/1 [==============================] - 0s 1ms/step - loss: 0.0015 - accuracy: 1.0000
Epoch 38/100
1/1 [==============================] - 0s 1ms/step - loss: 0.0013 - accuracy: 1.0000
Epoch 39/100
1/1 [==============================] - 0s 1ms/step - loss: 0.0012 - accuracy: 1.0000
Epoch 40/100
1/1 [==============================] - 0s 2ms/step - loss: 0.0011 - accuracy: 1.0000
Epoch 41/100
1/1 [==============================] - 0s 1ms/step - loss: 9.9555e-04 - accuracy: 1.0000
Epoch 42/100
1/1 [==============================] - 0s 2ms/step - loss: 9.3087e-04 - accuracy: 1.0000
Epoch 43/100
1/1 [==============================] - 0s 2ms/step - loss: 8.7452e-04 - accuracy: 1.0000
Epoch 44/100
1/1 [==============================] - 0s 1ms/step - loss: 8.2497e-04 - accuracy: 1.0000
Epoch 45/100
1/1 [==============================] - 0s 2ms/step - loss: 7.8108e-04 - accuracy: 1.0000
Epoch 46/100
1/1 [==============================] - 0s 1ms/step - loss: 7.4192e-04 - accuracy: 1.0000
Epoch 47/100
1/1 [==============================] - 0s 1ms/step - loss: 7.0681e-04 - accuracy: 1.0000
Epoch 48/100
1/1 [==============================] - 0s 2ms/step - loss: 6.7513e-04 - accuracy: 1.0000
Epoch 49/100
1/1 [==============================] - 0s 2ms/step - loss: 6.4641e-04 - accuracy: 1.0000
Epoch 50/100
1/1 [==============================] - 0s 1ms/step - loss: 6.2031e-04 - accuracy: 1.0000
Epoch 51/100
1/1 [==============================] - 0s 1ms/step - loss: 5.9645e-04 - accuracy: 1.0000
Epoch 52/100
1/1 [==============================] - 0s 1ms/step - loss: 5.7461e-04 - accuracy: 1.0000
Epoch 53/100
1/1 [==============================] - 0s 1ms/step - loss: 5.5451e-04 - accuracy: 1.0000
Epoch 54/100
1/1 [==============================] - 0s 1ms/step - loss: 5.3596e-04 - accuracy: 1.0000
Epoch 55/100
1/1 [==============================] - 0s 1ms/step - loss: 5.1884e-04 - accuracy: 1.0000
Epoch 56/100
1/1 [==============================] - 0s 2ms/step - loss: 5.0297e-04 - accuracy: 1.0000
Epoch 57/100
1/1 [==============================] - 0s 1ms/step - loss: 4.8824e-04 - accuracy: 1.0000
Epoch 58/100
1/1 [==============================] - 0s 1ms/step - loss: 4.7451e-04 - accuracy: 1.0000
Epoch 59/100
1/1 [==============================] - 0s 1ms/step - loss: 4.6172e-04 - accuracy: 1.0000
Epoch 60/100
1/1 [==============================] - 0s 2ms/step - loss: 4.4975e-04 - accuracy: 1.0000
Epoch 61/100
1/1 [==============================] - 0s 2ms/step - loss: 4.3855e-04 - accuracy: 1.0000
Epoch 62/100
1/1 [==============================] - 0s 1ms/step - loss: 4.2805e-04 - accuracy: 1.0000
Epoch 63/100
1/1 [==============================] - 0s 2ms/step - loss: 4.1815e-04 - accuracy: 1.0000
Epoch 64/100
1/1 [==============================] - 0s 1ms/step - loss: 4.0887e-04 - accuracy: 1.0000
Epoch 65/100
1/1 [==============================] - 0s 1ms/step - loss: 4.0008e-04 - accuracy: 1.0000
Epoch 66/100
1/1 [==============================] - 0s 1ms/step - loss: 3.9178e-04 - accuracy: 1.0000
Epoch 67/100
1/1 [==============================] - 0s 2ms/step - loss: 3.8394e-04 - accuracy: 1.0000
Epoch 68/100
1/1 [==============================] - 0s 1ms/step - loss: 3.7648e-04 - accuracy: 1.0000
Epoch 69/100
1/1 [==============================] - 0s 1ms/step - loss: 3.6936e-04 - accuracy: 1.0000
Epoch 70/100
1/1 [==============================] - 0s 2ms/step - loss: 3.6258e-04 - accuracy: 1.0000
Epoch 71/100
1/1 [==============================] - 0s 2ms/step - loss: 3.5612e-04 - accuracy: 1.0000
Epoch 72/100
1/1 [==============================] - 0s 1ms/step - loss: 3.4996e-04 - accuracy: 1.0000
Epoch 73/100
1/1 [==============================] - 0s 2ms/step - loss: 3.4400e-04 - accuracy: 1.0000
Epoch 74/100
1/1 [==============================] - 0s 2ms/step - loss: 3.3835e-04 - accuracy: 1.0000
Epoch 75/100
1/1 [==============================] - 0s 1ms/step - loss: 3.3290e-04 - accuracy: 1.0000
Epoch 76/100
1/1 [==============================] - 0s 1ms/step - loss: 3.2766e-04 - accuracy: 1.0000
Epoch 77/100
1/1 [==============================] - 0s 2ms/step - loss: 3.2264e-04 - accuracy: 1.0000
Epoch 78/100
1/1 [==============================] - 0s 2ms/step - loss: 3.1780e-04 - accuracy: 1.0000
Epoch 79/100
1/1 [==============================] - 0s 1ms/step - loss: 3.1311e-04 - accuracy: 1.0000
Epoch 80/100
1/1 [==============================] - 0s 1ms/step - loss: 3.0862e-04 - accuracy: 1.0000
Epoch 81/100
1/1 [==============================] - 0s 1ms/step - loss: 3.0425e-04 - accuracy: 1.0000
Epoch 82/100
1/1 [==============================] - 0s 1ms/step - loss: 3.0001e-04 - accuracy: 1.0000
Epoch 83/100
1/1 [==============================] - 0s 1ms/step - loss: 2.9591e-04 - accuracy: 1.0000
Epoch 84/100
1/1 [==============================] - 0s 1ms/step - loss: 2.9193e-04 - accuracy: 1.0000
Epoch 85/100
1/1 [==============================] - 0s 2ms/step - loss: 2.8809e-04 - accuracy: 1.0000
Epoch 86/100
1/1 [==============================] - 0s 2ms/step - loss: 2.8432e-04 - accuracy: 1.0000
Epoch 87/100
1/1 [==============================] - 0s 1ms/step - loss: 2.8066e-04 - accuracy: 1.0000
Epoch 88/100
1/1 [==============================] - 0s 1ms/step - loss: 2.7710e-04 - accuracy: 1.0000
Epoch 89/100
1/1 [==============================] - 0s 2ms/step - loss: 2.7364e-04 - accuracy: 1.0000
Epoch 90/100
1/1 [==============================] - 0s 2ms/step - loss: 2.7025e-04 - accuracy: 1.0000
Epoch 91/100
1/1 [==============================] - 0s 1ms/step - loss: 2.6696e-04 - accuracy: 1.0000
Epoch 92/100
1/1 [==============================] - 0s 1ms/step - loss: 2.6374e-04 - accuracy: 1.0000
Epoch 93/100
1/1 [==============================] - 0s 2ms/step - loss: 2.6058e-04 - accuracy: 1.0000
Epoch 94/100
1/1 [==============================] - 0s 2ms/step - loss: 2.5751e-04 - accuracy: 1.0000
Epoch 95/100
1/1 [==============================] - 0s 1ms/step - loss: 2.5452e-04 - accuracy: 1.0000
Epoch 96/100
1/1 [==============================] - 0s 1ms/step - loss: 2.5158e-04 - accuracy: 1.0000
Epoch 97/100
1/1 [==============================] - 0s 2ms/step - loss: 2.4870e-04 - accuracy: 1.0000
Epoch 98/100
1/1 [==============================] - 0s 2ms/step - loss: 2.4591e-04 - accuracy: 1.0000
Epoch 99/100
1/1 [==============================] - 0s 1ms/step - loss: 2.4314e-04 - accuracy: 1.0000
Epoch 100/100
1/1 [==============================] - 0s 1ms/step - loss: 2.4047e-04 - accuracy: 1.0000
1/1 [==============================] - 0s 358us/step - loss: 5.2434e-04 - accuracy: 1.0000
```