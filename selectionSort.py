import time


startTime = time.time()
values = []
sortedValues = []

def selectionSort(arr):
    
    for i in range(len(arr)):
        smallestVal = min(arr)
        sortedValues.append(smallestVal)
        values.remove(min(values))


    return arr

        



fileObj = open('data.txt', 'r')
values = fileObj.read().splitlines()
fileObj.close()

for i in range(len(values)):
    values[i] = float(values[i])


selectionSort(values)
values = sortedValues

endTime = str(time.time() - startTime)

print('\nsorted:\n')
print(values)

print('time elapsed: ' + endTime)