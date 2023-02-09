N, M = map(int, input().split());
arr = list(map(int, input().split()));

start = 0;
end = max(arr); 

while(1):
    if(start > end):
        break;

    sm = 0;
    mid = (start + end) // 2;

    for i in arr:
        if (i > mid):
            sm += i - mid;
    
    if(sm < M):
        end = mid - 1;
    else:
        answer = mid;
        start = mid + 1;

print(answer);