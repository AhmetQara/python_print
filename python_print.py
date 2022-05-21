
def myFunc(n):
    
    for i in range(1, n):
        print(i, end='')
        i+=1
    return n
        
if __name__ == '__main__':
    n = int(input())
    

print(myFunc(n))
