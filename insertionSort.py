import time

startTime = time.time()

values = []

def insertionSort(arr):
    for i in range(1, len(arr)):
        item = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > item:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = item

    return arr


fileObj = open('data.txt', 'r')
values = fileObj.read().splitlines()
fileObj.close()
for i in range(len(values)):
    values[i] = float(values[i])

insertionSort(values)

endTime = str(time.time() - startTime)

print('\nsorted:\n')
print(values)

print('time elapsed: ' + endTime)

