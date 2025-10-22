from collections import Counter
class DetectSquares:

    def __init__(self):
        self.dataStream = Counter()

    def add(self, point: List[int]) -> None:
        self.dataStream[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        point = tuple(point)
        for i in self.dataStream: 
            minItem, maxItem = sorted([i, point], key = lambda x : x[1])
            if abs(minItem[0] - maxItem[0]) != abs(minItem[1] - maxItem[1]) or maxItem == minItem:
                continue; 
            # We have a diagonal now we need to know are they left or right? 

            if (minItem[0], maxItem[1]) in self.dataStream and (maxItem[0], minItem[1]) in self.dataStream:
                count += self.dataStream[(minItem[0], maxItem[1])] * self.dataStream[(maxItem[0], minItem[1])] * self.dataStream[i]
        return count; 


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)