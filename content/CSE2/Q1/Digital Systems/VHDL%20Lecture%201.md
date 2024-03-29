+++
title = "VHDL Lecture 1"
date = 2019-09-11
+++
<div style="white-space: normal;" class="markdown-body"><h1 id="what-is-vhdl?">What is VHDL?</h1>
<p>VHDL stands for <code>Very High Speed Integrated Circuits Hardware Description language</code>.
It's a <em>hardware modeling language</em>, not a programming language.
The key difference is that you program for concurrent events, while programming languages are sequential.</p>
<h2 id="contains-three-different-parts:">Contains three different parts:</h2>
</div><ul><li>Specification of design:<em> Non-ambiguous definition of functionality, components, and interfaces in a large design.</em></li><li>Simulation of design: <em>Verification of system/subsystem/chip in terms of performance, functionality, etc. before these are implemented.</em></li><li>Synthesis of design: <em>Automatic generation of hardware design.</em></li></ul><p><br></p><div style="white-space: normal;" class="markdown-body"><h2 id="definition-of-words:">Definition of words:</h2>
</div><ul><li>Entry: Give your design a name.</li><li>Port(s): Specify inputs and outputs.</li><li>Architecture: Specify function.</li><li class="ql-indent-1">-&gt; Behavioral: Functional (e.g., ‘a + b’ or ‘a and b’).</li><li class="ql-indent-1">-&gt; Structural: Structural (with components).</li><li>Specify connections (signals) and their values (values) over time.</li><li class="ql-indent-1">-&gt; Event(s): Changes over time.</li><li>Propagation delays: Delays.</li><li>concurrency</li><li>Waveform: Order series of event in time.</li></ul><div style="white-space: normal;" class="markdown-body"><h2 id="entity">Entity</h2>
<p>An entity looks like this:</p>
<pre data-lang="null"><code>entity half_adder is
port (
	a, b: in bit;
	sum, carry: out bit
);
end half_adder
</code></pre>
<p>Or for an full_adder:</p>
<pre data-lang="null"><code>entity full_adder is
port(
	a, b: in bit_vector(7 downto 0);
	cin: in bit;
	sum: out bit_vector(7 downto 0);
	cout: out bit
);
end full_adder
</code></pre>
<p>An entity defines the ports of the gate. Every port is a signal with a type and a mode, as defined below:</p>
<h3 id="types">Types</h3>
<h4><code>bit</code></h4>
<p>Most basic type. Either <code>1</code> or <code>0</code>.</p>
<p>You can define a bit like this:</p>
<pre data-lang="null"><code>port(cin: in bit);
</code></pre>
<h4><code>bit_vector</code></h4>
<p>This is an 'list' of bits. This can be used in for example an adder, where the inputs are 8 bits.</p>
<p>You can define a bit vector like this:</p>
<pre data-lang="null"><code>port(a, b: in bit_vector(7 downto 0)));
</code></pre>
<h3 id="mode">Mode</h3>
<p>There are three different modes a port can be in: <code>in</code>, <code>out</code> and <code>inout</code> (bidirectional). It is defined at the highlighted spot.</p>
<pre data-lang="null"><code>port(cin: *in* bit);
</code></pre>
<h2 id="architecture">Architecture</h2>
<p>The architecture of a entity defines the actual implementation of the gate. The entity are the bones, and the architecture the flesh. Without the architecture the entity does not have content, and without the entity it collapses.
For example, take the following entity for the and-gate:</p>
<pre data-lang="null"><code>entity and_gate is
port(
	a, b: in bit;
	z: out bit
);
end and_gate;
</code></pre>
<p>Now you can use the entity of the and_gate to create the architecture like the following.</p>
<pre data-lang="null"><code>architecture abc of and_gate is
begin
	z &lt;= a and b;
end abc;
</code></pre>
<p>The construct contains of two parts, the declarative region and the architecture body. The declarative region creates signals, components and more, while the architecture body makes a description of the functionality of the entity.</p>
<h3 id="intermediate-signals">Intermediate signals</h3>
<p>Intermediate signals are internal signals, which are not 'exported' or 'imported'. This is used to connect the output of an internal gate to the input of another internal gate. Take this image:</p>
<p><img src="https://i.imgur.com/SHzVXel.png" alt=""></p>
<p>With this entity:</p>
<pre data-lang="null"><code>entity circuit is
port(
	a, b, c: in bit;
	z: out bit
);
end circuit;
</code></pre>
<p>You can see that the intermediate signals have been marked already. Your first instinct might be to write something like this:</p>
<pre data-lang="null"><code>architecture abc of circuit is
begin
	z &lt;= (a and b) or (not b and c);
end abc;
</code></pre>
<p>This works, but is not really efficient. It's better to write it like this.</p>
<pre data-lang="null"><code>architecture abc of circuit is
signal s1, s2, s3: bit;
begin
	s1 &lt;= not b;
	s2 &lt;= a and b;
	s3 &lt;= s1 and c;
	z  &lt;= s2 or s3;
end abc;
</code></pre>
<p>Just don't forget to define the signals first in the declarative region.</p>
<h3 id="timing">Timing</h3>
<p>Timing is really important, and you can define this in the architecture like this.</p>
<pre data-lang="null"><code>architecture half_adder_arch of half_adder
begin
	carry &lt;= a and b after 5ns;
	sum	&lt;= a xor b after 5ns;
end half_adder_arch
</code></pre>
<p>Take note of the after statement. For the carry this means that the action will be ran 5ns <strong>after a or b changes</strong>. In this case it means when a or b changes, both the carry and the sum will change (if required) after 5 ns at the same time. If before that time the change gets undone (for example a gets pulled down again), then the action is not fired. This means there will be no new event created for carry or sum.</p>
</div>