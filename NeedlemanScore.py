class NeedlemanScore:
    matrix = None
    whichOne = None
    def __init__(self, matrix,whichOne):
        self.whichOne=whichOne
        self.matrix=matrix
        self.calculate()

    def calculate(self):
        xIndis=51
        yIndis=51
        my_dict = {}
        valueIn=self.matrix[xIndis][yIndis]
        i=0
        while 1:
         try:
            my_dict.update({str(i)+' '+self.matrix[0][yIndis]+' '+self.matrix[xIndis][0]:valueIn})
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
            if(self.matrix[xIndis][yIndis]=='x'):
                continue
            valueIn=self.matrix[xIndis][yIndis]

         except TypeError:
                break
        return self.conclusionPrint(my_dict,self.matrix)

    def score(self,my_dict):
        return sum(my_dict.values())

    def conclusionPrint(self,my_dict,matrix):

        cs=[]
        for i in range(len(my_dict)-1, 0,-1):

         spt=str(list(my_dict)[i]).split(' ')
         count=spt[0]
         ourSequence=spt[1]
         otherSequence=spt[2]
         if(ourSequence!=otherSequence):
             cs.append('-')
         else: cs.append(otherSequence)

        del matrix[0][0]
        del matrix[0][0]
        if(self.whichOne==1):
         print('##needleman wunsch##')
        else:
         print('##Smith Waterman##')
        print(matrix[0])
        print(cs)
        print(self.score(my_dict))
        print('####################################')


