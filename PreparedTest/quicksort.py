a = [3, 7, 6, 1, 8, 2];

def quick(arr, start, end):
    if start >= end:
        return;
    
    pivot = start;
    left = start + 1;
    right = end;

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1;
        while right > start and arr[right] >= arr[pivot]:
            right -= 1;
        
        if left > right:
            tmp = arr[right];
            arr[right] = arr[pivot];
            arr[pivot] = tmp;
        else:
            tmp = arr[left];
            arr[left] = arr[right];
            arr[right] = tmp;
    quick(arr, start, right - 1);
    quick(arr, right + 1, end);

quick(a, 0, len(a) - 1);

print(a);