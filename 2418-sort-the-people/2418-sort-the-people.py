class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        people=list(zip(heights,names))
        people.sort(reverse=True)
        print(people)
        res=[]
        for i in range(0,len(people)):
            res.append(people[i][1])
        return res