string = input()
input2 = input()
Input = input2.split(" ")
int1 = int(Input[0])
char1 = Input[1]
str_lst = list(string)
if int1 in range(0, len(string)):
    str_lst[int1] = char1
    string2 = ''.join(str_lst)
    print(string2)
