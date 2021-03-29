class Heap:
    def __init__(self, heap, size):
        self.swaps = list(list())
        self.heap = heap
        self.size = size
        assert len(self.heap) == self.size

    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp
        self.swaps.append([index1, index2])
        return

    def parent_index(self, i):
        return i // 2

    def leftchild_index(self, i):
        return (2 * (i))

    def rightchild_index(self, i):
        return (2 * i) + 1

    def shiftdown(self, i):
        i += 1
        minIndex = i
        l = self.leftchild_index(i)
        r = self.rightchild_index(i)

        if l <= self.size and self.heap[minIndex - 1] > self.heap[l - 1]:
            minIndex = l
        if r <= self.size and self.heap[minIndex - 1] > self.heap[r - 1]:
            minIndex = r
        if i != minIndex:
            self.swap(i - 1, minIndex - 1)
            self.shiftdown(minIndex - 1)

        return

    def buildHeap(self):
        half = self.size // 2
        for i in range(half, 0, -1):
            self.shiftdown(i - 1)

    def display(self):
        print(len(self.swaps))
        for i in self.swaps:
            print(*i, sep=' ')


if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    h = Heap(data, n)
    h.buildHeap()
    h.display()
