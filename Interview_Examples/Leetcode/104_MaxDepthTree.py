def maxDepth(root):
    if root == None:
        return 0

    depth = 0
    queue = collections.deque()
    queue.append(root)
    while (len(queue) > 0):
        level_size = len(queue)
        depth += 1
        for i in range(0, level_size, 1):
            popped = queue.popleft()
            print(popped.val)
            if popped.left != None:
                queue.append(popped.left)
            if popped.right != None:
                queue.append(popped.right)

    return depth