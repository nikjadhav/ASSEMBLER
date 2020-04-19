from define import *
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
