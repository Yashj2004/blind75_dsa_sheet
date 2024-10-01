class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        a=1
        c=0
        for i in nums:
            if i!=0:
                a*=i
            else:
                c+=1
        for i in nums:
            if i==0 and c<2:
                l.append(a)
            elif c>0:
                l.append(0)
            else:
                l.append(a//i)
        return l
