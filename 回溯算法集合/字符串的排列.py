#题目描述
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

#样例输出
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

#使用visited标记数组去标记访问过的元素
#不能有重复的元素因此可以进行剪枝

#字符串的排列
s = 'abc'
res = set()
def huisu(tmp,visited):
    if len(tmp)==len(s):
        res.add(''.join(tmp[:]))
    
    for i in range(len(s)):
        if visited[i]:
            continue
        if i>0 and  not visited[i-1] and s[i]==s[i-1]:
            continue
        visited[i] = True 
        huisu(tmp+[s[i]],visited) 
        visited[i] = False

visited = [False]*(len(s))
huisu([],visited)
print(res)
