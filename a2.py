registers32=['eax','ebx','ecx','edx','esi','edi','ebp','esp']
registers16=['ax','bx','cx','dx','si','di','bp','sp']
registers8=['al','ah','bl','bh','cl','ch','dl','dh']
instruction=['add','sub','mul','mov','xor','cmp']
label=[]
jumpz=['jmp','jeq','je','jne','jg','jge','jnz','jl','jle','jz','loop']
symbols=[]
literals=[]
symlist=[]
litlist=[]
interlist=[]
lstlist=[]
addr=0
sym=1
lit=1
temp1=[]
lineno=0
dbflag=0;
def filling_zero(word):
    word=word[2:]
    return word.zfill(8)
def focc(st):
    for i in range(0,len(st)):
        
        if(st[i]=='"' or st[i]=='\''):
            return i
            break

def return_index(str1,list1,list2,list3,list4,list5):
    for i in range(len(list1)):
        if(list1[i]==str1):
            return "R32"+str(i)
            break

        else:
            for i in range(len(list2)):
                if(list2[i]==str1):
                    return "R16"+str(i)
                    break
                else:
                    for i in range(len(list3)):
                        if(list3[i]==str1):
                            return "R8"+str(i)
                            break
                        for i in range(len(list4)):
                            if(list4[i][1]==str1):
                                return "sym"+str(list4[i][0])
                                break
                            for i in range(0,len(list5)):
                                if(list5[i][1]==str1):
                                    return "lit"+str(list5[i][0])
                
def charTohex(word):
	v=hex(ord(word))
	return v[2:]
			
def intTohex(word):
	v=int(word)
	if(v<=10):
		v=hex(v)
		return '0'+v[2:]
	else:
		v=hex(v)
		return v[2:]
def stlen(s):
    j=0
    i=0
    specifier=['d','s','f','l','x','u','']
    cnt=0
    len1=len(s)-1
    j=len1
    while(s[j]!='"'):
        j=j-1
    while(i!=j):
        #print i
        if(s[i]=='%'):
            if s[i+1] in specifier:
                i=i+2
                cnt=cnt+1
                break
            else:
                i=i+1
                cnt=cnt+1
                break
        cnt=cnt+1
        i=i+1
    while(j!=len1):
        if(s[j]==','):
            cnt=cnt+1
        j=j+1
    cnt=cnt-2
    return cnt
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
            #lit=lit+1
            #print litlist
    else:
        if(word[4]=='s' and word[5]=='d' and word[7]=='-'):
            h=int(word[2])*int(word[3])
            h=filling_zero(hex(h))
            temp=[word[8],'-',h,word[9]]
            litlist.append(temp)
            
def inter_code(word):
    for i in range(len(word)):
        temp=[]
        if word[i] in instruction:
            split1=word[i+1].split(',')
            i1=return_index(split1[0],registers32,registers16,registers8,symlist,litlist)
            j1=return_index(split1[1],registers32,registers16,registers8,symlist,litlist)
            interlist.append([word[i],str(i1),str(j1)])
#            print word[i]+" "+str(i1)+" "+str(j1)

def lst(word):
    print word[0]
    for i in range(0,len(symlist)):
         #word[0]+" "+ symlist[i][1]
        if(word[0]==symlist[i][1]):
            #print word[0]
            for j in range(0,len(litlist)):
                if symlist[i][0]==litlist[j][0]:
                    #print litlist[j][2]
                    lstlist.append([symlist[i][6],litlist[j][2],word])
#                    print str(symlist[i][6])+" "+str(litlist[j][2])+ " "+str(word)
    
def main():
    content=[]
    with open("/home/nikhil/MCA/sem-3/syspro/assembler/nikhil/assign4.asm","r")as f:
        for l in f:
            l=l.split()
            content.append(l)
        #print content
        for i in range (0,len(content)):            
            word=content[i]
            #print(len(word))
            symbol(word)
        #printing symbol
        for i in range(0,len(symlist)):
               print symlist[i]
        for i in range(0,len(symlist)):
            literal(symlist[i])
        #print len(litlist)
        for i in range(0,len(literals)):
            constant_literals(literals[i])
        #printing litral
        for i in range(0,len(litlist)):
            print litlist[i]
        for i in range(0,len(content)):
            inter_code(content[i])
        #printing intermediate code
        for i in range(0,len(interlist)):
            print interlist[i]
        for i in range(0,len(content)):
            lst(content[i])
        for i in range(0,len(lstlist)):
            print lstlist[i]
if __name__=="__main__":
    main()


