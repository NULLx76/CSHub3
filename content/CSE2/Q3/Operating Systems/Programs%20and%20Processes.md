+++
title = "Programs and Processes"
date = 2020-02-25
+++
<div style="white-space: normal;" class="markdown-body"><h1 id="elf/program">Elf/Program</h1>
<p>ELF Layout: &lt;insert slide pic&gt;</p>
<p>ELF loading:</p>
<p>allocate sections
copy data sections from disk to ram
jump to a well known entry point.</p>
<h1 id="process">Process</h1>
<p>A process is a program during execution.</p>
<h2 id="process-life-cycle">Process Life cycle</h2>
<ul>
<li>Ready</li>
<li>Running</li>
<li>Blocked</li>
</ul>
<p>On IO: ready process --&gt; blocked, another ready process --&gt; running</p>
<h2 id="process-state">process state</h2>
<ul>
<li>Execution state
<ul>
<li>Registers</li>
<li>memory pages</li>
<li>open file descriptors</li>
<li>... add more?</li>
</ul>
</li>
<li>General state
<ul>
<li>process ID</li>
<li>Priority</li>
<li>.... add more</li>
</ul>
</li>
</ul>
<h2 id="process-manipulation">Process Manipulation</h2>
<h3 id="fork-(bomb)">Fork (bomb)</h3>
<p><code>:(){:|: &amp;};:</code></p>
<p>Clones a process. Both processes continue get the same instruction pointer so both execute the same next instruction.t</p>
<h3 id="wait">Wait</h3>
<p>Blocks until a child process terminates. The return code of this process is returned from the wait call.</p>
<p>One can wait for a specific pid to exit with <code>waitpid()</code></p>
<h3 id="exec">Exec</h3>
<p>Replaces the currently running process with a new process, specified through the shell command given as parameter.</p>
<p><em>Note</em>: Kills the old process</p>
<h3 id="exit">Exit</h3>
<p>yeets the process out of the window</p>
<h3 id="kill">Kill</h3>
<p>Sends a signal to a process.</p>
<h3 id="scheduling-of-tasks">Scheduling of tasks</h3>
<p><em><strong>THIS WILL BE ON THE EXAM</strong></em>
Response time/latency:
The time between the arrival of a task and when it's finished completely. This means that when multiple tasks arrive at the same time, the response time of a later-scheduled tasks <em>does</em> include the time it took to run the earlier-scheduled tasks.</p>
<p>examples from the slides:</p>
<p>example 1: p1=1, p2=6, p3=8 avg=15/3=5
example 2: p1=1, p2=3, p3=8 avg=13/3=4</p>
<p>Throughput:
Rate of tasks completed per time unit.</p>
<p>Fairness:</p>
</div>