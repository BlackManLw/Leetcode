#leetcode485
https://leetcode-cn.com/problems/max-consecutive-ones/
  
#题目描述
给定一个二进制数组， 计算其中最大连续 1 的个数。


#输出示例
输入：[1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.


#代码
def help(num):
  num = int(''.join([str(i) for i in nums]),base=2)
  res = 0
  while num>0:
      num&=num<<1
      res+=1

  return res
