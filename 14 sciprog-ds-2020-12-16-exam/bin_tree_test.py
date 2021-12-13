from bin_tree import *
import unittest


def bt(*args):
    """ Shorthand function that returns a BinaryTree containing the provided 
        data and children. First parameter is the data, the following ones are the children.

        Usage examples:

        >>> print bt('a')
        a

        >>> print bt('a', bt('b'), bt('c'))
            a
            ├b
            └c

    """
    if (len(args) == 0):
        raise Exception("You need to provide at least one argument for the data!")
    if (len(args) > 3):
        raise Exception("You must provide at most two nodes ! Found instead: %s " % (len(args) - 1))

    data = args[0]
    children = args[1:]

    ret = BinaryTree(data)

    if len(children) > 0:
        if children[0] != None and not isinstance(children[0], BinaryTree):
            raise Exception('Wrong type %s for left child!' % type(children[0]))
        ret._left = children[0]
    if len(children) == 2:
        if children[1] != None and not isinstance(children[1], BinaryTree):
            raise Exception('Wrong type %s for right child!' % type(children[1]))
        ret._right = children[1]
    return ret


def str_btrees(bt1, bt2, error_row=-1):
    """ Returns a string version of the two trees side by side

        If error_row is given, the line in error is marked.
        If error_row == -1 it is ignored
    """

    s1 = str(bt1)
    s2 = str(bt2)

    lines1 = s1.split("\n")
    lines2 = s2.split("\n")

    max_len1 = 0
    for line in lines1:
        max_len1 = max(len(line.rstrip()), max_len1)
    max_len1 = max(max_len1, len("ACTUAL"))

    max_len2 = len("EXPECTED")
    for line in lines2:
        max_len2 = max(len(line.rstrip()), max_len2)

    strings = []

    dist = 2

    strings.append(("ACTUAL").ljust(max_len1 + dist))
    strings.append("  EXPECTED\n")

    i = 0

    while i < len(lines1) or i < len(lines2):

        if i < len(lines1):
            strings.append(lines1[i].rstrip())
            len1 = len(lines1[i].rstrip())
        else:
            len1 = 0

        if (i < len(lines2)):
            len2 = len(lines2[i].rstrip())

            pad_len1 = 4 + max_len1 - len1
            strings.append((" " * pad_len1) + lines2[i].rstrip())
        else:
            len2 = 0

        if (error_row == i):
            pad_len2 = 2 + max_len1 + max_len2 - len1 - len2
            strings.append((" " * pad_len2) + "<--- DIFFERENT ! ")  # TODO this shoots 'DIFFERENT' too far !

        strings.append("\n")

        i += 1

    return "".join(strings)


class BinaryTreeTest(unittest.TestCase):

    def assertTreeEqual(self, actual, expected):
        """ Asserts the trees actual and expected are equal """

        def get_children(bt):
            ret = []
            if bt._left:
                ret.append(bt._left)
            if bt._right:
                ret.append(bt._right)
            return ret

        def rec_assert(c1, c2, row):

            if c2 == None:
                raise Exception("Found a None node in EXPECTED tree!\n\n"
                                + str_btrees(actual, expected, row))

            if c1 == None:
                raise Exception("Found a None node in ACTUAL tree! \n\n"
                                + str_btrees(actual, expected, row))

            if not isinstance(c2, BinaryTree):
                raise Exception("EXPECTED value is an instance of  %s , which is not a BinaryTree !\n\n%s" % (
                type(c2).__name__, str_btrees(actual, expected, row)))

            if not isinstance(c1, BinaryTree):
                raise Exception("ACTUAL node is an instance of  %s  , which is not a  BinaryTree  !\n\n%s"
                                % (type(c1).__name__, str_btrees(actual, expected, row)))

            if c1.data() != c2.data():
                raise Exception("ACTUAL data is different from expected!\n\n"
                                + str_btrees(actual, expected, row))

            i = 0

            cs1 = get_children(c1)
            cs2 = get_children(c2)
            if (len(cs1) != len(cs2)):
                raise Exception("Number of children is different !\n\n"
                                + str_btrees(actual, expected, row + min(len(cs1), len(cs2))))
            while (i < len(cs1)):
                rec_assert(cs1[i], cs2[i], row + 1)
                i += 1

        try:
            rec_assert(actual, expected, 0)
        except Exception as e:
            # not all exceptions have 'message'
            raise AssertionError(getattr(e, 'message', e.args[0])) from None


