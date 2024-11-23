import pdb

"""
c continue
q quit
h help
    

(Pdb) h

Documented commands (type help <topic>):
========================================
EOF    cl         disable     ignore    n        return  u          where
a      clear      display     interact  next     retval  unalias  
alias  commands   down        j         p        run     undisplay
args   condition  enable      jump      pp       rv      unt      
b      cont       exceptions  l         q        s       until    
break  continue   exit        list      quit     source  up       
bt     d          h           ll        r        step    w        
c      debug      help        longlist  restart  tbreak  whatis   

-> pdb.set_trace()
(Pdb) p i, number
(0, 5)
(Pdb) c
0

-> pdb.set_trace()
(Pdb) p i,number
(1, 5)
(Pdb) q ->  throws error and exits
"""


def sequence(number):
    for i in range(number):
        pdb.set_trace()
        print(i)
    return


if __name__ == '__main__':
    sequence(5)
