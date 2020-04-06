class NeedlemanScore:
    matrix = None
    whichOne = None
    scoreMatrixLine=None
    def __init__(self, matrix,whichOne,scoreMatrixLine):
        self.whichOne=whichOne
        self.matrix=matrix
        self.scoreMatrixLine=scoreMatrixLine
        self.calculate()

    def calculate(self):
        xIndis=51
        yIndis=51
        my_dict = {}
        valueIn=self.matrix[xIndis][yIndis]
        i=0
        while 1:
         try:
            my_dict.update({str(xIndis)+' '+str(yIndis)+' '+self.matrix[0][yIndis]+' '+self.matrix[xIndis][0]:valueIn})
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
            if(self.matrix[xIndis][yIndis]=='x'or self.matrix[xIndis][yIndis]=='-'):
                continue
            valueIn=self.matrix[xIndis][yIndis]

         except TypeError:
                break
        return self.conclusionPrint(my_dict,self.matrix)

    def score(self,my_dict):
        sumofScore=0
        for i in range(len(my_dict)-1, 0,-1):
         spt=str(list(my_dict)[i]).split(' ')
         count=spt[0]
         ourSequence=spt[2]
         otherSequence=spt[3]
         if(otherSequence=='-' or ourSequence=='-' or
         ourSequence=='x' or otherSequence=='x'
         ):
             continue
         sumofScore +=  self.scoreMatrixLine[ourSequence+otherSequence]

        return sumofScore

    def conclusionPrint(self,my_dict,matrix):
        ourSequenceArr=[]
        otherSequenceArr=[]
        m=2
        n=2

        for z in range(len(my_dict)-1, 0,-1):
            spt=str(list(my_dict)[z]).split(' ')
            xIndis=int(spt[0])
            yIndis=int(spt[1])
            ourSequence=spt[2]
            otherSequence=spt[3]
            sptNext=str(list(my_dict)[z-1]).split(' ')
            xIndisNext=int(sptNext[0])
            yIndisNext=int(sptNext[1])


            if(xIndis - xIndisNext== -1 and yIndis- yIndisNext ==-1):
                ourSequenceArr.append(matrix[0][xIndis])
                otherSequenceArr.append(matrix[yIndis][0])
            elif(xIndis - xIndisNext==-1):
                ourSequenceArr.append(matrix[0][xIndis])
                otherSequenceArr.append('-')
            elif(yIndis-yIndisNext==-1):
                ourSequenceArr.append('-')
                otherSequenceArr.append(matrix[yIndis][0])



        if(self.whichOne==1):
         print('##needleman wunsch##')
        else:
         print('##Smith Waterman##')

        print(ourSequenceArr)
        print(otherSequenceArr)
        print(self.score(my_dict))
        print('####################################')




