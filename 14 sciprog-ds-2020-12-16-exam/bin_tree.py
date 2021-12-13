class BinaryTree:

    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    def data(self):
        return self._data

    def left(self):
        return self._left

    def right(self):
        return self._right

    def __str__(self):
        """ Returns a pretty string of the tree """

        def str_branches(node, branches):
            """ Returns a string with the tree pretty printed.

                branches: a list of characters representing the parent branches. Characters can be either ` ` or '│'
            """
            strings = [str(node._data)]

            i = 0
            if node._left != None or node._right != None:
                for current in [node._left, node._right]:
                    if i == 0:
                        joint = '├'
                    else:
                        joint = '└'

                    strings.append('\n')
                    for b in branches:
                        strings.append(b)
                    strings.append(joint)
                    if i == 0:
                        branches.append('│')
                    else:
                        branches.append(' ')

                    if current != None:
                        if isinstance(current, BinaryTree):
                            strings.append(str_branches(current, branches))
                        else:
                            strings.append('ERROR: FOUND CHILD OF TYPE %s' % type(current))
                    branches.pop()
                    i += 1
            return "".join(strings)

        return str_branches(self, [])

    def insert_left(self, data):
        """ Takes as input DATA (*NOT* a node !!) and MODIFIES current node this way:

            - First creates a new BinaryTree (let's call it B) into which provided data is wrapped.
            - Then:
                - if there is no left node in self, new node B is attached to the left of self
                - if there already is a left node L, it is substituted by new node B, and L becomes the
                  left node of B
        """
        
        B = BinaryTree(data)
        if self._left == None:
            self._left = B
        else:
            B._left = self._left
            self._left = B
        

    def insert_right(self, data):
        """ Takes as input DATA (*NOT* a node !!) and MODIFIES current node this way:

            - First creates a new BinaryTree (let's call it B) into which provided data is wrapped.
            - Then:
                - if there is no right node in self, new node B is attached to the right of self
                - if there already is a right node L, it is substituted by new node B, and L becomes the 
                  right node of B
        """
        
        B = BinaryTree(data)
        if self._right == None:
            self._right = B
        else:
            B._right = self._right
            self._right = B
        

    def swap_stack(self, a, b):
        """ Given two elements a and b, locates the two nodes where they are contained
            and swaps *only the data* in the found nodes.

            - if a or b are not found, raise LookupError

            - IMPORTANT 1: assume tree is NOT ordered
            - IMPORTANT 2: assume all nodes have different data
            - Implement it with a while and a stack
            - MUST execute in O(n) where n is the size of the tree
        """
        stack = [self]
        node_a = None
        node_b = None
            
        while len(stack) > 0:
            temp = stack.pop()
            
            if temp._data == a:
                node_a = temp
                
            if temp._data == b:
                node_b = temp
                
            if node_a != None and node_b != None:
                temp2 = node_a._data
                node_a._data = node_b._data
                node_b._data = temp2
                return    
                
            if temp._left != None:
                stack.append(temp._left)
            if temp._right != None:
                stack.append(temp._right)                
        
        raise LookupError("A or b not found!")
        
    def family_sum_rec(self):
        """ MODIFIES the tree by adding to each node data its *original* parent and children data

            - MUST execute in O(n) where n is the size of the tree
            - a recursive implementation is acceptable
            - HINT: you will probably want to define a helper function
        """
        if self._data == 0:
            return self
            
        
        def helper(node, parent):
            current = node
            pdata = parent
            
            if pdata == None:
                pdata = current._data
                if current._left != None and current._right != None:
                    current._data += current._left._data + current._right._data
                elif current._left != None:
                    current._data += current._left._data
                elif current._right != None:
                    current._data += + current._right._data
            else:
                tmp = current._data
                if current._left != None and current._right != None:
                    current._data += pdata + current._left._data + current._right._data
                    pdata = tmp
                elif current._left != None:
                    current._data += pdata + current._left._data
                    pdata = tmp
                elif current._right != None:
                    current._data += pdata + current._right._data
                    pdata = tmp
                else:
                    current._data += pdata
                    pdata = tmp
                
            if current._left != None:
                helper(current._left, pdata)
                    
            if current._right != None:
                helper(current._right, pdata)
                
        helper(self, None)
    
# TEST #
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

t = bt(1, 
        bt(2))
t.family_sum_rec()