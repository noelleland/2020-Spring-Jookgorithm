import math
start = int(input())
end = int(input())
ans = 0
min = 0
for i in range(start, end + 1, 1):
    flag = 1
    for j in range(2,int(math.sqrt(i)) + 1, 1):
        if i % j == 0:
            flag = 0
            break;
    if flag == 1 and i != 1:
        ans += i
        if min == 0:
            min = i
if min > 0:
    print(ans)
    print(min)
else:
    print(-1)
