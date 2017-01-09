#-- coding:utf-8 --#

#列表自动生成

l=range(10)
l1=l[2:9:2]#第三个参数是间隔
print l1

print '\\' #""是一样的不需要变
print r'\\' #r中没有转义字符
print u'\\' #u是unicode编码普通的是ascii编码
print '\n'
print '\t'

a = 'python'
print 'hello,', a or 'world' #在计算 a and b 时，如果 a 是 False，则根据与运算法则，整个结果必定为 False，因此返回 a；如果 a 是 True，则整个计算结果必定取决与 b，因此返回 b
b = ''
print 'hello,', b or 'world' #在计算 a or b 时，如果 a 是 True，则根据或运算法则，整个计算结果必定为 True，因此返回 a；如果 a 是 False，则整个计算结果必定取决于 b，因此返回 b。

c=['a','b','c']
for i,j in enumerate(c):
    print i,'-',j
for i ,j in zip(range(1,len(c)+1),c):
    print i ,'-',j

print filter(lambda s:s and len(s.strip())>0, ['test', None, '', 'str', '  ', 'END']) #冒号前面是函数参数，冒号后边是表达式也是return值。
#print type(None)
#python中的map函数
def format_name(s):
    return s[0].upper()+s[1:].lower()

print map(format_name, ['adam', 'LISA', 'barT'])#函数返回新的元素
#python中的filter函数
import math
def is_sqr(x):
    return x and math.sqrt(x)%1==0
print is_sqr(100)
print filter(is_sqr, range(1, 101)) #函数返回布尔类型的值
#python中的reduce函数
def prod(x, y):
    return x*y

print reduce(prod, [2, 4, 5, 7, 12])