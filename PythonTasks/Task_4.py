# Task 4 Write a Python program to count the number 4 in a given list

NumberToSearch = 4

MyList1 = [1,2,3,4,5,6,7,8,9,0,23,344,55,22]
MyList2 = [1,2,3,5,6,7,8,9,0,23,344,55,22]
MyList3 = [1,2,4,4,6,7,4,9,0,4,344,55,22]

def SearchForNumber (MyList):
    counter = 0
    for i in MyList:
        if i == NumberToSearch:
            counter +=1
    else:
        print(f"there is {counter} of Number {NumberToSearch} in the {MyList}")


SearchForNumber(MyList1)
SearchForNumber(MyList2)
SearchForNumber(MyList3)