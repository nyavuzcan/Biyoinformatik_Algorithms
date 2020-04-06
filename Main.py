import numpy as np

from Needleman import Needleman
from ReadScoreMatrix import ReadScoreMatrix
from NeedlemanScore import NeedlemanScore
from ReadScoreMatrixForSmith import ReadScoreMatrixForSmith
with open('dna_sequences.txt') as f:
    lines = f.readlines()

DNA_ARRAY = lines[0]
lines.pop(0)

# !!!BOŞLUK CEZA PUANI BELİRTİLMEMİŞ FAKAT İNTERNETTE ARAŞTIRDIĞIM KADARIYLA
# BOŞL İLK SATIR VE SÜTÜNLAR '-' BOŞLUK İFADESİ İLE ÇALIŞMAKTA
# BEN İLK CEZA PUANLARINI '-1' DAHA SONRA BİRBİRLERİYLE EŞLEŞMEME DURUMLARINI
# SİZİN BELİRTTİĞİNİZ ŞEKİLDE DİNAMİK OLARAK SCORE_MATRİX.TXT FORMATINDA OKUDUM
# ALGORİTMA SAĞLIKLI BİR ŞEKİLDE ÇALIŞMAKTADIR
# readScoreMatrix.operator() PARAMETRE OLARAK 0,17,34,51 GÖNDERİLEREK TÜM SCORE MATRİXLER İÇİN
# AYRI AYRI OUTPUTLAR ALMAK MÜMKÜNDÜR. İYİ ÇALIŞMALAR.


def putFirstPenalty(matrix):
    for i in range(51):
        matrix[i + 1][1] = -1
        matrix[1][i + 1] = -1
    return matrix


def createMatrix(line):
    w, h = 52, 52
    matrix = [['x' for x in range(w)] for y in range(h)]
    for i in range(len(DNA_ARRAY) - 1):
     matrix[0][i + 2] = DNA_ARRAY[i]

    for i in range(len(line) - 1):
        matrix[i + 2][0] = line[i]
        matrix[0][1] = '-'
        matrix[1][0] = '-'

    return putFirstPenalty(matrix)

def putPenaltyForSmith(matrix):
    for i in range(51):
        matrix[i + 1][1] = 0
        matrix[1][i + 1] = 0
    return matrix

def createMatrixForSmith(line):

    w, h = 52, 52
    matrix = [['x' for x in range(w)] for y in range(h)]
    for i in range(len(DNA_ARRAY) - 1):
     matrix[0][i + 2] = DNA_ARRAY[i]

    for i in range(len(line) - 1):
        matrix[i + 2][0] = line[i]
        matrix[0][1] = '-'
        matrix[1][0] = '-'

    return putPenaltyForSmith(matrix)




def calculateForLine(lines):
    for j in range(len(lines)):
        matrix= createMatrix(lines[j])
        readScoreMatrix = ReadScoreMatrix()
        #operator parameter olarak 0,17,34,51 alabilir scorematrix deigiskliği için
        scoreMatrixLine = readScoreMatrix.operator(0)
        needleman = Needleman(matrix, scoreMatrixLine)
        prMatrix = needleman.calculateMatris()
        needlemanScore = NeedlemanScore(prMatrix,1,scoreMatrixLine)



def calculateForSmithLine(lines):
    for j in range(len(lines)):
        matrixSmith=createMatrixForSmith(lines[j])
        readScoreMatrixSmith = ReadScoreMatrixForSmith()
        SmithWaterScoreLine=  readScoreMatrixSmith.operator(0)
        needlemanSmith = Needleman(matrixSmith, SmithWaterScoreLine)
        prMatrixSmith = needlemanSmith.calculateMatris()
        NeedlemanScore(prMatrixSmith,0,SmithWaterScoreLine)

calculateForLine(lines)
calculateForSmithLine(lines)
