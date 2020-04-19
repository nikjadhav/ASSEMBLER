from define import *
from  func import *            
def inter_code(word):
    for i in range(len(word)):
        temp=[]
        if word[i] in instruction:
            if(word[i]=='dec' or word[i]=='inc'):
                i1=return_index(word[i+1],registers32,registers16,registers8,symlist,litlist)
                interlist.append(word[i],str(i1))
            else:
                split1=word[i+1].split(',')
            i1=return_index(split1[0],registers32,registers16,registers8,symlist,litlist)
            j1=return_index(split1[1],registers32,registers16,registers8,symlist,litlist)
            interlist.append([word[i],str(i1),str(j1)])
        else:
            if((word)!=[] and word[0] in jumpz):
                i1=return_index(word[1],registers32,registers16,registers8,symlist,litlist)
                interlist.append([str(word[i]),str(i1)])

