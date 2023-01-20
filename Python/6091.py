#Euclidean algorithm

def gcd(a, b):
    if a < b:
        a, b = b, a;

    while b != 0:
        n = a % b;
        a = b;
        b = n;

    return a;

a, b, c = map(int, input().split());

ans = a * b / gcd(a, b);
ans = ans * c / gcd(ans, c);

print(int(ans));