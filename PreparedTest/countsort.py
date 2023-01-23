a = [0, 0, 4, 1, 2, 1, 6, 3 ,2, 8, 1, 9];
cnt = [0 for i in range(10)];

for i in a:
    cnt[i] += 1;

for i in range(len(cnt)):
    for j in range(cnt[i]):
            print(i, end = " ");
    print();