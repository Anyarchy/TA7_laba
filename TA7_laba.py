from itertools import islice
import math

def HashFunctionDivision(key, m):
    return key%m

def HashFunctionMultiplication(key, m):
    return int((key*((math.sqrt(5)-1)/2)%1)*m)

def HashInsertDivision(T, key, m):
    collisions = 0
    T[HashFunctionDivision(key, m)].append(key)
    if len(T[HashFunctionDivision(key, m)])!=1:
        collisions+=1
    return collisions

def HashSearchDivision(key, m, T):
    if key in T[HashFunctionDivision(key, m)]:
            return True
    return False

def HashInsertMultiplication(T, key, m):
    collisions = 0
    T[HashFunctionMultiplication(key, m)].append(key)
    if len(T[HashFunctionMultiplication(key, m)])!=1:
        collisions+=1
    return collisions


def HashSearchMultiplication(key, m, T):
    if key in T[HashFunctionMultiplication(key, m)]:
            return True
    return False

def main():
    file = open('MyInput.txt', 'r')
    A = []
    Sums = []
    line = file.readline().split()
    n = int(line[0])
    k = int(line[1])
    for el in islice(file, 0, n):
        A.append(int(el)) 

    for el in islice(file, 0, k):
        Sums.append(int(el)) 
    file.close
    m = 3*len(A)

    file_res = open('MyOutput.txt', 'w')

    collisions_d = 0
    file_res.write(str("Хешування діленням")+"\n")


    table_div = [[]for i in range(m) ]
    for x in A:
        collisions_d += HashInsertDivision(table_div, x, m)
    file_res.write(str(collisions_d)+"\n")
    for i in Sums:
        bool = True
        for x in range(len(A)):
            y = i - A[x]
            if(HashSearchDivision(y, m,table_div)):
               file_res.write(str(A[x])+" "+str(y)+"\n")
               bool = False
               break
        if bool:
            file_res.write(str("0 0")+"\n")  
    file_res.write("\n")         

    collisions_m = 0
    file_res.write(str("Хешування множенням")+"\n")

    table_mult = [[]for i in range(m) ]

    for x in A:
        collisions_m += HashInsertMultiplication(table_mult, x, m)
    
    file_res.write(str(collisions_m)+"\n")
    for i in Sums:
        bool = True
        for x in range(len(A)):
            y = i - A[x]
            if(HashSearchMultiplication(y, m,table_mult)):
               file_res.write(str(A[x])+" "+ str(y)+"\n")
               bool = False
               break
        if bool:  
            file_res.write(str("0 0")+"\n")  

    file_res.close()

if __name__=="__main__":
    main()
