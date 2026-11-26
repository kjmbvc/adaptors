n = int(input())

def print_rectangle(n):
    num = 1
    for _ in range(n):         
        for _ in range(n):      
            print(num, end=" ") 
            num += 1
            if num > 9:        
                num = 1
        print()                 

print_rectangle(n)