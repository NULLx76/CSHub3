+++
title = "Introduction to C++"
date = 2019-09-10
+++
<h1 id="about-c++">About C++</h1><h3 id="what-is-c++?">What is C++?</h3><p>C++ is a language set to improve C, mostly by adding class support. </p><p><br></p><p><strong>What makes C++ different to Java?</strong></p><p>C++ focuses on performance, efficiency and flexibility. C++ makes it possible to program low level and high level in one language.</p><p><br></p><p>There are a few advantages of C++ to Java:</p><ul><li><strong>Memory management:</strong> the programmer can control how memory is utilized</li><li><strong>Run-time Error Detection:</strong> the programmer is responsible for checking errors at run-time</li><li><strong>Type and Program Structure Enforcement:</strong> the programmer can choose to violate the class and type structure</li></ul><p><br></p><h1 id="guide-to-c++">Guide to C++</h1><h2 id="organization">Organization</h2><p>C++ makes use of header files (.h or .hpp):</p><ul><li>Function &amp; method declarations (but you don't have to implement it!)</li><li>Inform compiler about arguments and type returns of functions</li></ul><p><br></p><p>and class files (.cpp):</p><ul><li>Function &amp; method definitions</li><li>Responsible for implementation and logic</li><li>Can import system repository dependencies (dependencies which. are in the standard library) with <em>#include &lt;content&gt;</em></li><li>Can import local dependencies (local files) with <em>#include "content"</em></li></ul><p><br></p><p>The reason we use header files is so that the compiler doesn't have to go through all the class files. This is a big performance win</p><p><br></p><p>Some remarks:</p><ul><li>Only one class file can have the main method</li><li>Always use forward slashes in files</li><li>The name of the library and the name you use to refer to it in code doesn't have to be the same</li><li>Header files may only be imported once! If you don't, you might cause recursive imports. In order to tackle this, you can use <em>#ifndef 'Name'</em>, then the compiler will make sure it wont import it the second time. The name is an arbitrary name.</li></ul><h3 id=""><br></h3><h3 id="examples">Examples</h3><p><strong>bank.hpp</strong></p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-c++src"><code>int amount;
int limit;
int balance;
int deposit(int amount);
</code></pre>
</div><p><br></p><p><strong>bank.cpp</strong></p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-c++src"><code>#include "bank.hpp"
 
int deposit (int amount) {
	if (amount &lt;= limit)
		balance -= amount;
	return balance;
}
</code></pre>
</div><p><br></p><h3 id="namespace">Namespace</h3><p>It is possible to group a number of classes, objects and methods within a namespace. This is commonly used when importing libraries and external dependencies:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-c++src"><code>namespace foo
{
	int var = 50;
}
 
namespace bar
{
	int var = 42;
}
 
foo::var --&gt; 50
bar::var --&gt; 42
</code></pre>
</div><p><br></p><h2 id="input/output">Input/output</h2><p>Input and output is handled by a library called <strong>iostream. </strong>Example:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-c++src"><code>std::cout &lt;&lt; "Output" &lt;&lt; std::endl; // It prints "Output", pushing the content to the output stream
 
string userInput; // use #include &lt;string&gt;
std::cin &gt;&gt; userInput; // Pushing the input stream into a variable
</code></pre>
</div><p><br></p><h2 id="objects-and-methods">Objects and methods</h2><p>In the header files, classes and objects are defined,<strong> e.g</strong></p><p><br></p><p><strong>Test.hpp</strong></p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-c++src"><code>class Example {
	public:
		int example();
		void change(int est);
	protected:
		// Nothing
	private:
		int value;
}; // &lt;-- semicolon is required
</code></pre>
</div><p><br></p><p><strong>Test.cpp</strong></p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-c++src"><code>...
Example::example() {
	// Stuff
}
 
