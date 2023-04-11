import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow import keras
from keras.models import Sequential
from keras import initializers, optimizers
from keras.layers import InputLayer, Dense, LSTM, Dropout, BatchNormalization, LayerNormalization, GroupNormalization
from keras.callbacks import Callback, EarlyStopping, ReduceLROnPlateau

from help import Help
from data import Data

class Test:

    def __init__(self):
        data = Data()
        self.batch_size = 1
        self.number_of_inputs = data.get_number_of_inputs
        self.number_of_outputs = data.get_number_of_outputs
        self.time_steps = data.get_time_steps
        self.lr = data.get_lr
        self.filename = "Laptop/DataSets/Initialization.txt"
        self.NeuralFunction = Help()
        
        self.opt = optimizers.Adam(learning_rate=self.lr,decay=0.04)
        self.k_initializer=initializers.HeNormal()

    def makeIntialzationList(self):
        self.X_train,self.Y_train = self.NeuralFunction.readFile(self.filename, self.number_of_inputs)
        self.X_train_, self.Y_train_ = self.NeuralFunction.intializeDataSet(self.X_train,self.Y_train)


        self.Input_Data_For_Prediction = self.NeuralFunction.makeInputForPradict(self.X_train_, self.Y_train_, self.time_steps)
        print(self.X_train_)
        print(self.Input_Data_For_Prediction)
        self.model = self.NeuralFunction.createModel(self.Input_Data_For_Prediction[0].shape, self.number_of_outputs, self.k_initializer, self.opt,  self.batch_size)
        self.model.load_weights('./Laptop/Weights/my_model_weights.h5')
    
    def predictresult(self, inputData):

        self.X_train.append([int(x) for x in inputData.split()])
        self.Y_train.append([])
        self.X_train.pop(0)
        self.Y_train.pop(0)

        self.X_train_, self.Y_train_ = self.NeuralFunction.intializeDataSet(self.X_train,self.Y_train)
        self.Input_Data_For_Prediction = self.NeuralFunction.makeInputForPradict(self.X_train_, self.Y_train_, self.time_steps)

        predicted_result = self.model.predict(self.Input_Data_For_Prediction)
        predicted_result, predictresultlist = self.NeuralFunction.listToString(predicted_result)

        self.Y_train[-1] = predictresultlist
        print(self.Input_Data_For_Prediction[0], " ---> ", np.array(predictresultlist))
      
        return predicted_result
        # For wights & model
        # model.save('NN for testing/saved_model/my_model.hdf5')
        # model.save_weights('NN for testing/saved_model/my_model_weights.h5')
        
"""
test = Test()
test.makeIntialzationList()
while True:
    i = input("Give Input: ")
    test.predictresult(i)
    print(" ")
"""