"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from functools import cmp_to_key
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        def cmp_items(a, b):
            if a.start > b.start:
                return 1
            elif a.start == b.start:
                return 0
            else:
                return -1   
        sorted_intervals = sorted(intervals, key=cmp_to_key(cmp_items))

        for i in range(len(sorted_intervals) - 1):
            curr = sorted_intervals[i]
            next_meeting = sorted_intervals[i + 1]
            print(curr.end)
            print(next_meeting.start)
            if curr.end > next_meeting.start:
                print('wtf')
                return False

        return True



