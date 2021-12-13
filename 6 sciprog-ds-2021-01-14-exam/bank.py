


class Bank:

    def __init__(self):
        """ Initializes an empty bank
        
            Add a data structure of your choice for indexing the log
        """
        self._trans = []
        raise Exception('TODO IMPLEMENT ME !')

    def __str__(self):
        """Already implemented, if you want you can add display of your own index (not mandatory)
        """
        return "%s: %s" % (self.__class__.__name__, ','.join(str(t) for t in self._trans))
        
    def log(self, transaction):
        """ Appends transaction to the log
        
            - REMEMBER to also update the index
            - MUST EXECUTE IN O(1)
        """
        raise Exception('TODO IMPLEMENT ME !')
    
    
    def pos(self, biseq):
        """ RETURN a NEW list with all the indeces where the sequence of 
            two transactions can be found
        
            - MUST execute in O(1)
        """
        raise Exception('TODO IMPLEMENT ME !')
        
    def revert(self):
        """ Completely eliminates last transaction and RETURN it

            - if bank is empty, raises IndexError
            
            - REMEMBER to update any index referring to it
            - *MUST* EXECUTE IN O(1) 
        """
        
        raise Exception('TODO IMPLEMENT ME !')
        
    def max_interval(self, bi_start, bi_end):
        """ RETURN a list with all the transactions occurred between 
            the *largest* interval among bi-sequences bi_start and bi_end
        
            - bi_start and bi_end are EXCLUDED 
            - if bi_start / bi_end are not found, or if bi_end is before/includes bi_start, 
              raise LookupError

            
            - DO *NOT* MODIFY the data structure
            - MUST EXECUTE IN O(k) where k is the length of the *largest* interval you can return
            - consider number of repetitions a negligible size
        """
        raise Exception('TODO IMPLEMENT ME !')
