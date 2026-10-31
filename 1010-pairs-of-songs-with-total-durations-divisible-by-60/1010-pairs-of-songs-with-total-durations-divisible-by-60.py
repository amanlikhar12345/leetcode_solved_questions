class Solution(object):
    def numPairsDivisibleBy60(self, time):

        # c=0
        # n=len(time)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if (time[i]+time[j])%60==0:
        #             c+=1
        # return c

        c=0
        d={}
        for i in range(len(time)):
            rem=time[i]%60
            req=(60-rem)%60
            if req in d:
                c+=d[req]
            d[rem]=d.get(rem,0)+1
        return c
