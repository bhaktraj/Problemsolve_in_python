def passflip(n):
    count = 0
    for i in range(0, len(n)-1):

        if n[i]!=n[i+1]:
            count+=1
        i=i+2
    return count

n = input()
result = passflip(n)
print(result)