class InputGenerate:
    def __init__(self):
        self.CurrentList = ["11", "11", "11", "11"]
        self.angle = [10, 5, 5, 3]
        self.fileWrite = open("./InputFile/input.txt", "w")
        for _ in range(1):
            self.fileWrite.write(self.ListToString(self.CurrentList)+"\n")


    def ListToString(self,lis):
        string = ""
        for i in lis:
            string = string + i + " "
        return string[:-1]
    
    def mainLogic(self):
        with open('./InputFile/code.txt', 'r') as file:
            for line in file:
                servernum = int(line[0]) -1
                serverstage = line[1]
                if serverstage == "1":
                    self.CurrentList[servernum] = "10"
                if serverstage == "0":
                    self.CurrentList[servernum] = "00"
                for j in range(self.angle[servernum]):
                    self.fileWrite.write(self.ListToString(self.CurrentList)+"\n")
                self.CurrentList[servernum] = "11"


