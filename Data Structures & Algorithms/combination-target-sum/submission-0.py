class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        def Tracking(i,curr,total):
            if total==target:
                result.append(curr.copy())
                return 
            if i>=len(nums) or total>target:
                return
            curr.append(nums[i])
            Tracking(i,curr,total+nums[i])
            curr.pop()
            Tracking(i+1,curr,total)
        Tracking(0,[],0)
        return result