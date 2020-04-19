from define import *
from func import *
def symbol(word):
    global addr
    global sym
    global lit
    global lineno
    l=0
    i=0
    t=""
    cnt=0
    temp=[]
    #len1=len(word)
    lineno=lineno+1
    #print len(word)
    for i in range (0,len(word)):
        s=""
        temp=[]
        l=len(word[i])-1
        #print word[i]+"\t"+word[i][l]
    #    print l
 #       print word[i]
        #if(word[i]=='db' or word[i]=='dd' or word[i]=='dw' or word[i]=='dq' or word[l]==':'):
        if(word[i]=='.bss'):
                addr=0
        if(word[i]=='db'):
            j=i+1
            while(j<len(word)):
                s=s+" "+(word[j])
                j=j+1
            cnt=stlen(s)
            symbols.append(word[i-1])
            temp=["#"+str(sym),word[i-1],1,cnt,'s','d',filling_zero(hex(addr)),s,"#"+str(lit),lineno]
            sym=sym+1
            lit=lit+1
            addr=addr+cnt
            #lineno=lineno+1
            symlist.append(temp)             
        else:
            if(word[i]=='dd'):
                j=i+1
                while(j<len(word)):
                    s=s+" "+(word[j])
                    j=j+1
                s1=s.split(',')
                cnt=len(s1)
                symbols.append(word[i-1])
                temp=["#"+str(sym),word[i-1],4,cnt,'s','d',filling_zero(hex(addr)),s1,"#"+str(lit),lineno]
                addr=addr+cnt*4
                sym=sym+1
                lit=lit+1
             #   lineno=lineno+1
                symlist.append(temp)
                #print(symlist)
            else:
                if(word[i]=='dw'):
                    j=i+1
                    while(j<len(word)):
                        s=s+" "+(word[j])
                        j=j+1
                    s1=s.split(',')
                    cnt=len(s1)
                    symbols.append(word[i-1])
                    temp=["#"+str(sym),word[i-1],2,cnt,'s','d',filling_zero(hex(addr)),s1,"#"+str(lit),lineno]
                    addr=addr+cnt*2
                    sym=sym+1
                    lit=lit+1
              #      line=lineno+1
                    symlist.append(temp)
                else:
                    if(word[i]=='dq'):
                        while(j<len(word)):
                            s=s+" "+(word[j])
                            j=j+1
                        s1=s.split(',')
                        cnt=len(s1)
                        symbols.append(word[i-1])
                        temp=["#"+str(sym),word[i-1],8,cnt,'s','d',filling_zero(hex(addr)),s1,"#"+str(lit),lineno]
                        addr=addr+cnt*8
                        sym=sym+1
               #         lineno=lineno+1
                        symlist.append(temp)
                    else:
                        if(word[i]=='resb'):
                           symbols.append(word[i-1])
                           temp=["#"+str(sym),word[i-1],1,word[i+1],'s','d',filling_zero(hex(addr)),'-',"#"+str(lit),lineno]
                           addr=addr+int(word[i+1])
                           sym=sym+1
                           lit=lit+1
                #           lineno=lineno+1
                           symlist.append(temp)
                        else:
                           if(word[i]=='resd'):
                              symbols.append(word[i-1])
                              temp=["#"+str(sym),word[i-1],4,word[i+1],'s','d',filling_zero(hex(addr)),'-',"#"+str(lit),lineno]
                              addr=addr+int(word[i+1])*4
                              sym=sym+1
                              lit=lit+1
                 #             lineno=lineno+1
                              symlist.append(temp)
                           else:
                              if(word[i]=='resw'):
                                      temp=["#"+str(sym),word[i-1],2,word[i+1],'s','d',filling_zero(hex(addr)),'-',"#"+str(lit),lineno]
                                      addr=addr+int(word[i+1])*2
                                      sym=sym+1
                                      lit=lit+1
                  #                    lineno=lineno+1
                                      symlist.append(temp)
                                      #print(symlist)
                              else:
                                 if(word[i]=='resq'):
                                    symbols.append(word[i-1])
                                    temp=["#"+str(sym),word[i-1],8,word[i+1],'s','d',filling_zero(hex(addr)),'-',"#"+str(lit),lineno]
                                    addr=addr+int(word[i+1])*8
                                    sym=sym+1
                                    lit=lit+1
                   #                 lineno=lineno+1
                                    symlist.append(temp)
                                    #print(symlist)
                                 else:
                                     if(word[i] in jumpz):
                                         #print word[i+1]
    #                                     print word[i+1]
   #                                      print label
                                         #print label
                                         if(word[i+1] not in label):
                                             label.append(word[i+1])  
                                             temp=["#"+str(sym),word[i+1],'-','-','l','u','-','-','-',i,lineno]
                                             sym=sym+1
                    #                         lineno=lineno+1
#                                            lit=lit+1

                                             symlist.append(temp)
                                     else:
                                         if(word[i][l]==':'):
     #                                        print word[i][l]
                                             t=word[i][:-1]
       #                                      print t
        #                                     print label
        #                                     print t

         #                                    print label
                                             if t not in label:
                                                 label.append(t)
                                                 temp=["#"+str(sym),t,'-','-','l','d','-','-','-',lineno]
                                                 sym=sym+1
                     #                            lineno=lineno+1
         #                                        lit=lit+1
                                                 symlist.append(temp)
                                             else:
                                                 for i in range(len(symlist)):
                                                     if(t==symlist[i][1]):
                                                         if(symlist[i][5]=='u'):
                                                             symlist[i][5]='d'
                                         else:
                                             if(word[i] in instruction):
                                                 t=word[i+1].split(',')
                                                 if(t[1] not in registers32 and t[1] not in registers16 and t[1] not in registers8):
                                                     if(t[1] not in symbols and t[1] not in label):
                                                         
                                                         if(t[1].isdigit()):
                                                             
                                                             temp1=[t[1],lineno]
                                                             literals.append(temp1)
                                                         else:
                                                             
                                                             symbols.append(t[1])
                                                             temp=["#"+str(sym),t[1],'-','-','s','u','-','-','-',lineno]
                                                             sym=sym+1
                                                         #   lit=lit+1
                                                             symlist.append(temp)
