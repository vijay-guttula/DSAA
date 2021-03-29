'''
sorts an array using heap sort at O(nlogn)
'''


class Heap:
    def __init__(self, heap, size):
        self.heap = heap
        self.size = size

    def left_child(self, i):
        return (i * 2) + 1

    def right_child(self, i):
        return i * 2 + 2

    def shift_down(self, i):
        minHeap = i
        l = self.left_child(i)
        r = self.right_child(i)

        if l < self.size and self.heap[l] < self.heap[minHeap]:
            minHeap = l
        if r < self.size and self.heap[r] < self.heap[minHeap]:
            minHeap = r

        if minHeap is not i:
            self.heap[minHeap], self.heap[i] = self.heap[minHeap], self.heap[i]
            self.shift_down(minHeap)

    def build_heap(self):
        for i in range(self.size // 2, -1, -1):
            self.shift_down(i)


if __name__ == '__main__':
    n = int(input())
    heap = list(map(int, input().split()))
    h = Heap(heap, n)
    h.build_heap()
    print(h.heap)
