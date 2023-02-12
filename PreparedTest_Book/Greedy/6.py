n = list(map(int, input()));
tmp = 0;

n.sort();

for i in n:
    if(i <= 1 or tmp == 0):
        tmp += i;
    else:
        tmp *= i;

answer = tmp;

print(answer);