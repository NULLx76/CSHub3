+++
title = "Sampling (Mobius 4 - Q2)"
date = 2020-10-28
+++
<p>In figure 1, the single-sided amplitude spectrum of an analog signal is shown. The maximum signal frequency&nbsp;<span class="ql-formula" data-value="f_{\max}=5\ kHz">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>f</mi><mi>max</mi><mo>⁡</mo></msub><mo>=</mo><mn>5</mn><mtext>&nbsp;</mtext><mi>k</mi><mi>H</mi><mi>z</mi></mrow><annotation encoding="application/x-tex">f_{\max}=5\ kHz</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.8888799999999999em; vertical-align: -0.19444em;"></span><span class="mord"><span style="margin-right: 0.10764em;" class="mord mathdefault">f</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.151392em;"><span class="" style="top: -2.151392em; margin-left: -0.10764em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.301392em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mop mtight">max</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.69444em; vertical-align: 0em;"></span><span class="mord">5</span><span class="mspace">&nbsp;</span><span style="margin-right: 0.03148em;" class="mord mathdefault">k</span><span style="margin-right: 0.08125em;" class="mord mathdefault">H</span><span style="margin-right: 0.04398em;" class="mord mathdefault">z</span></span></span></span></span>﻿</span>. This signal is sampled with a frequency <span class="ql-formula" data-value="f_s=11\ kHz">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>f</mi><mi>s</mi></msub><mo>=</mo><mn>11</mn><mtext>&nbsp;</mtext><mi>k</mi><mi>H</mi><mi>z</mi></mrow><annotation encoding="application/x-tex">f_s=11\ kHz</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.8888799999999999em; vertical-align: -0.19444em;"></span><span class="mord"><span style="margin-right: 0.10764em;" class="mord mathdefault">f</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.151392em;"><span class="" style="top: -2.5500000000000003em; margin-left: -0.10764em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">s</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.69444em; vertical-align: 0em;"></span><span class="mord">1</span><span class="mord">1</span><span class="mspace">&nbsp;</span><span style="margin-right: 0.03148em;" class="mord mathdefault">k</span><span style="margin-right: 0.08125em;" class="mord mathdefault">H</span><span style="margin-right: 0.04398em;" class="mord mathdefault">z</span></span></span></span></span>﻿</span> and the sample pulse width <span class="ql-formula" data-value="\tau=69.1">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>τ</mi><mo>=</mo><mn>69.1</mn></mrow><annotation encoding="application/x-tex">\tau=69.1</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span style="margin-right: 0.1132em;" class="mord mathdefault">τ</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">6</span><span class="mord">9</span><span class="mord">.</span><span class="mord">1</span></span></span></span></span>﻿</span> <span class="ql-formula" data-value="\mu s">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>μ</mi><mi>s</mi></mrow><annotation encoding="application/x-tex">\mu s</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.625em; vertical-align: -0.19444em;"></span><span class="mord mathdefault">μ</span><span class="mord mathdefault">s</span></span></span></span></span>﻿</span>.</p><p><br></p><p><img src="https://tudelft-exercise.mobius.cloud/web/Ee2t11t005/Public_Html/ImportedQuestions/2ff4cfd4-d7f7-4216-a820-d1fabd25e3f4/TelecomI/Oefenopgave5/Oefenopgave5.1.gif" width="288"></p><h3 id="amplitude-coefficients">Amplitude coefficients</h3><p>Determine the values of the amplitude coefficients <span class="ql-formula" data-value="c_n">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>c</mi><mi>n</mi></msub></mrow><annotation encoding="application/x-tex">c_n</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.58056em; vertical-align: -0.15em;"></span><span class="mord"><span class="mord mathdefault">c</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.151392em;"><span class="" style="top: -2.5500000000000003em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span></span></span></span></span>﻿</span> of the signal spectrum replicas in the sampled signal around the frequencies <span class="ql-formula" data-value="n\cdot f_s">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi><mo>⋅</mo><msub><mi>f</mi><mi>s</mi></msub></mrow><annotation encoding="application/x-tex">n\cdot f_s</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.44445em; vertical-align: 0em;"></span><span class="mord mathdefault">n</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">⋅</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 0.8888799999999999em; vertical-align: -0.19444em;"></span><span class="mord"><span style="margin-right: 0.10764em;" class="mord mathdefault">f</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.151392em;"><span class="" style="top: -2.5500000000000003em; margin-left: -0.10764em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">s</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span></span></span></span></span>﻿</span> for <span class="ql-formula" data-value="n=1,2,3">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi><mo>=</mo><mn>1</mn><mo separator="true">,</mo><mn>2</mn><mo separator="true">,</mo><mn>3</mn></mrow><annotation encoding="application/x-tex">n=1,2,3</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord mathdefault">n</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.8388800000000001em; vertical-align: -0.19444em;"></span><span class="mord">1</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mord">2</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mord">3</span></span></span></span></span>﻿</span>, in case of natural sampling (normal PAM).	</p><p><br></p><p>This can be calculated using <span class="ql-formula" data-value="c_n=d\cdot\sin c\left(\pi\cdot n\cdot d\right)">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>c</mi><mi>n</mi></msub><mo>=</mo><mi>d</mi><mo>⋅</mo><mi>sin</mi><mo>⁡</mo><mi>c</mi><mrow><mo fence="true">(</mo><mi>π</mi><mo>⋅</mo><mi>n</mi><mo>⋅</mo><mi>d</mi><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">c_n=d\cdot\sin c\left(\pi\cdot n\cdot d\right)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.58056em; vertical-align: -0.15em;"></span><span class="mord"><span class="mord mathdefault">c</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.151392em;"><span class="" style="top: -2.5500000000000003em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.69444em; vertical-align: 0em;"></span><span class="mord mathdefault">d</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">⋅</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mop">sin</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mord mathdefault">c</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span style="margin-right: 0.03588em;" class="mord mathdefault">π</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">⋅</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mord mathdefault">n</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">⋅</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mord mathdefault">d</span><span class="mclose delimcenter" style="top: 0em;">)</span></span></span></span></span></span>﻿</span>. with <span class="ql-formula" data-value="d">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>d</mi></mrow><annotation encoding="application/x-tex">d</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.69444em; vertical-align: 0em;"></span><span class="mord mathdefault">d</span></span></span></span></span>﻿</span> being the duty cycle (<span class="ql-formula" data-value="d=...">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>d</mi><mo>=</mo><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">d=...</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.69444em; vertical-align: 0em;"></span><span class="mord mathdefault">d</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.10556em; vertical-align: 0em;"></span><span class="mord">.</span><span class="mord">.</span><span class="mord">.</span></span></span></span></span>﻿</span> <span class="ql-formula" data-value="d=\frac{69.1\cdot10^{-6}}{1/\left(11\cdot10^3\right)}=0.76">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>d</mi><mo>=</mo><mfrac><mrow><mn>69.1</mn><mo>⋅</mo><mn>1</mn><msup><mn>0</mn><mrow><mo>−</mo><mn>6</mn></mrow></msup></mrow><mrow><mn>1</mn><mi mathvariant="normal">/</mi><mrow><mo fence="true">(</mo><mn>11</mn><mo>⋅</mo><mn>1</mn><msup><mn>0</mn><mn>3</mn></msup><mo fence="true">)</mo></mrow></mrow></mfrac><mo>=</mo><mn>0.76</mn></mrow><annotation encoding="application/x-tex">d=\frac{69.1\cdot10^{-6}}{1/\left(11\cdot10^3\right)}=0.76</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.69444em; vertical-align: 0em;"></span><span class="mord mathdefault">d</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 1.53792em; vertical-align: -0.52em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 1.01792em;"><span class="" style="top: -2.655em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">1</span><span class="mord mtight">/</span><span class="minner mtight"><span class="mopen mtight delimcenter" style="top: 0em;"><span class="mtight">(</span></span><span class="mord mtight">1</span><span class="mord mtight">1</span><span class="mbin mtight">⋅</span><span class="mord mtight">1</span><span class="mord mtight"><span class="mord mtight">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.7463142857142857em;"><span class="" style="top: -2.786em; margin-right: 0.07142857142857144em;"><span class="pstrut" style="height: 2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight">3</span></span></span></span></span></span></span></span><span class="mclose mtight delimcenter" style="top: 0em;"><span class="mtight">)</span></span></span></span></span></span><span class="" style="top: -3.23em;"><span class="pstrut" style="height: 3em;"></span><span class="frac-line" style="border-bottom-width: 0.04em;"></span></span><span class="" style="top: -3.394em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">6</span><span class="mord mtight">9</span><span class="mord mtight">.</span><span class="mord mtight">1</span><span class="mbin mtight">⋅</span><span class="mord mtight">1</span><span class="mord mtight"><span class="mord mtight">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.8913142857142857em;"><span class="" style="top: -2.931em; margin-right: 0.07142857142857144em;"><span class="pstrut" style="height: 2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mtight">6</span></span></span></span></span></span></span></span></span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.52em;"><span class=""></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">0</span><span class="mord">.</span><span class="mord">7</span><span class="mord">6</span></span></span></span></span>﻿</span>).</p><p><br></p><p>So <span class="ql-formula" data-value="n=1">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">n=1</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord mathdefault">n</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">1</span></span></span></span></span>﻿</span> yields <span class="ql-formula" data-value="c_1=d\cdot\sin c\left(\pi\cdot1\cdot d\right)=d\cdot\frac{\sin\left(\pi\cdot1\cdot d\right)}{\pi\cdot1\cdot d}=217.9">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>c</mi><mn>1</mn></msub><mo>=</mo><mi>d</mi><mo>⋅</mo><mi>sin</mi><mo>⁡</mo><mi>c</mi><mrow><mo fence="true">(</mo><mi>π</mi><mo>⋅</mo><mn>1</mn><mo>⋅</mo><mi>d</mi><mo fence="true">)</mo></mrow><mo>=</mo><mi>d</mi><mo>⋅</mo><mfrac><mrow><mi>sin</mi><mo>⁡</mo><mrow><mo fence="true">(</mo><mi>π</mi><mo>⋅</mo><mn>1</mn><mo>⋅</mo><mi>d</mi><mo fence="true">)</mo></mrow></mrow><mrow><mi>π</mi><mo>⋅</mo><mn>1</mn><mo>⋅</mo><mi>d</mi></mrow></mfrac><mo>=</mo><mn>217.9</mn></mrow><annotation encoding="application/x-tex">c_1=d\cdot\sin c\left(\pi\cdot1\cdot d\right)=d\cdot\frac{\sin\left(\pi\cdot1\cdot d\right)}{\pi\cdot1\cdot d}=217.9</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.58056em; vertical-align: -0.15em;"></span><span class="mord"><span class="mord mathdefault">c</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.30110799999999993em;"><span class="" style="top: -2.5500000000000003em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.69444em; vertical-align: 0em;"></span><span class="mord mathdefault">d</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">⋅</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mop">sin</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mord mathdefault">c</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span style="margin-right: 0.03588em;" class="mord mathdefault">π</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">⋅</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mord">1</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">⋅</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mord mathdefault">d</span><span class="mclose delimcenter" style="top: 0em;">)</span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.69444em; vertical-align: 0em;"></span><span class="mord mathdefault">d</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">⋅</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 1.355em; vertical-align: -0.345em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 1.01em;"><span class="" style="top: -2.6550000000000002em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span style="margin-right: 0.03588em;" class="mord mathdefault mtight">π</span><span class="mbin mtight">⋅</span><span class="mord mtight">1</span><span class="mbin mtight">⋅</span><span class="mord mathdefault mtight">d</span></span></span></span><span class="" style="top: -3.23em;"><span class="pstrut" style="height: 3em;"></span><span class="frac-line" style="border-bottom-width: 0.04em;"></span></span><span class="" style="top: -3.485em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mop mtight">sin</span><span class="minner mtight"><span class="mopen mtight delimcenter" style="top: 0em;"><span class="mtight">(</span></span><span style="margin-right: 0.03588em;" class="mord mathdefault mtight">π</span><span class="mbin mtight">⋅</span><span class="mord mtight">1</span><span class="mbin mtight">⋅</span><span class="mord mathdefault mtight">d</span><span class="mclose mtight delimcenter" style="top: 0em;"><span class="mtight">)</span></span></span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.345em;"><span class=""></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">2</span><span class="mord">1</span><span class="mord">7</span><span class="mord">.</span><span class="mord">9</span></span></span></span></span>﻿</span>, etc.</p><p><br></p><h3 id="natural-sampling">Natural sampling</h3><p>Natural sampling (normal PAM) is applied to the signal of figure 1 with a sample frequency of&nbsp;<span class="ql-formula" data-value="f_s=15\ kHz">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>f</mi><mi>s</mi></msub><mo>=</mo><mn>15</mn><mtext>&nbsp;</mtext><mi>k</mi><mi>H</mi><mi>z</mi></mrow><annotation encoding="application/x-tex">f_s=15\ kHz</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.8888799999999999em; vertical-align: -0.19444em;"></span><span class="mord"><span style="margin-right: 0.10764em;" class="mord mathdefault">f</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.151392em;"><span class="" style="top: -2.5500000000000003em; margin-left: -0.10764em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">s</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.69444em; vertical-align: 0em;"></span><span class="mord">1</span><span class="mord">5</span><span class="mspace">&nbsp;</span><span style="margin-right: 0.03148em;" class="mord mathdefault">k</span><span style="margin-right: 0.08125em;" class="mord mathdefault">H</span><span style="margin-right: 0.04398em;" class="mord mathdefault">z</span></span></span></span></span>﻿</span> and a sample pulse width <span class="ql-formula" data-value="\tau=20\mu s">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>τ</mi><mo>=</mo><mn>20</mn><mi>μ</mi><mi>s</mi></mrow><annotation encoding="application/x-tex">\tau=20\mu s</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span style="margin-right: 0.1132em;" class="mord mathdefault">τ</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.8388800000000001em; vertical-align: -0.19444em;"></span><span class="mord">2</span><span class="mord">0</span><span class="mord mathdefault">μ</span><span class="mord mathdefault">s</span></span></span></span></span>﻿</span> . Which of the double-sided amplitude spectra (signal value as a function of frequency) of the sampled signal is correct?	</p><p><br></p><p><img src="https://tudelft-exercise.mobius.cloud/web/Ee2t11t005/Public_Html/ImportedQuestions/2ff4cfd4-d7f7-4216-a820-d1fabd25e3f4/TelecomI/Oefenopgave5/Oefenopgave5.1.b.c.gif"></p><p>When you sample regions of this graph, this is what it will look like. </p><p><br></p><h3 id="flat-top-sampling">Flat-top sampling</h3><p>Now flat-top PAM is applied to the signal of figure 1 with a sample frequency of&nbsp;<span class="ql-formula" data-value="f_s=15\ kHz">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>f</mi><mi>s</mi></msub><mo>=</mo><mn>15</mn><mtext>&nbsp;</mtext><mi>k</mi><mi>H</mi><mi>z</mi></mrow><annotation encoding="application/x-tex">f_s=15\ kHz</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.8888799999999999em; vertical-align: -0.19444em;"></span><span class="mord"><span style="margin-right: 0.10764em;" class="mord mathdefault">f</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.151392em;"><span class="" style="top: -2.5500000000000003em; margin-left: -0.10764em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">s</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.69444em; vertical-align: 0em;"></span><span class="mord">1</span><span class="mord">5</span><span class="mspace">&nbsp;</span><span style="margin-right: 0.03148em;" class="mord mathdefault">k</span><span style="margin-right: 0.08125em;" class="mord mathdefault">H</span><span style="margin-right: 0.04398em;" class="mord mathdefault">z</span></span></span></span></span>﻿</span> and a sample pulse width <span class="ql-formula" data-value="\tau=50\mu s">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>τ</mi><mo>=</mo><mn>50</mn><mi>μ</mi><mi>s</mi></mrow><annotation encoding="application/x-tex">\tau=50\mu s</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span style="margin-right: 0.1132em;" class="mord mathdefault">τ</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.8388800000000001em; vertical-align: -0.19444em;"></span><span class="mord">5</span><span class="mord">0</span><span class="mord mathdefault">μ</span><span class="mord mathdefault">s</span></span></span></span></span>﻿</span>. Which of the double-sided amplitude spectra (signal value as a function of frequency) of the sampled signal is correct?</p><p><br></p><p><img src="https://tudelft-exercise.mobius.cloud/web/Ee2t11t005/Public_Html/ImportedQuestions/2ff4cfd4-d7f7-4216-a820-d1fabd25e3f4/TelecomI/Oefenopgave5/Oefenopgave5.1.c.a.gif" width="268"></p><p>This is what you'd get when you fill in the formulas.</p>