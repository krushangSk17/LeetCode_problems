class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        n = len(nums)
        self.inv = 0
        
        def count_inv(a,b):
            i = len(a)-1
            j = len(b)-1
            # print("a = ",a," counting ","b = ",b)
            while(j>=0 and i>=0):
                # print("i = ",i,"j = ",j)
                if(a[i] > 2*b[j]):
                    self.inv += j+1
                    i-=1
                else:
                    j-=1

        def merger(a,b):
            ai = 0
            bi = 0
            a_len = len(a)
            b_len = len(b)
            merged = []
            
            while(ai < a_len and bi < b_len):
                if(a[ai] < b[bi]):
                    merged.append(a[ai])
                    ai+=1
                else:
                    merged.append(b[bi])
                    bi+=1
            if(ai == a_len):
                while(bi < b_len):
                    merged.append(b[bi])
                    bi+=1
            else:
                while(ai < a_len):
                    merged.append(a[ai])
                    ai+=1
            return merged
            
        def helper(nums):
            if(len(nums)<=1):
                return nums
            a = helper(nums[:len(nums)//2])
            b = helper(nums[len(nums)//2:])
            
            # print("a = ",a," counting ","b = ",b)
            
            merged = merger(a,b)
            count_inv(a,b)
            
            return merged
            
        print(helper(nums))
        return self.inv
