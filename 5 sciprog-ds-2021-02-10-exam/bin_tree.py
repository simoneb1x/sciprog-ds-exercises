
class BinaryTree:
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
        
        B =  BinaryTree(data)
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
        


def reconstruct(root, iterator):
    """ Takes a root (i.e. 'a') and a sequence of tuples (node, branch, subnode) 
        *in no particular order* 
        i.e. ('b','R','c'), ('a','L','b'), ('a','R','b') ...
        
        and RETURN a NEW BinaryTree reconstructed from such tuples
            
        - node and subnode are represented as node data
        - a branch is indicated by either 'L' or 'R'           
        
        - MUST perform in O(n) where n is the length of the stream 
          produced by the iterator
        - NOTE: you can read the sequence only once (you are given an iterator)                
        - in case a branch is repeated (i.e. ('a','L','b') and ('a','L','c'))
          the new definition replaces old one        
    """ 
    
    diz = {
        root: BinaryTree(root)
    }
    
    for elem in iterator:
        if elem[0] not in diz:
            diz[elem[0]] = BinaryTree(elem[0])
            node = diz[elem[0]]
        else:
            node = diz[elem[0]]
        
        if elem[2] not in diz:
            diz[elem[2]] = BinaryTree(elem[2])
            sub = diz[elem[2]]
        else:
            sub = diz[elem[2]]
        
        if elem[1] == 'L':
            node._left = sub
            
        if elem[1] == 'R':
            node._right = sub
            
    return diz[root]
        
        
        

        
    