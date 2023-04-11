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

class Train():

    def __init__(self):
        data = Data()
        self.batch_size = data.get_batch_size
        self.number_of_inputs = data.get_number_of_inputs
        self.number_of_outputs = data.get_number_of_outputs
        self.time_steps = data.get_time_steps
        self.epochs = data.get_epochs
        self.lr = data.get_lr
        self.NeuralFunction = Help()
    
    def traingstart(self, filename):

        self.NeuralFunction.writeintialfile(filename, self.time_steps)

        opt = optimizers.Adam(learning_rate=self.lr,decay=0.04)
        k_initializer=initializers.HeNormal()

        X_train,Y_train = self.NeuralFunction.readFile(filename, self.number_of_inputs)
        X_train_, Y_train_ = self.NeuralFunction.intializeDataSet(X_train,Y_train)
        Sequential_X_train, Sequential_Y_train = self.NeuralFunction.reArangeDataSet(X_train_, Y_train_, self.time_steps)
        len_of_x_train = int(len(Sequential_X_train)*0.8)

        Sequential_X_val = Sequential_X_train[len_of_x_train:]
        Sequential_Y_val = Sequential_Y_train[len_of_x_train:]
        Sequential_X_train = Sequential_X_train[:len_of_x_train]
        Sequential_Y_train = Sequential_Y_train[:len_of_x_train]
  
        Training_data_set_size = len(Sequential_X_train) - len(Sequential_X_train)%self.batch_size
        Validation_data_set_size = len(Sequential_X_val) - len(Sequential_X_val)%self.batch_size

        X_train = Sequential_X_train[:Training_data_set_size]
        Y_train = Sequential_Y_train[:Training_data_set_size]
        X_val = Sequential_X_val[:Validation_data_set_size]
        Y_val = Sequential_Y_val[:Validation_data_set_size]

        for i,j in zip(X_train[:50], Y_train[:50]):
            print(i, " ----> ", j)

        model = self.NeuralFunction.createModel(Sequential_X_train[0].shape, self.number_of_outputs, k_initializer, opt,  self.batch_size)            
        try:
            model.load_weights('./Laptop/Weights/my_model_weights.h5')
        except:
            pass
        model = self.NeuralFunction.trainModel(model, X_train, Y_train, X_val, Y_val, self.epochs, self.batch_size)
        model.save_weights('./Laptop/Weights/my_model_weights.h5')
        # For wights & model
        # model.save('NN for testing/saved_model/my_model.hdf5')
        # model.save_weights('NN for testing/saved_model/my_model_weights.h5')
"""
train = Train()
train.traingstart(filename="./Laptop/DataSets/counter.txt")
"""        