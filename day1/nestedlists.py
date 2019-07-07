'''Given the names and grades for each student in a Physics class of N

students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.'''


if __name__ == '__main__':
    l=[] 
    p=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
    l.sort(key=lambda x:x[1])
    for i in l:
        p.append(i[1])
    p=sorted(list(set(p)))
    k=[]
    for i in l:
         if i[1]==p[1]:
            k.append(i[0])      
    k.sort()
    print ("\n".join(k))
    
