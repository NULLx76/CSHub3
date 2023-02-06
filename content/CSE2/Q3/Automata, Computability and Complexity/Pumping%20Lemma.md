+++
title = "Pumping Lemma"
date = 2020-02-28
+++
<p>An example of a non-regular is <span class="ql-formula" data-value="B=\left\{0^N1^N\mid N\ge0\right\}">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>B</mi><mo>=</mo><mrow><mo fence="true">{</mo><msup><mn>0</mn><mi>N</mi></msup><msup><mn>1</mn><mi>N</mi></msup><mo>∣</mo><mi>N</mi><mo>≥</mo><mn>0</mn><mo fence="true">}</mo></mrow></mrow><annotation encoding="application/x-tex">B=\left\{0^N1^N\mid N\ge0\right\}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 1.20001em; vertical-align: -0.35001em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;"><span class="delimsizing size1">{</span></span><span class="mord"><span class="mord">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.8413309999999999em;"><span class="" style="top: -3.063em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span style="margin-right: 0.10903em;" class="mord mathdefault mtight">N</span></span></span></span></span></span></span></span><span class="mord"><span class="mord">1</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.8413309999999999em;"><span class="" style="top: -3.063em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span style="margin-right: 0.10903em;" class="mord mathdefault mtight">N</span></span></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">∣</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span style="margin-right: 0.10903em;" class="mord mathdefault">N</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">≥</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mord">0</span><span class="mclose delimcenter" style="top: 0em;"><span class="delimsizing size1">}</span></span></span></span></span></span></span>﻿</span>, as this requires counting. If we want to prove that a language is not regular, we can use the pumping lemma.</p><p><br></p><p>Imagine a F.S.M. with a small number of states that generates really long strings. If <span class="ql-formula" data-value="\left|Q\right|=5">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mo fence="true">∣</mo><mi>Q</mi><mo fence="true">∣</mo></mrow><mo>=</mo><mn>5</mn></mrow><annotation encoding="application/x-tex">\left|Q\right|=5</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">∣</span><span class="mord mathdefault">Q</span><span class="mclose delimcenter" style="top: 0em;">∣</span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">5</span></span></span></span></span>﻿</span> , we will need cycles to generate long strings.</p><p><br></p><p>The key ideas of a pumping lemma are: </p><ul><li>if you can go around a cycle once, then you can go around it <span class="ql-formula" data-value="n">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi></mrow><annotation encoding="application/x-tex">n</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord mathdefault">n</span></span></span></span></span>﻿</span> times, and that string must also be in the language</li><li>you can also skip a cycle, and that string must also be in the language</li></ul><p><br></p><p><strong>Pumping Lemma</strong></p><p>If <span class="ql-formula" data-value="A">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathdefault">A</span></span></span></span></span>﻿</span> is a regular language, then <span class="ql-formula" data-value="A">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathdefault">A</span></span></span></span></span>﻿</span> has a pumping length <span class="ql-formula" data-value="P">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>P</mi></mrow><annotation encoding="application/x-tex">P</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.13889em;" class="mord mathdefault">P</span></span></span></span></span>﻿</span> such that <strong>any </strong>string <span class="ql-formula" data-value="s">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>s</mi></mrow><annotation encoding="application/x-tex">s</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord mathdefault">s</span></span></span></span></span>﻿</span> (as long as <span class="ql-formula" data-value="\left|s\right|\ge P">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mo fence="true">∣</mo><mi>s</mi><mo fence="true">∣</mo></mrow><mo>≥</mo><mi>P</mi></mrow><annotation encoding="application/x-tex">\left|s\right|\ge P</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">∣</span><span class="mord mathdefault">s</span><span class="mclose delimcenter" style="top: 0em;">∣</span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">≥</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.13889em;" class="mord mathdefault">P</span></span></span></span></span>﻿</span>) may be divided into 3 pieces <span class="ql-formula" data-value="s=xyz">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>s</mi><mo>=</mo><mi>x</mi><mi>y</mi><mi>z</mi></mrow><annotation encoding="application/x-tex">s=xyz</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord mathdefault">s</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.625em; vertical-align: -0.19444em;"></span><span class="mord mathdefault">x</span><span style="margin-right: 0.03588em;" class="mord mathdefault">y</span><span style="margin-right: 0.04398em;" class="mord mathdefault">z</span></span></span></span></span>﻿</span> such that all these conditions hold:</p><ul><li><span class="ql-formula" data-value="xy^iz">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><msup><mi>y</mi><mi>i</mi></msup><mi>z</mi></mrow><annotation encoding="application/x-tex">xy^iz</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1.019104em; vertical-align: -0.19444em;"></span><span class="mord mathdefault">x</span><span class="mord"><span style="margin-right: 0.03588em;" class="mord mathdefault">y</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.824664em;"><span class="" style="top: -3.063em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">i</span></span></span></span></span></span></span></span><span style="margin-right: 0.04398em;" class="mord mathdefault">z</span></span></span></span></span>﻿</span> is in the language for <span class="ql-formula" data-value="i\ge0">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>i</mi><mo>≥</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">i\ge0</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.79549em; vertical-align: -0.13597em;"></span><span class="mord mathdefault">i</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">≥</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">0</span></span></span></span></span>﻿</span></li><li><span class="ql-formula" data-value="\left|y\right|>0">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mo fence="true">∣</mo><mi>y</mi><mo fence="true">∣</mo></mrow><mo>&amp;gt;</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">\left|y\right|&amp;gt;0</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">∣</span><span style="margin-right: 0.03588em;" class="mord mathdefault">y</span><span class="mclose delimcenter" style="top: 0em;">∣</span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">&gt;</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">0</span></span></span></span></span>﻿</span>, so the cycle has at least one edge</li><li><span class="ql-formula" data-value="\left|xy\right|\le P">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mo fence="true">∣</mo><mi>x</mi><mi>y</mi><mo fence="true">∣</mo></mrow><mo>≤</mo><mi>P</mi></mrow><annotation encoding="application/x-tex">\left|xy\right|\le P</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">∣</span><span class="mord mathdefault">x</span><span style="margin-right: 0.03588em;" class="mord mathdefault">y</span><span class="mclose delimcenter" style="top: 0em;">∣</span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.13889em;" class="mord mathdefault">P</span></span></span></span></span>﻿</span>, so you have to hit the cycle before the string gets longer than <span class="ql-formula" data-value="P">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>P</mi></mrow><annotation encoding="application/x-tex">P</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.13889em;" class="mord mathdefault">P</span></span></span></span></span>﻿</span></li></ul><p><br></p><p>Note that this pumping length depends on the language itself, not on a specific FSM.</p><p><br></p><p><strong>Example</strong></p><p>Some odd examples:</p><p><img src="https://i.imgur.com/yrwkjae.png" width="443"></p><p><em>Image taken from video lectures by Harry Porter</em></p><p><br></p><p>You can see here that <span class="ql-formula" data-value="z">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>z</mi></mrow><annotation encoding="application/x-tex">z</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span style="margin-right: 0.04398em;" class="mord mathdefault">z</span></span></span></span></span>﻿</span> can be empty and multiple nodes can be repeated.</p><p><br></p><p><strong>Proving a language is not regular</strong></p><p>General form by contradiction:</p><ul><li>Assume <span class="ql-formula" data-value="A">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathdefault">A</span></span></span></span></span>﻿</span> is regular, then it'll have a pumping length <span class="ql-formula" data-value="P">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>P</mi></mrow><annotation encoding="application/x-tex">P</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.13889em;" class="mord mathdefault">P</span></span></span></span></span>﻿</span> </li><li>All strings longer than <span class="ql-formula" data-value="P">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>P</mi></mrow><annotation encoding="application/x-tex">P</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.13889em;" class="mord mathdefault">P</span></span></span></span></span>﻿</span> can be pumped</li><li>Find a string <span class="ql-formula" data-value="s">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>s</mi></mrow><annotation encoding="application/x-tex">s</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord mathdefault">s</span></span></span></span></span>﻿</span> in <span class="ql-formula" data-value="A">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathdefault">A</span></span></span></span></span>﻿</span> such that <span class="ql-formula" data-value="\left|s\right|\ge P">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mo fence="true">∣</mo><mi>s</mi><mo fence="true">∣</mo></mrow><mo>≥</mo><mi>P</mi></mrow><annotation encoding="application/x-tex">\left|s\right|\ge P</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">∣</span><span class="mord mathdefault">s</span><span class="mclose delimcenter" style="top: 0em;">∣</span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">≥</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.13889em;" class="mord mathdefault">P</span></span></span></span></span>﻿</span> and divide <span class="ql-formula" data-value="s">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>s</mi></mrow><annotation encoding="application/x-tex">s</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord mathdefault">s</span></span></span></span></span>﻿</span> into <span class="ql-formula" data-value="xyz">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mi>y</mi><mi>z</mi></mrow><annotation encoding="application/x-tex">xyz</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.625em; vertical-align: -0.19444em;"></span><span class="mord mathdefault">x</span><span style="margin-right: 0.03588em;" class="mord mathdefault">y</span><span style="margin-right: 0.04398em;" class="mord mathdefault">z</span></span></span></span></span>﻿</span> </li><li>Then consider all ways that <span class="ql-formula" data-value="s">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>s</mi></mrow><annotation encoding="application/x-tex">s</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord mathdefault">s</span></span></span></span></span>﻿</span> can be divided into <span class="ql-formula" data-value="xyz">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mi>y</mi><mi>z</mi></mrow><annotation encoding="application/x-tex">xyz</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.625em; vertical-align: -0.19444em;"></span><span class="mord mathdefault">x</span><span style="margin-right: 0.03588em;" class="mord mathdefault">y</span><span style="margin-right: 0.04398em;" class="mord mathdefault">z</span></span></span></span></span>﻿</span> and show that none of these satisfy all the <span class="ql-formula" data-value="3">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>3</mn></mrow><annotation encoding="application/x-tex">3</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">3</span></span></span></span></span>﻿</span> pumping conditions at the same time</li><li>This is a contradiction, as <span class="ql-formula" data-value="s">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>s</mi></mrow><annotation encoding="application/x-tex">s</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord mathdefault">s</span></span></span></span></span>﻿</span> cannot be pumped.</li></ul><p><br></p><p>An example can be found in the examples tab.</p><p><br></p><h3 id="pigeonhole-principle">Pigeonhole principle</h3><p>No clue where to put this lol: let <span class="ql-formula" data-value="A">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathdefault">A</span></span></span></span></span>﻿</span> and <span class="ql-formula" data-value="B">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>B</mi></mrow><annotation encoding="application/x-tex">B</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span></span></span></span></span>﻿</span> be finite sets with <span class="ql-formula" data-value="n">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi></mrow><annotation encoding="application/x-tex">n</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord mathdefault">n</span></span></span></span></span>﻿</span> and <span class="ql-formula" data-value="m">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>m</mi></mrow><annotation encoding="application/x-tex">m</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord mathdefault">m</span></span></span></span></span>﻿</span> If you put <span class="ql-formula" data-value="n">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi></mrow><annotation encoding="application/x-tex">n</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord mathdefault">n</span></span></span></span></span>﻿</span> objects into <span class="ql-formula" data-value="m">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>m</mi></mrow><annotation encoding="application/x-tex">m</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord mathdefault">m</span></span></span></span></span>﻿</span> holes and <span class="ql-formula" data-value="n>m">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi><mo>&amp;gt;</mo><mi>m</mi></mrow><annotation encoding="application/x-tex">n&amp;gt;m</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.5782em; vertical-align: -0.0391em;"></span><span class="mord mathdefault">n</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">&gt;</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord mathdefault">m</span></span></span></span></span>﻿</span>, then there is at least a hole with 2 or more objects</p>