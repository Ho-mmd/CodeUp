n = int(input());
arr = list(map(int, input().split()));
target = 1;

arr.sort();

for i in arr:
    if(target < i):
        break;
    target += i;

print(target);