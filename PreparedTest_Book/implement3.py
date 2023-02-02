a = input();

x, y = ord(a[0]) - 96, int(a[1]); 
cnt = 0;

if 8 > x + 2 and x + 2 > 0 and 8 > y + 1 and y + 1 > 0:
    cnt += 1;
if 8 > x + 2 and x + 2 > 0 and 8 > y - 1 and y - 1 > 0:
    cnt += 1;
if 8 > x - 2 and x - 2 > 0 and 8 > y + 1 and y + 1 > 0:
    cnt += 1;
if 8 > x - 2 and x - 2 > 0 and 8 > y - 1 and y - 1 > 0:
    cnt += 1;
if 8 > x + 1 and x + 1 > 0 and 8 > y + 2 and y + 2 > 0:
    cnt += 1;
if 8 > x + 1 and x + 1 > 0 and 8 > y - 2 and  y - 2 > 0:
    cnt += 1;
if 8 > x - 1 and x - 1 > 0 and 8 > y + 2 and y + 2 > 0:
    cnt += 1;
if 8 > x - 1 and x - 1 > 0 and 8 > y - 2 and y - 2 > 0:
    cnt += 1;

print(cnt)