from define import *
from func import *
def lst(word):
    #print word[0]
    for i in range(0,len(symlist)):
         #word[0]+" "+ symlist[i][1]
        if(word[0]==symlist[i][1]):
            #print word[0]
            for j in range(0,len(litlist)):
                if symlist[i][0]==litlist[j][0]:
                    #print litlist[j][2]
                    lstlist.append([symlist[i][6],litlist[j][2],word])
#                    print str(symlist[i][6])+" "+str(litlist[j][2])+ " "+str(word)
