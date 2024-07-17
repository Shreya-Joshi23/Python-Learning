# print opposite right angled triangle

def printtri(rows):
    for i in range(rows,0,-1):
        # this wont't work in c++ bcoz string multiplication not supported in c++
        print('*'*i)


rows=int(input("Enter the number of rows"))
printtri(rows)