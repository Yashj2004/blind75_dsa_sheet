class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans,i,j=0,0,0
        while j<(len(prices)):
            if prices[i] < prices[j]:
                if ans<(prices[j] - prices[i]):
                    ans=prices[j] - prices[i]
            if prices[i] > prices[j]:
                i=j
            j+=1
        return ans
