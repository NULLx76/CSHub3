+++
title = "Abstract, Lexical and Concrete syntax"
date = 2021-09-03
+++
<div style="white-space: normal;" class="markdown-body"><h1 id="summary-of-lecture-1-(friday-september-3rd)">Summary of lecture 1 (Friday September 3rd)</h1>
<h1 id="syntax">Syntax</h1>
<ul>
<li>Linguistics: set of rules associated with a language, defining word order and punctuation</li>
<li>Maths: rules governing the behavior of mathematical systems like formal logic</li>
<li>Greek: syn-taxis "ordering together"</li>
<li>Programming languages: the set of rules that define which combinations of symbols are considered correct. This is also true for markup languages. It's all about <strong>structure</strong>.</li>
</ul>
<h2 id="syntactic-categories">Syntactic categories</h2>
<ul>
<li>program</li>
<li>function</li>
<li>statement</li>
<li>expression</li>
<li>type</li>
<li>etc.</li>
</ul>
<p>Categories are ordered in some way (defined by the syntax rules). Some categories are valid in some places and not in others.
Categories may have multiple "elements". For instance, expressions may look different in different parts of the program.</p>
<h2 id="decomposition-of-programs-into-its-elements">Decomposition of programs into its elements</h2>
<p>In general, this can be done by building a tree representing the program. This tree is called the <em>abstract syntax tree</em>. Parts of this tree are sometimes called terms. Programs are transformed from a textual to a structural representation.</p>
<p>See: <a href="https://craftinginterpreters.com/representing-code.html">Syntax trees</a></p>
<h2 id="defining-syntax-in-sdf">Defining syntax in SDF</h2>
<ul>
<li>sorts: syntactic categories. "like sum types in haskell"</li>
<li>constructors: rules combining sorts and returning a new sort "like variant constructors in haskell"</li>
</ul>
<p>TODO: image from slides with title "Well-Formed Terms: Example"</p>
<h1 id="concrete-syntax">Concrete syntax</h1>
<p>Abstract syntax is a simplifaction, but concrete syntax adds superfluous notation like parentheses, braces, colons, semicolons, commas, etc. To define this concrete syntax, a context-free grammar can be used.</p>
<h3 id="context-free-grammars">Context free grammars</h3>
<ul>
<li>non-terminals (correspond to syntactic categories)</li>
<li>terminals (parts of sentences, like keywords or symbols; leaves on the AST)</li>
<li>productions (rules to combine terminals and/or non-terminals)</li>
</ul>
<p>If a sentence is valid within a grammar, the sentence is <em>well-formed</em>
The set of all well-formed sentences is called the Language of the grammar G: <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>L</mi><mo stretchy="false">(</mo><mi>G</mi><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">L(G)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathdefault">L</span><span class="mopen">(</span><span class="mord mathdefault">G</span><span class="mclose">)</span></span></span></span></p>
<p>TODO: add grammar images from lecture slide with title "what is teh relation between concrete and abstract syntax"</p>
<p>It is possible to rewrite grammars to remove ambiguity. But instead you can use disambiguation rules (TODO: link to lecture of next week)</p>
<h2 id="sdf">SDF</h2>
<p>In SDF it's possible to derive both abstract and concrete syntax definitions from one definition. Combining this way can simplify the process of creating a language, but it becomes impossible to have multiple concrete syntaxes associated with a single abstract syntax. "you lose some abstraction".</p>
<p>(TODO: Add image from lecture slide titled "Context free grammars with constructor declarations")</p>
<p>rewrite rules can be used to create a simpler syntax tree removing for example superfluous recursion in the grammar (simplifying to for example a list).</p>
<h1 id="lexical-syntax">Lexical syntax</h1>
<p>Tokens (or lexemes) are the words that programs consists of. For example "if" or "for". Tokens are separated by layout: spaces and punctuation. Lexical syntax can be defined using character classes and sequences of them. These form the leaves (terminals) of the syntax definition. Character classes can be ranges of character codes or letters. Sequences of character classes/codes (or strings) define tokens.</p>
<p>An "Injection" means a context free symbol which is equal to a lexical symbol.</p>
<h2 id="lexical-ambiguity">Lexical ambiguity</h2>
<p>for example: haskell's curried function calls: does "A B" mean a variable called "A B" or is "A" a function called with "B". In SDF "lexical restrictions" can define rules that forbid certain tokens being followed by others. This is called a "longest match disambiguation".
See: <a href="https://en.cppreference.com/w/cpp/language/translation_phases">C++'s "Maximal Munch rule"</a></p>
</div>