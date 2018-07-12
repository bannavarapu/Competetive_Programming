import unittest


def bfs_get_path(graph, start_node, end_node):
    
    start= graph.setdefault(start_node,None)
    end= graph.setdefault(end_node,None)
    if start is None or end is None:
        raise Exception

    # Find the shortest route in the network between the two users
    # print graph[start_node]
    path={}
    visited=[]
    queue=[]
    queue.append(start_node)
    while(queue!=[]):
        vertex = queue.pop(0)
        visited.append(vertex)
        for j in graph[vertex]:
            if j not in visited:
                queue.append(j)
                path[j]=vertex
                if j is end_node:
                    break
    
    # print path
    value=path.setdefault(end_node,None)
    treturn=[]
    current=end_node
    while(current!=start_node):
        if current is None:
            return None
        treturn.append(current)
        current=path[current]
    treturn.append(start_node)
    treturn.reverse()
    return treturn
# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = bfs_get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = bfs_get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = bfs_get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'a', 'h')


unittest.main(verbosity=2)
