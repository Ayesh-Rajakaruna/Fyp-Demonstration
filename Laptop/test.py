import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow import keras
from keras.models import Sequential
from keras import initializers, optimizers
from keras.layers import InputLayer, Dense, LSTM, Dropout, BatchNormalization, LayerNormalization, GroupNormalization
from keras.callbacks import Callback, EarlyStopping, ReduceLROnPlateau

from help import Help

class Test:

    def __init__(self):
        self.batch_size = 100
        self.number_of_inputs = 1
        self.number_of_outputs = 16
        self.time_steps = 16
        self.epochs = 10
        self.lr = 0.01
        self.filename = "Laptop/DataSets/Initialization.txt"
        self.NeuralFunction = Help()
        self.X_train,self.Y_train = self.NeuralFunction.readFile(self.NeuralFunction, self.filename, self.number_of_inputs)
        self.model == None
    
    def predictresult(self, inputData):

        
        self.X_train.append([int(x) for x in inputData.split()])
        self.Y_train.append([0 for y in range(self.number_of_outputs)])
        self.X_train.pop(0)
        self.Y_train.pop(0)

        X_train_, Y_train_ = self.NeuralFunction.intializeDataSet(self.NeuralFunction, self.X_train,self.Y_train)
        Sequential_X_train = self.NeuralFunction.makeInputForPradict(self.NeuralFunction, X_train_, Y_train_, self.time_steps)

        opt = optimizers.Adam(learning_rate=self.lr,decay=0.04)
        k_initializer=initializers.HeNormal()

        if self.model == None:
            self.model = self.NeuralFunction.createModel(self.NeuralFunction, Sequential_X_train[0].shape, self.number_of_outputs, k_initializer, opt,  self.batch_size)
            self.model.load_weights('./Laptop/Model/Weights/my_model_weights.h5')
        else:
            pass
        
        return self.model.predict(Sequential_X_train)
        # For wights & model
        # model.save('NN for testing/saved_model/my_model.hdf5')
        # model.save_weights('NN for testing/saved_model/my_model_weights.h5')