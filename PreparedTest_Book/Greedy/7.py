arr = input();
answer = 0;

for i in range(len(arr) - 1):  
    if(arr[i] != arr[i + 1]):
        answer += 0.5;

if(answer - int(answer) > 0):
    answer = int(answer) + 1;
else:
    answer = int(answer);

print(answer);