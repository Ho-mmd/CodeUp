N = int(input());
answer = [];

for i in range(N):
    answer.append(int(input()));

answer.sort(reverse = True);

print(answer);