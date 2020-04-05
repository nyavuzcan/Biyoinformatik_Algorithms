class NeedlemanScore:
    matrix = None
    def __init__(self, matrix):
        self.matrix=matrix
        self.calculate()

    def calculate(self):
        xIndis=51
        yIndis=51
        my_dict = {}
        valueIn=self.matrix[xIndis][yIndis]
        i=0
        while 1:

            my_dict.update({str(i)+self.matrix[0][yIndis]+self.matrix[xIndis][0]:valueIn})
            temp=self.matrix[xIndis-1][yIndis-1]
            tempIndisX=xIndis-1
            tempIndisY=yIndis-1
            if(temp<self.matrix[xIndis][yIndis-1]):
                temp=self.matrix[xIndis][yIndis-1]
                tempIndisX=xIndis
                tempIndisY=yIndis-1
            if(temp<self.matrix[xIndis-1][yIndis]):
                temp=self.matrix[xIndis-1][yIndis]
                tempIndisX=xIndis-1
                tempIndisY=yIndis


            xIndis=tempIndisX
            yIndis=tempIndisY

            i+=1
            valueIn=self.matrix[xIndis][yIndis]


            if((xIndis==2 and (yIndis==2 or yIndis ==1))or (yIndis==2 and (xIndis==2 or xIndis==1))):
                break
        return my_dict


    def printScoreAndSequence(self,my_dict):

        print(my_dict)
