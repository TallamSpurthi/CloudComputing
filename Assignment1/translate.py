fp = open("32_bit.asm")
lines = fp.readlines()
counta = 0
countb = 0
for line in lines:
	line = line[:-1]
	if "mov	eax" in line and counta == 0:
		line1 = line
		counta += 1
	if "mov	ebx" in line and countb == 0:
		line2 = line
		countb += 1

line1 = line1.split(' ')[-1]
line2 = line2.split(' ')[-1]
s = line1[:1] + '$' + line1[1:]
s1 = line2[:1] + '$' + line2[1:]

text = ".LC0:" + "\n" + "\t" + ".string" + " " + '"%d' + "\\" + "n" + "\"" + "\n" + ".text" + "\n\t" + ".globl main" + "\n" + "main:" + "\n" + ".LFB0:" + "\n\t" + ".cfi_startproc" + "\n\t" + "pushq   %rbp" + "\n\t" + ".cfi_def_cfa_offset 16" + "\n\t" + ".cfi_offset 6, -16" + "\n\t" + "movq   %rsp, %rbp" + "\n\t" + ".cfi_def_cfa_register 6" + "\n\t" + "subq   $16, %rsp" + "\n\t" "movl   " + s + ", -12(%rbp)\n\t" + "movl   " + s1 + ", -8(%rbp)\n\t"+ "movl   -8(%rbp), %eax" + "\n\t" + "movl   -12(%rbp), %edx" "\n\t" + "addl   %edx, %eax\n\t" + "movl   %eax, -4(%rbp)\n\t" + "movl   -4(%rbp), %eax\n\t" + "movl   %eax, %esi\n\t" + "movl   $.LC0, %edi\n\t" + "movl   $0, %eax\n\t" + "call   printf\n\t" + "movl   $0, %eax\n\t" + "leave\n\t" + ".cfi_def_cfa 7, 8\n\t" + "ret\n\t" + ".cfi_endproc\n"

text = text.replace("'", "")
#print text

f = open("64_bit.s",'w')
f.write(text)
f.close()
