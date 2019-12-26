def maxDepthRecursive(root):
    """
    :param root: TreeNode
    :return: int
    """
    if root is None:
        return 0
    else:
        print("root: " + str(root.val))
        left_height = maxDepthRecursive(root.left)
        right_height = maxDepthRecursive(root.right)

        print("left: "+str(left_height))
        print("right: "+str(right_height))

    return max(left_height, right_height) + 1


def maxDepthIterativeDFS(root):
    """
    :param root: TreeNode
    :return: int
    """

    if root is None:
        return 0

    queue = [(1, root)]
    depth = 0

    while len(queue)>0:
        current_depth, node = queue.pop(0)

        if node:
            depth = max(depth, current_depth)
            queue.append((current_depth+1, node.left))
            queue.append((current_depth+1, node.right))


    return depth


def maxDepthIterativeBFS(root):
    """
    :param root: TreeNode
    :return: int
    """

    if root is None:
        return 0

    stack = [(1, root)]
    depth = 0

    while len(stack)>0:
        current_depth, node = stack.pop()

        if node:
            depth = max(depth, current_depth)
            stack.append((current_depth+1, node.left))
            stack.append((current_depth+1, node.right))


    return depth