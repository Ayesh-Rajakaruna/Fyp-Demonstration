import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow import keras
from keras.models import Sequential
from keras import initializers, optimizers
from keras.layers import InputLayer, Dense, LSTM, Dropout, BatchNormalization, LayerNormalization, GroupNormalization
from keras.callbacks import Callback, EarlyStopping, ReduceLROnPlateau

from help import Help

class Train():

    def __init__(self):
        self.batch_size = 100
        self.number_of_inputs = 1
        self.number_of_outputs = 16
        self.time_steps = 16
        self.epochs = 10
        self.lr = 0.01
        self.NeuralFunction = Help()
    
    def traingstart(self, filename):

        self.NeuralFunction.writeintialfile(self.NeuralFunction, filename, self.timestep)

        opt = optimizers.Adam(learning_rate=self.lr,decay=0.04)
        k_initializer=initializers.HeNormal()

        X_train,Y_train = self.NeuralFunction.readFile(self.NeuralFunction, filename, self.number_of_inputs)
        X_train_, Y_train_ = self.NeuralFunction.intializeDataSet(self.NeuralFunction, X_train,Y_train)
        Sequential_X_train, Sequential_Y_train = self.NeuralFunction.reArangeDataSet(self.NeuralFunction, X_train_, Y_train_, self.time_steps)
        len_of_x_train = int(len(Sequential_X_train)*0.8)

        Sequential_X_val = Sequential_X_train[len_of_x_train:]
        Sequential_Y_val = Sequential_Y_train[len_of_x_train:]
        Sequential_X_train = Sequential_X_train[:len_of_x_train]
        Sequential_Y_train = Sequential_Y_train[:len_of_x_train]
        X_train, X_val, y_train, y_val = Sequential_X_train[len(Sequential_X_train)%self.batch_size:], Sequential_X_val[len(Sequential_X_val)%self.batch_size:], Sequential_Y_train[len(Sequential_Y_train)%self.batch_size:], Sequential_Y_val[len(Sequential_Y_val)%self.batch_size:]

        model = self.NeuralFunction.createModel(self.NeuralFunction, Sequential_X_train[0].shape, self.number_of_outputs, k_initializer, opt,  self.batch_size)
        try:
            model.load_weights('./Laptop/Model/Weights/my_model_weights.h5')
        except:
            pass
        model = self.NeuralFunction.trainModel(self.NeuralFunction, model, X_train, y_train, X_val, y_val, self.epochs, self.batch_size)
        model.save_weights('./Laptop/Model/Weights/my_model_weights.h5')
        # For wights & model
        # model.save('NN for testing/saved_model/my_model.hdf5')
        # model.save_weights('NN for testing/saved_model/my_model_weights.h5')