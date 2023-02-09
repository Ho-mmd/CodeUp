N, K = map(int, input().split());
answer = 0;

while(1):
    if(N % K == 0):
        N //= K;
    else:
        N -= 1;
    
    answer += 1;
    
    if(N == 1):
        break;
    

print(answer);