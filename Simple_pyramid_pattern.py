'''
*
* *
* * *
* * * *
* * * * *
'''

def star_simple_pyramid(n):
    for i in range(1,n+1):
        for j in range(0,i):
            print('*'*1,end="")
        print()

star_simple_pyramid(5)