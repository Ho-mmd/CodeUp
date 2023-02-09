N = int(input());
answer = 0;

answer += N // 500;
N %= 500;
answer += N // 100;
N %= 100;
answer += N // 50;
N %= 50;
answer += N // 10;

print(answer);