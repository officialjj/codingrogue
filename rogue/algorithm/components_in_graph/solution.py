def find_set(node: int, root: list) -> int:
    if root[node] == node:
        return node
    else:
        return find_set(root[node], root)


def components_in_graph(queries: list[list]) -> list[int]:
    """Questions: Find out the max/min number of components in a connected graph, given queries.
    i.e.
    queries = [1, 6], [2, 7], [3, 8], [4, 9], [2, 6]
    There are 3 graphs 1-2-6-7, 3-8 and 4-9.
    Return [2, 4] = [smallest # of components, largest # of components]
    """
    # init 2 list, 1 for count, 1 for storing the root
    # root =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # count = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    n = len(queries)
    nodes_count = 2 * n + 1
    root = [0] * nodes_count
    count = [0] * nodes_count
    for i in range(1, nodes_count):
        root[i] = i
        count[i] = 1

    # loop through the queries, find out the parent of a node.
    for query in queries:
        a, b = query

        # find parent (root) of a & b
        a_root = find_set(a, root)
        b_root = find_set(b, root)
        if a_root == b_root:
            continue

        # changing the parent of a node, and calculate the count (component count)
        root[b_root] = a_root
        count[a_root] += count[b_root]
        count[b_root] = 0
        print(f"changing root of {b_root} to {a_root}")
        print(root)
        print(count)

    # find min and max
    print(count)
    smallest, biggest = nodes_count, -1
    for i in range(1, nodes_count):
        if count[i] > biggest:
            biggest = count[i]

        if 1 < count[i] < smallest:
            smallest = count[i]

    return [smallest, biggest]
