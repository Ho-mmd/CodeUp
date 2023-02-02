a, b, c = map(int, input().split());
list = list(map(int, input().split()));

sum = 0;
list.sort(reverse = True);

for i in range(b):
    if (i + 1) >= c and (i + 1) % c == 0:
        sum += list[1];
    else:
        sum += list[0];

print(sum);