# import jupman
# jupman.mem_limit()

class BinTree:
    """ A simple binary tree with left and right branches
    """
    
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
                        if isinstance(current, BinTree):
                            strings.append(str_branches(current, branches))
                        else:
                            strings.append('ERROR: FOUND CHILD OF TYPE %s' % type(current))
                    branches.pop()                
                    i += 1
            return "".join(strings)
        
        return str_branches(self, [])

    def insert_left(self, data):
        """ Takes as input DATA (*NOT* a node !!) and MODIFIES current node this way:
        
            - First creates a new BinTree (let's call it B) into which provided data is wrapped.
            - Then:
                - if there is no left node in self, new node B is attached to the left of self
                - if there already is a left node L, it is substituted by new node B, and L becomes the 
                  left node of B
        """
        
        B =  BinTree(data)
        if self._left == None:
            self._left = B
        else:
            B._left = self._left
            self._left = B
        

    def insert_right(self, data):
        """ Takes as input DATA (*NOT* a node !!) and MODIFIES current node this way:
        
            - First creates a new BinTree (let's call it B) into which provided data is wrapped.
            - Then:
                - if there is no right node in self, new node B is attached to the right of self
                - if there already is a right node L, it is substituted by new node B, and L becomes the 
                  right node of B
        """
        
        B = BinTree(data)
        if self._right == None:
            self._right = B
        else:
            B._right = self._right
            self._right = B
        

    def family_sum_rec(self):
        """ MODIFIES the tree by adding to each node data its *original* parent and children data

            - MUST execute in O(n) where n is the size of the tree
            - a recursive implementation is acceptable
            - HINT: you will probably want to define a helper function
        """
        
        # X will be the variable to pass to helper function in order to understand
        #   if a node as a parent or not
        x = None
        
        # Define helper function which receives 'prec' as input. We will pass 'x' to it.
        def helper(self, prec):
            
            # if prec is none, we should be in the root. So we have to check if root has children, in this case we sum them
            if prec == None:
                prec = self._data # we set the root as parent that we will pass to the recursive function
                
                if self._left != None and self._right != None:
                    self._data += self._left._data + self._right._data
                elif self._left != None:
                    self._data += self._left._data
                elif self._right != None:
                    self._data += self._right._data
                    
            # if prec is different from None, then we have a parent. So we have to consider it in the sum        
            else:
                tmp = self._data # we store current data node in a temporary variable
                
                if self._left != None and self._right != None:
                    self._data += self._left._data + self._right._data + prec
                elif self._left != None:
                    self._data += self._left._data + prec
                elif self._right != None:
                    self._data += self._right._data + prec
                else:
                    self._data += prec
                
                prec = tmp # we set 'prec' variable equal to the temporary variable that we declared before
                
            if self.left() != None:
                helper(self.left(), prec)
            
            if self.right() != None:
                helper(self.right(), prec)
                
        helper(self, x)
            
# TESTING - OK #
# python3 -m unittest bin_tree_test.FamilySumTest