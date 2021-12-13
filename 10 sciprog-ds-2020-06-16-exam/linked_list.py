class Node:
    """ A Node of an LinkedList. Holds data provided by the user. """
    
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
    """
        This is a stripped down version of the LinkedList as previously seen.
        
    """
        
    def __init__(self):
        self._head = None

        
    def __str__(self):
        current = self._head
        strings = []
        
        while (current != None):
            strings.append(str(current.get_data()))            
            current = current.get_next()            
        
        return "LinkedList: " + ",".join(strings)
        
        
    def add(self,item):    
        """ Adds item at the beginning of the list """
        
        new_head = Node(item)
        new_head.set_next(self._head)
        self._head = new_head


    def slice(self, start, end):
        """ RETURN a NEW LinkedList created by copying nodes of this list
            from index start INCLUDED to index end EXCLUDED

            - if start is greater or equal than end, returns an empty LinkedList
            - if start is greater than available nodes, returns an empty LinkedList
            - if end is greater than the available nodes, copies all items until the tail without errors
            - if start index is negative, raises ValueError
            - if end index is negative, raises ValueError            

            - IMPORTANT: All nodes in the returned LinkedList MUST be NEW
            - DO *NOT* modify original linked list
            - DO *NOT* add an extra size field
            - MUST execute in O(n), where n is the size of the list
            
        """
        ret = LinkedList()
        
        if end < 0:
            raise ValueError("end is negative")
        
        if start < 0:
            raise ValueError("start is negative")
        
        if start >= end:
            return ret
        
        current = self._head
        
        if current == None:
            return ret
        
        index = 0
        cur_ret = None
        
        while current != None:
            if index == start:
                while index < end:
                    if ret._head == None:
                        ret.add(current._data)
                        cur_ret = ret._head
                    else:
                        if current == None:
                            return ret
                        new_node = Node(current._data)
                        cur_ret.set_next(new_node)
                        cur_ret = cur_ret.get_next()
                    current = current.get_next()
                    index +=1
                return ret
            else:
                current = current.get_next()
                index += 1
        
        return ret
        
def to_ll(python_list):
    """ Creates a LinkedList from a regular Python list - very handy for testing
    """
    ret = LinkedList()
    
    for el in reversed(python_list):
        ret.add(el)
    return ret

la = to_ll(['a','b','c'])
lb = la.slice(1,4) # b c