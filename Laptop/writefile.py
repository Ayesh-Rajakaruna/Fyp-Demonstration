from train import Train

class WriteFile:
    def __init__(self):
        self.traninDataSet = Train()
        
    def start(self, Name= "Data"):
        self.count = 1
        self.fileNum = 1
        self.Name = Name
        self.fw = open("./Laptop/DataSets/{}{}.txt".format(self.Name, self.fileNum), "w")
    
    def write(self,data):
        if(self.count % 25000 == 0):
            self.fileNum += 1
            self.fw.close()
            Train.traingstart(self.traninDataSet, "./Laptop/DataSets/{}{}.txt".format(self.Name, self.fileNum - 1) )
            self.fw = open("./Laptop/DataSets/{}{}.txt".format(self.Name, self.fileNum), "w")
        self.fw.write(data+"\n")
        self.count += 1
