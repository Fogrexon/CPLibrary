import sys
sys.setrecursionlimit(10**6)

f = open('./L', mode='r')
ans = open('./A', mode='w')

def input():
  return f.readline().strip()
ansList = []

# 処理

ans.write('\n'.join(ansList))

ans.close()
f.close()
