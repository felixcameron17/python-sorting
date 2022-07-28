import time

startTime = time.time()

values = []

def bubbleSort(arr):

    swapped = False

    for n in range(len(arr)-1, 0, -1):

        for i in range(n):
            if arr[i] < arr[i + 1]:
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

            if not swapped:
                return arr
    return arr


fileObj = open('data.txt', 'r')
values = fileObj.read().splitlines()
fileObj.close()

for i in range(len(values)):
    values[i] = float(values[i])


bubbleSort(values)

endTime = str(time.time() - startTime)

print('\nsorted:\n')
print(values)

print('time elapsed: ' + endTime)


