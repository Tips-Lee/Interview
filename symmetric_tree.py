class Solution:
    def getLeastNumbers(self, arr, k: int):
        if k == 0:
            return []
        # tmp = sorted(arr[:k])
        # for idx in range(k, len(arr)):
        #     if arr[idx] < tmp[-1]:
        #         tmp[-1] = arr[idx]
        #         tmp = sorted(tmp)
        # return tmp
        tmp = arr[:k]
        self.heapify(tmp)
        for idx in range(k, len(arr)):
            if arr[idx] < tmp[0]:
                tmp[0] = arr[idx]
                self.sift(tmp)
        return tmp

    def sift(self, arr, start=0):
        i, j = start, 2*start+1
        while j < len(arr):
            if j+1 < len(arr) and arr[j] < arr[j+1]:
                j = j + 1
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            i, j = j, 2*j + 1

    def heapify(self, arr):
        for idx in reversed(range((len(arr)-1)//2 + 1)):
            self.sift(arr, idx)

if __name__ == '__main__':
    s = Solution()
    print(s.getLeastNumbers([1, 3, 2], 2))

