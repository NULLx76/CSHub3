+++
title = "Haskell Basics"
date = 2021-02-16
+++
<h1 id="types">Types</h1><p>A type is a name for a collection of values.</p><p><br></p><p><code>Bool</code> has two values <code>True</code> and <code>False</code>.</p><p><br></p><div style="white-space: normal;" class="markdown-body"><pre data-lang="haskell"><code>data Bool = True | False
</code></pre>
</div><p><br></p><p>The compiler will try to infer the type if it is not given. It's still recommended to give everything explicit types.</p><h2 id=""><br></h2><h2 id="list-type">List Type</h2><p>In general, <span class="ql-formula" data-value="\left[t\right]">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo fence="true">[</mo><mi>t</mi><mo fence="true">]</mo></mrow><annotation encoding="application/x-tex">\left[t\right]</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">[</span><span class="mord mathdefault">t</span><span class="mclose delimcenter" style="top: 0em;">]</span></span></span></span></span></span>﻿</span> , is the type of lists with the elements of type <span class="ql-formula" data-value="t">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>t</mi></mrow><annotation encoding="application/x-tex">t</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.61508em; vertical-align: 0em;"></span><span class="mord mathdefault">t</span></span></span></span></span>﻿</span>.</p><p>Lists can also be nested freely in <span class="ql-formula" data-value="\left[\left[t\right]\right]">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo fence="true">[</mo><mrow><mo fence="true">[</mo><mi>t</mi><mo fence="true">]</mo></mrow><mo fence="true">]</mo></mrow><annotation encoding="application/x-tex">\left[\left[t\right]\right]</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">[</span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">[</span><span class="mord mathdefault">t</span><span class="mclose delimcenter" style="top: 0em;">]</span></span><span class="mclose delimcenter" style="top: 0em;">]</span></span></span></span></span></span>﻿</span> </p><div style="white-space: normal;" class="markdown-body"><pre data-lang="haskell"><code>[1,2,3] :: [Int]
[True,False] :: [Bool]
[[1], [1,2], [1,2,3]] :: [[Int]]
</code></pre>
</div><p><br></p><p><br></p><div style="white-space: normal;" class="markdown-body"><p><em><strong>(Additional note)</strong></em></p>
</div><div style="white-space: normal;" class="markdown-body"><p>It's also worth noting that the internal representation of lists is lisp-like, that is to say all Haskell lists are linked lists ending with the specials "empty list", this is clear when using the cons operator (<code>:</code>) like so</p>
<pre data-lang="haskell"><code>&gt; 1 : (2 : (3 : (4 : [])))
[1,2,3,4]
</code></pre>
<p>This does mean that operations like <code>length</code> are <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="script">O</mi><mo stretchy="false">(</mo><mi>n</mi><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">\mathcal{O}(n)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord"><span class="mord mathcal" style="margin-right:0.02778em;">O</span></span><span class="mopen">(</span><span class="mord mathdefault">n</span><span class="mclose">)</span></span></span></span></p>
</div><p><br></p><p><br></p><h2 id="strings-as-lists">Strings as lists</h2><p>Strings are just defined as an list of characters.</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="haskell"><code>type String = [Char]
['a', 'b', 'c'] == "abc"
</code></pre>
</div><p><br></p><h2 id="ranges">Ranges</h2><p>Ranges are the most simple case of list comprehension.</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="haskell"><code>&gt; [1..10]
[1,2,3,4,5,6,7,8,9,10]
&gt; [42..42]
[42]
&gt; [10..1]
[]
&gt; [10, 9 .. 1]
[10,9,8,7,6,5,4,3,2,1]
&gt; ['a'..'z']
"abcdefghijklmnopqrstuvwxyz"
</code></pre>
</div><p><br></p><h2 id="tuple-types">Tuple Types</h2><p>Tuples are a Type that can combine other different types. It can be used as a replacement for structs.</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="haskell"><code>(42, True) :: (Int, Bool)
('x', 'y', 'z') :: (Char, Char, Char)
(('a', 1.0), [7,8,9]) :: ((Char, Float), [Int])
</code></pre>
<p>In general <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo stretchy="false">(</mo><msub><mi>t</mi><mn>1</mn></msub><mo separator="true">,</mo><msub><mi>t</mi><mn>2</mn></msub><mo separator="true">,</mo><mo>…</mo><mo separator="true">,</mo><msub><mi>t</mi><mi>n</mi></msub><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">(t_1,t_2,\dots,t_n)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathdefault">t</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord"><span class="mord mathdefault">t</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="minner">…</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord"><span class="mord mathdefault">t</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span> is the type of tuples <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo stretchy="false">(</mo><msub><mi>x</mi><mn>1</mn></msub><mo separator="true">,</mo><msub><mi>x</mi><mn>2</mn></msub><mo separator="true">,</mo><mo>…</mo><mo separator="true">,</mo><msub><mi>x</mi><mi>n</mi></msub><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">(x_1,x_2, \dots, x_n)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathdefault">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord"><span class="mord mathdefault">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="minner">…</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord"><span class="mord mathdefault">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span> where <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>:</mo><mo>:</mo><msub><mi>t</mi><mn>1</mn></msub></mrow><annotation encoding="application/x-tex">x_1 :: t_1</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.58056em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathdefault">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">:</span></span><span class="base"><span class="strut" style="height:0.43056em;vertical-align:0em;"></span><span class="mrel">:</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.76508em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathdefault">t</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span>, <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>:</mo><mo>:</mo><msub><mi>t</mi><mn>2</mn></msub></mrow><annotation encoding="application/x-tex">x_2 :: t_2</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.58056em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathdefault">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">:</span></span><span class="base"><span class="strut" style="height:0.43056em;vertical-align:0em;"></span><span class="mrel">:</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.76508em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathdefault">t</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span>, <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>x</mi><mi>n</mi></msub><mo>:</mo><mo>:</mo><msub><mi>t</mi><mi>n</mi></msub></mrow><annotation encoding="application/x-tex">x_n :: t_n</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.58056em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathdefault">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">:</span></span><span class="base"><span class="strut" style="height:0.43056em;vertical-align:0em;"></span><span class="mrel">:</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.76508em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathdefault">t</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span>.</p>
</div><h2 id=""><br></h2><h2 id="function-types">Function Types</h2><div style="white-space: normal;" class="markdown-body"><pre data-lang="haskell"><code>not :: Bool -&gt; Bool
isDigit :: Char -&gt; Bool
&gt; isDigit '5'
True


add1 :: (Int, Int) -&gt; Int
add2 :: Int -&gt; (Int -&gt; Int)
</code></pre>
<p>In general <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>a</mi><mo>→</mo><mi>b</mi></mrow><annotation encoding="application/x-tex">a → b</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.43056em;vertical-align:0em;"></span><span class="mord mathdefault">a</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">→</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathdefault">b</span></span></span></span> is the type of (pure) functions from <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>a</mi></mrow><annotation encoding="application/x-tex">a</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.43056em;vertical-align:0em;"></span><span class="mord mathdefault">a</span></span></span></span> to <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>b</mi></mrow><annotation encoding="application/x-tex">b</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathdefault">b</span></span></span></span>.
A function of type <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>a</mi><mo>→</mo><mi>b</mi></mrow><annotation encoding="application/x-tex">a → b</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.43056em;vertical-align:0em;"></span><span class="mord mathdefault">a</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">→</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathdefault">b</span></span></span></span> can be applied to an argument of type <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>a</mi></mrow><annotation encoding="application/x-tex">a</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.43056em;vertical-align:0em;"></span><span class="mord mathdefault">a</span></span></span></span> to get a result of type <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>b</mi></mrow><annotation encoding="application/x-tex">b</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathdefault">b</span></span></span></span>.</p>
</div><p><code>add1</code> takes as argument a tuple <code>(x, y)</code> and returns an <code>Int</code>.</p><p><code>add2</code> takes as argument an <code>Int</code> and returns a function of type <code>Int -&gt; Int</code> that can be applied to the second argument.</p><h2 id=""><br></h2><h2 id="curried-functions">Curried Functions</h2><p>A function that returns another function is called a curried function.</p><p>As a convention, Haskell functions with multiple arguments are curried.</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="haskell"><code>&gt; :t add2 1
Int -&gt; Int
&gt; (add2 1) 1
2
</code></pre>
</div><h2 id=""><br></h2><h2 id="syntax-conventions">Syntax Conventions</h2><p>The function arrow <code>-&gt;</code> associates to the right.</p><p>Function application associates to the left.</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="haskell"><code>a -&gt; b -&gt; c = a -&gt; (b -&gt; c)
f x y = (f x) y
</code></pre>
</div><p><br></p><h2 id="polymorphic-functions">Polymorphic Functions</h2><p>Many functions can be given several types, these functions are given a polymorphic type. No type has to be given, as Haskell can infer it.</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="haskell"><code>length :: [Int] -&gt; Int
length :: [Bool] -&gt; Int


length :: [a] -&gt; Int


&gt; length [2,3,5,7]
4
</code></pre>
</div><p><br></p><p><br></p><h3 id="examples">Examples</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="haskell"><code>id :: a -&gt; a
fst :: (a,b) -&gt; a
snd :: (a,b) -&gt; b
curry ::    ((a,b) -&gt; c)
         -&gt; (a -&gt; b -&gt; c)
uncurry ::    (a -&gt; b -&gt; c)
           -&gt; ((a,b) -&gt; c)


head :: [a] -&gt; a -- On non-empty list
tail :: [a] -&gt; [a] -- On non-empty list
(!!) :: [a] -&gt; Int -&gt; a -- On non-empty list
take :: Int -&gt; [a] -&gt; [a]
drop :: Int -&gt; [a] -&gt; [a]
zip  :: [a] -&gt; [b] -&gt; [(a,b)]
unzip :: [(a,b)] -&gt; ([a], [b])
</code></pre>
</div><h2 id=""><br></h2><h2 id="errors">Errors</h2><div style="white-space: normal;" class="markdown-body"><pre data-lang="haskell"><code>undefined :: a
error :: String -&gt; a
</code></pre>
</div><p>Functions like <code>head</code> call <code>error</code> for an empty list. These functions throw a run-time error when evaluated, making your code partial.</p><p>Advice:</p><ul><li>Only use <code>undefined</code> during development.</li><li>Only use <code>error</code> for unreachable cases.</li><li>(ed. note) For fallible operations use the `Maybe` monad</li></ul><h2 id=""><br></h2><h2 id="operator-syntax">Operator Syntax</h2><p>Infix operators such as <code>(+), (-), (==), (!!)</code> are just regular Haskell functions.</p><ul><li>Name must consist of special characters only.</li><li>Must be parenthesized when appearing by themselves.</li></ul><p>Any function can be used as an infix operator with a backtick.</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="null"><code>(+) 1 1 = 1 + 1
&gt; 5 `div` 2 -- div is integer divide
2
</code></pre>
</div><h1 id=""><br></h1><h1 id="type-classes">Type classes</h1><p>What should be the type of <code>double x = x + x</code>?</p><ul><li><code>double :: Int -&gt; Int</code> is too restrictive, as it should work with <code>Float</code>.</li><li><code>double :: a -&gt; a</code> is too general, as it shouldn't work with <code>Bool</code>.</li></ul><p>Solution: add a constraint <code>Num a =&gt;: double :: Num a =&gt; a -&gt; a</code>.</p><p><code>Num</code> is an example class of a type class: a collection of types that support a common interface.</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="haskell"><code>(+)         :: Num a =&gt; a -&gt; a -&gt; a
(-)         :: Num a =&gt; a -&gt; a -&gt; a
(*)         :: Num a =&gt; a -&gt; a -&gt; a
negate      :: Num a =&gt; a -&gt; a
abs         :: Num a =&gt; a -&gt; a
fromInteger :: Num a =&gt; Integer -&gt; a
</code></pre>
</div><h3 id="eq-class"><code>Eq</code> class</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="haskell"><code>(==) :: Eq a =&gt; a -&gt; a -&gt; Bool
(/=) :: Eq a =&gt; a -&gt; a -&gt; Bool
</code></pre>
</div><h3 id="ord-class"><code>Ord</code> class</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="haskell"><code>(&lt;)  : Ord a =&gt; a -&gt; a -&gt; Bool
(&lt;=) : Ord a =&gt; a -&gt; a -&gt; Bool
(&gt;)  : Ord a =&gt; a -&gt; a -&gt; Bool
(&gt;=) : Ord a =&gt; a -&gt; a -&gt; Bool
max  : Ord a =&gt; a -&gt; a -&gt; a
min  : Ord a =&gt; a -&gt; a -&gt; a
</code></pre>
</div><h3 id="show-class"><code>Show</code> class</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="haskell"><code>show :: Show a =&gt; a -&gt; String


&gt; show False
"False"
&gt; show 123
"123"
&gt; show "123"
"\\"123\\""
</code></pre>
</div><h3 id="read-class"><code>Read</code> class</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="haskell"><code>read :: Read a =&gt; String -&gt; a


&gt; read "False" :: Bool
False
&gt; read "123" :: Int
123
&gt; read "123" :: Bool
**Exception: read: no parse**
</code></pre>
</div><h1 id="list-comprehension">List Comprehension</h1><div style="white-space: normal;" class="markdown-body"><pre data-lang="haskell"><code>&gt; [ x*x | x &lt;- [1..5] ]
[1,4,9,16,25]
</code></pre>
</div><p>We can construct new lists using a list comprehension.</p><p>The <code>x &lt;- [1..5]</code> part is called a generator.</p><h2 id=""><br></h2><h2 id="multiple-generators">Multiple Generators</h2><div style="white-space: normal;" class="markdown-body"><pre data-lang="haskell"><code>&gt; [ x*y | x &lt;- [1,2,3], y &lt;- [10,100]]
[10,100,20,200,30,300]
&gt; [ x*y | y &lt;- [10,100], x &lt;- [1,2,3]]
[10,20,30,100,200,300]
&gt; [ 10*x+y | x &lt;- [1..3], y &lt;- [x..3]]
[11,12,13,22,23,33]
</code></pre>
</div><p>You can also use more than one generator, but the order matters!</p><p>Later generators can depend on previous ones.</p><h2 id=""><br></h2><h2 id="filtering">Filtering</h2><div style="white-space: normal;" class="markdown-body"><pre data-lang="haskell"><code>even :: Integral a =&gt; a -&gt; Bool


&gt; [ x | x &lt;- [1..10], even x]
[2,4,6,8,10]
</code></pre>
</div><p>We can select only elements that satisfy a boolean predicate.</p><p>The predicate <code>even x</code> is called a guard. A guard must be of type <code>Bool</code>.</p><h2 id=""><br></h2><h2 id="list-comprehensions-as-a-general-control-structure">List Comprehensions as a General Control Structure</h2><p>Haskell does not have build-in control like <code>for</code> or <code>while</code>. Instead we van use lists to define iterative algorithms.</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="javascript"><code>let result=0;
let i=0;
while (i&lt;=10) {
	result += i*i;
	i += 1;
}
</code></pre>
<p>vs</p>
<pre data-lang="haskell"><code>result = sum [i * i | i &lt;- [1..10]]
</code></pre>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>Based on the <a href="https://www.notion.so/Haskell-Basics-c6e04121b68f4e77bb8419362b3f0fd4">Notes by Dany Sluijk</a></p>
</div>