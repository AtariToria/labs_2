#coding:utf8
from memory_profiler import profile

def mergeSort(myList):
    if len(myList) <= 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)
        myList = mergeSort(left, right)
        for i in range(len(left)):
            left[i] = myList[i]
        # Two iterators for traversing the two halves
        i = 0
        j = 0
        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                myList[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1
        return myList



##myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
##mergeSort(myList)
##print(myList)

@profile
def main():
    f = open('lab_2/output.txt', 'r')
    lines = f.read().split('\n')
    f.close()
    s = open('lab_2/sort.txt', 'w')
    mergeSort(lines)
    for stroka in lines:
        stroka = stroka.split()
        mergeSort(stroka)
        for word in stroka:
            s.write(word + ' ')
        s.write('\n')
    s.close()


if __name__ == "__main__":
    main()



