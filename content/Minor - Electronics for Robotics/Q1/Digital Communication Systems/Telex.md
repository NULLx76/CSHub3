+++
title = "Telex"
date = 2020-09-01
+++
<p><strong>Question</strong></p><p>A telex machine can generate 26 letters + 6 special characters. The source-encoder generates the equivalent bit stream.</p><p><br></p><p>What is the bit rate of this system in case we send 10 char/s, and assuming that the symbols are equally-likely?</p><p><br></p><p><strong>Answer</strong></p><p>We have 32 symbols, each symbol contains <span class="ql-formula" data-value="\log_232=5">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>log</mi><mo>⁡</mo><mn>2</mn></msub><mn>32</mn><mo>=</mo><mn>5</mn></mrow><annotation encoding="application/x-tex">\log_232=5</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.93858em; vertical-align: -0.24414em;"></span><span class="mop"><span class="mop">lo<span style="margin-right: 0.01389em;">g</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.20696799999999996em;"><span class="" style="top: -2.4558600000000004em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.24414em;"><span class=""></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mord">3</span><span class="mord">2</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">5</span></span></span></span></span>﻿</span> bits of information per symbol (since they are equally likely). If we can send 10 chars per second, <span class="ql-formula" data-value="T=100ms">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>T</mi><mo>=</mo><mn>100</mn><mi>m</mi><mi>s</mi></mrow><annotation encoding="application/x-tex">T=100ms</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.13889em;" class="mord mathdefault">T</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">1</span><span class="mord">0</span><span class="mord">0</span><span class="mord mathdefault">m</span><span class="mord mathdefault">s</span></span></span></span></span>﻿</span>.</p><p><br></p><p>This yields the source rate of <span class="ql-formula" data-value="R=\frac{H}{T}=\frac{1}{T}\left(\sum_{j=1}^{32}-P_j\log_2P_j\right)=10\left(\sum_{j=1}^{32}\frac{5}{32}\right)">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>=</mo><mfrac><mi>H</mi><mi>T</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>T</mi></mfrac><mrow><mo fence="true">(</mo><msubsup><mo>∑</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mn>32</mn></msubsup><mo>−</mo><msub><mi>P</mi><mi>j</mi></msub><msub><mi>log</mi><mo>⁡</mo><mn>2</mn></msub><msub><mi>P</mi><mi>j</mi></msub><mo fence="true">)</mo></mrow><mo>=</mo><mn>10</mn><mrow><mo fence="true">(</mo><msubsup><mo>∑</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mn>32</mn></msubsup><mfrac><mn>5</mn><mn>32</mn></mfrac><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">R=\frac{H}{T}=\frac{1}{T}\left(\sum_{j=1}^{32}-P_j\log_2P_j\right)=10\left(\sum_{j=1}^{32}\frac{5}{32}\right)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.00773em;" class="mord mathdefault">R</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 1.217331em; vertical-align: -0.345em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.872331em;"><span class="" style="top: -2.6550000000000002em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span style="margin-right: 0.13889em;" class="mord mathdefault mtight">T</span></span></span></span><span class="" style="top: -3.23em;"><span class="pstrut" style="height: 3em;"></span><span class="frac-line" style="border-bottom-width: 0.04em;"></span></span><span class="" style="top: -3.394em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span style="margin-right: 0.08125em;" class="mord mathdefault mtight">H</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.345em;"><span class=""></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 1.80002em; vertical-align: -0.65002em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.845108em;"><span class="" style="top: -2.6550000000000002em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span style="margin-right: 0.13889em;" class="mord mathdefault mtight">T</span></span></span></span><span class="" style="top: -3.23em;"><span class="pstrut" style="height: 3em;"></span><span class="frac-line" style="border-bottom-width: 0.04em;"></span></span><span class="" style="top: -3.394em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">1</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.345em;"><span class=""></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;"><span class="delimsizing size2">(</span></span><span class="mop"><span class="mop op-symbol small-op" style="position: relative; top: -0.0000050000000000050004em;">∑</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.954008em;"><span class="" style="top: -2.40029em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span style="margin-right: 0.05724em;" class="mord mathdefault mtight">j</span><span class="mrel mtight">=</span><span class="mord mtight">1</span></span></span></span><span class="" style="top: -3.2029em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">3</span><span class="mord mtight">2</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.43581800000000004em;"><span class=""></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mord">−</span><span class="mord"><span style="margin-right: 0.13889em;" class="mord mathdefault">P</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.311664em;"><span class="" style="top: -2.5500000000000003em; margin-left: -0.13889em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span style="margin-right: 0.05724em;" class="mord mathdefault mtight">j</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.286108em;"><span class=""></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mop"><span class="mop">lo<span style="margin-right: 0.01389em;">g</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.20696799999999996em;"><span class="" style="top: -2.4558600000000004em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.24414em;"><span class=""></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mord"><span style="margin-right: 0.13889em;" class="mord mathdefault">P</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.311664em;"><span class="" style="top: -2.5500000000000003em; margin-left: -0.13889em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span style="margin-right: 0.05724em;" class="mord mathdefault mtight">j</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.286108em;"><span class=""></span></span></span></span></span></span><span class="mclose delimcenter" style="top: 0em;"><span class="delimsizing size2">)</span></span></span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 1.80002em; vertical-align: -0.65002em;"></span><span class="mord">1</span><span class="mord">0</span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;"><span class="delimsizing size2">(</span></span><span class="mop"><span class="mop op-symbol small-op" style="position: relative; top: -0.0000050000000000050004em;">∑</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.954008em;"><span class="" style="top: -2.40029em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span style="margin-right: 0.05724em;" class="mord mathdefault mtight">j</span><span class="mrel mtight">=</span><span class="mord mtight">1</span></span></span></span><span class="" style="top: -3.2029em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">3</span><span class="mord mtight">2</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.43581800000000004em;"><span class=""></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.16666666666666666em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.845108em;"><span class="" style="top: -2.6550000000000002em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">3</span><span class="mord mtight">2</span></span></span></span><span class="" style="top: -3.23em;"><span class="pstrut" style="height: 3em;"></span><span class="frac-line" style="border-bottom-width: 0.04em;"></span></span><span class="" style="top: -3.394em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">5</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.345em;"><span class=""></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mclose delimcenter" style="top: 0em;"><span class="delimsizing size2">)</span></span></span></span></span></span></span>﻿</span><span class="ql-formula" data-value="=10">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>=</mo><mn>10</mn></mrow><annotation encoding="application/x-tex">=10</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.36687em; vertical-align: 0em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">1</span><span class="mord">0</span></span></span></span></span>﻿</span> symbols of 5 bits each<span class="ql-formula" data-value="=50\ \frac{bit}{s}">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>=</mo><mn>50</mn><mtext>&nbsp;</mtext><mfrac><mrow><mi>b</mi><mi>i</mi><mi>t</mi></mrow><mi>s</mi></mfrac></mrow><annotation encoding="application/x-tex">=50\ \frac{bit}{s}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.36687em; vertical-align: 0em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 1.2251079999999999em; vertical-align: -0.345em;"></span><span class="mord">5</span><span class="mord">0</span><span class="mspace">&nbsp;</span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.8801079999999999em;"><span class="" style="top: -2.6550000000000002em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">s</span></span></span></span><span class="" style="top: -3.23em;"><span class="pstrut" style="height: 3em;"></span><span class="frac-line" style="border-bottom-width: 0.04em;"></span></span><span class="" style="top: -3.394em;"><span class="pstrut" style="height: 3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">b</span><span class="mord mathdefault mtight">i</span><span class="mord mathdefault mtight">t</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.345em;"><span class=""></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span></span>﻿</span> </p>