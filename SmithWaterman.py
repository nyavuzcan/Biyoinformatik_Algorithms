class SmithWaterman:
    #Bu Algoritmada Needleman ile aynı kurallar geçerlidir tek fark
    #Negatif degeler almamasıdır. Bu sebeple Needleman Class'ın dönen
    #degerlerin negatifleri 0'lanarak Smithwaterman'a uygun hale getirelerek
    #tekrar hesaplama işlemlerinin olduğu needleman' classına return ettirilmiştir.
    matrix = None
    def __init__(self,matrix):
        self.matrix=matrix



    def deleteNegatives(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                self.matrix[i+1][j+1]=0
        return self.matrix
