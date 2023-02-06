+++
title = "Oscillators (lecture 2 & 3)"
date = 2020-10-14
+++
<h2 id="2.7-&amp;-3.10-oscillators">2.7 &amp; 3.10 Oscillators</h2><p>We need to be able to recognize families of oscillators:</p><p><img src="https://i.imgur.com/oOqus05.png" width="731"></p><p><br></p><p>An oscillator is a circuit that:</p><ul><li>generates a <strong>periodical signal </strong>(a signal that repeats itself from <span class="ql-formula" data-value="-\infty">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>−</mo><mi mathvariant="normal">∞</mi></mrow><annotation encoding="application/x-tex">-\infty</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.66666em; vertical-align: -0.08333em;"></span><span class="mord">−</span><span class="mord">∞</span></span></span></span></span>﻿</span> and <span class="ql-formula" data-value="+\infty">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>+</mo><mi mathvariant="normal">∞</mi></mrow><annotation encoding="application/x-tex">+\infty</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.66666em; vertical-align: -0.08333em;"></span><span class="mord">+</span><span class="mord">∞</span></span></span></span></span>﻿</span>). This means we need a second order differential equations, with at least two dynamic elements.</li><li>which is in the limit <strong>independent of the starting values. </strong>This means we need a non-linear system.</li></ul><p><br></p><p>The mathematical description is: <span class="ql-formula" data-value="\frac{dx^2}{dt^2}+f_1\left(x\right)\frac{dx}{dt}+f_2\left(x\right)=0">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mfrac><mrow><mi>d</mi><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mi>d</mi><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><msub><mi>f</mi><mn>1</mn></msub><mrow><mo fence="true">(</mo><mi>x</mi><mo fence="true">)</mo></mrow><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>+</mo><msub><mi>f</mi><mn>2</mn></msub><mrow><mo fence="true">(</mo><mi>x</mi><mo fence="true">)</mo></mrow><mo>=</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">\frac{dx^2}{dt^2}+f_1\left(x\right)\frac{dx}{dt}+f_2\left(x\right)=0</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1.36292em; vertical-align: -0.345em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 1.01792em;"><span class="" style="top: -2.6550000000000002em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">d</span><span class="mord mtight"><span class="mord mathdefault mtight">t</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.7463142857142857em;"><span class="" style="top: -2.786em; margin-right: 0.07142857142857144em;"><span class="pstrut" style="height: 2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span></span><span class="" style="top: -3.23em;"><span class="pstrut" style="height: 3em;"></span><span class="frac-line" style="border-bottom-width: 0.04em;"></span></span><span class="" style="top: -3.394em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">d</span><span class="mord mtight"><span class="mord mathdefault mtight">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.8913142857142857em;"><span class="" style="top: -2.931em; margin-right: 0.07142857142857144em;"><span class="pstrut" style="height: 2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.345em;"><span class=""></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 1.2251079999999999em; vertical-align: -0.345em;"></span><span class="mord"><span style="margin-right: 0.10764em;" class="mord mathdefault">f</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.30110799999999993em;"><span class="" style="top: -2.5500000000000003em; margin-left: -0.10764em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord mathdefault">x</span><span class="mclose delimcenter" style="top: 0em;">)</span></span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.8801079999999999em;"><span class="" style="top: -2.6550000000000002em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">d</span><span class="mord mathdefault mtight">t</span></span></span></span><span class="" style="top: -3.23em;"><span class="pstrut" style="height: 3em;"></span><span class="frac-line" style="border-bottom-width: 0.04em;"></span></span><span class="" style="top: -3.394em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">d</span><span class="mord mathdefault mtight">x</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.345em;"><span class=""></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mord"><span style="margin-right: 0.10764em;" class="mord mathdefault">f</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.30110799999999993em;"><span class="" style="top: -2.5500000000000003em; margin-left: -0.10764em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord mathdefault">x</span><span class="mclose delimcenter" style="top: 0em;">)</span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">0</span></span></span></span></span>﻿</span></p><p><br></p><h3 id="limit-cycle">Limit cycle</h3><p>A non-linear system means that parameters are changed until a certain amplitude of the solution is reached. Then it will stay at this amplitude and go into a cycle.</p><p><br></p><p>This cycle is a <strong>limit cycle </strong>(a closed loop)<strong>, </strong>which frequency is always the same.</p><p><br></p><p><img src="https://i.imgur.com/2exHkwr.png" width="501"></p><p><br></p><h3 id="questions">Questions</h3><p>When we look at oscillators, we look at:</p><ul><li>What are the dynamic elements?</li><li>What is the order of the system?</li><li>Where is the non-linearity</li><li>How is the frequency determined?</li></ul><p><br></p><h3 id="dynamic-elements">Dynamic elements</h3><p>Some example dynamic elements:</p><ul><li>Capacitors</li><li>Inductors</li><li>Resonators: <span class="ql-formula" data-value="\frac{dx^2}{dt^2}+2\zeta\omega_0\frac{dx}{dt}+\omega_o^2x=0">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mfrac><mrow><mi>d</mi><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mi>d</mi><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mn>2</mn><mi>ζ</mi><msub><mi>ω</mi><mn>0</mn></msub><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>+</mo><msubsup><mi>ω</mi><mi>o</mi><mn>2</mn></msubsup><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">\frac{dx^2}{dt^2}+2\zeta\omega_0\frac{dx}{dt}+\omega_o^2x=0</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1.36292em; vertical-align: -0.345em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 1.01792em;"><span class="" style="top: -2.6550000000000002em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">d</span><span class="mord mtight"><span class="mord mathdefault mtight">t</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.7463142857142857em;"><span class="" style="top: -2.786em; margin-right: 0.07142857142857144em;"><span class="pstrut" style="height: 2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span></span><span class="" style="top: -3.23em;"><span class="pstrut" style="height: 3em;"></span><span class="frac-line" style="border-bottom-width: 0.04em;"></span></span><span class="" style="top: -3.394em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">d</span><span class="mord mtight"><span class="mord mathdefault mtight">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.8913142857142857em;"><span class="" style="top: -2.931em; margin-right: 0.07142857142857144em;"><span class="pstrut" style="height: 2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.345em;"><span class=""></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 1.2251079999999999em; vertical-align: -0.345em;"></span><span class="mord">2</span><span style="margin-right: 0.07378em;" class="mord mathdefault">ζ</span><span class="mord"><span style="margin-right: 0.03588em;" class="mord mathdefault">ω</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.30110799999999993em;"><span class="" style="top: -2.5500000000000003em; margin-left: -0.03588em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.8801079999999999em;"><span class="" style="top: -2.6550000000000002em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">d</span><span class="mord mathdefault mtight">t</span></span></span></span><span class="" style="top: -3.23em;"><span class="pstrut" style="height: 3em;"></span><span class="frac-line" style="border-bottom-width: 0.04em;"></span></span><span class="" style="top: -3.394em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">d</span><span class="mord mathdefault mtight">x</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.345em;"><span class=""></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 1.061108em; vertical-align: -0.247em;"></span><span class="mord"><span style="margin-right: 0.03588em;" class="mord mathdefault">ω</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.8141079999999999em;"><span class="" style="top: -2.4530000000000003em; margin-left: -0.03588em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">o</span></span></span><span class="" style="top: -3.063em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.247em;"><span class=""></span></span></span></span></span></span><span class="mord mathdefault">x</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">0</span></span></span></span></span>﻿</span></li></ul><p><br></p><h3 id="example">Example</h3><p>We can take for example a neon lamp as an example:</p><p><img src="https://i.imgur.com/xmRnrhE.png" width="467"></p><p>To turn it on, you need a certain voltage (say <span class="ql-formula" data-value="70V">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>70</mn><mi>V</mi></mrow><annotation encoding="application/x-tex">70V</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord">7</span><span class="mord">0</span><span style="margin-right: 0.22222em;" class="mord mathdefault">V</span></span></span></span></span>﻿</span>). Once it is on, it will stay on until <span class="ql-formula" data-value="\sim50V">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>∼</mo><mn>50</mn><mi>V</mi></mrow><annotation encoding="application/x-tex">\sim50V</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.36687em; vertical-align: 0em;"></span><span class="mrel">∼</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord">5</span><span class="mord">0</span><span style="margin-right: 0.22222em;" class="mord mathdefault">V</span></span></span></span></span>﻿</span>. This is a dynamic element, since its value depends on the past.</p><p><br></p><p>Now, we are putting a certain voltage through a resistor with high impedance, i.e. it can't deliver much current. When the neon lamp turns on, it needs more current than this resistor can give, so this current is drawn from the capacitor, which is subsequently drained.</p><p><br></p><p>Because of this draining, the voltage of the capacitor goes down and in the end the lamp will turn off again.</p><p><br></p><p>The charging of the capacitor is the most important dynamic element here. And since there is basically only one dynamic element (the others are negligible), this is a <strong>first-order oscillator. </strong></p><p><br></p><h2 id="6.8-6.10-first-order-oscillators">6.8-6.10 First-order oscillators</h2><ul><li>One dominant time constant</li><li><strong>Second</strong> dynamic element only plays a role during transition (e.g. binary memory)</li><li>Tuning is <strong>very easy</strong>, but they are <strong>not very stable</strong> (memory is very noise sensitive: oscillator is noisy)</li><li>Current switching and level detection are separate functions (it is advantageous to orthogonalize them)</li><li>They can lock to anything (tuning signals, noise, resonators, each other)</li></ul>