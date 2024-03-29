+++
title = "Unix"
date = 2019-09-18
+++
<p><a href="http://gousios.org/courses/bigdata/ds-cmd-line.html" target="_blank" style="background-color: rgb(255, 255, 255);"><em>The slides are very useful and this is basically just a documentation lecture. Thus this post will only describe things that aren't in the slides but are mentioned in the lectures</em></a></p><p><br></p><h2 id="data-engineering-pipeline:">Data engineering pipeline:</h2><ul><li><strong>Extract / generate: </strong>retrieve the data</li><li><strong>Select:</strong> filter the data to what you want</li><li><strong>Process:</strong> process the data into your format</li><li><strong>Summarize:</strong> aggregation</li><li><strong>Plumb:</strong> outputting in the desired way</li></ul><p><br></p><h2 id="commands-not-mentioned-in-slides">Commands not mentioned in slides</h2><h3 id="git">Git</h3><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>git blame</code>- shows which users have changed a certain line in a file</li>
<li><code>git log</code>- shows a list of commits and their authors</li>
</ul>
</div><p><br></p><h3 id="processing">Processing</h3><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>awk</code>- run commands on lines that match expression, e.g.:
<ul>
<li><code>ls -l | awk '$5 &gt; 10000 {print $5}'</code>- lists files in a directory and if the 5th field is larger than <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>10000</mn></mrow><annotation encoding="application/x-tex">10000</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.64444em;vertical-align:0em;"></span><span class="mord">1</span><span class="mord">0</span><span class="mord">0</span><span class="mord">0</span><span class="mord">0</span></span></span></span>, it prints that value</li>
<li><code>-F:</code>- specifies the delimiter (standard space)</li>
</ul>
</li>
<li><code>sed</code>- transform data, e.g.
<ul>
<li><code>sed s/if(/if (/</code>- replaces if( by if (</li>
<li><code>sed /SCCS/d</code>- delete SCCS</li>
</ul>
</li>
</ul>
</div><p><br></p><h3 id="various">Various</h3><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>ar</code>- create, modifies and extracts from archives</li>
<li><code>tar</code> / <code>jar</code>- archives files to a single file</li>
<li><code>ldd</code>- prints shared libraries used by each program</li>
<li><code>comm</code>- compares two files line by line, creates 3 column output</li>
</ul>
</div>