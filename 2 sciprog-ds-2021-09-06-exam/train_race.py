class TrainRace:
    
    
    def __init__(self, lengths, velocities):
        """ Initializes the class with two lists holding the lengths and velocities of trains

            - if list lengths mismatches, raise ValueError
            - if a length or a velocity is less than one, raises ValueError
            
            - MUST execute in O(n) where n is sum of train lengths
            - HINT: think about additional fields which may help speeding up the program
        """
        if len(lengths) != len(velocities):
            raise ValueError("List lengths mismatches")
        
        total_length = len(lengths)
        
        for elem in range(total_length):
            if lengths[elem] < 1 or velocities[elem] < 1:
                raise ValueError("elem is less than 0!")
        
        self._lengths = lengths
        self._velocities = velocities
        self._paths = []
            
        for elem in self._lengths:
            self._paths.append(['*'] * elem)


    def get_paths(self):
        """ 
            Return the train paths as a list of list of characters
        
            ********  MUST RUN IN O(1)  *********
        
            HAVE YOU READ THE REQUIREMENT ABOVE ?
        """
        return self._paths


    def step(self):
        """ Steps the simulation by moving each train toward right 
            by a number of cells given by its velocity.            
            
                        
            *** MUST run in O(v) where v is the sum of all velocities     
            
            *** Complexity MUST *NOT* depend on train length nor dashes length
            
            *** For simplicity, ASSUME velocity is always 
                less or equal than train length                 
            
            ********      HAVE YOU READ THE REQUIREMENTS ABOVE ?   ********
        """
        i = 0
        temp = []
        for elem in self._velocities:
            temp.append(['-'] * elem)
            self._paths[i] = temp[i] + self._paths[i] 
            i += 1
    
tr = TrainRace([5,3,6,3], [2,1,3,2])
tr.step()
tr.get_paths()