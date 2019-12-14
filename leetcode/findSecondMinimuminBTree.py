def findSecondMin(root):
    if root is None:
        return None

    stack = [root]
    visited = set()

    while stack:
        node = stack.pop()
        visited.add(node.val)

        if node.left is not None:
            stack.append(node.left)

        if node.right is not None:
            stack.append(node.right)

    min_val = root.val
    second_min = float('inf')

    for val in visited:
        if min_val < val < second_min:
            second_min = val

    return second_min if second_min < float('inf') else -1
