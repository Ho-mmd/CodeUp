answer = 0;
N, M, K = map(int, input().split());
arr = list(map(int, input().split()));

arr.sort(reverse = True);

answer = K * (M // K) * arr[0] + M % K * arr[1];

print(answer);