string1 = str(input())
string2 = str(input())
len1 = len(string1)
len2 = len(string2)
count = 0
for i in range(0, (len1 - len2 + 1)):
    temp = string1[i:i+len2]
    print(temp)
    if temp == string2:
        count += 1
print(count)
