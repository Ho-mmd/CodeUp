#Retry

N, M = map(int, input().split());
A, B, d = map(int, input().split());

Mp = [[] for i in range(4)];
cnt = 0;

for i in range(N):
    Mp[i] = list(map(int, input().split()));

while(1):
    if d == 0:
        if Mp[A - 1] == 0:
            Mp[A - 1] = 2;
            A -= 1;
        elif Mp[B + 1] == 0:
            Mp[B + 1] = 2;
            B += 1;
        elif Mp[A + 1] == 0:
            Mp[A + 1] = 2;
            A += 1;
        elif Mp[B - 1] == 0:
            Mp[B - 1] = 2;
            B -= 1;
    elif d == 1:
        if Mp[B + 1] == 0:
            Mp[B + 1] = 2;
            B += 1;
        elif Mp[A + 1] == 0:
            Mp[A + 1] = 2;
            A += 1;
        elif Mp[B - 1] == 0:
            Mp[B - 1] = 2;
            B -= 1;
        elif Mp[A - 1] == 0:
            Mp[A - 1] = 2;
            A -= 1;
