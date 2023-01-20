a = list(map(int, input().split()));

print("%.1f MB" % round(a[0] * a[1] * a[2] * a[3] / 8 / 1024 / 1024, 1));