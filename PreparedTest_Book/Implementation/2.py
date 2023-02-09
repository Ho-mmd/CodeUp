N = int(input());
answer = 0;

for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            if(i == 3 or j == 3 or k == 3 or k // 10 == 3 or k % 10 == 3 or j // 10 == 3 or j % 10 == 3):
                answer += 1;

print(answer);