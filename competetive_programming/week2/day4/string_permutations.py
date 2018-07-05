import unittest


def get_permutations(string):

    glist=[]
    # Generate all permutations of the input string
    if(len(string)==0 or len(string)==1):
        return set([string])
    for i in range(len(string)):
        newstring=string[0:i]+string[i+1:]
        newlist= get_permutations(newstring)
        for tlist in newlist:
            glist.append(string[i]+tlist)
    return set(glist)

# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
