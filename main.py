from define import *
from func import *
from symbol import *
from literal import *
from  inter import *
from lst import *
from sys import argv

def main():
    fname1,action,fname2=argv
    content=[]
    with open(fname2,"r")as f:
        for l in f:
            l=l.split()
            content.append(l)
        #print content
        for i in range (0,len(content)):            
            word=content[i]
            #print(len(word))
            symbol(word)
        #printing symbol
        if(action=='-s'):
            print "symno\tsymname\tsize\tlength\tsymbol/label\tdefine\undefine\taddress\tvalue\tlitno\tlineno\n"
            for i in range(0,len(symlist)):
                word=symlist[i]
                print str(word[0])+"\t"+str(word[1])+"\t"+str(word[2])+"\t"+str(word[3])+"\t"+str(word[4])+"\t"+str(word[5])+"\t"+str(word[6])+"\t"+str(word[7])+"\t"+str(word[8])+"\t"+str(word[9])+"\n"
                #for j in range(0,len(word)):
                    #print str(word[j])+"\t"
        for i in range(0,len(symlist)):
            literal(symlist[i])
        for i in range(0,len(literals)):
            constant_literals(literals[i])
        #printing litral

        if(action=='-l'):
            print "\nlitno\tvalue\thexcode\tlineno\n"
            for i in range(0,len(litlist)):
                print str(litlist[i][0])+"\t"+str(litlist[i][1])+"\t"+str(litlist[i][2])+"\t"+str(litlist[i][3])+"\n"
        for i in range(0,len(content)):
            inter_code(content[i])
        #printing intermediate code
        if(action=='-i'):
            print "instruction\t\treg/sym/lit\t\treg/sym/lit\n"
            for i in range(0,len(interlist)):
                if(len(interlist[i])==3):
                    print str(interlist[i][0])+"\t\t\t"+str(interlist[i][1])+"\t\t\t"+str(interlist[i][2])+"\n"
                else:
                    print str(interlist[i][0])+"\t\t\t"+str(interlist[i][1])+"\n"
        for i in range(0,len(content)):
            lst(content[i])
        if(action=='-lst'):
            for i in range(0,len(lstlist)):
                print lstlist[i]
if __name__=="__main__":
    main()
