# import jupman
# jupman.mem_limit()

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
        
    def norep(self):
        """ MODIFIES this list by removing all the consecutive 
            repetitions from it.

            - MUST perform in O(n), where n is the list size.
        """
        
        # I set the current node variable
        current = self._head
        
        # If current is none, just simply return the list
        if current == None:
            return current
        
        # Start a while cycle until next element is None
        while current.get_next() != None:
            
            # If current is equal to next element, we have a repetition and we have to remove the consecutive element
            if current._data == current._next._data:
                current._next = current._next._next # Link current node to next one
            else:
                current = current._next
            

# TESTING - OK #
# python3 -m unittest linked_list_test.NorepTest
