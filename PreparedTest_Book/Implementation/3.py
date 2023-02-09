n = input();
answer = 0;

x = ord(n[0]) - ord('a') + 1;
y = int(n[1]);

if(x + 2 <= 8 and y + 1 <= 8):
    answer += 1;
if(x + 2 <= 8 and y - 1 > 0):
    answer += 1;
if(x - 2 > 0 and y + 1 <= 8):
    answer += 1;
if(x - 2 > 0 and y - 1 > 0):
    answer += 1;
if(x + 1 <= 8 and y + 2 <= 8):
    answer += 1;
if(x + 1 <= 8 and y - 2 > 0):
    answer += 1;
if(x - 1 > 0 and y + 2 <= 8):
    answer += 1;
if(x - 1 > 0 and y - 2 > 0):
    answer += 1;

print(answer);