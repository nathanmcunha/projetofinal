# -*- coding: utf-8 -*-
"""
Author: Andre Pacheco
Email: pacheco.comp@gmail.com

An example of how to use the TOPSIS class.

"""

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from topsis.TOPSIS import TOPSIS

import numpy as np
import pandas as pd

def getTopSisDataframe(filename):
    A = TOPSIS(filename)
    A.normalizeMatrix()
    A.introWeights()
    A.getIdealSolutions()
    A.distanceToIdeal()
    A.relativeCloseness()
    # Showing the results
    print(A.rCloseness)
    alternatives = np.array(['A1', 'A2', 'A3'])
    resultado = A.getnumpyarray()
    resultDataFrame = pd.DataFrame(resultado, index=alternatives)
    return resultDataFrame.to_html()

def runTaskTopsis():
    A = TOPSIS('file2.txt')
    A.normalizeMatrix()
    A.introWeights()
    A.getIdealSolutions()
    A.distanceToIdeal()
    A.relativeCloseness()
    # Showing the results
    print(A.rCloseness)
    Alternatives = np.array(['A1', 'A2', 'A3'])
    A.plotRankBar(Alternatives)


# If you don't wanna use the file .txt, you can set the values
# as lists or numpy arrays

def gettopsisdfbyarray():
    global resultDataFrame
    w = np.array([0.3, 0.05, 0.6, 0.05])
    cb = np.array([1, 0, 1, 0])
    matrix = np.array([
        [15, 6, 25000, 7],
        [12, 7, 35000, 7],
        [10, 9, 55000, 8]
    ])
    B = TOPSIS(matrix, w, cb)
    B.normalizeMatrix()
    B.introWeights()
    B.getIdealSolutions()
    B.distanceToIdeal()
    B.relativeCloseness()
    resultado = B.getnumpyarray()
    alternatives = np.array(['A1', 'A2', 'A3'])
    resultDataFrame = pd.DataFrame(resultado, index=alternatives)
    return resultDataFrame.to_html()



