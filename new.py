k = list(map(int, input().split()))
l_1 = list(map(int, input().split()))
l_2 = list(map(int, input().split()))
l_3 = list(map(int, input().split()))
l_4 = list(map(int, input().split()))
l_5 = list(map(int, input().split()))
f_list = l_1 + l_2 + l_3 + l_4 +l_5
# total=0
f_list = sorted(f_list)
# for i in range(5):
#     total+=k[i]
elected = []

i = 0
# j = len(f_list)-1
for i in f_list:
    n = f_list.count(i)
    if n>3:
        elected.append(i)
print(elected)        

















while(i<len(f_list)):

    if (f_list.count(k[i])>3) and (f_list[i]==f_list[i+1]) and (i!=j):
        elected.append(k[i])

    if f_list[i]==f_list[i+1]:
        i+=2
        continue

    i+=1

print(elected)
