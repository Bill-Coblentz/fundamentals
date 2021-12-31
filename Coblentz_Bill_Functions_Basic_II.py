#1 Countdown
def countdown(x):
    mylist = []
    for i in range(x + 1):
        mylist.append(i)
    mylist.reverse()
    print(mylist)
countdown(5)

#2 Print and Return
cars=[3,4]
def print_n_return(somelist):
    print(somelist[0])
    return somelist[1]
b = print_n_return(cars)
print(b)

#3 First plus length
testList = [3, 2, 3, 7]
def first_plus_length(alist):
    b = (len(alist))
    print(alist[0] + b)
first_plus_length(testList)

#4 Values greater than second
trucks = [1, 2, 3, 4, 5, 6, 8]
jeeps = [1,2]
def greater_than_second(firstList):
    secondList = []
    a = firstList[1]
    for x in firstList:
        if x > a:
            secondList.append(x)
    if len(secondList) < 2:
        return False
    print(len(secondList))
    print(secondList)           
b = greater_than_second(jeeps)
print(b)

#5 This length that value
def length_and_value(size, value):
    thisArray = []
    for x in range(size):
        thisArray.append(value)
    print(thisArray)
length_and_value(7, 3)