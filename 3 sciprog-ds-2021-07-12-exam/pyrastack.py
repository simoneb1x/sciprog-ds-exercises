import jupman;

DEBUG = True

def debug(msg):
    if DEBUG:
        print("DEBUG: ", msg.replace('\n', '\n' + (' '*8)))

class PyraStack:

    def __init__(self):        
        self._rows = []

    def __str__(self):        
        """ NOTE: rows are printed bottom-up
        """
        return "\n".join(''.join(row) for row in reversed(self._rows))    

    def push(self, item):
        self._rows.append(item)

    def pop(self):
        return self._rows.pop()

    def peek(self):
        if len(self._rows) == 0:
            return
        else:
            return self._rows[len(self._rows)-1]

    def drop(self, w):
        """ Drops a block of size w on the pyrastack, trying to place it on
            the top leftmost position without having missing blocks below.
            If top row is not feasible, scans for the first available leftmost 
            place which can fully accomodate the block.            

            - if w is negative, raise ValueError
            - if w is zero, no change is made

            - MUST run in O(h + w) where h is the stack height 
        """
        if w < 0:
            raise ValueError("w is negative")
        
        if w == 0:
            return
        
        temp = self.peek()
        
        if temp == None:
            self.push(['-'] * w)
            return
        
        if len(self._rows) == 1 and w == len(temp):
            self.push(['-'] * w)
            return
        
        status = False
        
        if w >= len(temp):
            for elem in reversed(range(len(self._rows))):
                if len(self._rows[elem-1]) >= len(self._rows[elem]) + w:
                    self._rows[elem].extend(['-'] * w)
                    status = True
                    return
            
            if status == False:
                self._rows[0].extend(['-'] * w)
                return
            else:
                return
        
        self.push(['-'] * w)
        
s = PyraStack()
s.drop(3)
s.drop(3)

