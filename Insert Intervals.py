class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        newStart, newEnd = newInterval;
        while i < len(intervals): 
            start, end = intervals[i]
            if newEnd < start: 
                intervals.insert(i, newInterval)
                return intervals
                # We can return if we can just insert between two intervals; 
            # end is end of current interval
            elif newStart <= start or (newStart > start and newStart <= end):
                cStart = min(newStart,start)
                while i < len(intervals) and newEnd > intervals[i][1]:
                    intervals.pop(i)
                if i == len(intervals):
                    intervals.insert(i, [cStart, newEnd])
                    return intervals
                f = True if newEnd >= intervals[i][0] else False
                newEnd = intervals[i][1] if newEnd >= intervals[i][0] else newEnd
                intervals.insert(i, [cStart, newEnd])
                if f:
                    intervals.pop(i+1)
                return intervals
            i += 1
        # We can just add to the end; 
        intervals.append(newInterval)
        return intervals
        