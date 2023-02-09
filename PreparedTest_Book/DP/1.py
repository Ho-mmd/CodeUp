answer = [0] * 30001;
X = int(input());

for i in range(2, X + 1):
    answer[i] = answer[i - 1] + 1;

    if(i % 2 == 0):
        if(answer[i // 2] + 1 < answer[i]):
            answer[i] = answer[i // 2] + 1;
    if(i % 3 == 0):
        if(answer[i // 3] + 1 < answer[i]):
            answer[i] = answer[i // 3] + 1;
    if(i % 5 == 0):
        if(answer[i // 5] + 1 < answer[i]):
            answer[i] = answer[i // 5] + 1;
    

print(answer[X]);