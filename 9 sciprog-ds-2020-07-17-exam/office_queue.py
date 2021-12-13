
class Node:
    """ A Node of a OfficeQueue.
    """
    def __init__(self, initdata, service):
        self._data = initdata
        self._service = service
        self._next = None        

    def get_data(self):
        return self._data

    def get_service(self):
        return self._service

    def get_next(self):
        return self._next

    def set_data(self,new_data):
        self._data = new_data

    def set_next(self,new_next):
        self._next = new_next

    def set_service(self, new_service):
        self.service = new_service

class OfficeQueue:    
    """ A queue implemented as a LinkedList
    """
    def __init__(self, services):
        """ Initializes the queue
            - services is a dictionary mapping service labels to their average completion time            
            - Complexity: O(1)
        """        
        self._head = None
        self._tail = None        
        self._size = 0
        self._wait_time = 0
        self._services = dict(services)  # defensive copy

    def __str__(self):
        """ RETURN a string representation of the OfficeQueue
        """
        current = self._head
        clients = []
        services = []
        while (current != None):
            services.append(str(current.get_service()))
            clients.append(str(current.get_data()))            
            current = current.get_next()

        return "OfficeQueue: \n" \
                + "  " + "    ".join(services) + '\n' \
                + "  " + " -> ".join(clients)

    
    def size(self):
        """ Return the size of the queue.

            - Complexity: O(1)
        """
        return self._size

    def is_empty(self):
        """ Return True if the queue is empty, False otherwise.

            - Complexity: O(1)
        """
        return self._head == None


    def enqueue(self, el, service):        
        """ Enqueues provided element el with given service. 
                    
            - If given service not among office ones, raises ValueError
            - MUST run in O(n)
        """
        
        if service not in self._services:
            raise ValueError('Unknown service %s' % service)

        new_node = Node(el, service)        

        if self._head == None:
            self._head = new_node            
        else:
            self._tail.set_next(new_node)
        self._tail = new_node
        self._size += 1

        self._wait_time += self._services[service]        
        

    def dequeue(self):
        """ Removes the node at the head and RETURN the *data* in the node

            - if queue is empty raise LookupError
        """                
        if self._head == None:
            raise LookupError
        
        self._wait_time -= self._services[service]

        ret = self._head.get_data()
        self._head = self._head.get_next()        
        
        if self._head == None:
            self._tail = None

        self._size -= 1
        return ret        

    def wait_time(self):
        """ RETURN the total wait time of the queue """
        return self._wait_time

    def time_to_service(self):
        """ In order to schedule work and pauses, for each service office employees 
            want to know after how long they will have to process the first client
            requiring that particular service. 

            RETURN a dictionary mapping each service to the time interval after which
            the service is first required.

            - If a service is not required by any client, time interval is set to 
              the queue total wait time
            - MUST run in O(n) where n is the size of the queue.
        """
        raise Exception('TODO IMPLEMENT ME !')


    def split(self):
        """ Perform two operations:
            - MODIFY the queue by cutting it so that the wait time of this cut
              will be half (or slightly more) of wait time for the whole original queue
            - RETURN a NEW queue holding remaining nodes after the cut - the wait time of  
              new queue will be half (or slightly less) than original wait time

            - If queue to split is empty or has only one element, modify nothing
              and RETURN a NEW empty queue
            - After the call, present queue wait time should be equal or slightly bigger 
              than returned queue.
            - DO *NOT* create new nodes, just reuse existing ones
            - REMEMBER to set _size, _wait_time, _tail in both original and new queue
            - MUST execute in O(n) where n is the size of the queue
        """
        raise Exception('TODO IMPLEMENT ME !')





