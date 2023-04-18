import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow import keras
from keras.models import Sequential
from keras import initializers, optimizers
from keras.layers import InputLayer, Dense, LSTM, Dropout, BatchNormalization, LayerNormalization, GroupNormalization
from keras.callbacks import Callback, EarlyStopping, ReduceLROnPlateau


class Help:

    class ResetStatesCallback(tf.keras.callbacks.Callback):
        def on_epoch_end(self, epoch, logs=None):
            self.model.reset_states()
            print(" -> Resetting model states at end of epoch ", epoch)

    def __init__(self):
        # For the purpose of omitting "WARNING:absl:Found untraced functions"
        import absl.logging
        absl.logging.set_verbosity(absl.logging.ERROR)


    # Read the dataset file and seperate inputs and outputs
    def readFile(self, file, number_of_input):
        f1 = open(file, "r")
        X = []
        Y = []
        for line in f1:
            items = [int(x) for x in line.strip()] 
            X.append(items[:number_of_input])
            Y.append(items[number_of_input:])
        return X,Y

    # Concatanate (n-1)th output to (n)th inputs
    # New input ------> [ (n)th inputs + (n-1)th output ]
    def intializeDataSet(self, X, Y):
        X_ = []
        Y_ = []
        for i in range(len(X)):
            if i == 0:
                pass
            else:
                X_.append([i for i in X[i]]+[i for i in Y[i-1]])
                Y_.append([i for i in Y[i]])
        return X_,Y_

    # Dataset reshaping/ converting 2D input array to 3D array
    # 3D array ------> [Samples, Time steps, Features]
    def reArangeDataSet(self, X, Y, time_steps):
        Sequential_X = []
        Sequential_Y = Y[time_steps-1:]
        for i in range(len(X)-time_steps+1):
            Sequential_X.append(X[i:i + time_steps])
        Sequential_X = np.array(Sequential_X)
        Sequential_Y = np.array(Sequential_Y)
        return Sequential_X, Sequential_Y
    
    # Make the input for prediction
    def makeInputForPradict(self, X, Y, time_steps):
        Sequential_X = []
        for i in range(len(X)+1 - time_steps):
            Sequential_X.append(X[i:i + time_steps])
        Sequential_X = np.array([Sequential_X[-1]])
        return Sequential_X

    # creating the NN model for training
    def createModel(self, i_shape, Outputs, k_initializer, opt, b_size=1):
        model = Sequential()
        model.add(InputLayer(input_shape=i_shape,batch_size=b_size))
        model.add(LSTM(32, activation='tanh', recurrent_activation='tanh',return_sequences=False,stateful=True,kernel_initializer=k_initializer,bias_initializer ='uniform',recurrent_initializer='Zeros',dropout=0.0,recurrent_dropout=0.0))
        model.add(Dense(64, activation='tanh'))
        model.add(Dense(64, activation='tanh'))
        model.add(Dense(Outputs,activation='sigmoid'))
        model.summary()
        model.compile(loss='binary_crossentropy',optimizer=opt, metrics=['binary_accuracy'])
        return model

    # fit network / training
    def trainModel(self, model, X_train, y_train, X_val, y_val, Epochs, b_size):    
        model.fit(X_train, y_train, validation_data=(X_val, y_val), batch_size=b_size, epochs = Epochs, verbose=1, shuffle=False) # callbacks=[tensorboard_callback, early_stopping, reduce_lr, WandbCallback(), ResetStatesCallback])
        return model


    # copy weights & compile the model
    def copyWeights(self, model, newModel):
        old_weights = model.get_weights()
        newModel.set_weights(old_weights)
        newModel.compile(loss='binary_crossentropy', optimizer='rmsprop')

    def writeintialfile(self, filename, timestep):
        fr = open(filename,"r")
        count = 0
        fw = open("Laptop/DataSets/Initialization.txt","w")
        for line in fr:
            fw.write(line)
            if (count > timestep):
                break
            count = count + 1

            
    def listToString(self, listofoutput):
        output = ""
        lis = []
        for i in listofoutput[0]:
            output = output + str(round(i)) + " "
            lis.append(round(i))
        return output[:-1],lis