#leetcode1004
https://leetcode-cn.com/problems/max-consecutive-ones-iii/



#题目描述
给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
返回仅包含 1 的最长（连续）子数组的长度。



#输出示例
输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释： 
[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。





#代码
def longestOnes(self, A: List[int], K: int) -> int:   
        #题目的关键是转化为找到一个最长的字符串，该字符串含有最多不超过K个0
        size = len(A)
        right,left = 0,0
        zeros = 0
        res = 0
        while right<size:
            #对0的个数计数
            if A[right]==0:
                zeros+=1
            #如果0的个数超过K，那判断左指针是否为0，如果左指针为0，0的个数减去1，然后左指针向右移动
            while zeros>K:
                if A[left]==0:
                    zeros-=1
                left+=1
            #更新字符串的最长长度
            res = max(res,right-left+1)
            right+=1
 
        return res