class BinaryTreeTestTest(BinaryTreeTest):
    """ Tests the test itself ... """

    def test_str_btrees(self):
        self.assertTrue('a' in str_btrees(bt('a'), bt('b')))
        self.assertTrue('b' in str_btrees(bt('a'), bt('b')))

        self.assertTrue('a' in str_btrees(bt('a', bt('b')), bt('b', bt('c'))))
        self.assertTrue('c' in str_btrees(bt('a', bt('b')), bt('b', bt('c'))))

    def test_assert_tree_equal(self):
        self.assertTreeEqual(bt('a'), bt('a'))
        self.assertTreeEqual(bt('a', bt('b')), bt('a', bt('b')))

        with self.assertRaises(Exception):
            self.assertTreeEqual(bt('a'), bt('b'))
        with self.assertRaises(Exception):
            self.assertTreeEqual(bt('a', bt('b')), bt('a', bt('c')))

        # different structure
        with self.assertRaises(Exception):
            self.assertTreeEqual(bt('a', bt('b')), bt('a', bt('b', bt('c'))))

        with self.assertRaises(Exception):
            self.assertTreeEqual(bt('a', bt('b', bt('c'))), bt('a', bt('b')))

    def test_print(self):
        # self.assertTreeEqual(bt('a', bt('b', bt('v')), bt('b', bt('v'))), bt('a', bt('b', bt('v'), bt('b', bt('v'))), bt('b')))
        return None

    def test_bt(self):
        with self.assertRaises(Exception):
            bt(0, bt(1), bt(2), bt(3))

        with self.assertRaises(Exception):
            bt(2, 666)

        with self.assertRaises(Exception):
            bt(2, None, 666)

        with self.assertRaises(Exception):
            bt(2, 666, 666)

        with self.assertRaises(Exception):
            bt(1, bt(2), 666)

        with self.assertRaises(Exception):
            bt(1, 666, bt(2))


class InsertLeftTest(BinaryTreeTest):

    def test_insert_left(self):
        ta = BinaryTree('a')
        self.assertEqual(ta.left(), None)
        self.assertEqual(ta.right(), None)
        ret = ta.insert_left('c')
        self.assertEqual(ret, None)
        tc = ta.left()
        self.assertEqual(tc.data(), 'c')
        self.assertEqual(tc.left(), None)
        self.assertEqual(tc.right(), None)
        self.assertEqual(ta.right(), None)

        ta.insert_left('b')
        tb = ta.left()
        self.assertEqual(ta.right(), None)
        self.assertEqual(tb.data(), 'b')
        self.assertEqual(tb.left(), tc)
        self.assertEqual(tb.right(), None)
        self.assertEqual(tc.left(), None)
        self.assertEqual(tc.right(), None)


class InsertRightTest(BinaryTreeTest):

    def test_insert_right(self):
        ta = BinaryTree('a')
        self.assertEqual(ta.left(), None)
        self.assertEqual(ta.right(), None)
        ret = ta.insert_right('c')
        self.assertEqual(ret, None)
        tc = ta.right()
        self.assertEqual(tc.data(), 'c')
        self.assertEqual(tc.left(), None)
        self.assertEqual(tc.right(), None)
        self.assertEqual(ta.left(), None)

        ta.insert_right('b')
        tb = ta.right()
        self.assertEqual(ta.left(), None)
        self.assertEqual(tb.data(), 'b')
        self.assertEqual(tb.left(), None)
        self.assertEqual(tb.right(), tc)
        self.assertEqual(tc.left(), None)
        self.assertEqual(tc.right(), None)

