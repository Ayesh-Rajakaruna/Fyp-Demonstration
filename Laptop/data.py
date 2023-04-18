class Data:
    def __init__(self):
        self.__batch_size = 50
        self.__number_of_inputs = 1
        self.__number_of_outputs = 16
        self.__time_steps = 10
        self.__epochs = 10
        self.__lr = 0.01
        self.__number_of_data_point = 10000
    
    def get_batch_size(self):
        return self.__batch_size
    
    def get_number_of_inputs(self):
        return self.__number_of_inputs
    
    def get_number_of_outputs(self):
        return self.__number_of_outputs
    
    def get_time_steps(self):
        return self.__time_steps
    
    def get_epochs(self):
        return self.__epochs
    
    def get_lr(self):
        return self.__lr
    
    def get_number_of_data_point(self):
        return self.__number_of_data_point