#BFS traversal in a tree
def BFS(root):
  q=collections.deque([root])
  while q:
    v=q.popleft()
    print(v.val)
    if v.left:
      q.append(v.left)
    if v.right:
      q.append(v.right)
BFS(root)
      
      
  
