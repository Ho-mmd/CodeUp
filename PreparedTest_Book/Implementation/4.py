N, M = map(int, input().split());
A, B, d = map(int, input().split());
answer = 0;

arr = [];

for i in range(N):
    arr.append(list(map(int, input().split())));

arr[A][B] = 2;

while(1):
    if(arr[A + 1][B] != 0 and arr[A - 1][B] != 0 and arr[A][B + 1] != 0 and arr[A][B - 1] != 0):
        if(arr[A + 1][B] == 1 and arr[A - 1][B] == 1 and arr[A][B + 1] == 1 and arr[A][B - 1] == 1):
            break;
        else:
            if(arr[A + 1][B] == 2 and d == 2):
                A += 1;
            elif(arr[A - 1][B] == 2 and d == 0):
                A -= 1;
            elif(arr[A][B + 1] == 2 and d == 3):
                B += 1;
            elif(arr[A][B - 1] == 2 and d == 1):
                B -= 1;
            else:
                break;

    if(d == 0):
        if(arr[A][B - 1] == 0):
            B -= 1;
            d = 3;
        elif(arr[A - 1][B] == 0):
            A -= 1;
            d = 2;
        elif(arr[A][B + 1] == 0):
            B += 1;
            d = 1;
        elif(arr[A + 1][B] == 0):
            A += 1;
        answer += 1;
        arr[A][B] = 2;
    elif(d == 1):
        if(arr[A + 1][B] == 0):
            A += 1;
            d = 0;
        elif(arr[A][B - 1] == 0):
            B -= 1;
            d = 3;
        elif(arr[A - 1][B] == 0):
            A -= 1;
            d = 2;
        elif(arr[A][B + 1] == 0):
            B += 1;
        answer += 1;
        arr[A][B] = 2;
    elif(d == 2):
        if(arr[A][B + 1] == 0):
            B += 1;
            d == 1;
        elif(arr[A + 1][B] == 0):
            A += 1;
            d = 0;
        elif(arr[A][B - 1] == 0):
            B -= 1;
            d = 3;
        elif(arr[A - 1][B] == 0):
            A -= 1;
        answer += 1;
        arr[A][B] = 2;
    elif(d == 3):
        if(arr[A - 1][B] == 0):
            A -= 1;
            d = 2;
        elif(arr[A][B + 1] == 0):
            B += 1;
            d == 1;
        elif(arr[A + 1][B] == 0):
            A += 1;
            d = 0;
        elif(arr[A][B - 1] == 0):
            B -= 1;
        answer += 1;
        arr[A][B] = 2;

print(answer);