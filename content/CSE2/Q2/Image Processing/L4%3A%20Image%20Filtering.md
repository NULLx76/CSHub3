+++
title = "L4: Image Filtering"
date = 2021-01-24
+++
<p>*what are 2D signals*</p><p><br></p><ul><li><strong>Frequency </strong>- how big the change in values is between two pixels</li><li class="ql-indent-1">EG, black to white (1 to 0) is a high frequency</li></ul><p><br></p><h1 id="convolution">Convolution</h1><p><br></p><ul><li><strong>Cross-correlation </strong>- place kernel filter once over each pixel &lt;FINISH&gt;</li></ul><p><br></p><ul><li><strong>Convolution</strong> - flip filter in both dimensions then place once over each pixel in the signal (cross-correlation)</li><li class="ql-indent-1">Notation: <span class="ql-formula" data-value="G=H*F">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi><mo>=</mo><mi>H</mi><mo>∗</mo><mi>F</mi></mrow><annotation encoding="application/x-tex">G=H*F</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathdefault">G</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.08125em;" class="mord mathdefault">H</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">∗</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.13889em;" class="mord mathdefault">F</span></span></span></span></span>﻿</span> </li><li class="ql-indent-1">Assume the origin of the kernel is the middle pixel</li></ul><p><br></p><p>				<span class="ql-formula" data-value="G[i,j]=\sum_{u=-k}^k\sum_{v=-k}^kH[u,v]F[i-u,j-v]">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi><mo>[</mo><mi>i</mi><mo separator="true">,</mo><mi>j</mi><mo>]</mo><mo>=</mo><msubsup><mo>∑</mo><mrow><mi>u</mi><mo>=</mo><mo>−</mo><mi>k</mi></mrow><mi>k</mi></msubsup><msubsup><mo>∑</mo><mrow><mi>v</mi><mo>=</mo><mo>−</mo><mi>k</mi></mrow><mi>k</mi></msubsup><mi>H</mi><mo>[</mo><mi>u</mi><mo separator="true">,</mo><mi>v</mi><mo>]</mo><mi>F</mi><mo>[</mo><mi>i</mi><mo>−</mo><mi>u</mi><mo separator="true">,</mo><mi>j</mi><mo>−</mo><mi>v</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">G[i,j]=\sum_{u=-k}^k\sum_{v=-k}^kH[u,v]F[i-u,j-v]</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathdefault">G</span><span class="mopen">[</span><span class="mord mathdefault">i</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span style="margin-right: 0.05724em;" class="mord mathdefault">j</span><span class="mclose">]</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 1.347049em; vertical-align: -0.35804100000000005em;"></span><span class="mop"><span class="mop op-symbol small-op" style="position: relative; top: -0.0000050000000000050004em;">∑</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.9890079999999999em;"><span class="" style="top: -2.40029em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">u</span><span class="mrel mtight">=</span><span class="mord mtight">−</span><span style="margin-right: 0.03148em;" class="mord mathdefault mtight">k</span></span></span></span><span class="" style="top: -3.2029em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span style="margin-right: 0.03148em;" class="mord mathdefault mtight">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.35804100000000005em;"><span class=""></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mop"><span class="mop op-symbol small-op" style="position: relative; top: -0.0000050000000000050004em;">∑</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.9890079999999999em;"><span class="" style="top: -2.40029em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span style="margin-right: 0.03588em;" class="mord mathdefault mtight">v</span><span class="mrel mtight">=</span><span class="mord mtight">−</span><span style="margin-right: 0.03148em;" class="mord mathdefault mtight">k</span></span></span></span><span class="" style="top: -3.2029em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span style="margin-right: 0.03148em;" class="mord mathdefault mtight">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.35804100000000005em;"><span class=""></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span style="margin-right: 0.08125em;" class="mord mathdefault">H</span><span class="mopen">[</span><span class="mord mathdefault">u</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span style="margin-right: 0.03588em;" class="mord mathdefault">v</span><span class="mclose">]</span><span style="margin-right: 0.13889em;" class="mord mathdefault">F</span><span class="mopen">[</span><span class="mord mathdefault">i</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 0.85396em; vertical-align: -0.19444em;"></span><span class="mord mathdefault">u</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span style="margin-right: 0.05724em;" class="mord mathdefault">j</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span style="margin-right: 0.03588em;" class="mord mathdefault">v</span><span class="mclose">]</span></span></span></span></span>﻿</span> </p><p><br></p><p><br></p><p>&lt; insert picture from slides of convolving &gt;</p><p><br></p><h2 id="averaging-filter">Averaging Filter</h2><p><br></p><ul><li><strong>Averaging filter</strong> - replace each pixel with the average of all values in its neighbourhood</li><li class="ql-indent-1">Aka box filter</li></ul><p><br></p><p>&lt;insert picture&gt;</p><p><br></p><h2 id="properties-of-convolution">Properties of convolution</h2><p><br></p><ul><li><strong>Linear and shift-invariant</strong></li><li><strong>Commutative </strong>- <span class="ql-formula" data-value="f*g=g*f">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>∗</mo><mi>g</mi><mo>=</mo><mi>g</mi><mo>∗</mo><mi>f</mi></mrow><annotation encoding="application/x-tex">f*g=g*f</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.8888799999999999em; vertical-align: -0.19444em;"></span><span style="margin-right: 0.10764em;" class="mord mathdefault">f</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">∗</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 0.625em; vertical-align: -0.19444em;"></span><span style="margin-right: 0.03588em;" class="mord mathdefault">g</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.6597200000000001em; vertical-align: -0.19444em;"></span><span style="margin-right: 0.03588em;" class="mord mathdefault">g</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">∗</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 0.8888799999999999em; vertical-align: -0.19444em;"></span><span style="margin-right: 0.10764em;" class="mord mathdefault">f</span></span></span></span></span>﻿</span> </li><li><strong>Associative </strong>- <span class="ql-formula" data-value="(f*g)*h=f*(g*h)">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>f</mi><mo>∗</mo><mi>g</mi><mo>)</mo><mo>∗</mo><mi>h</mi><mo>=</mo><mi>f</mi><mo>∗</mo><mo>(</mo><mi>g</mi><mo>∗</mo><mi>h</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">(f*g)*h=f*(g*h)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mopen">(</span><span style="margin-right: 0.10764em;" class="mord mathdefault">f</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">∗</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span style="margin-right: 0.03588em;" class="mord mathdefault">g</span><span class="mclose">)</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">∗</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 0.69444em; vertical-align: 0em;"></span><span class="mord mathdefault">h</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.8888799999999999em; vertical-align: -0.19444em;"></span><span style="margin-right: 0.10764em;" class="mord mathdefault">f</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">∗</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mopen">(</span><span style="margin-right: 0.03588em;" class="mord mathdefault">g</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">∗</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathdefault">h</span><span class="mclose">)</span></span></span></span></span>﻿</span> </li><li><strong>Identity </strong>- for unit impulse <span class="ql-formula" data-value="e">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>e</mi></mrow><annotation encoding="application/x-tex">e</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord mathdefault">e</span></span></span></span></span>﻿</span>, <span class="ql-formula" data-value="f*e=f">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>∗</mo><mi>e</mi><mo>=</mo><mi>f</mi></mrow><annotation encoding="application/x-tex">f*e=f</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.8888799999999999em; vertical-align: -0.19444em;"></span><span style="margin-right: 0.10764em;" class="mord mathdefault">f</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">∗</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord mathdefault">e</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.8888799999999999em; vertical-align: -0.19444em;"></span><span style="margin-right: 0.10764em;" class="mord mathdefault">f</span></span></span></span></span>﻿</span> </li><li class="ql-indent-1"><span class="ql-formula" data-value="e=\begin{bmatrix}0&amp;0&amp;0\\0&amp;1&amp;0\\0&amp;0&amp;0\end{bmatrix}">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>e</mi><mo>=</mo><mrow><mo fence="true">[</mo><mtable><mtr><mtd><mstyle scriptlevel="0" displaystyle="false"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="false"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="false"><mn>0</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="false"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="false"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="false"><mn>0</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="false"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="false"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="false"><mn>0</mn></mstyle></mtd></mtr></mtable><mo fence="true">]</mo></mrow></mrow><annotation encoding="application/x-tex">e=\begin{bmatrix}0&amp;amp;0&amp;amp;0\\0&amp;amp;1&amp;amp;0\\0&amp;amp;0&amp;amp;0\end{bmatrix}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord mathdefault">e</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 3.60004em; vertical-align: -1.55002em;"></span><span class="minner"><span class="mopen"><span class="delimsizing mult"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 2.05002em;"><span class="" style="top: -2.2500000000000004em;"><span class="pstrut" style="height: 3.1550000000000002em;"></span><span class="delimsizinginner delim-size4"><span class="">⎣</span></span></span><span class="" style="top: -4.05002em;"><span class="pstrut" style="height: 3.1550000000000002em;"></span><span class="delimsizinginner delim-size4"><span class="">⎡</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 1.55002em;"><span class=""></span></span></span></span></span></span><span class="mord"><span class="mtable"><span class="col-align-c"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 2.05em;"><span class="" style="top: -4.21em;"><span class="pstrut" style="height: 3em;"></span><span class="mord"><span class="mord">0</span></span></span><span class="" style="top: -3.0099999999999993em;"><span class="pstrut" style="height: 3em;"></span><span class="mord"><span class="mord">0</span></span></span><span class="" style="top: -1.8099999999999994em;"><span class="pstrut" style="height: 3em;"></span><span class="mord"><span class="mord">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 1.5500000000000007em;"><span class=""></span></span></span></span></span><span class="arraycolsep" style="width: 0.5em;"></span><span class="arraycolsep" style="width: 0.5em;"></span><span class="col-align-c"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 2.05em;"><span class="" style="top: -4.21em;"><span class="pstrut" style="height: 3em;"></span><span class="mord"><span class="mord">0</span></span></span><span class="" style="top: -3.0099999999999993em;"><span class="pstrut" style="height: 3em;"></span><span class="mord"><span class="mord">1</span></span></span><span class="" style="top: -1.8099999999999994em;"><span class="pstrut" style="height: 3em;"></span><span class="mord"><span class="mord">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 1.5500000000000007em;"><span class=""></span></span></span></span></span><span class="arraycolsep" style="width: 0.5em;"></span><span class="arraycolsep" style="width: 0.5em;"></span><span class="col-align-c"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 2.05em;"><span class="" style="top: -4.21em;"><span class="pstrut" style="height: 3em;"></span><span class="mord"><span class="mord">0</span></span></span><span class="" style="top: -3.0099999999999993em;"><span class="pstrut" style="height: 3em;"></span><span class="mord"><span class="mord">0</span></span></span><span class="" style="top: -1.8099999999999994em;"><span class="pstrut" style="height: 3em;"></span><span class="mord"><span class="mord">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 1.5500000000000007em;"><span class=""></span></span></span></span></span></span></span><span class="mclose"><span class="delimsizing mult"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 2.05002em;"><span class="" style="top: -2.2500000000000004em;"><span class="pstrut" style="height: 3.1550000000000002em;"></span><span class="delimsizinginner delim-size4"><span class="">⎦</span></span></span><span class="" style="top: -4.05002em;"><span class="pstrut" style="height: 3.1550000000000002em;"></span><span class="delimsizinginner delim-size4"><span class="">⎤</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 1.55002em;"><span class=""></span></span></span></span></span></span></span></span></span></span></span>﻿</span> </li><li><strong>Differentiation </strong>- differentiating a convolution gives the same result as differentiating and then convolving</li><li class="ql-indent-1"><span class="ql-formula" data-value="\frac{\partial}{\partial x}(f*g)=\frac{\partial f}{\partial x}*g">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mfrac><mi mathvariant="normal">∂</mi><mrow><mi mathvariant="normal">∂</mi><mi>x</mi></mrow></mfrac><mo>(</mo><mi>f</mi><mo>∗</mo><mi>g</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mi mathvariant="normal">∂</mi><mi>f</mi></mrow><mrow><mi mathvariant="normal">∂</mi><mi>x</mi></mrow></mfrac><mo>∗</mo><mi>g</mi></mrow><annotation encoding="application/x-tex">\frac{\partial}{\partial x}(f*g)=\frac{\partial f}{\partial x}*g</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1.2251079999999999em; vertical-align: -0.345em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.8801079999999999em;"><span class="" style="top: -2.6550000000000002em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span style="margin-right: 0.05556em;" class="mord mtight">∂</span><span class="mord mathdefault mtight">x</span></span></span></span><span class="" style="top: -3.23em;"><span class="pstrut" style="height: 3em;"></span><span class="frac-line" style="border-bottom-width: 0.04em;"></span></span><span class="" style="top: -3.394em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span style="margin-right: 0.05556em;" class="mord mtight">∂</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.345em;"><span class=""></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mopen">(</span><span style="margin-right: 0.10764em;" class="mord mathdefault">f</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">∗</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span style="margin-right: 0.03588em;" class="mord mathdefault">g</span><span class="mclose">)</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 1.277216em; vertical-align: -0.345em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.9322159999999999em;"><span class="" style="top: -2.6550000000000002em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span style="margin-right: 0.05556em;" class="mord mtight">∂</span><span class="mord mathdefault mtight">x</span></span></span></span><span class="" style="top: -3.23em;"><span class="pstrut" style="height: 3em;"></span><span class="frac-line" style="border-bottom-width: 0.04em;"></span></span><span class="" style="top: -3.446108em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span style="margin-right: 0.05556em;" class="mord mtight">∂</span><span style="margin-right: 0.10764em;" class="mord mathdefault mtight">f</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.345em;"><span class=""></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">∗</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 0.625em; vertical-align: -0.19444em;"></span><span style="margin-right: 0.03588em;" class="mord mathdefault">g</span></span></span></span></span>﻿</span> </li></ul><p><br></p><h2 id="boundary-issues-<finish>">Boundary issues &lt;FINISH&gt;</h2><p><br></p><ul><li>The filter window may cross the image border</li><li>Several methods to deal:</li><li class="ql-indent-1">clip filter</li><li class="ql-indent-1">wrap around</li><li class="ql-indent-1">copy edge</li><li class="ql-indent-1">mirroring of edges</li></ul><p><br></p><h2 id="convolution-vs-cross-correlation">Convolution vs Cross-correlation</h2><p><br></p><p>&lt;picture / formulae&gt;</p><p><br></p><ul><li>convolution flips the filter before being applied</li><li>are equal is kernel H is symmetrical</li></ul><p><br></p><h1 id="noise-reduction">Noise Reduction</h1><p><br></p><h2 id="salt-and-pepper-noise">Salt and pepper noise</h2><p><br></p><ul><li><strong>Salt and pepper noise </strong>- random occurrences of white and black pixels</li></ul><p><br></p><p>&lt;insert image&gt;</p><p><br></p><h3 id="how-to-remove">How to remove</h3><p><br></p><ul><li><strong>Median filter </strong>- replace each pixel with the median of all values in the direct neighbourhood</li><li class="ql-indent-1">Assumptions:</li><li class="ql-indent-2">each pixel should be similar to its neighbours</li><li class="ql-indent-2">noise happens randomly</li><li class="ql-indent-1">Use a <span class="ql-formula" data-value="3\times3">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>3</mn><mo>×</mo><mn>3</mn></mrow><annotation encoding="application/x-tex">3\times3</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.72777em; vertical-align: -0.08333em;"></span><span class="mord">3</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">×</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">3</span></span></span></span></span>﻿</span> median filter</li><li class="ql-indent-2">Order by grey values</li><li class="ql-indent-2">Choose median pixel (5th value)</li><li class="ql-indent-2">Replace pixel with the median value</li><li class="ql-indent-1">Results:</li><li class="ql-indent-2">Not linear</li><li class="ql-indent-2">Uses an order statistics filters / spatial filter</li><li class="ql-indent-2">Removes noise but makes more blurry</li></ul><p><br></p><ul><li><strong>Averaging filter </strong>- use a moving average filter</li><li class="ql-indent-1">Assumptions:</li><li class="ql-indent-2">Pixels should look similar to neighbours</li><li class="ql-indent-2">Independent variations</li><li class="ql-indent-1">Results</li><li class="ql-indent-2">Not great solutions</li><li class="ql-indent-2">Not great since we know it's salt and pepper</li><li class="ql-indent-3">noise has extreme values which will affect the average</li></ul><p><br></p><h2 id="gaussian-noise">Gaussian noise</h2><p><br></p><ul><li><strong>Gaussian noise </strong>- variations in intensity drawn from a Gaussian normal distribution</li></ul><p><br></p><p>&lt;insert image&gt;</p><p><br></p><h3 id="how-to-remove">How to remove</h3><p><br></p><ul><li><strong>Box filter</strong> - averaging filter applied</li><li class="ql-indent-1">&lt;image&gt;</li></ul><p><br></p><ul><li><strong>Gaussian filter </strong>- convolve using Gaussian kernel</li><li class="ql-indent-1">Parameters</li><li class="ql-indent-2"><span class="ql-formula" data-value="\sigma">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>σ</mi></mrow><annotation encoding="application/x-tex">\sigma</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span style="margin-right: 0.03588em;" class="mord mathdefault">σ</span></span></span></span></span>﻿</span> - extent of smoothing</li><li class="ql-indent-2"><span class="ql-formula" data-value="K">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>K</mi></mrow><annotation encoding="application/x-tex">K</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.07153em;" class="mord mathdefault">K</span></span></span></span></span>﻿</span>  - size of kernel</li><li class="ql-indent-3">rule of thumb - <span class="ql-formula" data-value="K\ =\ 3\sigma">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>K</mi><mtext>&nbsp;</mtext><mo>=</mo><mtext>&nbsp;</mtext><mn>3</mn><mi>σ</mi></mrow><annotation encoding="application/x-tex">K\ =\ 3\sigma</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.07153em;" class="mord mathdefault">K</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mspace">&nbsp;</span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mspace">&nbsp;</span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">3</span><span style="margin-right: 0.03588em;" class="mord mathdefault">σ</span></span></span></span></span>﻿</span> </li><li class="ql-indent-4">When you try to visualise this, <span class="ql-formula" data-value="3\sigma">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>3</mn><mi>σ</mi></mrow><annotation encoding="application/x-tex">3\sigma</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">3</span><span style="margin-right: 0.03588em;" class="mord mathdefault">σ</span></span></span></span></span>﻿</span> is about 90% of a curve</li><li class="ql-indent-3">has support for infinite values, but discrete filters use finite kernels</li><li class="ql-indent-1">Normalised, approximated <span class="ql-formula" data-value="3\ \times3">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>3</mn><mtext>&nbsp;</mtext><mo>×</mo><mn>3</mn></mrow><annotation encoding="application/x-tex">3\ \times3</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.72777em; vertical-align: -0.08333em;"></span><span class="mord">3</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">×</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">3</span></span></span></span></span>﻿</span> kernel is following (<span class="ql-formula" data-value="X\ \sim N\left(0,1\right)">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>X</mi><mtext>&nbsp;</mtext><mo>∼</mo><mi>N</mi><mrow><mo fence="true">(</mo><mn>0</mn><mo separator="true">,</mo><mn>1</mn><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">X\ \sim N\left(0,1\right)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.07847em;" class="mord mathdefault">X</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mspace">&nbsp;</span><span class="mrel">∼</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord">0</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mord">1</span><span class="mclose delimcenter" style="top: 0em;">)</span></span></span></span></span></span>﻿</span>): </li></ul><p class="ql-indent-3"><span class="ql-formula" data-value="\frac{1}{16}\begin{bmatrix}1&amp;2&amp;1\\2&amp;4&amp;2\\1&amp;2&amp;1\end{bmatrix}">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mfrac><mn>1</mn><mn>16</mn></mfrac><mrow><mo fence="true">[</mo><mtable><mtr><mtd><mstyle scriptlevel="0" displaystyle="false"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="false"><mn>2</mn></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="false"><mn>1</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="false"><mn>2</mn></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="false"><mn>4</mn></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="false"><mn>2</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="false"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="false"><mn>2</mn></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="false"><mn>1</mn></mstyle></mtd></mtr></mtable><mo fence="true">]</mo></mrow></mrow><annotation encoding="application/x-tex">\frac{1}{16}\begin{bmatrix}1&amp;amp;2&amp;amp;1\\2&amp;amp;4&amp;amp;2\\1&amp;amp;2&amp;amp;1\end{bmatrix}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 3.60004em; vertical-align: -1.55002em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.845108em;"><span class="" style="top: -2.6550000000000002em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">1</span><span class="mord mtight">6</span></span></span></span><span class="" style="top: -3.23em;"><span class="pstrut" style="height: 3em;"></span><span class="frac-line" style="border-bottom-width: 0.04em;"></span></span><span class="" style="top: -3.394em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">1</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.345em;"><span class=""></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen"><span class="delimsizing mult"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 2.05002em;"><span class="" style="top: -2.2500000000000004em;"><span class="pstrut" style="height: 3.1550000000000002em;"></span><span class="delimsizinginner delim-size4"><span class="">⎣</span></span></span><span class="" style="top: -4.05002em;"><span class="pstrut" style="height: 3.1550000000000002em;"></span><span class="delimsizinginner delim-size4"><span class="">⎡</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 1.55002em;"><span class=""></span></span></span></span></span></span><span class="mord"><span class="mtable"><span class="col-align-c"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 2.05em;"><span class="" style="top: -4.21em;"><span class="pstrut" style="height: 3em;"></span><span class="mord"><span class="mord">1</span></span></span><span class="" style="top: -3.0099999999999993em;"><span class="pstrut" style="height: 3em;"></span><span class="mord"><span class="mord">2</span></span></span><span class="" style="top: -1.8099999999999994em;"><span class="pstrut" style="height: 3em;"></span><span class="mord"><span class="mord">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 1.5500000000000007em;"><span class=""></span></span></span></span></span><span class="arraycolsep" style="width: 0.5em;"></span><span class="arraycolsep" style="width: 0.5em;"></span><span class="col-align-c"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 2.05em;"><span class="" style="top: -4.21em;"><span class="pstrut" style="height: 3em;"></span><span class="mord"><span class="mord">2</span></span></span><span class="" style="top: -3.0099999999999993em;"><span class="pstrut" style="height: 3em;"></span><span class="mord"><span class="mord">4</span></span></span><span class="" style="top: -1.8099999999999994em;"><span class="pstrut" style="height: 3em;"></span><span class="mord"><span class="mord">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 1.5500000000000007em;"><span class=""></span></span></span></span></span><span class="arraycolsep" style="width: 0.5em;"></span><span class="arraycolsep" style="width: 0.5em;"></span><span class="col-align-c"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 2.05em;"><span class="" style="top: -4.21em;"><span class="pstrut" style="height: 3em;"></span><span class="mord"><span class="mord">1</span></span></span><span class="" style="top: -3.0099999999999993em;"><span class="pstrut" style="height: 3em;"></span><span class="mord"><span class="mord">2</span></span></span><span class="" style="top: -1.8099999999999994em;"><span class="pstrut" style="height: 3em;"></span><span class="mord"><span class="mord">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 1.5500000000000007em;"><span class=""></span></span></span></span></span></span></span><span class="mclose"><span class="delimsizing mult"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 2.05002em;"><span class="" style="top: -2.2500000000000004em;"><span class="pstrut" style="height: 3.1550000000000002em;"></span><span class="delimsizinginner delim-size4"><span class="">⎦</span></span></span><span class="" style="top: -4.05002em;"><span class="pstrut" style="height: 3.1550000000000002em;"></span><span class="delimsizinginner delim-size4"><span class="">⎤</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 1.55002em;"><span class=""></span></span></span></span></span></span></span></span></span></span></span>﻿</span> </p><p class="ql-indent-3"><br></p><p>&lt;insert image&gt;</p><p><br></p><h2 id="blurry-image">Blurry image</h2><p><br></p><ul><li><strong>Blurry image</strong> - without clear outline; not clear</li></ul><p><br></p><p>&lt;insert image&gt;</p><p><br></p><h3 id="how-to-remove">How to remove</h3><p><br></p><ul><li><strong>Contrast </strong>- the difference between colour values of neighbouring pixels</li><li class="ql-indent-1">Bigger difference = bigger contrast</li></ul><p><br></p><ul><li><strong>Sharpening </strong>- increase contrast, then subtract average filter</li><li class="ql-indent-1">Accentuate differences and take the local average</li><li class="ql-indent-1">Will show noise much clearer &gt; apply to smooth first then sharpening</li><li class="ql-indent-1">Clipping is done after subtraction</li></ul><p>&lt;image&gt;</p><p><br></p>