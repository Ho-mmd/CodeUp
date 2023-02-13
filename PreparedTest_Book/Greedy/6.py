arr = list(map(int, input()));
answer = 0;

arr.sort();

for i in arr:
    if(answer == 0 or i <= 1):
        answer += i;
    else:
        answer *= i;

print(answer);