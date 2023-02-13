n = int(input());
arr = list(map(int, input().split()));

arr.sort();
tmp = 0;
answer = 0;

for i in arr:
    tmp += 1;
    if(i <= tmp):
        tmp = 0;
        answer += 1;

print(answer);