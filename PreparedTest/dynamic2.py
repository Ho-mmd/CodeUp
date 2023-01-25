a = eval(input());
b = [0] * 30001;

for i in range(2, a + 1):
    b[i] = b[i - 1] + 1;

    if i % 2 == 0:
        if b[i] > (b[i // 2] + 1):
             b[i] = b[i // 2] + 1;
    if i % 3 == 0:
        if b[i] > (b[i // 3] + 1):
            b[i] = b[i // 3] + 1;
    if i % 5 == 0:
        if b[i] > (b[i // 5] + 1):
            b[i] = b[i // 5] + 1;

print(b[a]);