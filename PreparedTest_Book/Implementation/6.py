tmp = input();
ar1 = [];
ar2 = 0;

for i in tmp:
    if(48 <= ord(i) and ord(i) <= 57):
       ar2 += int(i);
    else:
        ar1.append(i); 

ar1.sort();

for i in ar1:
    print(i, end="");

print(ar2);