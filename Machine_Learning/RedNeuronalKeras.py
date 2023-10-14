from keras import models
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense

training_data = np.array([[0,0],[0,1],[1,0],[1,1]], np.float32)

target_data= np.array([[0],[1],[1],[0]], np.float32)

model = Sequential()
model.add(Dense(16,input_dim =2,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss = 'mean_squared_error',
              optimizer = 'adam',
              metrics=['binary_accuracy'])

model.fit(training_data,target_data,epochs=1000)

scores = model.evaluate(training_data,target_data)

print("\n%s:%.2f%%"%(model.metrics_names[1], scores[1]*100))
print(model.predict(training_data).round())

model_json = model.to_json()
with open("model.json","w") as json_file:
    json_file.write(model_json)

model.save_weights("model.h5")
print("modelo guardado")

json_file = open('model.json','r')
loaded_model_json = json_file.read()
json_file.close()

