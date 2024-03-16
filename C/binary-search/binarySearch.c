#include <stdio.h>
#include <math.h>

int binarySearch(int arr[], int size, int targ) {
    int l = 0;
    int r = size - 1;
    
    while (l <= r) {
        int mid = floor((l+r)/2); // To prevent potential overflow

        if (arr[mid] == targ) {
            return mid; // Return the index of the target
        } else if (arr[mid] < targ) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return -1; // Target not found
}

int main() {
    int arr[] = {1, 2, 3};
    int target = 2;
    int result = binarySearch(arr, sizeof(arr) / sizeof(arr[0]), target);
    
    if (result != -1) {
        printf("Element found at index: %d\n", result);
    } else {
        printf("Element not found\n");
    }

    return 0;
}
