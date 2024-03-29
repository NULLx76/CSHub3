+++
title = "Assembly Cheatsheet"
date = 2019-09-04
+++
<div style="white-space: normal;" class="markdown-body"><h2 id="registers">Registers</h2>
</div><div style="white-space: normal;" class="markdown-body"><h3 id="registers-table">Registers Table</h3>
<table>
<thead>
<tr>
<th>64-bit register</th>
<th>Lower 32 bits</th>
<th>Lower 16 bits</th>
<th>Lower 8 bits</th>
</tr>
</thead>
<tbody>
<tr>
<td>rax</td>
<td>eax</td>
<td>ax</td>
<td>al</td>
</tr>
<tr>
<td>rbx</td>
<td>ebx</td>
<td>bx</td>
<td>bl</td>
</tr>
<tr>
<td>rcx</td>
<td>ecx</td>
<td>cx</td>
<td>cl</td>
</tr>
<tr>
<td>rdx</td>
<td>edx</td>
<td>dx</td>
<td>dl</td>
</tr>
<tr>
<td>rsi</td>
<td>esi</td>
<td>si</td>
<td>sil</td>
</tr>
<tr>
<td>rdi</td>
<td>edi</td>
<td>di</td>
<td>dil</td>
</tr>
<tr>
<td>rbp</td>
<td>ebp</td>
<td>bp</td>
<td>bpl</td>
</tr>
<tr>
<td>rsp</td>
<td>esp</td>
<td>sp</td>
<td>spl</td>
</tr>
<tr>
<td>r8</td>
<td>r8d</td>
<td>r8w</td>
<td>r8b</td>
</tr>
<tr>
<td>r9</td>
<td>r9d</td>
<td>r9w</td>
<td>r9b</td>
</tr>
<tr>
<td>r10</td>
<td>r10d</td>
<td>r10w</td>
<td>r10b</td>
</tr>
<tr>
<td>r11</td>
<td>r11d</td>
<td>r11w</td>
<td>r11b</td>
</tr>
<tr>
<td>r12</td>
<td>r12d</td>
<td>r12w</td>
<td>r12b</td>
</tr>
<tr>
<td>r13</td>
<td>r13d</td>
<td>r13w</td>
<td>r13b</td>
</tr>
<tr>
<td>r14</td>
<td>r14d</td>
<td>r14w</td>
<td>r14b</td>
</tr>
<tr>
<td>r15</td>
<td>r15d</td>
<td>r15w</td>
<td>r15b</td>
</tr>
</tbody>
</table>
</div><div style="white-space: normal;" class="markdown-body"><p>Other important registers:
RIP = instruction pointer, points to the next instruction to be executed. changing this register is the same as a jumps<br>
RFLAGS = register that stores information about the last calculation (flags) to use for conditional jumps</p>
</div><div style="white-space: normal;" class="markdown-body"><p><a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/x64-architecture">Source/More Info</a></p>
</div><div style="white-space: normal;" class="markdown-body"></div><div style="white-space: normal;" class="markdown-body"><h3 id="register-memory-layout">Register Memory Layout</h3>
<p>Registers work like this, meaning every row in the above table is actually the same register but parts of it as shown below:</p>
</div><div style="white-space: normal;" class="markdown-body"><p><img src="https://i.imgur.com/NWV45Vf.png" alt=""></p>
</div><div style="white-space: normal;" class="markdown-body"><h2 id="opcode-table">Opcode Table</h2>
<table>
<thead>
<tr>
<th>opcode</th>
<th>operands</th>
<th>function</th>
<th>description</th>
</tr>
</thead>
<tbody>
<tr>
<td>mov</td>
<td>src,dst</td>
<td>dst = src</td>
<td>copy</td>
</tr>
<tr>
<td>push</td>
<td>dst</td>
<td>(%rsp) = dst, %rsp -= 8</td>
<td>pushes a value onto the stack</td>
</tr>
<tr>
<td>pop</td>
<td>src</td>
<td>%rsp += 8,src=(%rsp)</td>
<td>pops a value off the stack</td>
</tr>
<tr>
<td>xchg</td>
<td>A,B</td>
<td>A,B = B,A</td>
<td>switches the contents of A and B</td>
</tr>
<tr>
<td>---</td>
<td>---</td>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td>addq</td>
<td>src,dst</td>
<td>dst = dst + src</td>
<td>adds src to dst</td>
</tr>
<tr>
<td>subq</td>
<td>src,dst</td>
<td>dst = dst - src</td>
<td>subtracts src from dst</td>
</tr>
<tr>
<td>inc</td>
<td>dst</td>
<td>dst = dst + 1</td>
<td>adds 1 to dst</td>
</tr>
<tr>
<td>dec</td>
<td>dst</td>
<td>dst = dst - 1</td>
<td>subtracts 1 from dst</td>
</tr>
<tr>
<td>mulq</td>
<td>src</td>
<td>rdx:rax = rax * src</td>
<td>multiplies rax by src (UNSIGNED)</td>
</tr>
<tr>
<td>imulq</td>
<td>src</td>
<td>rdx:rax = rax * src</td>
<td>multiplies rax by src (SIGNED)</td>
</tr>
<tr>
<td>divq</td>
<td>src</td>
<td>rdx:rax = rax / src</td>
<td>divides rax by src (SIGNED)</td>
</tr>
<tr>
<td>idivq</td>
<td>src</td>
<td>rdx:rax = rax / src</td>
<td>divides rax by src (SIGNED)</td>
</tr>
<tr>
<td>---</td>
<td>---</td>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td>jmp</td>
<td>label</td>
<td></td>
<td>jumps to label (unconditional)</td>
</tr>
<tr>
<td>je</td>
<td>label</td>
<td></td>
<td>jumps to label (if equal)</td>
</tr>
<tr>
<td>jne</td>
<td>label</td>
<td></td>
<td>jumps to label (if not equal)</td>
</tr>
<tr>
<td>jg</td>
<td>label</td>
<td></td>
<td>jumps to label (if greater than)</td>
</tr>
<tr>
<td>jl</td>
<td>label</td>
<td></td>
<td>jumps to label (if less than)</td>
</tr>
<tr>
<td>jle</td>
<td>label</td>
<td></td>
<td>jumps to label (if less than or equal)</td>
</tr>
<tr>
<td>jge</td>
<td>label</td>
<td></td>
<td>jumps to label (if greater than or equal)</td>
</tr>
<tr>
<td>call</td>
<td>label</td>
<td>push &lt;current adress + 1&gt;, jmp label</td>
<td>calls a function</td>
</tr>
<tr>
<td>ret</td>
<td></td>
<td>jmp (%rsp)</td>
<td>returns to caller</td>
</tr>
<tr>
<td>loop</td>
<td>label</td>
<td>dec %rcx, jnz label</td>
<td></td>
</tr>
<tr>
<td>---</td>
<td>---</td>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td>cmp</td>
<td>A,B</td>
<td>A - B (answer not stored but flags set)</td>
<td>compares 2 numbers. jump instruction follows</td>
</tr>
<tr>
<td>xorq</td>
<td>src,dst</td>
<td>src = src xor dst</td>
<td>bitwise xor</td>
</tr>
<tr>
<td>orq</td>
<td>src,dst</td>
<td>src = src and dst</td>
<td>bitwise and</td>
</tr>
<tr>
<td>andq</td>
<td>src,dst</td>
<td>src = src or dst</td>
<td>bitwise and</td>
</tr>
<tr>
<td>shlq</td>
<td>A,dst</td>
<td>src = src &lt;&lt; A</td>
<td>shift left</td>
</tr>
<tr>
<td>shrq</td>
<td>A,dst</td>
<td>src = src &gt;&gt; A</td>
<td>shift right</td>
</tr>
<tr>
<td>not</td>
<td>dst</td>
<td>dst = 1111111- dst</td>
<td>bitwise inversion of dst</td>
</tr>
<tr>
<td>neg</td>
<td>dst</td>
<td>dst = 0 - dst</td>
<td>2's complement, result of not and add 1</td>
</tr>
<tr>
<td>leaq</td>
<td>A, dst</td>
<td>dst = &amp;A</td>
<td>load effective adress (&amp; means adress of)</td>
</tr>
<tr>
<td>int</td>
<td>int_no</td>
<td></td>
<td>software interrupt (see linux system calls above, used together with int 0x80)</td>
</tr>
</tbody>
</table>
</div><div style="white-space: normal;" class="markdown-body"><h2 id="stackframe">Stackframe</h2>
<p>Generally, to initialize a stackframe use:</p>
<pre data-lang="assembly"><code>push %rbx #save necessary registers
push %r12
push %r13
push %r14
push %r15
push %rbp #generate stackframe
movq %rsp, %rbp
</code></pre>
</div><div style="white-space: normal;" class="markdown-body"><p>And to destroy it again use:</p>
<pre data-lang="assembly"><code>movq %rbp, %rsp #restore last stackframe
pop %rbp
pop %r15 #restore necessary registers
pop %r14	
pop %r13	
pop %r12	
pop %rbx	
ret
</code></pre>
</div><div style="white-space: normal;" class="markdown-body"><h2 id="addressing-modes">Addressing Modes</h2>
<table>
<thead>
<tr>
<th>example</th>
<th>name</th>
<th>description</th>
</tr>
</thead>
<tbody>
<tr>
<td>movq $label,%rax</td>
<td>immediate (pointer)</td>
<td>loads the location of the label into rax</td>
</tr>
<tr>
<td>movq label,%rax</td>
<td>immediate</td>
<td>loads the quadword at the location of the label into rax</td>
</tr>
<tr>
<td>movq (%rbx),%rax</td>
<td>indirect</td>
<td>loads the quadword at the location pointed to by rbx into rax</td>
</tr>
<tr>
<td>movq 8(%rbx),%rax</td>
<td>indirect offset (positive)</td>
<td>loads the quadword 8 after the location pointed to by rbx into rax</td>
</tr>
<tr>
<td>movq -8(%rbx),%rax</td>
<td>indirect offset (negative)</td>
<td>loads the quadword 8 before the location pointed to by rbx into rax</td>
</tr>
<tr>
<td>movq (%rbx,%rcx),%rax</td>
<td>indirect variable offset</td>
<td>loads the quadword at %rcx after the location pointed to by rbx into rax</td>
</tr>
<tr>
<td>movq (%rbx,%rcx,8),%rax</td>
<td>indirect variable scaled offset (negative)</td>
<td>loads the quadword at %rcx*8 after the location pointed to by rbx into rax</td>
</tr>
<tr>
<td>movq 8(%rbx,%rcx,8),%rax</td>
<td>indirect variable scaled offset (negative) +constant</td>
<td>loads the quadword at 8 after %rcx*8 after the location pointed to by rbx into rax</td>
</tr>
</tbody>
</table>
</div><div style="white-space: normal;" class="markdown-body"><h2 id="assembler-directives">Assembler Directives</h2>
</div><div style="white-space: normal;" class="markdown-body"><p>Assembler directives are notes for the assembler which tell it how to do the compiling.</p>
</div><div style="white-space: normal;" class="markdown-body"><table>
<thead>
<tr>
<th>directive</th>
<th>explaination</th>
</tr>
</thead>
<tbody>
<tr>
<td>.quad</td>
<td>reserves space for a 64 bit number to be stored</td>
</tr>
<tr>
<td>.long</td>
<td>reserves space for a 32 bit number to be stored</td>
</tr>
<tr>
<td>.word</td>
<td>reserves space for a 16 bit number to be stored</td>
</tr>
<tr>
<td>.byte</td>
<td>reserves space for a 8  bit number to be stored</td>
</tr>
<tr>
<td>.asciz</td>
<td>reserves space for a string of text to be stored, automatically terminated by a 0 (NULL )</td>
</tr>
<tr>
<td>.ascii</td>
<td>reserves space for a string of text to be stored, <em>not</em> automatically terminated by a 0 (NULL )</td>
</tr>
<tr>
<td>.skip n</td>
<td>skips n bytes. useful for defining arrays of data. This should normally only be used in the .bss <a href="#bss">section</a></td>
</tr>
</tbody>
</table>
</div><div style="white-space: normal;" class="markdown-body"><h2 id="sections">Sections</h2>
</div><div style="white-space: normal;" class="markdown-body"><p>The 4 sections of an assembly program are</p>
<ul>
<li><a href="#text">.text</a></li>
<li><a href="#data">.data</a></li>
<li><a href="#bss">.bss</a></li>
<li><a href="#rodata">.rodata</a></li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><p>using linker scripts (google if you want to know more) more sections can be added. this is done in the gamelib for assignment 7</p>
</div><div style="white-space: normal;" class="markdown-body"><p>note that any part of assembly can be in any section. sections are <em>just</em> for optimalization. This means you can put data in text, and text in bss. the only 'restrictive' section is rodata because it can only store read only data.
<em>note</em>: <a href="#GDB">using GDB</a> works only if code is in .text</p>
</div><div style="white-space: normal;" class="markdown-body"><p>defining a section is easy. just put a  . plus the name of the section (like .bss or .text) and then everything after that in the file is part of that section. you can make multiple instances of the same section in different parts of your program (for example two .data sections) and the assembler (gcc) will make sure everything is combined into one.</p>
</div><div style="white-space: normal;" class="markdown-body"><h3 id="text">text</h3>
</div><div style="white-space: normal;" class="markdown-body"><p>in .text code is stored. you write your program in this section. make sure you do this for <a href="#GDB">GDB</a> to work.</p>
</div><div style="white-space: normal;" class="markdown-body"><h3 id="data">data</h3>
</div><div style="white-space: normal;" class="markdown-body"><p>in .data small variables (integers, text) is stored to be used in your program</p>
</div><div style="white-space: normal;" class="markdown-body"><h3 id="bss">bss</h3>
</div><div style="white-space: normal;" class="markdown-body"><p>in .bss data can also be stored. the difference is that bss data <em>must</em> be uninitialized. this is the case because all of the other sections will actually become a part of the executable file, while the bss section is only a 'promise' for the os. when the program runs the space is created in ram by the os. if you define large arrays of data this should be done in bss to keep the executable small</p>
</div><div style="white-space: normal;" class="markdown-body"><h3 id="rodata">rodata</h3>
</div><div style="white-space: normal;" class="markdown-body"><p>rodata should be used (and is optimized for) storing constant data. this section can <em>only</em> be read from.</p>
</div><div style="white-space: normal;" class="markdown-body"><h2 id="x86-calling-convention">X86 Calling Convention</h2>
<p>The calling convention (System V AMD64 ABI) that is used on *nix systems is as follows. <em>for <strong>64</strong> bit programs only</em>
The first six integer or pointer arguments passed in the registers in this order:</p>
<ol>
<li><code>RDI</code></li>
<li><code>RSI</code></li>
<li><code>RDX</code></li>
<li><code>RCX</code></li>
<li><code>R8</code></li>
<li><code>R9</code></li>
<li>(with sometimes <code>R10</code> as a static chain pointer in case of nested functions)</li>
<li>Additional arguments are to be passed on to the stack</li>
</ol>
</div><div style="white-space: normal;" class="markdown-body"><p>The return values are stored in <code>RAX</code> (In case of a 64 bit number) and in <code>RDX:RAX</code> (MSB:LSB) in case of 128 bit numbers.</p>
</div><div style="white-space: normal;" class="markdown-body"><p><a href="https://en.wikipedia.org/wiki/X86_calling_conventions#System_V_AMD64_ABI">Source (x86 Calling Conventions Wikipedia)</a></p>
</div><div style="white-space: normal;" class="markdown-body"><p>An illustration of how C functions are called in respect to the x86_64 SysV calling convention:
<img src="https://user-images.githubusercontent.com/10385659/45920669-305d3c80-bea8-11e8-932f-f198d48c4e2d.jpg" alt="args"></p>
</div><div style="white-space: normal;" class="markdown-body"><h2 id="gdb">GDB</h2>
</div><div style="white-space: normal;" class="markdown-body"><p>GDB is a debugger which can help find segfaults or find other mistakes in your program. to use it compile it using the <em>-g</em> option (put it directly after "gcc") and then instead of running it like ./&lt;programname&gt;, you run it as gdb ./&lt;programname&gt;. this should launch you into a gdb environment. in this environment you can use the following commands:</p>
</div><div style="white-space: normal;" class="markdown-body"><ul>
<li>b n (or breakpoint). this sets a breakpoint on line n</li>
<li>print code. this prints whatever you specify in code. this can be a full c expression, or a register name (e.g. $rdi or $rax)</li>
<li>x/nx p print n 32 bit words after p. p can be an adress or register. this is useful for reading whats on the stack (e.g. x/10x $rbp)</li>
<li>n (or next) steps ahead one instruction. when it finds a function call it will not step into instructions inside this function. useful to skip large functions like c stdlib function like printf</li>
<li>s (or step) steps ahead one instruction. this one does go into large functions</li>
<li>r (or run) runs the program until the next breakpoint or the end</li>
<li>c (or continue) after a breakpoint, continue restarts execution like run did until it encounters another breakpoint or the program ends. useful if a breakpoint is in a loop and you want to go to the next iteration</li>
<li>start starts the program, places a breakpoint on line one so you can imediately start using s and n</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><p>when using GDB your program <em>must</em> be compiled with -g and your code <em>must</em> be in a .text section</p>
</div><div style="white-space: normal;" class="markdown-body"><h2 id="command-line-arguments">command line arguments</h2>
</div><div style="white-space: normal;" class="markdown-body"><p>Getting command line arguments is easy in assembly. basically it works the same as in C. The main function/label is actually called with 2 arguments in rdi and rsi. rdi is the ammount of arguments, and rsi is a pointer to an array of strings which holds the arguments. you know where the array ends with argc/rdi.</p>
</div><div style="white-space: normal;" class="markdown-body"><h2 id="useful-links">Useful Links</h2>
<ul>
<li><a href="http://syscalls.kernelgrok.com/">reference of linux syscalls</a></li>
<li><a href="https://www3.nd.edu/~dthain/courses/cse40243/fall2015/intel-intro.html">quick assembly cheatsheet</a></li>
<li><a href="https://www.cs.uaf.edu/2005/fall/cs301/support/x86/index.html">quick assembly cheatsheet 2</a></li>
<li><a href="https://cs.brown.edu/courses/cs033/docs/guides/x64_cheatsheet.pdf">quick assembly cheatsheet 3</a></li>
</ul>
</div><p><br></p>