class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        stack = [colors[0]]
        idx = 1 
        count = 0 
        while idx < len(neededTime):
            #print(count, stack, colors[idx])
            if colors[idx] == stack[-1]:
                stack.pop()
                if neededTime[idx] >= neededTime[idx-1]:
                    # Prev item, 
                    count += neededTime[idx-1]
                    neededTime[idx-1] = float('inf')
                else:
                    count += neededTime[idx]
                    neededTime[idx] = neededTime[idx-1]
            stack.append(colors[idx])
            idx += 1 
        return count; 

# Code may fail for items that need to carry 2 as it currently carries 1. 