+++
title = "Logic summary"
date = 2019-09-05
+++
<h2 id="disjunctive-normal-form"><span style="background-color: rgba(0, 0, 0, 0);">Disjunctive Normal Form</span></h2><p><span style="background-color: rgba(0, 0, 0, 0);">Disjunctive Normal Form or DNF for short is the disjunction of conjunctions of literals. Every formula has an equivalent in DNF.</span></p><p><br></p><h3 id="examples-of-dnf"><span style="background-color: rgba(0, 0, 0, 0);">Examples of DNF</span></h3><p><span style="background-color: rgba(0, 0, 0, 0);"><span class="ql-formula" data-value="A">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathdefault">A</span></span></span></span></span>﻿</span> </span></p><p><span style="background-color: rgba(0, 0, 0, 0);"><span class="ql-formula" data-value="A\ \vee\ \neg A">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi><mtext>&nbsp;</mtext><mo>∨</mo><mtext>&nbsp;</mtext><mi mathvariant="normal">¬</mi><mi>A</mi></mrow><annotation encoding="application/x-tex">A\ \vee\ \neg A</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∨</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord">¬</span><span class="mord mathdefault">A</span></span></span></span></span>﻿</span> </span></p><p><span style="background-color: rgba(0, 0, 0, 0);"><span class="ql-formula" data-value="A\ \vee\ \left(B\ \wedge\ \neg C\right)\ \vee\ D">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi><mtext>&nbsp;</mtext><mo>∨</mo><mtext>&nbsp;</mtext><mrow><mo fence="true">(</mo><mi>B</mi><mtext>&nbsp;</mtext><mo>∧</mo><mtext>&nbsp;</mtext><mi mathvariant="normal">¬</mi><mi>C</mi><mo fence="true">)</mo></mrow><mtext>&nbsp;</mtext><mo>∨</mo><mtext>&nbsp;</mtext><mi>D</mi></mrow><annotation encoding="application/x-tex">A\ \vee\ \left(B\ \wedge\ \neg C\right)\ \vee\ D</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∨</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∧</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mord">¬</span><span style="margin-right: 0.07153em;" class="mord mathdefault">C</span><span class="mclose delimcenter" style="top: 0em;">)</span></span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∨</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.02778em;" class="mord mathdefault">D</span></span></span></span></span>﻿</span> </span></p><p><br></p><h3 id="transformation-algorithm"><span style="background-color: rgba(0, 0, 0, 0);">Transformation Algorithm</span></h3><p><span style="background-color: rgba(0, 0, 0, 0);">There are several different methods for transforming an arbitrary formula into DNF. The following is one of the simplest with three steps:</span></p><ul><li><span style="background-color: rgba(0, 0, 0, 0);">Eliminate the connectives for implication (<span class="ql-formula" data-value="\Rightarrow">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>⇒</mo></mrow><annotation encoding="application/x-tex">\Rightarrow</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.36687em; vertical-align: 0em;"></span><span class="mrel">⇒</span></span></span></span></span>﻿</span>) and equivalence (<span class="ql-formula" data-value="\Leftrightarrow">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>⇔</mo></mrow><annotation encoding="application/x-tex">\Leftrightarrow</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.36687em; vertical-align: 0em;"></span><span class="mrel">⇔</span></span></span></span></span>﻿</span> ) by rewriting using the following equivalences:</span></li><li class="ql-indent-1"><span style="background-color: rgba(0, 0, 0, 0);"><span class="ql-formula" data-value="A\ \Rightarrow B">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi><mtext>&nbsp;</mtext><mo>⇒</mo><mi>B</mi></mrow><annotation encoding="application/x-tex">A\ \Rightarrow B</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mspace">&nbsp;</span><span class="mrel">⇒</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span></span></span></span></span>﻿</span> is equivalent to <span class="ql-formula" data-value="\neg A\ \vee\ B">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mi>A</mi><mtext>&nbsp;</mtext><mo>∨</mo><mtext>&nbsp;</mtext><mi>B</mi></mrow><annotation encoding="application/x-tex">\neg A\ \vee\ B</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord">¬</span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∨</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span></span></span></span></span>﻿</span></span></li><li class="ql-indent-1"><span style="background-color: rgba(0, 0, 0, 0);"><span class="ql-formula" data-value="A\ \Leftrightarrow B">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi><mtext>&nbsp;</mtext><mo>⇔</mo><mi>B</mi></mrow><annotation encoding="application/x-tex">A\ \Leftrightarrow B</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mspace">&nbsp;</span><span class="mrel">⇔</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span></span></span></span></span>﻿</span> is equivalent to <span class="ql-formula" data-value="\left(\neg A\ \vee\ B\right)\ \wedge\ \left(A\ \vee\ \neg B\right)">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mo fence="true">(</mo><mi mathvariant="normal">¬</mi><mi>A</mi><mtext>&nbsp;</mtext><mo>∨</mo><mtext>&nbsp;</mtext><mi>B</mi><mo fence="true">)</mo></mrow><mtext>&nbsp;</mtext><mo>∧</mo><mtext>&nbsp;</mtext><mrow><mo fence="true">(</mo><mi>A</mi><mtext>&nbsp;</mtext><mo>∨</mo><mtext>&nbsp;</mtext><mi mathvariant="normal">¬</mi><mi>B</mi><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">\left(\neg A\ \vee\ B\right)\ \wedge\ \left(A\ \vee\ \neg B\right)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord">¬</span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∨</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span><span class="mclose delimcenter" style="top: 0em;">)</span></span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∧</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∨</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mord">¬</span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span><span class="mclose delimcenter" style="top: 0em;">)</span></span></span></span></span></span>﻿</span></span></li><li><span style="background-color: rgba(0, 0, 0, 0);">Push negations (<span class="ql-formula" data-value="\neg">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi></mrow><annotation encoding="application/x-tex">\neg</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord">¬</span></span></span></span></span>﻿</span> ) inside sub-formulas as far as possible, applying&nbsp;</span><strong style="background-color: rgba(0, 0, 0, 0);">De Morgan's Law</strong><span style="background-color: rgba(0, 0, 0, 0);">&nbsp;where possible, and eliminate double negations. We also handle the negation of the propositional constants. We do this by rewriting with the following equivalences:</span></li><li class="ql-indent-1"><span style="background-color: rgba(0, 0, 0, 0);"><span class="ql-formula" data-value="\neg\left(\neg A\right)">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mrow><mo fence="true">(</mo><mi mathvariant="normal">¬</mi><mi>A</mi><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">\neg\left(\neg A\right)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mord">¬</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord">¬</span><span class="mord mathdefault">A</span><span class="mclose delimcenter" style="top: 0em;">)</span></span></span></span></span></span>﻿</span>  is equivalent to <span class="ql-formula" data-value="A">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathdefault">A</span></span></span></span></span>﻿</span> </span></li><li class="ql-indent-1"><span style="background-color: rgba(0, 0, 0, 0);"><span class="ql-formula" data-value="\neg\left(A\ \wedge\ B\right)">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mrow><mo fence="true">(</mo><mi>A</mi><mtext>&nbsp;</mtext><mo>∧</mo><mtext>&nbsp;</mtext><mi>B</mi><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">\neg\left(A\ \wedge\ B\right)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mord">¬</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∧</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span><span class="mclose delimcenter" style="top: 0em;">)</span></span></span></span></span></span>﻿</span> is equivalent to <span class="ql-formula" data-value="\neg A\ \vee\ \neg B">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mi>A</mi><mtext>&nbsp;</mtext><mo>∨</mo><mtext>&nbsp;</mtext><mi mathvariant="normal">¬</mi><mi>B</mi></mrow><annotation encoding="application/x-tex">\neg A\ \vee\ \neg B</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord">¬</span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∨</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord">¬</span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span></span></span></span></span>﻿</span></span></li><li class="ql-indent-1"><span style="background-color: rgba(0, 0, 0, 0);"><span class="ql-formula" data-value="\neg\left(A\ \vee B\right)">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mrow><mo fence="true">(</mo><mi>A</mi><mtext>&nbsp;</mtext><mo>∨</mo><mi>B</mi><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">\neg\left(A\ \vee B\right)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mord">¬</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∨</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span><span class="mclose delimcenter" style="top: 0em;">)</span></span></span></span></span></span>﻿</span> is equivalent to <span class="ql-formula" data-value="\neg A\ \wedge\ \neg B">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mi>A</mi><mtext>&nbsp;</mtext><mo>∧</mo><mtext>&nbsp;</mtext><mi mathvariant="normal">¬</mi><mi>B</mi></mrow><annotation encoding="application/x-tex">\neg A\ \wedge\ \neg B</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord">¬</span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∧</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord">¬</span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span></span></span></span></span>﻿</span></span></li><li class="ql-indent-1"><span style="background-color: rgba(0, 0, 0, 0);"><span class="ql-formula" data-value="\neg\top">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mi mathvariant="normal">⊤</mi></mrow><annotation encoding="application/x-tex">\neg\top</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.69444em; vertical-align: 0em;"></span><span class="mord">¬</span><span class="mord">⊤</span></span></span></span></span>﻿</span>  is equivalent to <span class="ql-formula" data-value="\bot">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">⊥</mi></mrow><annotation encoding="application/x-tex">\bot</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.69444em; vertical-align: 0em;"></span><span class="mord">⊥</span></span></span></span></span>﻿</span> (false)</span></li><li class="ql-indent-1"><span style="background-color: rgba(0, 0, 0, 0);"><span class="ql-formula" data-value="\neg\bot">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mi mathvariant="normal">⊥</mi></mrow><annotation encoding="application/x-tex">\neg\bot</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.69444em; vertical-align: 0em;"></span><span class="mord">¬</span><span class="mord">⊥</span></span></span></span></span>﻿</span>  is equivalent to <span class="ql-formula" data-value="\top">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">⊤</mi></mrow><annotation encoding="application/x-tex">\top</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.69444em; vertical-align: 0em;"></span><span class="mord">⊤</span></span></span></span></span>﻿</span> (true)</span></li><li><span style="background-color: rgba(0, 0, 0, 0);">Distribute conjunctions (<span class="ql-formula" data-value="\wedge">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>∧</mo></mrow><annotation encoding="application/x-tex">\wedge</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.55556em; vertical-align: 0em;"></span><span class="mord">∧</span></span></span></span></span>﻿</span>) over disjunctions (<span class="ql-formula" data-value="\vee">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>∨</mo></mrow><annotation encoding="application/x-tex">\vee</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.55556em; vertical-align: 0em;"></span><span class="mord">∨</span></span></span></span></span>﻿</span>). We rewrite all applicable subterms of the formula using one of the following two equivalences:</span></li><li class="ql-indent-1"><span style="background-color: rgba(0, 0, 0, 0);"><span class="ql-formula" data-value="A\ \wedge\ \left(B\ \vee\ C\right)">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi><mtext>&nbsp;</mtext><mo>∧</mo><mtext>&nbsp;</mtext><mrow><mo fence="true">(</mo><mi>B</mi><mtext>&nbsp;</mtext><mo>∨</mo><mtext>&nbsp;</mtext><mi>C</mi><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">A\ \wedge\ \left(B\ \vee\ C\right)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∧</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∨</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span style="margin-right: 0.07153em;" class="mord mathdefault">C</span><span class="mclose delimcenter" style="top: 0em;">)</span></span></span></span></span></span>﻿</span> is equivalent to <span class="ql-formula" data-value="\left(A\ \wedge\ B\right)\ \vee\ \left(A\ \ \wedge\ C\right)">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mo fence="true">(</mo><mi>A</mi><mtext>&nbsp;</mtext><mo>∧</mo><mtext>&nbsp;</mtext><mi>B</mi><mo fence="true">)</mo></mrow><mtext>&nbsp;</mtext><mo>∨</mo><mtext>&nbsp;</mtext><mrow><mo fence="true">(</mo><mi>A</mi><mtext>&nbsp;&nbsp;</mtext><mo>∧</mo><mtext>&nbsp;</mtext><mi>C</mi><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">\left(A\ \wedge\ B\right)\ \vee\ \left(A\ \ \wedge\ C\right)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∧</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span><span class="mclose delimcenter" style="top: 0em;">)</span></span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∨</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mspace">&nbsp;</span><span class="mbin">∧</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span style="margin-right: 0.07153em;" class="mord mathdefault">C</span><span class="mclose delimcenter" style="top: 0em;">)</span></span></span></span></span></span>﻿</span></span></li><li class="ql-indent-1"><span style="background-color: rgba(0, 0, 0, 0);"><span class="ql-formula" data-value="\left(A\ \vee\ B\right)\ \wedge\ C">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mo fence="true">(</mo><mi>A</mi><mtext>&nbsp;</mtext><mo>∨</mo><mtext>&nbsp;</mtext><mi>B</mi><mo fence="true">)</mo></mrow><mtext>&nbsp;</mtext><mo>∧</mo><mtext>&nbsp;</mtext><mi>C</mi></mrow><annotation encoding="application/x-tex">\left(A\ \vee\ B\right)\ \wedge\ C</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∨</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span><span class="mclose delimcenter" style="top: 0em;">)</span></span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∧</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.07153em;" class="mord mathdefault">C</span></span></span></span></span>﻿</span> is equivalent to <span class="ql-formula" data-value="\left(A\ \wedge\ C\right)\ \vee\ \left(B\ \wedge\ C\right)">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mo fence="true">(</mo><mi>A</mi><mtext>&nbsp;</mtext><mo>∧</mo><mtext>&nbsp;</mtext><mi>C</mi><mo fence="true">)</mo></mrow><mtext>&nbsp;</mtext><mo>∨</mo><mtext>&nbsp;</mtext><mrow><mo fence="true">(</mo><mi>B</mi><mtext>&nbsp;</mtext><mo>∧</mo><mtext>&nbsp;</mtext><mi>C</mi><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">\left(A\ \wedge\ C\right)\ \vee\ \left(B\ \wedge\ C\right)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∧</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span style="margin-right: 0.07153em;" class="mord mathdefault">C</span><span class="mclose delimcenter" style="top: 0em;">)</span></span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∨</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∧</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span style="margin-right: 0.07153em;" class="mord mathdefault">C</span><span class="mclose delimcenter" style="top: 0em;">)</span></span></span></span></span></span>﻿</span></span></li></ul><p><br></p><h2 id="de-morgan's-law"><span style="background-color: rgba(0, 0, 0, 0);">De Morgan's law</span></h2><p><span style="background-color: rgba(0, 0, 0, 0);">De Morgan's law states the following equivalences:</span></p><ul><li><span style="background-color: rgba(0, 0, 0, 0);"><span class="ql-formula" data-value="\neg\left(A\ \wedge\ B\right)\Leftrightarrow\neg A\ \vee\ \neg B">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mrow><mo fence="true">(</mo><mi>A</mi><mtext>&nbsp;</mtext><mo>∧</mo><mtext>&nbsp;</mtext><mi>B</mi><mo fence="true">)</mo></mrow><mo>⇔</mo><mi mathvariant="normal">¬</mi><mi>A</mi><mtext>&nbsp;</mtext><mo>∨</mo><mtext>&nbsp;</mtext><mi mathvariant="normal">¬</mi><mi>B</mi></mrow><annotation encoding="application/x-tex">\neg\left(A\ \wedge\ B\right)\Leftrightarrow\neg A\ \vee\ \neg B</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mord">¬</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∧</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span><span class="mclose delimcenter" style="top: 0em;">)</span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">⇔</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord">¬</span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∨</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord">¬</span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span></span></span></span></span>﻿</span> </span></li><li><span style="background-color: rgba(0, 0, 0, 0);"><span class="ql-formula" data-value="\neg\left(A\ \vee\ B\right)\ \Leftrightarrow\neg A\ \wedge\ \neg B">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mrow><mo fence="true">(</mo><mi>A</mi><mtext>&nbsp;</mtext><mo>∨</mo><mtext>&nbsp;</mtext><mi>B</mi><mo fence="true">)</mo></mrow><mtext>&nbsp;</mtext><mo>⇔</mo><mi mathvariant="normal">¬</mi><mi>A</mi><mtext>&nbsp;</mtext><mo>∧</mo><mtext>&nbsp;</mtext><mi mathvariant="normal">¬</mi><mi>B</mi></mrow><annotation encoding="application/x-tex">\neg\left(A\ \vee\ B\right)\ \Leftrightarrow\neg A\ \wedge\ \neg B</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mord">¬</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∨</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span><span class="mclose delimcenter" style="top: 0em;">)</span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mspace">&nbsp;</span><span class="mrel">⇔</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord">¬</span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span><span class="mbin">∧</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mspace">&nbsp;</span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord">¬</span><span style="margin-right: 0.05017em;" class="mord mathdefault">B</span></span></span></span></span>﻿</span> </span></li></ul><p><br></p><p><br></p><h2 id="arguments"><span style="background-color: rgba(0, 0, 0, 0);">Arguments</span></h2><p><span style="background-color: rgba(0, 0, 0, 0);">An argument consists of a conclusion and a number of premises. There can be one, more then one or even zero premises in an argument.</span></p><p><span style="background-color: rgba(0, 0, 0, 0);">An argument is valid if and only if the conclusion is true for all cases (i.e. rows in the truth table) where all propositions are true. For propositional logic it is relatively easy to prove that an argument is valid. You draw out the truth table. You look at the conclusion. If and only if the conclusion is true, you look at the column of all the premises. All premises have to be true. If this isn't the case, the argument is invalid. Repeat this process for all rows where the conclusion is true.</span></p><p><span style="background-color: rgba(0, 0, 0, 0);">For predicate logic, this process is more difficult. You need to use a mathematical proof. I can't explain all mathematical proofs here, because they are different for every argument. Look at the text book, that explains it pretty well.</span></p><p><br></p><h3 id="special-cases"><span style="background-color: rgba(0, 0, 0, 0);">Special cases</span></h3><p><span style="background-color: rgba(0, 0, 0, 0);">If an argument has no premises, the conclusion must be a tautology (i.e. always true) for the argument to be valid. A example of a tautology is (p or not p).</span></p><p><span style="background-color: rgba(0, 0, 0, 0);">Principal of explosion: if one of the premises is a contradiction (i.e. always false), the argument is always valid. Look at the definition of a valid argument. The conclusion has to be true for all cases where all propositions are true. If there are no cases where the propositions are true, this definition technically holds. It won't win you a debate, but the argument is logically valid.</span></p><p><br></p><p><br></p><h2 id="sources"><span style="background-color: rgba(0, 0, 0, 0);">Sources</span></h2><ul><li><span style="background-color: rgba(0, 0, 0, 0);">Hugtenburg, S. &amp; Yorke-Smith, N. (2018) Delftse Foundations of Computation. Available for download&nbsp;</span><a href="https://textbooks.open.tudelft.nl/index.php/textbooks/catalog/book/13" target="_blank" style="background-color: rgba(0, 0, 0, 0);">here</a></li><li><a href="http://www.barrywatson.se/cl/cl_dnf.html" target="_blank" style="background-color: rgba(0, 0, 0, 0);">DNF</a></li><li><a href="https://github.com/CSEdelft/FAQ/blob/master/reasoning-and-logic/README.md" target="_blank" style="background-color: rgba(0, 0, 0, 0);">CSEDelft Github FAQ</a></li></ul><p><br></p><p><br></p><h2 id="useful-links"><span style="background-color: rgba(0, 0, 0, 0);">Useful Links</span></h2><ul><li><a href="https://en.wikipedia.org/wiki/Logical_equivalence" target="_blank" style="background-color: rgba(0, 0, 0, 0);">Logical Equivalence</a></li><li><a href="https://en.wikipedia.org/wiki/Recursion#In_mathematics" target="_blank" style="background-color: rgba(0, 0, 0, 0);">Recursion</a></li></ul><p><br></p>