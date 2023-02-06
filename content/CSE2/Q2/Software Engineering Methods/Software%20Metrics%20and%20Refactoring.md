+++
title = "Software Metrics and Refactoring"
date = 2020-01-09
+++
<h2 id="bad-code-smells">Bad code smells</h2><ul><li><strong>High cohesion</strong> facilitates reuse (well-defined modules)</li><li><strong>Low coupling</strong> simplifies modification (all relevant code in one place)</li><li>Reducing coupling leads to higher cohesion and vice versa</li><li><strong>Action</strong>: split or combine modules</li></ul><p><br></p><p><strong>Code smells</strong> are not bugs, they are not technically incorrect and do not prevent the program from functioning.</p><p>However, they indicate weaknesses in design that may slow down development or increase the risk of bugs or failures in the future.</p><p><br></p><p>There are a few categories:</p><ul><li><strong>Blob code</strong>: methods and classes that are too large</li><li><strong>Object-oriented abusers</strong>: incomplete or incorrect application of object-oriented principles</li><li><strong>Change preventers</strong>: changes to some parts of the code require to make many changes in other parts too</li><li><strong>Dispensable: </strong>classes and methods that are pointless and not necessary</li><li><strong>Couplers: </strong>classes and methods with very high coupling</li></ul><p><br></p><h2 id="software-metrics">Software metrics</h2><p><strong>Measure:</strong> A measure provides a quantitative indication of the extent, amount, dimension, capacity, or size of some attribute of a product or process</p><p><strong>Metric</strong>: A quantitative measure of the degree to which a system, component, or process has a certain attribute</p><p><br></p><p>You can subdivide this into different kinds of metrics:</p><ul><li><strong>Process metrics</strong>: measures for analyzing the software development process (e.g. productivity)</li><li><strong>Project metrics</strong>: measure for analyzing the quality of the project (e.g. diff between expected and actual time estimates)</li><li><strong>Product metrics</strong>: measures for analyzing the quality of the product</li></ul><p><br></p><h2 id="refactoring">Refactoring</h2><p><strong>Refactoring</strong>: a change made to the internal structure of software to make it easier to understand and cheaper to modify without changing its observable behavior.</p><p><strong>Refactor</strong>: to restructure software by applying a series of refactoring operations without changing its observable behavior.</p><p><br></p><h1 id="examples">Examples</h1><h2 id="code-smell:-long-method">Code smell: long method</h2><p>Sometimes, a long method is hard to read and test. </p><p><br></p><p><strong>Code size</strong></p><p>We have a few metrics for measuring code size:</p><ul><li><strong>LOC</strong> (lines of code)</li><li><strong>eLOC</strong> (effective lines of code)</li></ul><p><br></p><p>These are easy to compute but depend on the programmer and language.</p><p><br></p><p><strong>Code complexity</strong></p><p>We can also use a code complexity measure, using the cyclomatic complexity; the number of independent linear paths in the source code. </p><p><br></p><p>This can determine the right number of tests required, but it harder to compute. There are a few ways to compute it:</p><ul><li><span class="ql-formula" data-value="C=\left|E\right|-\left|N\right|+2">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>C</mi><mo>=</mo><mrow><mo fence="true">∣</mo><mi>E</mi><mo fence="true">∣</mo></mrow><mo>−</mo><mrow><mo fence="true">∣</mo><mi>N</mi><mo fence="true">∣</mo></mrow><mo>+</mo><mn>2</mn></mrow><annotation encoding="application/x-tex">C=\left|E\right|-\left|N\right|+2</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.07153em;" class="mord mathdefault">C</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">∣</span><span style="margin-right: 0.05764em;" class="mord mathdefault">E</span><span class="mclose delimcenter" style="top: 0em;">∣</span></span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">∣</span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span class="mclose delimcenter" style="top: 0em;">∣</span></span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">2</span></span></span></span></span>﻿</span>, where <span class="ql-formula" data-value="E">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>E</mi></mrow><annotation encoding="application/x-tex">E</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.05764em;" class="mord mathdefault">E</span></span></span></span></span>﻿</span> is the number of edges of the graph, <span class="ql-formula" data-value="N">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>N</mi></mrow><annotation encoding="application/x-tex">N</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span></span></span></span></span>﻿</span> is the number of nodes on the graph and <span class="ql-formula" data-value="C">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>C</mi></mrow><annotation encoding="application/x-tex">C</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.07153em;" class="mord mathdefault">C</span></span></span></span></span>﻿</span> is the number of tests to be written</li><li><span class="ql-formula" data-value="C=\text{number of decision points}+1">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>C</mi><mo>=</mo><mtext>number&nbsp;of&nbsp;decision&nbsp;points</mtext><mo>+</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">C=\text{number of decision points}+1</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.07153em;" class="mord mathdefault">C</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.8888799999999999em; vertical-align: -0.19444em;"></span><span class="mord text"><span class="mord">number&nbsp;of&nbsp;decision&nbsp;points</span></span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">1</span></span></span></span></span>﻿</span> </li><li>If <span class="ql-formula" data-value="C>10">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>C</mi><mo>&amp;gt;</mo><mn>10</mn></mrow><annotation encoding="application/x-tex">C&amp;gt;10</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.72243em; vertical-align: -0.0391em;"></span><span style="margin-right: 0.07153em;" class="mord mathdefault">C</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">&gt;</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">1</span><span class="mord">0</span></span></span></span></span>﻿</span>, the method is too complex </li></ul><p><br></p><p><strong>Extract method</strong></p><p>General Mechanism:</p><ol><li>Create a new method, and name it after the intention of the method</li><li>Copy the extracted code from the source method into the new target method</li><li>Add parameters and temporary variables to the new methods</li><li>Replace the extracted code in the source method with a call to the target method.</li><li>Update (if needed) and run your tests</li></ol><p><br></p><h2 id="code-smell:-large-class">Code smell: large class</h2><p>A large class (or blob) implements too many functionalities (or too many responsibilities). It violates the single-responsibility principle.</p><p><br></p><p><strong>Measuring cohesion</strong></p><p>We have a few metrics for measuring cohesion:</p><ul><li><strong>LCOM</strong> (lack of cohesion of methods)</li><li><strong>CM</strong> (connectivity metric)</li></ul><p><br></p><p>They are different metrics to determine cohesion but are not easy to compute.</p><p><br></p><p><strong>LCOM</strong></p><div style="white-space: normal;" class="markdown-body"><p><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mtext>LCOM</mtext><mo>=</mo><mrow><mo fence="true">{</mo><mtable rowspacing="0.3599999999999999em" columnalign="left left" columnspacing="1em"><mtr><mtd><mstyle scriptlevel="0" displaystyle="false"><mrow><mi mathvariant="normal">∣</mi><mi>P</mi><mi mathvariant="normal">∣</mi><mo>−</mo><mi mathvariant="normal">∣</mi><mi>Q</mi><mi mathvariant="normal">∣</mi></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="false"><mrow><mtext>if&nbsp;</mtext><mi mathvariant="normal">∣</mi><mi>P</mi><mi mathvariant="normal">∣</mi><mo>&gt;</mo><mi mathvariant="normal">∣</mi><mi>Q</mi><mi mathvariant="normal">∣</mi></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="false"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="false"><mtext>otherwise</mtext></mstyle></mtd></mtr></mtable></mrow></mrow><annotation encoding="application/x-tex">\text{LCOM}=\begin{cases}
|P|-|Q| &amp;\text{if }|P|\gt|Q| \\
0 &amp;\text{otherwise}
\end{cases}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord text"><span class="mord">LCOM</span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:3.0000299999999998em;vertical-align:-1.25003em;"></span><span class="minner"><span class="mopen delimcenter" style="top:0em;"><span class="delimsizing size4">{</span></span><span class="mord"><span class="mtable"><span class="col-align-l"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.69em;"><span style="top:-3.69em;"><span class="pstrut" style="height:3.008em;"></span><span class="mord"><span class="mord">∣</span><span class="mord mathdefault" style="margin-right:0.13889em;">P</span><span class="mord">∣</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mord">∣</span><span class="mord mathdefault">Q</span><span class="mord">∣</span></span></span><span style="top:-2.25em;"><span class="pstrut" style="height:3.008em;"></span><span class="mord"><span class="mord">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:1.19em;"><span></span></span></span></span></span><span class="arraycolsep" style="width:1em;"></span><span class="col-align-l"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.69em;"><span style="top:-3.69em;"><span class="pstrut" style="height:3.008em;"></span><span class="mord"><span class="mord text"><span class="mord">if&nbsp;</span></span><span class="mord">∣</span><span class="mord mathdefault" style="margin-right:0.13889em;">P</span><span class="mord">∣</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">&gt;</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mord">∣</span><span class="mord mathdefault">Q</span><span class="mord">∣</span></span></span><span style="top:-2.25em;"><span class="pstrut" style="height:3.008em;"></span><span class="mord"><span class="mord text"><span class="mord">otherwise</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:1.19em;"><span></span></span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span></p>
</div><p>where</p><div style="white-space: normal;" class="markdown-body"><p><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mo>=</mo><mo stretchy="false">{</mo><mo stretchy="false">(</mo><msub><mi>m</mi><mi>i</mi></msub><mo separator="true">,</mo><msub><mi>m</mi><mi>j</mi></msub><mo stretchy="false">)</mo><mi mathvariant="normal">∣</mi><msub><mi>A</mi><mi>i</mi></msub><mo>∩</mo><msub><mi>A</mi><mi>j</mi></msub><mo>=</mo><mi mathvariant="normal">∅</mi><mo stretchy="false">}</mo></mrow><annotation encoding="application/x-tex">P=\{(m_i, m_j) \vert A_i \cap A_j = \emptyset \}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathdefault" style="margin-right:0.13889em;">P</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:1.036108em;vertical-align:-0.286108em;"></span><span class="mopen">{</span><span class="mopen">(</span><span class="mord"><span class="mord mathdefault">m</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord"><span class="mord mathdefault">m</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.311664em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight" style="margin-right:0.05724em;">j</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"><span></span></span></span></span></span></span><span class="mclose">)</span><span class="mord">∣</span><span class="mord"><span class="mord mathdefault">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">∩</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:0.969438em;vertical-align:-0.286108em;"></span><span class="mord"><span class="mord mathdefault">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.311664em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight" style="margin-right:0.05724em;">j</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord">∅</span><span class="mclose">}</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>Q</mi><mo>=</mo><mo stretchy="false">{</mo><mo stretchy="false">(</mo><msub><mi>m</mi><mi>i</mi></msub><mo separator="true">,</mo><msub><mi>m</mi><mi>j</mi></msub><mo stretchy="false">)</mo><mi mathvariant="normal">∣</mi><msub><mi>A</mi><mi>i</mi></msub><mo>∩</mo><msub><mi>A</mi><mi>j</mi></msub><mo mathvariant="normal">≠</mo><mi mathvariant="normal">∅</mi><mo stretchy="false">}</mo></mrow><annotation encoding="application/x-tex">Q=\{(m_i, m_j) \vert A_i \cap A_j \ne \emptyset \}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="mord mathdefault">Q</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:1.036108em;vertical-align:-0.286108em;"></span><span class="mopen">{</span><span class="mopen">(</span><span class="mord"><span class="mord mathdefault">m</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord"><span class="mord mathdefault">m</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.311664em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight" style="margin-right:0.05724em;">j</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"><span></span></span></span></span></span></span><span class="mclose">)</span><span class="mord">∣</span><span class="mord"><span class="mord mathdefault">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">∩</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:0.980548em;vertical-align:-0.286108em;"></span><span class="mord"><span class="mord mathdefault">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.311664em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight" style="margin-right:0.05724em;">j</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel"><span class="mrel"><span class="mord"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.69444em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="rlap"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="inner"><span class="mrel"></span></span><span class="fix"></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.19444em;"><span></span></span></span></span></span></span><span class="mrel">=</span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord">∅</span><span class="mclose">}</span></span></span></span>. Or: method pairs that do (not) share any attribute.</p>
</div><p><br></p><p>The LCOM should be as low as possible.</p><p><br></p><p><strong>CM</strong></p><p>We define the connectivity metric as the method pairs sharing attributes or having method calls among them divided by the method pairs in the class. If this number is high, we have high cohesion.</p><p><br></p><p><strong>Extract class</strong></p><p>General Mechanism:</p><ol><li>Decide how to split the responsibilities of the class</li><li>Create a new class to express the split-off responsibilities</li><li>Make a link from the old to the new class</li><li>Use Move Method refactoring to move methods over from old to new</li><li>Update and run your tests</li></ol><p><br></p><h2 id="code-smell:-long-parameter-list">Code smell: long parameter list</h2><p>A long parameter of a method has too many input parameters. In general, more than 4 parameters is too much. We use numbers of parameters as metric.</p><p><br></p><p><strong>Parameter objects</strong></p><p>General Mechanism:</p><ol><li>Create a new class to represent the group of parameters you are replacing. Make the class immutable</li><li>Add the parameters for the new data clump</li><li>For each parameter in the data clump, remove the parameter from the signature. Modify the callers and method body to use the parameter object for that value</li><li>Update and run your tests</li></ol><p><br></p><h2 id="code-smell:-couplers">Code smell: couplers</h2><p>A <strong>feature envy</strong> is a method that is more interested in other classes rather than the one it actually is in (i.e., a method that is highly coupled with other classes).</p><p><br></p><p><strong>Measuring coupling</strong></p><p>We have a few metrics for measuring coupling:</p><ul><li><strong>CBO</strong> (coupling between objects)</li><li><strong>MPC</strong> (message passing coupling)</li><li><strong>CAM</strong> (cohesion among method of class)</li></ul><p><br></p><p>They might be used to evaluate how much a maintenance operation might impact on other classes</p><p><br></p><p><strong>CBO</strong></p><p>CBO is defined as the number of dependencies with other classes. This can be through parameters or attributes modified/read, method calls, object instantiation etc.</p><p><br></p><p><strong>MPC</strong></p><p>MPC is defined as the number of messages (method calls) exchanged by two classes</p><p><br></p><p><strong>CAM</strong></p><p>CAM is defined as <span class="ql-formula" data-value="\frac{A}{K\cdot L}">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mfrac><mi>A</mi><mrow><mi>K</mi><mo>⋅</mo><mi>L</mi></mrow></mfrac></mrow><annotation encoding="application/x-tex">\frac{A}{K\cdot L}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1.217331em; vertical-align: -0.345em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.872331em;"><span class="" style="top: -2.6550000000000002em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span style="margin-right: 0.07153em;" class="mord mathdefault mtight">K</span><span class="mbin mtight">⋅</span><span class="mord mathdefault mtight">L</span></span></span></span><span class="" style="top: -3.23em;"><span class="pstrut" style="height: 3em;"></span><span class="frac-line" style="border-bottom-width: 0.04em;"></span></span><span class="" style="top: -3.394em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">A</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.345em;"><span class=""></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span></span>﻿</span> where:</p><ul><li><span class="ql-formula" data-value="A">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathdefault">A</span></span></span></span></span>﻿</span> is the number of distinct parameter types accross all methods in a class</li><li><span class="ql-formula" data-value="L">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>L</mi></mrow><annotation encoding="application/x-tex">L</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathdefault">L</span></span></span></span></span>﻿</span> is the number of distinct parameter types</li><li><span class="ql-formula" data-value="K">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>K</mi></mrow><annotation encoding="application/x-tex">K</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.07153em;" class="mord mathdefault">K</span></span></span></span></span>﻿</span> is the number of methods</li></ul><p><br></p><h2 id="code-smell:-coupled-classes">Code smell: coupled classes</h2><p>Coupled classes (also called inappropriate intimacy) occurs when one class <span class="ql-formula" data-value="A">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathdefault">A</span></span></span></span></span>﻿</span> uses the internal fields and methods of another class <span class="ql-formula" data-value="B">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>B</mi></mrow><annotation encoding="application/x-tex">B</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span></span></span></span></span>﻿</span> and vice-versa</p><p><br></p><p><strong>Measuring coupling between classes</strong></p><p>We have a few metrics for measuring coupling between classes:</p><ul><li><strong>CBO</strong> (coupling between objects)</li><li><strong>DIT</strong> (depth of inheritance tree, the maximum length from root to leaf of inheritance tree)</li><li><strong>NOC</strong> (number of children, the number of direct subclasses)</li></ul><p><br></p><p><strong>Replace delegation with inheritance</strong></p><p>Use this refactoring when you are using delegation and are</p><p>often writing many simple delegations for the entire interface</p><p><br></p><p>General Mechanism:</p><ol><li>Make the delegating object a subclass of the delegate</li><li>Set the delegate field to be the object itself</li><li>Replace all other delegations with calls to the object itself</li><li>Remove the delegate field</li><li>Update and run your tests</li></ol><p><br></p><h2 id="code-smell:-oo-abusers">Code smell: OO abusers</h2><p>If a switch statement is used in a factory to determine which method to call, you are dealing with a code smell. For this you can use polymorphism.</p><p><br></p><p><strong>Replace conditional with polymorphism</strong></p><p>Apply this refactoring when you have conditional statements that choose different behaviors depending on the type of an object.</p><p><br></p><p>General Mechanism:</p><ol><li>If the conditional statement is one part of a larger method, take apart the conditional statement and use Extract Method</li><li>If necessary use Move Method to place the conditional at the top of the inheritance structure</li><li>Create a subclass method that overrides the conditional statement method</li><li>Remove the (copied) conditional code</li><li>Update and run the tests</li></ol>