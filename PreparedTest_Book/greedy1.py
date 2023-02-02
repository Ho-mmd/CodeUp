a = eval(input());
sum = 0;

sum += a // 500;
a = a % 500;

sum += a // 100;
a = a % 100;

sum += a // 50;
a = a % 50;

sum += a // 10;

print(sum);