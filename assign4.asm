section .data
	First db "ab ,cd",10,0
 	l dd 10,20,30
	k dw 11,22,33,44,55
	last db "my name is nikhil",10,0
	name db '"nikhil","jadhav"',10,0
section .bss
	ten resb 10
	second resb 10
	third resw 10
section .text
	global main
main:	mov esi,First
	mov ecx,len
	mov edi,First
	xor eax,eax
	mov dx,5
loop1:
	mov esi,First
	mov ecx,ebx
	mov ah,al	
loop2: 
	cmp byte[esi],10
	loop loop2
swap:
	mov al,aaa
	stosb
	mov al,10
	stosb
	mov al,0
	stosb
print:
	mov eax,4
	mov ebx,1
	mov ecx,First
	int 0x80
	dec dx
	cmp dx,0
	jnz loop1	
