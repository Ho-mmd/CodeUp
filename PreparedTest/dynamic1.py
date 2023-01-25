a = [0] * 100;
b = int(input());

def fibo(n):
    if n == 1 or n == 2:
        return 1;
    if a[n] != 0:
        return a[n];
    else:
        a[n] = fibo(n - 1) + fibo(n - 2);
        
    return a[n];

print(fibo(b));
    