#printing i square


if __name__ == '__main__':
    n = int(input().strip())
    for i in range(n):
        print(i**2)

#printing numbers

if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1,n+1):
        print(i,end="")


#leap year
def is_leap(year):
    leap = False
    if year%4==0:
        leap=True
    if year%100==0:
        if year%400==0:
            leap=True
        else:
             leap=False   
    
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))
