def armstrong_number(n):
    sum = 0
    lengthof_digit= len(str(n))
    n1 = n
    while(n>0):
        digit = n%10
        sum = sum + digit**lengthof_digit
        n = n//10
    if(n1==sum):
        print("armstrong")
    else:
        print("Not ArmStrong")

n = int(input())
armstrong_number(n)