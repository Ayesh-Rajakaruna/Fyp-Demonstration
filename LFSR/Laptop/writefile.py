from train import Train
from data import Data

class WriteFile:
    def __init__(self):
        self.traninDataSet = Train()
        self.Data = Data()
        
    def start(self, Name= "Data"):
        self.count = 1
        self.fileNum = 1
        self.Name = Name
        self.fw = open("./Laptop/DataSets/{}{}.txt".format(self.Name, self.fileNum), "w")
    
    def write(self,data):
        if(self.count % self.Data.get_data_per_one_file() == 0):
            self.fileNum += 1
            self.fw.close()
            Train.traingstart(self.traninDataSet, filename="./Laptop/DataSets/{}{}.txt".format(self.Name, self.fileNum-1) )
            self.fw = open("./Laptop/DataSets/{}{}.txt".format(self.Name, self.fileNum), "w")
        self.fw.write(data+"\n")
        self.count += 1
<<<<<<< HEAD
        
=======
>>>>>>> 647db29cf017f626375f65fe19720d0fc714bc2e
    def getListOfInitialization(self):
        ListOfInitialization = []
        ReadFile = open("Laptop/DataSets/Initialization.txt","r")
        for line in ReadFile:
            ListOfInitialization.append(line[:-1])
<<<<<<< HEAD
        return ListOfInitialization
=======
        return ListOfInitialization
>>>>>>> 647db29cf017f626375f65fe19720d0fc714bc2e
