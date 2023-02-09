N, K = map(int, input().split());
ar1 = list(map(int, input().split()));
ar2 = list(map(int, input().split()));

answer = 0;
ar1.sort();
ar2.sort(reverse = True);

for i in range(N):
    if(ar1[i] < ar2[i]):
        ar1[i] = ar2[i];
        answer += 1;

    if(K == answer):
        break;

answer = 0;

for i in ar1:
    answer += i;

print(answer);