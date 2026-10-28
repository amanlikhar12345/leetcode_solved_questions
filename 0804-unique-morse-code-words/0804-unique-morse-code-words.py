class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        m=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d={}
        li=[]
        c=0
        for i in range(len(m)):
            d[chr(i+ord("a"))]=m[i]
        for i in words:
            row=""
            for j in i:
                    row+=d[j]
            li.append(row)
        return len(set(li))