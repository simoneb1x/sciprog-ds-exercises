class Node:
    
    def __init__(self,initdata):
        self._data = initdata
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self,newdata):
        self._data = newdata

    def set_next(self,newnext):
        self._next = newnext


class LinkedList:
        
    def __init__(self):
        self._head = None
        
    def __str__(self):
        current = self._head
        strings = []
        
        while (current != None):
            strings.append(str(current.get_data()))            
            current = current.get_next()            
        
        return "LinkedList: " + ",".join(strings)
        
        
    def is_empty(self):
        """ Return True if the list is empty, False otherwise
        
            - MUST execute in O(1)
        """        
        return self._head == None
        

    def add(self,item):            
        """ Adds item at the beginning of the list 
        
            - MUST execute in O(1)
        """
        
        new_head = Node(item)
        new_head.set_next(self._head)
        self._head = new_head
        


    def pivot(self):
        """
            Selects first node data as pivot, and then MOVES before the pivot
            all the nodes which have data value STRICTLY LESS (<) than the pivot.
            Finally, RETURN the number of moved nodes.

            IMPORTANT:
            - *DO NOT* create new nodes
            - nodes less than pivot must be in the reversed order they were found
            - nodes greater or equal than pivot will maintain the original order
            - MUST EXECUTE in O(n), where n is the list size
        """
        current = self._head
        
        if current == None:
            return 0
        
        pivot = current
        current = current.get_next()
        prev = None
        ret = 0
        
        while current != None:
            if current._data < pivot._data:
                if prev != None:
                    temp = self._head
                    
                    x = current
                    y = current.get_next()
                    prev.set_next(y)
                    x.set_next(None)
                    
                    self._head = x
                    self._head.set_next(temp)
                    
                    current = y
                    
                    ret += 1
                else:
                    temp = self._head
                    succ = current.get_next()
                    current._next = None
                    self._head = current
                    temp.set_next(None)
                    current._next = temp
                    temp.set_next(succ)
                    prev = temp
                    current = succ
                    
                    ret += 1
            else:
                prev = current
                current = current.get_next()
                
        return ret
                
def to_ll(python_list):
    """ Creates a LinkedList from a regular Python list - very handy for testing.
    """
    ret = LinkedList()

    for el in reversed(python_list):
        ret.add(el)
    return ret

ll = to_ll([8,6])
ll.pivot()