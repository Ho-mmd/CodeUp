n, m = map(int, input().split());
arr = list(map(int, input().split()));
al = len(arr);
answer = 0;

for i in range(1, m + 1):
    tmp = arr.count(i)
    al -= tmp;
    answer += al * tmp;

print(answer);    