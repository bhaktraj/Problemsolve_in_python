##################################################################################################################################
# A string is is taken from user you have to check that this string contain special character or not if is contain
# special character than print reverse of string otherwishe print string as well as user input(no change)
#################################################################################################################################


def stringcheck(n):
    for i in range(0,len(n)):
        n1 = ord(n[i])
    if n1 in range (65,91) or n1 in range (97,123):
        return True
    else:
        return False 
n = input()

result = stringcheck(n)
if result is True:
    print(n)
else:
    print(n[::-1])