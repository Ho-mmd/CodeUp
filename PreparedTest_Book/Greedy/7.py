n = list(map(int, input()));
answer = 0;

for i in range(len(n) - 1):
    if(n[i] != n[i + 1]):
        answer += 0.5;

if(answer > int(answer)):
    answer = int(answer) + 1;

print(int(answer));