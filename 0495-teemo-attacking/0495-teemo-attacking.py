class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        # res = 0

        # for i in range(len(timeSeries) - 1):
        #     res += min(duration, timeSeries[i + 1] - timeSeries[i])

        # if timeSeries:
        #     res += duration

        # return res
        total=0
        for i in range(len(timeSeries)-1):
            gap=timeSeries[i+1]-timeSeries[i]
            if gap>=duration:
                total+=duration
            else:
                total+=gap
        total+=duration
        return total