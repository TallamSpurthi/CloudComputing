.LC0:
	.string "%d\n"
.text
	.globl main
main:
.LFB0:
	.cfi_startproc
	pushq   %rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq   %rsp, %rbp
	.cfi_def_cfa_register 6
	subq   $16, %rsp
	movl   $3, -12(%rbp)
	movl   $4, -8(%rbp)
	movl   -8(%rbp), %eax
	movl   -12(%rbp), %edx
	addl   %edx, %eax
	movl   %eax, -4(%rbp)
	movl   -4(%rbp), %eax
	movl   %eax, %esi
	movl   $.LC0, %edi
	movl   $0, %eax
	call   printf
	movl   $0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
