f = input()
Input = []
for each in range(1, int(f) + 1):
    k = int(input())
    Input.append(k)


# Input = [32, 100, 9085, 999001]


def check_for_prime(num):
    p = 0
    for i in range(2, num + 1):
        if num % i == 0:
            p += 1
    if p < 2:
        return True
    else:
        return False


list_primes = []
for each in Input:
    N = each
    if not check_for_prime(N):
        for i in range(2, N + 1):
            temp = check_for_prime(i)
            if temp:
                if i not in list_primes:
                    list_primes.append(i)
    else:
        list_primes.append(each)
# print(list_primes)

for each in Input:
    N = each
    if N not in list_primes:
        list2 = []
        for i in list_primes:
            k = 0
            temp = 1
            while temp:
                if N != 0:
                    if N % i == 0:
                        N = N / i
                        k += 1
                    else:
                        list2.append([i, k])
                        temp = 0
        str1 = ''
        list3 = []
        list4 = []
        for each in list2:
            if each[1] > 0:
                str2 = str(each[0])
                str3 = str(each[1])
                str1 = str2 + '^' + str3
                list4.append(str1)
                list3.append([each[0], each[1]])
        # print(list_primes)
        # print(list3)
        # print(list4)
        str5 = ''
        str5 = '*'.join(list4)
        if str5 is not None:
            if not str5.find('2^'):
                str5 = '2^0*' + str5
        # print("String Value is %s" % str5)
    else:
        print('2^0')
