n = int(input());
arr = list(map(int, input().split()));
answer = 0;
cnt = 0;
arr.sort();

for i in arr:
    cnt += 1;
    if(cnt >= i):
        answer += 1;
        cnt = 0;

print(answer);