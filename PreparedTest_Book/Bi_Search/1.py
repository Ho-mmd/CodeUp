import sys

N = int(sys.stdin.readline().rstrip());
ar1 = list(map(int, sys.stdin.readline().rstrip().split()));

M = int(sys.stdin.readline().rstrip());
ar2 = list(map(int, sys.stdin.readline().rstrip().split()));

for i in ar2:
    if (i in ar1):
        print("yes", end = " ");
    else:
        print("no", end = " ");