class SwapStackTest(BinaryTreeTest):

    def test_01_missing(self):

        with self.assertRaises(LookupError):
            bt('a').swap_stack('a', 'z')

        with self.assertRaises(LookupError):
            bt('b').swap_stack('y', 'b')

        with self.assertRaises(LookupError):
            bt('c').swap_stack('z', 'x')

        with self.assertRaises(LookupError):
            bt('a', bt('b', bt('c')), bt('d')).swap_stack('c', 'y')

        with self.assertRaises(LookupError):
            bt('a', bt('b', bt('c')), bt('d')).swap_stack('w', 'd')

    def test_02_one(self):

        t = bt('a')

        t.swap_stack('a', 'a')

        self.assertTreeEqual(t, bt('a'))
        
        t2 = bt('a')
        with self.assertRaises(LookupError):
            t2.swap_stack('b', 'b')

    def test_03_ab(self):
        tb = bt('b')
        ta = bt('a', tb )

        ret = ta.swap_stack('a', 'b')
        

        self.assertTreeEqual(ta, bt('b', bt('a')))
        self.assertEqual(id(ta.left()), id(tb))  # shouldn't create new nodes
        self.assertEqual(ret, None) # should return nothing !

    def test_04_ba(self):
        tb = bt('b')
        ta = bt('a', tb )

        ta.swap_stack('b', 'a')

        self.assertTreeEqual(ta, bt('b', bt('a')))
        self.assertEqual(id(ta.left()), id(tb))  # shouldn't create new nodes

    def test_05_abc_ab(self):
        tb = bt('b')
        tc = bt('c')
        ta = bt('a', tb, tc)

        ta.swap_stack('a', 'b')

        self.assertTreeEqual(ta, bt('b', bt('a'), bt('c')))
        self.assertEqual(id(ta.left()), id(tb))  # shouldn't create new nodes
        self.assertEqual(id(ta.right()), id(tc))  # shouldn't create new nodes

    def test_06_abc_ba(self):
        tb = bt('b')
        tc = bt('c')
        ta = bt('a', tb, tc)

        ta.swap_stack('b', 'a')

        self.assertTreeEqual(ta, bt('b', bt('a'), bt('c')))
        self.assertEqual(id(ta.left()), id(tb))  # shouldn't create new nodes
        self.assertEqual(id(ta.right()), id(tc))  # shouldn't create new nodes

    def test_07_abc_ac(self):
        tb = bt('b')
        tc = bt('c')
        ta = bt('a', tb, tc)

        ta.swap_stack('a', 'c')

        self.assertTreeEqual(ta, bt('c', bt('b'), bt('a')))
        self.assertEqual(id(ta.left()), id(tb))  # shouldn't create new nodes
        self.assertEqual(id(ta.right()), id(tc))  # shouldn't create new nodes

    def test_08_abc_ca(self):
        tb = bt('b')
        tc = bt('c')
        ta = bt('a', tb, tc)

        ta.swap_stack('c', 'a')

        self.assertTreeEqual(ta, bt('c', bt('b'), bt('a')))
        self.assertEqual(id(ta.left()), id(tb))  # shouldn't create new nodes
        self.assertEqual(id(ta.right()), id(tc))  # shouldn't create new nodes

    def test_09_abc_bc(self):
        tb = bt('b')
        tc = bt('c')
        ta = bt('a', tb, tc)

        ta.swap_stack('b', 'c')

        self.assertTreeEqual(ta, bt('a', bt('c'), bt('b')))
        self.assertEqual(id(ta.left()), id(tb))  # shouldn't create new nodes
        self.assertEqual(id(ta.right()), id(tc))  # shouldn't create new nodes

    def test_10_abc_cb(self):
        tb = bt('b')
        tc = bt('c')
        ta = bt('a', tb, tc)

        ta.swap_stack('c', 'b')

        self.assertTreeEqual(ta, bt('a', bt('c'), bt('b')))
        self.assertEqual(id(ta.left()), id(tb))  # shouldn't create new nodes
        self.assertEqual(id(ta.right()), id(tc))  # shouldn't create new nodes

    def test_11_abcd_ad(self):
        td = bt('d')
        tb = bt('b', 
                     td)
        tc = bt('c')

        ta = bt('a', 
                     tb, 
                     tc)

        ta.swap_stack('a', 'd')

        self.assertTreeEqual(ta, bt('d',
                                        bt('b',
                                                bt('a')),
                                        bt('c')))
        # shouldn't create new nodes
        self.assertEqual(id(ta.left()), id(tb))  
        self.assertEqual(id(ta.right()), id(tc)) 
        self.assertEqual(id(ta.left().left()), id(td)) 


    def test_12_abcd_bd(self):
        td = bt('d')
        tb = bt('b')
        tc = bt('c', 
                     None,
                     td)

        ta = bt('a', 
                     tb, 
                     tc)

        ta.swap_stack('b', 'd')

        self.assertTreeEqual(ta, bt('a',
                                        bt('d'),
                                        bt('c',
                                               None,
                                               bt('b'))))
        # shouldn't create new nodes
        self.assertEqual(id(ta.left()), id(tb))  
        self.assertEqual(id(ta.right()), id(tc)) 
        self.assertEqual(id(ta.right().right()), id(td))

    def test_13_complex(self):

        t = bt('a', 
                    bt('b',
                            bt('c'),
                            bt('d')),
                    bt('e',
                            None,
                            bt('f',
                                    bt('g'))))
                            

        t.swap_stack('f', 'b')

        self.assertTreeEqual(t,
                             bt('a', 
                                    bt('f',
                                            bt('c'),
                                            bt('d')),
                                    bt('e',
                                            None,
                                            bt('b',
                                                    bt('g')))))

