class ReadScoreMatrix:
    lines = None
    scoreLines= ["" for x in range(48)]


    def __init__(self):
        with open('scorematrix.txt') as f:
            self.lines = f.readlines()

        print(self.operator(0))


    def operator(self,i):
        print(len(self.lines))
        print(len(self.lines[1]))
        y=0
        z=0
        for self.i in range(len(self.lines)):
            if(len(self.lines[i])==4):
                self.scoreLines[z]=self.lines[i][y]
                z+=1
                self.scoreLines[z]=self.lines[i][y+1]
                z+=1
                self.scoreLines[z]=int(self.lines[i][y+2])
                z+=1
                i+=1
            elif(len(self.lines[i])==5):
                 self.scoreLines[z]=self.lines[i][y]
                 z+=1
                 self.scoreLines[z]=self.lines[i][y+1]
                 z+=1
                 say = int(self.lines[i][y+3])
                 say*=(-1)
                 self.scoreLines[z]=say
                 z+=1
                 i+=1
            else:return self.parseScoreMatrix(self.scoreLines)

    def parseScoreMatrix(self,scoreLines):
        my_dict = {}
        i=0
        while i<46:
         my_dict.update({scoreLines[i]+scoreLines[i+1]:scoreLines[i+2]})
         i+=3
        print(my_dict)
        return my_dict
