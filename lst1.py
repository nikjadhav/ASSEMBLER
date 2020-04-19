def opcodeG2(r,line_no):
	global Literal_NO
	opcodeforreg=temp=singleregistervalue=""
	stri=""
	s=r.strip()
	s=s+'?'
	strn=interme=modrm=""
	slen=len(s)
	count=flag=flagforO=byte=0
	#strin =string input,stri
	for i in range(0,slen):
		stf=0
		if(s[i]==':' or s[i]==' ' or s[i]==',' or s[i]==';' or s[i]=='[' or s[i]==']' or s[i]=='?'):
			if(strn==""):
				continue
			if(s[i]==':'):											
				lst_table['line_num'].append(line_no)
				lst_table['hex'].append(' ')
				lst_table['instruction'].append(strn)
				strn=""
				continue
			if(strn!=""):
				for j in ins:	
					if(strn==j):
						stri=stri+strn
						interme=interme+strn
						strn=""
						break
				a,b=check_sym(strn)
				if(s[i]=='['):     #for memory operation
					for ty in mem:
						if(strn==ty):
							byte=mem[ty]
					if(opcodeforreg!=""):
						singleregistervalue=opcodeforreg
						opcodeforreg=""
					
				elif(s[i]==']'):
				#	tp,cal=addrcal(strn)  
				#	print("TP:",tp,"CAL:",cal,"Return") #temp
					ct,base,modrm_in=oprationcode(strn) 
				#	print(opcodeforreg,"ca=",ca)
					modrm=modrm+modrm_in
					if(len(ct)==2):
						opcodeforreg=ct+base
					#print(opcodeforreg,"after")
					interme=interme+' '+base	#interme=interme+' '+str(val) #interme=interme+' '+base
					stri=stri+' '+'mem'
					#print(opcodeforreg,"opcodeforregopcodeforregopcodeforregopcodeforreg",modrm)
				elif('y'==a and dic['seg'][b]!='code'):
					tp=dic['ele'][b]
					if(dic['seg'][b]=='bss'):
						tp=str(dic['size'][b])
					interme=interme+' '+tp
					stri=stri+' '+'mem'					

				#print(strn)		
				#handel jump line number
				if(s[i]!=']'):
					for i in range(len(dic['sym']) ):
						if(dic['sym'][i]==strn and dic['type'][i]=='lbl'):
							stf=1
							opcodeforreg=opcodeforreg+'lineNo'+str(dic['lineNo'][i]) 
						
				if(True==(strn.isdigit())):  #for the literal values
					digi=strn
					l=len(strn)
					if(True==stri[-2:].isdigit()):
						l=stri[-2:]
					elif(l<=3):
						l='08'
					elif(l<=5):
						l='16'
					elif(l<=10):
						l='32'
					stri=stri+' '+'lit'+l
					c=str(hex(int(strn))[2:])
					for i in range(len(str(dic['addr'][b])),8):
						c='0'+c
					
					opcodeforreg='['+c+']'+' '+opcodeforreg  #this for the literal values constant  also represent [ ] bracket 


				if('y'==check_reg(strn)):
					stri=stri+' '+rs[strn][0]
					interme=interme+' '+rs[strn][2]
					opcodeforreg=opcodeforreg+' '+format(rs[strn][1],'03b')
					modrm=modrm+format(rs[strn][1],'03b')
				#	print("modrm----====",modrm)
				#	print(opcodeforreg,"gh")
				a,b=check_sym(strn)
				if('y'==a and (dic['seg'][b]!='code') ):
					stf=0
					c=str(dic['addr'][b])
					for i in range(len(str(dic['addr'][b])),8):
						c=c+'0'
					if(('{' in opcodeforreg)==False):
						opcodeforreg=opcodeforreg+'{'+c+'}'

				if('y'==check_con(strn)):
					stri=stri+' '+'mem'
					interme=interme+' '+'mem'
					opcodeforreg=opcodeforreg+' '+'(00000000)'
					break

			strn=""		
		else:
			strn+=s[i]
		i+=1
	#print(stri)
	st=stri.split()
	for cl in st:
		if(cl[:3]=='lit'):
			dym='lit#'+str(Literal_NO)
			interme=interme+' '+dym
			Literal_NO=Literal_NO+1

	#print(stri,"intermediate",interme,"Line_no",line_no)		lst_tablelst_talst_tableble
	coun=op=0
	for opcode in instruction_type['ist']:     
		if(opcode==stri):

			if(len(stri.split())==2):
				print((stri.split()[1:][0])[:3])
			else:
				for i in modR:
					if((i==(stri.split()[1:][0])[:3]+' '+(stri.split()[1:][1])[:3])):
						op=modR[i]
						if(op==0 or op==1):
							modrm=format(op,'02')+modrm
						if(len(modrm)==8):
							temp=hex(int(modrm,2))[2:]
							if(len(temp)==1):
								temp='0'+temp
							opcodeforreg=opcodeforreg+' '+temp
			lst_table['line_num'].append(line_no)
			ls=opcodeforreg.split() #swap of register binary values
			#print(ls)
			if(len(ls)>=2):
				ls[0],ls[1]=ls[1],ls[0]
				opcodeforreg=''.join(ls)
				  #for register to register opcode 
				
			print(stri)
			if(op!=0):
				op=str(bin(op)[2:])
				s=""
				if('{' in opcodeforreg ):
					s=opcodeforreg
					opcodeforreg=opcodeforreg[:opcodeforreg.index('{')]
					s=s[s.index('{'):s.index('}')+1]
				opcodeforreg=op+opcodeforreg
				opcodeforreg=format(int(opcodeforreg,2),'02x')+s
			else:	
				op=''
			if(singleregistervalue!=""):
				ope=hex(int(singleregistervalue,2)+int(instruction_type['code'][coun]))[2:]
				if(len(ope)==1):
					ope='0'+ope
				lst_table['hex'].append(ope+' '+str(opcodeforreg))
			else:
				ope=hex(int(instruction_type['code'][coun]))[2:]
				if(len(ope)==1):
					ope='0'+ope
				lst_table['hex'].append(ope+' '+str(opcodeforreg))
			lst_table['instruction'].append(r)
			intermed['Iline'].append(interme)	
		coun=coun+1
	#End of opcode generation 

