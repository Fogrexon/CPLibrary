a = [0,1,2,3,4,5,6,7,8,9]
index = 4

del a[3]
a.pop(index)
a.remove(object)

from copy import deepcopy
deepcopy(a)

a = [2, 4, 6, 8]
b = [3, 6, 9]

print(list(set(a) | set(b)))  # 和集合
print(list(set(a) & set(b)))  # 積集合

# lsit.sort(func)
# sorted(list, func)
# 降順 reverse=True
# (結合文字).join(list)
# lambda x: (shori)
# key=キー関数
# 1番目でソートしたのち2番目でソート
# sorted(list, key=itemgetter(1,2))
# list.index(a)
print(sorted(a, key=lambda x: x.upper())) 

from collections import deque

l = [0,1,2,3]
q = deque(l)
q.append(4) # 後ろから4を挿入, l=deque([0,1,2,3,4])
q.appendleft(5)#前から5を挿入, l=deque([5,0,1,2,3,4])
x = q.pop() #後ろの要素を取り出す, x=4, l=deque([5,0,1,2,3])
y = q.popleft() # 前の要素を取り出す, y=5, l = deque([0,1,2,3])


# 存在しないキーに追加
from collections import defaultdict
A=[int(i) for i in input().split()]
dd=defaultdict(int)
for a in A:
    dd[a]+=1

from collections import Counter
l=['a','b','b','c','b','a','c','c','b','c','b','a']
S=Counter(l)#カウンタークラスが作られる。S=Counter({'b': 5, 'c': 4, 'a': 3})
print(S.most_common(2)) #[('b', 5), ('c', 4)]
print(S.keys()) #dict_keys(['a', 'b', 'c'])
print(S.values()) #dict_values([3, 5, 4])
print(S.items()) #dict_items([('a', 3), ('b', 5), ('c', 4)])

# 累積輪
from itertools import accumulate
A=[1,4,3,4,6,5]
print(list(accumulate(A))) #[1, 5, 8, 12, 18, 23]

# 順列と組み合わせ
from itertools import product, permutations,combinations
A=[1,2,3,4]
for i in permutations(A,2):
    print(i,end=' ')
#(1, 2) (1, 3) (1, 4) (2, 1) (2, 3) (2, 4) (3, 1) (3, 2) (3, 4) (4, 1) (4, 2) (4, 3) 
for i in combinations(A,2):
    print(i, end=' ')
#(1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4)


from operator import itemgetter
B =[(5,8), (6,10), (7,2),(4,1), (3,11),(9,0)]
print(sorted(B, key = itemgetter(0))) #第1変数で昇順ソートしてる
#[(3, 11), (4, 1), (5, 8), (6, 10), (7, 2), (9, 0)]
print(sorted(B, key = itemgetter(0),reverse=True)) #第1変数で降順ソートしてる
#[(9, 0), (7, 2), (6, 10), (5, 8), (4, 1), (3, 11)]
print(sorted(B, key = itemgetter(1))) #第2変数で昇順ソートしてる
#[(9, 0), (4, 1), (7, 2), (5, 8), (6, 10), (3, 11)]
print(sorted(B, key = itemgetter(1),reverse=True)) #第2変数で降順ソートしてる
#[(3, 11), (6, 10), (5, 8), (7, 2), (4, 1), (9, 0)]

# 二分探索
from bisect import bisect_left,bisect
L=[1,3,6,6,6,9,11]

print(bisect_left(L,0)) #0 
#0はLの先頭にくるので0番目に入ります、よって0が出力される。
print(bisect(L,0)) #0 上に同じ

print(bisect_left(L,5)) #2 
#5は3の次に入るので2番目に入ります。
print(bisect(L,5)) #2 上に同じ

print(bisect_left(L,6)) #2
#同じものがある場合は一番左の番号を出力するので、3の次にこの6は入ります。よって2番目に6がはいる。 
print(bisect(L,6)) #5 
#同じものがある場合は一番右の番号を出力するので、6の次にこの6は入ります。よって5番目に6がはいる。

print(bisect_left(L,12)) #7 
#12は一番後ろにくるので7番目に入ります。
print(bisect(L,12)) #7 上に同じ

# heap
from heapq import heappop, heappush
L=[3,0,2,5,7,2]
H=[]
for l in L: #ここはH=heapq.heapify(L)でもいいです。
    heappush(H,l) 
print(H) #[0, 3, 2, 5, 7, 2]
print(heappop(H)) #0
print(heappop(H)) #2
print(heappop(H)) #2

# 繰り返し二乗法
# n^mをpで割ったあまり
# pow(n, m, p)
# 逆元
# pow(n, p-2,p)

# 便利関数
from fractions import gcd
print(gcd(78627872,1798742872)) #8
# math.gcdかも

# アスキーコード
string = 'a'
code = 65
ord(string)
chr(code)

# itertools
## 累積和
from itertools import accumulate
A = [1,1,2,3,4,5,3]
list(accumulate(A))

# そこまで早くない　全列挙
from itertools import product, permutations,combinations
A=[1,2,3,4]
for i in permutations(A,2):
    print(i,end=' ')
#(1, 2) (1, 3) (1, 4) (2, 1) (2, 3) (2, 4) (3, 1) (3, 2) (3, 4) (4, 1) (4, 2) (4, 3) 
for i in combinations(A,2):
    print(i, end=' ')
#(1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4) 


# bisect





