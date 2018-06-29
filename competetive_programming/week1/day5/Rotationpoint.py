# import unittest


# def find_rotation_point(words):

#     # Find the rotation point in the list
#     mini=0
#     maxi=len(words)-1
#     print()
#     print(words)
#     while(mini<maxi):
#         print('min: ',mini, " max: ",maxi)
#         mid=(mini+maxi)//2
#         # if(mid-1<0 or mid+1>len(words)):
#         #     return mid
#         # else:
#         if(words[mid]<words[mid-1] and words[mid]<words[mid+1]):
#             return mid
#         elif(words[mid]>words[]):
#             mini=mid+1
#         else:
#             maxi=mid-1
        
#     return mini+1

# # Tests

# class Test(unittest.TestCase):

#     def test_small_list(self):
#         actual = find_rotation_point(['cape', 'cake'])
#         expected = 1
#         self.assertEqual(actual, expected)

#     def test_medium_list(self):
#         actual = find_rotation_point(['grape', 'orange', 'plum',
#                                       'radish', 'apple'])
#         expected = 4
#         self.assertEqual(actual, expected)

#     def test_large_list(self):
#         actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
#                                       'undulate', 'xenoepist', 'asymptote',
#                                       'babka', 'banoffee','engender',
#                                       'karpatka', 'othellolagkage','zoo'])
#         expected = 5
#         self.assertEqual(actual, expected)

#     # Are we missing any edge cases?


# unittest.main(verbosity=2)





import unittest


def find_rotation_point(words):

    # Find the rotation point in the list
    mini=0
    maxi=len(words)-1
    print()
    print(words)
    while(mini<maxi):
        print('min: ',mini, " max: ",maxi)
        mid=(mini+maxi)/2
        if(words[mid]<words[mid-1] and words[mid]<words[mid+1]):
            return mid
        elif(words[mid]>words[maxi]):
            mini=mid+1
        else:
            maxi=mid-1

    return mini

# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee','engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)
    def test_small_list2(self):
        actual = find_rotation_point(['a', 'b','c'])
        expected = 0
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)