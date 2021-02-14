# Naive iterative sol:
def all_kind_of_node_depths1(root):
    stack = [root]
    sum_node_depths = 0
    while len(stack):
        current = stack.pop()
        if current is None:
            continue
        sum_node_depths += nodeDepths(current)
        stack.append(root.left)
        stack.append(root.right)
    return sum_node_depths
# TC IS DISCUSSED IN NOTES IN DETAIL It will be around O(N(LOGN)) AND IN WORST CASE SCENARIOS IT WILL BE O(N^2)


def nodeDepths(node, depth=0):
    return depth+nodeDepths(node.left, depth+1)+nodeDepths(node.right, depth+1)

# Naive recursive sol:


def all_kind_of_node_depths2(root):
    if root is None:
        return 0
    return nodeDepths(root.left) + nodeDepths(root.right) + nodeDepths(root)
# TC IS DISCUSSED IN NOTES IN DETAIL It will be around O(N(LOGN)) AND IN WORST CASE SCENARIOS IT WILL BE O(N^2)


def nodeDepths(node, depth=0):
    return depth+nodeDepths(node.left, depth+1)+nodeDepths(node.right, depth+1)

# Optimized Approach for the above solution:


def all_kind_of_node_depths3(root):
    # We do 3 passes in this approach: The first one will be finding out the no of nodes
    # and the second pass will be finding out the depth on that node using the derived optimized formula
    # and the third pass will be summing up the no of nodes and the node depths on that particular thing.
    nodeCounts = {}
    addNodeCounts(root, nodeCounts)
    nodeDepths = {}
    addNodeDephs(root, nodeCounts, nodeCounts)
    return sumAllNodesDepth(root, nodeDepths)

# We are doing this in linear Time:


def addNodeCounts(node, nodeCounts):
    nodeCounts[node] = 1  # The base case if incase we dont have any children
    if node.left is not None:
        addNodeCounts(node.left, nodeCounts)
        nodeCounts[node] += nodeCounts[node.left]
    if node.right is not None:
        addNodeDephs(node.right, nodeCounts)
        nodeCounts[node] += nodeCounts[node.right]

# This will also operate in linear time:


def addNodeDephs(node, nodeCounts, nodeCounts):
    nodeCounts[node] = 0
    if node.left is not None:
        addNodeDephs(node.left, nodeCounts)
        nodeCounts[node] += addNodeDephs[node.left]+addNodeCountss[node.left]
    if node.right is not None:
        addNodeDephs(node.=right, nodeCounts)
        nodeCounts[node] += addNodeDephs[node.right]+addNodeCountss[node.left]

# This is the last function we write to get the desired output!


def sumAllNodesDepth(root, nodeDepths):
    if root is None:
        return 0
    return sumAllNodesDepth(root.left, nodeDepths)+sumAllNodesDepth(root.right, nodeDepths)+nodeDepths(root)

# Whole TC Of Optimized Approach: O(N) and SC:O(H) where H is the Height of the tree.
