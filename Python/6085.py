a, b, c = map(int, input().split());

print("%.2f MB" % round((a * b * c / (1024 ** 2 * 8)), 2));