Example::~example() {
	// Do destructor stuff, if nothing to do, leave empty
}
...
</code></pre>
</div><p><br></p><p>As you see, the constructor name is the same as the class name (though lower case). The constructor of a class is called automatically, no need to call the constructor using <strong>new </strong>or similar.</p><p><br></p><p>C++ also has destructors, which are used to destroy objects for memory management. In this destructor you are supposed to free all the memory used in this class. But, when writing proper C++ you shouldn't have to write a destructor.</p><p><br></p><h3 id="common-pitfalls">Common pitfalls</h3><h3 id="pointers">Pointers</h3><p>Referencing refers to how variables and objects can be found and used in memory. This can be done for you automatically, which is the safest and easiest. You can also call the constructor and destructor manualxt</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-c++src"><code>void function() {
	Object* obj = new Object();
	...
	delete obj;
}
</code></pre>
</div><p>The * is a pointer, which is a variable that points to something (variable or method). This prevents the variable or methods to be passed around. Note that pointers are a big source of memory leaks.</p><p><br></p><h3 id="references">References</h3><p>A reference directly passes an object in a more efficient manner. This allows you to access and change variables you get passed into a method. A reference is notated by &amp;. Use a reference if possible.</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-c++src"><code>void function(int&amp; test){
	test = 3
}
 
int testIn = 3;
function(testIn)
 
testIn --&gt; 3
</code></pre>
</div><p><br></p><h3 id="references-vs-pointers-vs-value">References vs pointers vs value</h3><div style="white-space: normal;" class="markdown-body"><table>
<thead>
<tr>
<th>Type of reference</th>
<th>Functionality</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Call-by-value (direct variable passing), <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>X</mi></mrow><annotation encoding="application/x-tex">X</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathdefault" style="margin-right:0.07847em;">X</span></span></span></span></td>
<td>Copy of the variable is created, which can be used as a new variable</td>
<td>If you make change to the copy, the original variable will not be affected</td>
</tr>
<tr>
<td>Call-by-reference, &amp;X</td>
<td>Variable is directly referenced, the changes affect the original variable</td>
<td>Be careful with concurrent accessing. Does not accept NULL references</td>
</tr>
<tr>
<td>Call-by-pointer, <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo>∗</mo><mi>X</mi></mrow><annotation encoding="application/x-tex">*X</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord">∗</span><span class="mord mathdefault" style="margin-right:0.07847em;">X</span></span></span></span></td>
<td>A location in memory is pointed to, difficult to change content</td>
<td>Requires manual deletion, avoid if possible</td>
</tr>
</tbody>
</table>
</div><p><br></p><h3 id="arrays">Arrays</h3><p>In C++, arrays are static in size with manual memory deallocation. If we want growing arrays, we can use the Vector implementation, which handles all memory and size-related aspects.</p><p><br></p><p>Example:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-c++src"><code>#include &lt;vector&gt;
vector&lt;int&gt; foo;
foo.push_back(42);
</code></pre>
</div><p><br></p><p>Notes:</p><ul><li>Never use a variable to declare the size of an array or vector, as different compilers treat it differently</li><li>In a normal array, out-of-bounds exceptions aren't caught for you</li></ul><p><br></p><h3 id="static">Static</h3><p>The static keyword allows you to share variables within a class across all instances and can be accessed by accessing any instance of the class.</p><p><br></p><h3 id="operators">Operators</h3><p>It is possible to redefine operators on a class basis. This allows us to  for example override <span class="ql-formula" data-value="+">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>+</mo></mrow><annotation encoding="application/x-tex">+</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.66666em; vertical-align: -0.08333em;"></span><span class="mord">+</span></span></span></span></span>﻿</span>, by defining this in the header file and implementing it in the cpp file:</p><p><br></p><p><strong>Vector2D.hpp</strong></p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-c++src"><code>class Vector2D {
	// We return a Vector2D&amp;, use the "operator" keyword
	// The operator to override is +=, which takes a constant other Vector2D&amp;
	Vector2D&amp; operator +=(const Vector2D&amp; other)
}
</code></pre>
</div><p><br></p><p><strong>Vector2D.cpp</strong></p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-c++src"><code>class Vector2D {
	...
	Vector2D&amp; Vector2D::operator+=(const Vector2D&amp; other) {
		this.X += other.x;
		this.Y += other.y;
		return *this;
	}
}
</code></pre>
</div><h3 id=""><br></h3><h3 id="new">New</h3><p>We can use the <strong>new </strong>keyword to create new object, but this returns a pointer. Thus it is recommended not to do it.</p>