import math
class Solution:
    def minOperation(self, mat):
        # Code here 
        # mat.sort(reverse=True)
        # temp = [sum(i) for i in trans]
        ans = 0
        res = math.inf
        n,m = len(mat), len(mat[0])
        trans = [[mat[i][j] for i in range(n)] for j in range(m)]
        temp = [sum(i) for i in trans]
        print(trans, temp)
        for i in range(len(trans)):
            ans = 0
            for j in range(len(trans)):
                
                # s=sum(trans[j])-trans[j][i]
                s = temp[j] - trans[j][i]
                ans += abs(s - trans[j][i])
                # print(trans[j][i],temp[j], ans)
            res = min(res, ans)
            # print(ans)
        return res
        



#{ 
 # Driver Code Starts
# Driver code
t = int(input())
for _ in range(t):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    sol = Solution()
    print(sol.minOperation(matrix))
    print("~")
# } Driver Code Ends