import random 
import time

unsorted = []
sortedRev = []
cont = True
highest = -10
position = 0

def generateList(ground, roof, limit):
    for i in range(limit):
        x = random.randint(ground,  roof)
        unsorted.append(x)    

def sort(highest):
    lenOfList = len(unsorted)
    for index in range(lenOfList):
        for i in range(len(unsorted)):
            x = unsorted[i]
            if (x >= highest):
                highest = x
                position = i
        del unsorted[position]
        print(str(unsorted))
        # time.sleep(1)
        sortedRev.append(highest)
        highest = -10
    sorted = sortedRev[::-1]
    return sorted

def main():
    ground = int(input("What is the lowest number in your list?"))
    roof = int(input("What is the maximum limit?"))
    limit = int(input("How many items should the list have?"))
    generateList(ground, roof, limit)
    print("This is your list: " + str(unsorted))
    input("Press 'ENTER' to sort.")
    sorted = sort(highest)
    print("\n \n \n \n \n")
    print("This is your sorted list:\n")
    print(sorted)

if __name__ in "__main__":
    main()