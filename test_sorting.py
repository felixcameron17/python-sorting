from random import randint, random
from insertionSort import insertionSort
from time import time

averagecase= [randint(1,10000) for _ in range(1000)]
bestcase= sorted(averagecase)
worstcase= sorted(averagecase, reverse=True)

def test_insertionWorst():
    start= time()
    assert insertionSort(worstcase) == worstcase
    print(time()-start)

def test_insertionBest():
    start= time()
    assert insertionSort(bestcase) == bestcase
    print(time()-start)

def test_insertionAvg():
    start= time()
    assert insertionSort(averagecase) == averagecase
    print(time()-start)