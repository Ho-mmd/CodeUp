tmp = input();
n = len(tmp);
s1, s2 = 0, 0;

for i in range(n):
    if(i < n // 2):
        s1 += int(tmp[i]);
    else:
        s2 += int(tmp[i]);

if(s1 == s2):
    print("LUCKY");
else:
    print("READY");