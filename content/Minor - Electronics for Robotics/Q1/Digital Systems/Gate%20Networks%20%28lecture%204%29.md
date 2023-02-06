+++
title = "Gate Networks (lecture 4)"
date = 2020-09-16
+++
<h1 id="gate-networks">Gate networks</h1><p>A gate network is a network of logical (combinational) gates. The inputs and outputs are digital values (<span class="ql-formula" data-value="0">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>0</mn></mrow><annotation encoding="application/x-tex">0</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">0</span></span></span></span></span>﻿</span> or <span class="ql-formula" data-value="1">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>1</mn></mrow><annotation encoding="application/x-tex">1</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">1</span></span></span></span></span>﻿</span>). In the end, the connections between the gates determine the functionality of the overall network.</p><p><br></p><h2 id="rules">Rules</h2><p>There are some rules associated with <strong>combinational </strong>gate networks:</p><ul><li>You cannot connect multiple outputs to one input<strong>, </strong>because there's a potential for short circuits</li><li>If the load exceeds the fanout factor of a specific output, this is considered bad as propagation delays will be too long, and not acceptable</li><li>Combinational networks are always loop-free as it must be possible to determine for each (set of) input(s) the corresponding outputs.</li></ul><p><br></p><p><img src="https://i.imgur.com/k5eAnTE.png" width="337"></p><p>Note that (d) has a loop, as this is a sequential network (which can be used for memory).</p><h2 id=""><br></h2><h2 id="universal-set-of-gates">Universal set of gates</h2><p>A set of gates that can represent any combinational circuit:</p><ul><li><span class="ql-formula" data-value="\left\{AND,\ OR,\ NOT\right\}">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo fence="true">{</mo><mi>A</mi><mi>N</mi><mi>D</mi><mo separator="true">,</mo><mtext>&nbsp;</mtext><mi>O</mi><mi>R</mi><mo separator="true">,</mo><mtext>&nbsp;</mtext><mi>N</mi><mi>O</mi><mi>T</mi><mo fence="true">}</mo></mrow><annotation encoding="application/x-tex">\left\{AND,\ OR,\ NOT\right\}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">{</span><span class="mord mathdefault">A</span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span style="margin-right: 0.02778em;" class="mord mathdefault">D</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mspace">&nbsp;</span><span style="margin-right: 0.02778em;" class="mord mathdefault">O</span><span style="margin-right: 0.00773em;" class="mord mathdefault">R</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mspace">&nbsp;</span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span style="margin-right: 0.02778em;" class="mord mathdefault">O</span><span style="margin-right: 0.13889em;" class="mord mathdefault">T</span><span class="mclose delimcenter" style="top: 0em;">}</span></span></span></span></span></span>﻿</span> </li><li><span class="ql-formula" data-value="\left\{AND,\ NOT\right\}">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo fence="true">{</mo><mi>A</mi><mi>N</mi><mi>D</mi><mo separator="true">,</mo><mtext>&nbsp;</mtext><mi>N</mi><mi>O</mi><mi>T</mi><mo fence="true">}</mo></mrow><annotation encoding="application/x-tex">\left\{AND,\ NOT\right\}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">{</span><span class="mord mathdefault">A</span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span style="margin-right: 0.02778em;" class="mord mathdefault">D</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mspace">&nbsp;</span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span style="margin-right: 0.02778em;" class="mord mathdefault">O</span><span style="margin-right: 0.13889em;" class="mord mathdefault">T</span><span class="mclose delimcenter" style="top: 0em;">}</span></span></span></span></span></span>﻿</span> - you can implement OR using AND and NOT. Can be done using DeMorgan's rules: <span class="ql-formula" data-value="\left(A\cup B\right)^c=A^c\cap B^c">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mrow><mo fence="true">(</mo><mi>A</mi><mo>∪</mo><mi>B</mi><mo fence="true">)</mo></mrow><mi>c</mi></msup><mo>=</mo><msup><mi>A</mi><mi>c</mi></msup><mo>∩</mo><msup><mi>B</mi><mi>c</mi></msup></mrow><annotation encoding="application/x-tex">\left(A\cup B\right)^c=A^c\cap B^c</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1.054292em; vertical-align: -0.25em;"></span><span class="minner"><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">∪</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span><span class="mclose delimcenter" style="top: 0em;">)</span></span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.804292em;"><span class="" style="top: -3.2029em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">c</span></span></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord"><span class="mord mathdefault">A</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.664392em;"><span class="" style="top: -3.063em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">c</span></span></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">∩</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord"><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.664392em;"><span class="" style="top: -3.063em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">c</span></span></span></span></span></span></span></span></span></span></span></span>﻿</span></li><li><span class="ql-formula" data-value="\left\{OR,\ NOT\right\}">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo fence="true">{</mo><mi>O</mi><mi>R</mi><mo separator="true">,</mo><mtext>&nbsp;</mtext><mi>N</mi><mi>O</mi><mi>T</mi><mo fence="true">}</mo></mrow><annotation encoding="application/x-tex">\left\{OR,\ NOT\right\}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">{</span><span style="margin-right: 0.02778em;" class="mord mathdefault">O</span><span style="margin-right: 0.00773em;" class="mord mathdefault">R</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mspace">&nbsp;</span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span style="margin-right: 0.02778em;" class="mord mathdefault">O</span><span style="margin-right: 0.13889em;" class="mord mathdefault">T</span><span class="mclose delimcenter" style="top: 0em;">}</span></span></span></span></span></span>﻿</span> - same as with previous: <span class="ql-formula" data-value="\left(A\cap B\right)^c=A^c\cup B^c">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mrow><mo fence="true">(</mo><mi>A</mi><mo>∩</mo><mi>B</mi><mo fence="true">)</mo></mrow><mi>c</mi></msup><mo>=</mo><msup><mi>A</mi><mi>c</mi></msup><mo>∪</mo><msup><mi>B</mi><mi>c</mi></msup></mrow><annotation encoding="application/x-tex">\left(A\cap B\right)^c=A^c\cup B^c</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1.054292em; vertical-align: -0.25em;"></span><span class="minner"><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">∩</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span><span class="mclose delimcenter" style="top: 0em;">)</span></span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.804292em;"><span class="" style="top: -3.2029em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">c</span></span></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord"><span class="mord mathdefault">A</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.664392em;"><span class="" style="top: -3.063em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">c</span></span></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">∪</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord"><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.664392em;"><span class="" style="top: -3.063em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">c</span></span></span></span></span></span></span></span></span></span></span></span>﻿</span></li><li><span class="ql-formula" data-value="\left\{NAND\right\}">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo fence="true">{</mo><mi>N</mi><mi>A</mi><mi>N</mi><mi>D</mi><mo fence="true">}</mo></mrow><annotation encoding="application/x-tex">\left\{NAND\right\}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">{</span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span class="mord mathdefault">A</span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span style="margin-right: 0.02778em;" class="mord mathdefault">D</span><span class="mclose delimcenter" style="top: 0em;">}</span></span></span></span></span></span>﻿</span> - <span class="ql-formula" data-value="NOT\left(x\right)=NAND\left(xx\right)">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>N</mi><mi>O</mi><mi>T</mi><mrow><mo fence="true">(</mo><mi>x</mi><mo fence="true">)</mo></mrow><mo>=</mo><mi>N</mi><mi>A</mi><mi>N</mi><mi>D</mi><mrow><mo fence="true">(</mo><mi>x</mi><mi>x</mi><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">NOT\left(x\right)=NAND\left(xx\right)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span style="margin-right: 0.02778em;" class="mord mathdefault">O</span><span style="margin-right: 0.13889em;" class="mord mathdefault">T</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord mathdefault">x</span><span class="mclose delimcenter" style="top: 0em;">)</span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span class="mord mathdefault">A</span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span style="margin-right: 0.02778em;" class="mord mathdefault">D</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord mathdefault">x</span><span class="mord mathdefault">x</span><span class="mclose delimcenter" style="top: 0em;">)</span></span></span></span></span></span>﻿</span> &amp; <span class="ql-formula" data-value="AND\left(x_1,x_0\right)=NAND\left(NAND\left(x_1,x_0\right),\ NAND\left(x_1,x_0\right)\right)">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi><mi>N</mi><mi>D</mi><mrow><mo fence="true">(</mo><msub><mi>x</mi><mn>1</mn></msub><mo separator="true">,</mo><msub><mi>x</mi><mn>0</mn></msub><mo fence="true">)</mo></mrow><mo>=</mo><mi>N</mi><mi>A</mi><mi>N</mi><mi>D</mi><mrow><mo fence="true">(</mo><mi>N</mi><mi>A</mi><mi>N</mi><mi>D</mi><mrow><mo fence="true">(</mo><msub><mi>x</mi><mn>1</mn></msub><mo separator="true">,</mo><msub><mi>x</mi><mn>0</mn></msub><mo fence="true">)</mo></mrow><mo separator="true">,</mo><mtext>&nbsp;</mtext><mi>N</mi><mi>A</mi><mi>N</mi><mi>D</mi><mrow><mo fence="true">(</mo><msub><mi>x</mi><mn>1</mn></msub><mo separator="true">,</mo><msub><mi>x</mi><mn>0</mn></msub><mo fence="true">)</mo></mrow><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">AND\left(x_1,x_0\right)=NAND\left(NAND\left(x_1,x_0\right),\ NAND\left(x_1,x_0\right)\right)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathdefault">A</span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span style="margin-right: 0.02778em;" class="mord mathdefault">D</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord"><span class="mord mathdefault">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.30110799999999993em;"><span class="" style="top: -2.5500000000000003em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mord"><span class="mord mathdefault">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.30110799999999993em;"><span class="" style="top: -2.5500000000000003em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span><span class="mclose delimcenter" style="top: 0em;">)</span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span class="mord mathdefault">A</span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span style="margin-right: 0.02778em;" class="mord mathdefault">D</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span class="mord mathdefault">A</span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span style="margin-right: 0.02778em;" class="mord mathdefault">D</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord"><span class="mord mathdefault">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.30110799999999993em;"><span class="" style="top: -2.5500000000000003em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mord"><span class="mord mathdefault">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.30110799999999993em;"><span class="" style="top: -2.5500000000000003em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span><span class="mclose delimcenter" style="top: 0em;">)</span></span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mspace">&nbsp;</span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span class="mord mathdefault">A</span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span style="margin-right: 0.02778em;" class="mord mathdefault">D</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord"><span class="mord mathdefault">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.30110799999999993em;"><span class="" style="top: -2.5500000000000003em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mord"><span class="mord mathdefault">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.30110799999999993em;"><span class="" style="top: -2.5500000000000003em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span><span class="mclose delimcenter" style="top: 0em;">)</span></span><span class="mclose delimcenter" style="top: 0em;">)</span></span></span></span></span></span>﻿</span></li><li><span class="ql-formula" data-value="\left\{NOR\right\}">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo fence="true">{</mo><mi>N</mi><mi>O</mi><mi>R</mi><mo fence="true">}</mo></mrow><annotation encoding="application/x-tex">\left\{NOR\right\}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">{</span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span style="margin-right: 0.02778em;" class="mord mathdefault">O</span><span style="margin-right: 0.00773em;" class="mord mathdefault">R</span><span class="mclose delimcenter" style="top: 0em;">}</span></span></span></span></span></span>﻿</span></li></ul><p><br></p><h2 id="analysis-of-gate-networks">Analysis of gate networks</h2><p>There are two main ways which we use to analyse gate networks, <strong>functional analysis</strong> and <strong>network characteristics.</strong></p><p><br></p><h3 id="functional-analysis"><strong>Functional analysis</strong></h3><ol><li>Obtain I/O switching expressions (also see examples)</li><li class="ql-indent-1">Assign names to each connection in the network</li><li class="ql-indent-1">Write switching expressions for each gate output</li><li class="ql-indent-1">Back-substitute all internal names to obtain external outputs in terms of external inputs. We can apply DeMorgan’s law on the circuit before creating the expression, to save time</li><li>Obtain a tabular expression from these switching functions. This can be useful to give hints as to what encoding was chosen on the input / output sets.</li><li>Define high-level input and output variables, and use codes to relate these</li><li>Obtain a high-level specification</li></ol><p><br></p><h3 id="network-characteristics"><strong>Network characteristics</strong></h3><ul><li><strong>Input load factors</strong> of the network input: how much load the input is exerting to the preceding output that it is connected to. This is a sum of the load factors of all the inputs.</li><li><strong>Fan-out factors</strong> of the network outputs: how much load (related to input load) can the output drive? Note that this is different than fan-out, which is the amount of gates that an output is connected to.</li><li><strong>Propagation delays</strong> through the network</li><li><strong>Level of gate:</strong> number of gates in longest path from input to output </li><li><strong>Size of the network</strong>: area on chip. This is the sum of the "equivalent gates" size that can be found in the characteristics table.</li></ul><p><br></p><h3 id="switching-expressions-with-not,-nand-and-nor">Switching expressions with NOT, NAND and NOR</h3><p>Having these gates in your network, makes the procedure quite a bit harder. Given the following network (figure 4.31) of which we want to derive the logical expression:</p><p><img src="https://i.imgur.com/ICrKEs2.png" width="548"></p><p>We want to remove the inversion operator. Using DeMorgan's law, we know that a NAND gate is an OR gate with the inputs inverted.</p><p><br></p><p>If we then substitute the NAND gates for this type of gate, the network becomes much easier to reason about (the same goes for the NOR). This yields double negations, which can then also be removed:</p><p><img src="https://i.imgur.com/tRPTUCX.png" width="527"></p><p><br></p><h2 id="propagation-delay">Propagation delay</h2><p>Worst case delay for an output to react <strong>after</strong> a change at the input. Note that we only talk about propagation delay if the output changes.</p><p><br></p><p><span class="ql-formula" data-value="tp_{LH}">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>t</mi><msub><mi>p</mi><mrow><mi>L</mi><mi>H</mi></mrow></msub></mrow><annotation encoding="application/x-tex">tp_{LH}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.80952em; vertical-align: -0.19444em;"></span><span class="mord mathdefault">t</span><span class="mord"><span class="mord mathdefault">p</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.32833099999999993em;"><span class="" style="top: -2.5500000000000003em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">L</span><span style="margin-right: 0.08125em;" class="mord mathdefault mtight">H</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span></span></span></span></span>﻿</span>: delay for changes from low to high (due to input change)</p><p><span class="ql-formula" data-value="tp_{HL}">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>t</mi><msub><mi>p</mi><mrow><mi>H</mi><mi>L</mi></mrow></msub></mrow><annotation encoding="application/x-tex">tp_{HL}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.80952em; vertical-align: -0.19444em;"></span><span class="mord mathdefault">t</span><span class="mord"><span class="mord mathdefault">p</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.32833099999999993em;"><span class="" style="top: -2.5500000000000003em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span style="margin-right: 0.08125em;" class="mord mathdefault mtight">H</span><span class="mord mathdefault mtight">L</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span></span></span></span></span>﻿</span>: delay for changes from high to low (due to input change)</p><p><br></p><p><span class="ql-formula" data-value="tp_{LH}\left(A,z\right)">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>t</mi><msub><mi>p</mi><mrow><mi>L</mi><mi>H</mi></mrow></msub><mrow><mo fence="true">(</mo><mi>A</mi><mo separator="true">,</mo><mi>z</mi><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">tp_{LH}\left(A,z\right)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathdefault">t</span><span class="mord"><span class="mord mathdefault">p</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.32833099999999993em;"><span class="" style="top: -2.5500000000000003em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">L</span><span style="margin-right: 0.08125em;" class="mord mathdefault mtight">H</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord mathdefault">A</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span style="margin-right: 0.04398em;" class="mord mathdefault">z</span><span class="mclose delimcenter" style="top: 0em;">)</span></span></span></span></span></span>﻿</span>: the propagation delay between input <span class="ql-formula" data-value="A">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathdefault">A</span></span></span></span></span>﻿</span> and output <span class="ql-formula" data-value="z">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>z</mi></mrow><annotation encoding="application/x-tex">z</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span style="margin-right: 0.04398em;" class="mord mathdefault">z</span></span></span></span></span>﻿</span>, for a low to high transition.</p><p><span class="ql-formula" data-value="tp_{HL}\left(A,z\right)">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>t</mi><msub><mi>p</mi><mrow><mi>H</mi><mi>L</mi></mrow></msub><mrow><mo fence="true">(</mo><mi>A</mi><mo separator="true">,</mo><mi>z</mi><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">tp_{HL}\left(A,z\right)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathdefault">t</span><span class="mord"><span class="mord mathdefault">p</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.32833099999999993em;"><span class="" style="top: -2.5500000000000003em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span style="margin-right: 0.08125em;" class="mord mathdefault mtight">H</span><span class="mord mathdefault mtight">L</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord mathdefault">A</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span style="margin-right: 0.04398em;" class="mord mathdefault">z</span><span class="mclose delimcenter" style="top: 0em;">)</span></span></span></span></span></span>﻿</span>: the propagation delay between input <span class="ql-formula" data-value="A">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathdefault">A</span></span></span></span></span>﻿</span> and output <span class="ql-formula" data-value="z">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>z</mi></mrow><annotation encoding="application/x-tex">z</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span style="margin-right: 0.04398em;" class="mord mathdefault">z</span></span></span></span></span>﻿</span>, for a high to low transition.</p><p><br></p><p>We can look up these times in our characteristics table, with <span class="ql-formula" data-value="L">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>L</mi></mrow><annotation encoding="application/x-tex">L</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathdefault">L</span></span></span></span></span>﻿</span> being the load of the output of the gate.</p><p><br></p><p>From the change of output you can infer the change of input.  If both options of change of input are possible, calculate both and choose the maximum. If there are multiple paths, calculate both.</p><p><br></p><p><br></p>