a = eval(input());
move = list(input().split());
x, y = 1, 1;

for i in move:
    if i == 'L' and x > 1:
        x -= 1;
    elif i == 'R' and x < a:
        x += 1;
    elif i == 'U' and y > 1:
        y -= 1;
    elif i == 'D' and y < a:
        y += 1;

print(y, x);