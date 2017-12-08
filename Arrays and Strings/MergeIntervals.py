# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their start times.
#
# Example 1:
#
# Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].
#
# Example 2:
#
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].
#
# i: [3, 5]
# j: [8, 10]
# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
#
# Make sure the returned intervals are also sorted.





            # # if intervals[i][0]
            # if new_interval[0] > intervals[i][1]: # new_interval[0] is greater than current interval's last element
            #     if i < (len(intervals) - 1): # not end of list
            #         if new_interval[1] < intervals[i+1][0]:
            #             intervals.insert(i+1, new_interval)
            #             return intervals
            #     else: #end of list
            #         intervals.append(new_interval)
            #         return intervals
            # elif new_interval[1] < intervals[i][0]:
            #     intervals.insert(i, new_interval)
            #     return intervals


        # if new_interval[0] >= intervals[i][0] and new_interval[0] <= intervals[i][1]: # need to merge
        #
        #     start_interval = intervals[i]
        #     j = i
        #     while intervals[j][0] < new_interval[1] and intervals[j][1] < new_interval[1] and j< len(intervals):
        #         # end_interval = intervals.pop(j)
        #         print j
        #         j += 1
        #     end_interval = intervals[j]
        #     if new_interval[0] > start_interval[0]:
        #         if new_interval[1] > start_interval[1]:
        #             # if new_interval[1] < intervals[j][0]: #if 5 is less than 6
        #             if new_interval[1] < end_interval[0]: #if 5 is less than 6
        #
        #                 start_interval[1] = new_interval[1]
        #                 # intervals.pop(j)
        #                 i += 1
        #                 while i != j:
        #                     intervals.pop(i)
        #                     i += 1
        #                 return intervals
        #             else:
        #                 end_interval[0] = new_interval[0]
        #                 new_intervals = intervals[:i+1] + intervals[j:]
        #                 i += 1
        #                 while i != j:
        #                     intervals.pop(i)
        #                     i += 1
        #                 return intervals
        #     # print intervals[i]
        #     # print intervals[j]
        #
        #
        # elif new_interval[0] > intervals[i][1]: # new_interval[0] is greater than current interval's last element
        #     if i < (len(intervals) - 1): # not end of list
        #         if new_interval[1] < intervals[i+1][0]:
        #             intervals.insert(i+1, new_interval)
        #             return intervals
        #     else: #end of list
        #         intervals.append(new_interval)
        #         return intervals
        # elif new_interval[1] < intervals[i][0]:
        #     intervals.insert(i, new_interval)
        #     return intervals
# def insert(intervals, new_interval):
#     # intervals.insert(0, new_interval)
#     result_list = []
#     # new_interval = tuple(new_interval)
#     # intervals = map(tuple, intervals)
#     # print intervals
#     for i in range(len(intervals)):
#         # if i < len(intervals) - 1:
#         if is_overlapping(intervals[i], new_interval):
#
#             result_list.append(merge_intervals(intervals[i], new_interval))
#             # new_interval = intervals[i]
#                 # new_interval = intervals.pop(i)
#
#         elif new_interval[1] < intervals[i][0]: # insert before
#                 # intervals.insert(i, new_interval)
#                 result_list.insert(i, new_interval)
#                 # return intervals
#         elif new_interval[0] > intervals[i][1]: # insert after
#             if i < (len(intervals) - 1): # not end of list
#                 if new_interval[1] < intervals[i+1][0]:
#                     # intervals.insert(i+1, new_interval)
#                     result_list.insert(i+1, new_interval)
#                         # return intervals
#             else: #end of list
#                 result_list.append(new_interval)
#                     # intervals.append(new_interval)
#                     # return intervals
#         else:
#             result_list.append(interval[i])
#     return result_list

def is_overlapping(a, b):
    a_low, a_high = a
    b_low, b_high = b
    if a_low <= b_low:
        if a_high >= b_low or a_high >= b_high:
            return True
    if b_low <= a_low:
        if b_high >= a_high or a_low <= b_high:
            return True
    return False

def merge_intervals(a, b):
    a_low, a_high = a
    b_low, b_high = b
    result_interval = [0,0]

    if a_low < b_low:
        result_interval[0] = a_low
    else:
        result_interval[0] = b_low
    if a_high > b_high:
        result_interval[1] = a_high
    else:
        result_interval[1] = b_high

    return result_interval

def insert(intervals, new_interval):
    new_intervals = []
    for interval in intervals:
        if new_interval is None:
            new_intervals.append(interval)
        elif new_interval[0] > interval[1]: # fully under
            new_intervals.append(interval)
        elif is_overlapping(interval, new_interval):
            new_interval = merge_intervals(interval, new_interval)
        elif new_interval[1] < interval[0]: # fully above
            new_intervals.append(new_interval)
            new_intervals.append(interval)
            new_interval = None

    if(not new_interval is None):
        new_intervals.append(new_interval)

    return new_intervals

#print "is overlapping test: " + str(is_overlapping([5, 7], [1, 2]))
#print "Merge test: " + str(merge_intervals([5, 7], [1, 2]))
#print "Merge test: " + str(merge_intervals([5, 7], [6, 8]))
#print "Merge test: " + str(merge_intervals([5, 7], [1, 6]))
#print "Merge test: " + str(merge_intervals([2, 7], [3, 5]))
#print "Merge test: " + str(merge_intervals([3, 5], [2, 7]))

assert insert([[5,7],[8,10], [12,15]], [1,3]) == [[1,3],[5,7],[8,10],[12,15]]
assert insert([[1,3],[8,10], [12,15]], [5,7]) == [[1,3],[5,7],[8,10],[12,15]]
assert insert([[1,3],[5,7], [8,10]], [12,15]) == [[1,3],[5,7],[8,10],[12,15]]

#requires merge:
assert insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
assert insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9]) == [[1,2],[3,10],[12,16]]
assert insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [3,7]) == [[1,2],[3,7],[8,10],[12,16]]

# print is_overlapping([5, 7], [8, 10]) # False
# print is_overlapping([8, 10],[5, 7]) # False
# print is_overlapping([5, 7], [5, 10]) #True
# print is_overlapping([5, 7], [6, 10]) #True
# print is_overlapping([5, 11], [8, 10]) #True
# print is_overlapping([10, 15], [1, 18]) #True
# print is_overlapping([10, 15], [8, 11]) #True


#print insert([[1,3],[8,10], [12,15]], [5,7]) # [[1,3],[5,7],[8,10],[12,15]]
#print insert([[1,3],[5,7], [8,10]], [12,15]) # [[1,3],[5,7],[8,10],[12,15]]
#requires merge:
#print insert([[1,3],[6,9]], [2,5]) # [1,5],[6,9]
#print insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9]) # [1,2],[3,10],[12,16]
#print insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [3,7]) # [1,2],[3,7],[8,10][12,16]