class FamilySumTest(BinaryTreeTest):

    def test_01_0(self):
        t = bt(0)
        t.family_sum_rec()
        self.assertTreeEqual(t, bt(0))

    def test_02_1(self):
        t = bt(1)
        t.family_sum_rec()
        self.assertTreeEqual(t, bt(1))    
    
    def test_03_1_2(self):
        t = bt(1, 
                    bt(2))
        t.family_sum_rec()
        self.assertTreeEqual(t, bt(3, 
                                      bt(3)))

    def test_04_5_none_3(self):
        t = bt(5, 
                   None,
                   bt(3))
        t.family_sum_rec()
        self.assertTreeEqual(t, bt(8, 
                                    None,
                                    bt(8)))

        
    def test_05_3_7_5(self):
        t = bt(3, 
                bt(7), 
                bt(5),)
        t.family_sum_rec()
        self.assertTreeEqual(t, bt(15, 
                                      bt(10),
                                      bt(8)))

    def test_06_4_6_1_3(self):
        t = bt(4, 
                bt(6), 
                      bt(1,
                      bt(3)))
        t.family_sum_rec()
        self.assertTreeEqual(t, bt(11, 
                                      bt(10),
                                      bt(8, 
                                           bt(4))))

    def test_07_4_6_3_1(self):
        t = bt(4, 
                bt(6, 
                    bt(3)), 
                bt(1))

        t.family_sum_rec()
        self.assertTreeEqual(t, bt(11, 
                                      bt(13,
                                            bt(9)),
                                      bt(5)))

    def test_08_5_none_3_7(self):
        t = bt(5, 
                None,
                bt(3, 
                    bt(7)))

        t.family_sum_rec()
        self.assertTreeEqual(t, bt(8, 
                                      None,
                                      bt(15,
                                            bt(10))))

    def test_09_complex(self):
        t = bt(5,
                bt(1,
                     bt(4,
                          None,
                          bt(3)),
                     bt(2)),
                 bt(9,
                     bt(11)))
                                              
        t.family_sum_rec()
        self.assertTreeEqual(t, bt(15,
                                     bt(12,
                                           bt(8,
                                               None,
                                               bt(7)),
                                           bt(3)),
                                     bt(25,
                                            bt(20))))
