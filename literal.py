from define import *
from func import *
def constant_literals(word):
    global lit
    global lineno
    lineno=lineno+1
    litlist.append(["#"+str(lit),word[0],intTohex(word[0]),word[1]])
    lit=lit+1
                   
def literal(word):
    global lit
    h=""
    temp1=""
    temp=[]
    if(word[4]=='s' and word[7]!='-'):
   #     print word[7]
        
        if(isinstance(word[7],list)):
                for i in range(len(word[7])):
                    h=h+intTohex(int(word[7][i]))
             #   print h
                temp=[word[8],word[7],h,word[9]]
                litlist.append(temp)
                lit=lit+1


        else:

            temp1=word[7]
            len1=len(word[7])
            s=focc(temp1)
            e=focc(temp1[::-1])
            e=len1-1-e
     #       print "s"+temp1[s+1:e]
            for i in range(s+1,e):
      #          print temp1[i]
                    h=h+charTohex(temp1[i])
            temp1=temp1[e+2:len(temp1)]
            temp1=list(temp1.split(','))
            #print temp1
            for i in range(len(temp1)):
            #    print temp1[i]
                h=h+(intTohex(int(temp1[i])))
           # print h
            temp=[word[8],word[7],h,word[9]]
            litlist.append(temp)
            lit=lit+1
            #print litlist
    else:
        if(word[4]=='s' and word[5]=='d' and word[7]=='-'):
            h=int(word[2])*int(word[3])
            h=filling_zero(hex(h))
            temp=[word[8],'-',h,word[9]]
            litlist.append(temp)
            lit=lit+1
