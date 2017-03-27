# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
l=[]

def check_binary_search_tree_(root):
    in_order(root)
    for i in range(1,len(l)):
        if l[i-1]>=l[i]:
            return False
    return True
def in_order(r):
    if r==None:
        return
    in_order(r.left)
    l.append(r.data)
    in_order(r.right)
