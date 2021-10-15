## Facial Emotion Recognition

This is a program to recognise the facial_emotions. 
The model is trained using the `fer2013` dataset and was trained for 8 hours on Google
Colab (it took a lot of time). As the training process was really slow, the model was trained only for 30 epochs, with the accuracy of nearly 65%.

![alt text](https://www.google.com/urlsa=i&url=https%3A%2F%2Fwww.kaggle.com%2Fmsambare%2Ffer2013&psig=AOvVaw0pX3d2s_WZ9nN_jTla_6n8&ust=1634358796723000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIi_vpLLy_MCFQAAAAAdAAAAABAD)

# Description
- `facial_recognition.h5` is the final trained model. 
- `fer2013.ipynb` is the jupyter notebook, and contains the code used in training the model
-  `face_emotion.py` is the program for performing facial emotion recognition on real time.

# Set Up Instruction
1. Clone the repo.
```sh
$ git clone https://github.com/Kaushal-Dhungel/facial_emotion_recognition.git
```
2. Go to the directory
```sh
$ cd facial_emotion_recognition 
```

3. Install the dependencies
```sh
$ pip3 install numpy tensorflow opencv-python 
```

4. Run the program.
```sh
$ python3 face_emotion.py
```
