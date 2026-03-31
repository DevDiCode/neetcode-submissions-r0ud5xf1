class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, low, mid, high):
            temp = []
            i, j = low, mid + 1

            # Merge the two halves
            while i <= mid and j <= high:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1

            # Append remaining elements
            temp.extend(arr[i:mid + 1])
            temp.extend(arr[j:high + 1])

            # Copy back to original array
            arr[low:high + 1] = temp

        def mergeSortHelper(arr, low, high):
            if low >= high:
                return
            mid = (low + high) // 2
            mergeSortHelper(arr, low, mid)
            mergeSortHelper(arr, mid + 1, high)
            merge(arr, low, mid, high)

        mergeSortHelper(nums, 0, len(nums) - 1)
        return nums
