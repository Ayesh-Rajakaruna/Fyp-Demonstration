class ReadFile:
    def __init__(self):
        from InputGenerate import InputGenerate
        InputGenerate = InputGenerate()
        InputGenerate.mainLogic()
        self.lis = []
    def Read(self):
        with open('./InputFile/input.txt', 'r') as file:
            for line in file:
                self.lis.append(line)
        return self.lis