+++
title = "Lecture 1 - Introduction"
date = 2019-09-20
+++
<h1 id="introduction">Introduction</h1><h2 id="analog-vs-digital-systems">Analog vs digital systems</h2><p>Analog systems have continuous input and output.</p><p>Digital systems have discrete input and output, which can jump between values. We also have discrete time. (I/O only change at certain time intervals)</p><p><br></p><p>Advantages of digital systems:</p><ul><li>Less sensitive to noise</li><li>We can easily exchange speed and amount of hardware</li></ul><p><br></p><p>We can use converters to change between Analog and Digital:</p><ul><li>ADC = Analog to Digital Converter</li><li>DAC = Digital to Analog Converter</li></ul><p><br></p><h2 id="combinational-vs-sequential-systems">Combinational vs Sequential systems</h2><p>Combinational systems only depend on the previous output, not the entire past, there is no memory.</p><p>Sequential systems depend on multiple (or all) previous outputs, memory is required.</p><p><br></p><h2 id="specification,-implementation,-analysis,-design">Specification, Implementation, Analysis, Design</h2><p>We can Design a Specification, in order to end up with an Implementation</p><p>We can Analyse an Implementation, in order to end up with the Specification</p><p><img src="https://lh6.googleusercontent.com/SzWF3kA9lHxhoVs05c3yMfuQdJ4Ek3gvHR_2LaL8zEFeG56S5wPAKtSckaFJNQazcEptKXA-B7vB3fqbKh68OGctjsHgyQdCzQL5M_pnWMXd0dlEOTRyTcNo7xU9-HZ1UX5hWKsy" width="339"></p><p><em>Image taken from slides by Stephan Wong &amp; Carmina Almudever</em></p><p><br></p><h2 id="computer-aided-design-(cad)-tools">Computer-Aided Design (CAD) tools</h2><p>Automated synthesis and optimization.</p><p>Simulation tools generate behaviour of a system for a given input</p><p><br></p><h1 id="combinational-systems">Combinational Systems</h1><p>We are trying to implement a function of F using a combinational system</p><p>The input is coded to binary, then transformed from input to output using some combinational system, then decoded to analog.</p><p>The underscore underneath the x and z, means that x and z are vectors of bits.</p><p><br></p><p><img src="https://lh4.googleusercontent.com/xd7MWw7K3YmBdkI8iqloKGvWSXzd3CD-HBTSDsiOpu2DZGNkyM694HeVBSQ9ZRvmZojnZ-Ipa1_lpief2nmGMDOW-sny6xyrlRIjC27d8zBwvE_qgzA2jk41si-NAhIEaZ27xP2I" alt="https://lh4.googleusercontent.com/xd7MWw7K3YmBdkI8iqloKGvWSXzd3CD-HBTSDsiOpu2DZGNkyM694HeVBSQ9ZRvmZojnZ-Ipa1_lpief2nmGMDOW-sny6xyrlRIjC27d8zBwvE_qgzA2jk41si-NAhIEaZ27xP2I" width="545"></p><p><em>Image taken from slides by Stephan Wong &amp; Carmina Almudever</em></p><p><br></p><h2 id="example">Example</h2><p>We define sets x and z, which are all possible values that the input and output can take. We then define a binary representation for each of these values, and then define the function that maps the values between the input and output, in this case using a table.</p><p><span style="background-color: transparent; color: rgb(0, 0, 0);"><img src="https://lh5.googleusercontent.com/gR7oCec5ljvMY1VvqzD2R4mmdP-FaINv_KWMevVMdH4WYgugpuHuVLbn7RwdLKuyUfB5dNkVZV4LWoYHh3u9U7BNCvVjE60h8k0C_Sa_XdJsiqLM46TXwg0xdqLcVcyWIRuhOiEc" height="341" width="537"></span></p><p><em>Image taken from slides by Stephan Wong &amp; Carmina Almudever</em></p><p><br></p><h2 id="input-output-function-representation">Input-output function representation</h2><p>These are some ways to represent input-output functions:</p><ul><li>Table</li><li>Arithmetic expression</li><li>Conditional expression&nbsp;</li><li>Logical expression</li><li>Composition of simpler functions</li></ul>