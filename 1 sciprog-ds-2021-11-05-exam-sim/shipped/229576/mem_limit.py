def mem_limit(MB=None):
    import os
    if os.name == 'nt':
        print('WARNING: limiting memory on Windows is not supported')
        return
    
    import resource
    with open('/proc/meminfo', 'r') as mem:
        free_memory = 0
        for i in mem:
            sline = i.split()            
            if str(sline[0]) == 'MemAvailable:':
                free_memory = int(sline[1])               
                break     
        if sline[2] != 'kB':
            raise Exception('Unrecognized memory unit:', sline[2])
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        if not MB:                    
            MB = (free_memory // 1024) // 2  
        print('Free mem:', free_memory//1024, 'MB', 
              ' Limiting to:', MB, 'MB')
        resource.setrlimit(resource.RLIMIT_AS, (MB *1024 * 1024, hard))

mem_limit()
