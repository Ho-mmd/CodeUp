def bin(arr, tar, start, end, index):
    while start <= end:
        sum = 0;
        mid = (start + end) // 2;
        
        for i in range(index):
            if arr[i] > mid:
                sum += arr[i] - mid;

        if sum == tar:
            return mid;
        elif sum < tar:
            end = mid - 1;
        else:
            start = mid + 1;

    if tar < sum:
        return mid;
    else:
        return mid - (tar - sum) // index - 1; 

a, b = map(int, input().split());
c = list(map(int, input().split()));

c.sort();

print(bin(c, b, c[0], c[len(c) - 1], a))

