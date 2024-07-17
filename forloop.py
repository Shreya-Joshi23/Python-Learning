# //print pattern - for loop

def printpattern(rows):
    for i in range(1,rows+1,+1):
        print(' '*(rows-i)+str(i)*i)


printpattern(5)