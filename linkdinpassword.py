# a person forget the password of there linkdin account but he know the reverse ascii code of there password
# you have to help him to bring back the password of there account

password = input()
s = password[::-1]
i = 0
res = ""
while(i<len(s)-1):
    x = s[i]+s[i+1]
    if x == "32":
        res = res + " "
    elif int(x) in range(65,91) or int(x) in range (97,100):
        res = res + chr(int(x))
    elif i+2<len(s):
        x = x+s[i+2]
        res = res + chr(int(x))
        i+=1
    i+=2
print(res)

