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