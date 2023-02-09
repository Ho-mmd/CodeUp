N = int(input());
answer = [];

for i in range(N):
    answer.append(input().split());
    answer[i][1] = int(answer[i][1]);

answer.sort(key = lambda x : x[1]);

for i in answer:
    print(i[0], end = " ");