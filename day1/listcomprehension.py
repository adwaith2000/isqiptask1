'''Let's learn about list comprehensions! You are given three integers x,y and z 
representing the dimensions of a cuboid along with an intege nr . You have to
 print a list of all possible coordinates given by (i,j,k) on a 3D grid where
 the sum of i+j+k is not equal to n. Here, i<=x,j<=y,k<=z'''



if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    l.append([i,j,k])
    print (l)

