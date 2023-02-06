+++
title = "Lookup sheet"
date = 2021-04-16
+++
<h2 id="week-1">Week 1</h2><h3 id="some-theory">Some theory</h3><ul><li><strong>Functional programming (declarative): </strong>treats programs as evaluating mathematical functions and <strong>avoids state and mutable data</strong></li><li class="ql-indent-1">A style of programming where programs are constructed by defining and applying functions.</li><li class="ql-indent-1">A toolbox of techniques aimed at writing clear code at a high level of abstraction.</li><li class="ql-indent-1">Function composition, partially applied function, currying</li><li><strong>Imperative programming: </strong>focuses on how to execute, defines control flow (a specified order of execution) as statements <strong>that change a program state </strong>(side-effects)</li></ul><p><br></p><ul><li><strong>Static typing: </strong>the process of verifying the type safety of a program based on analysis of a program's source code</li><li><strong>Dynamic typing:</strong> the process of verifying the type safety of a program at runtime</li></ul><p><br></p><ul><li><strong>Pure programming: </strong>its behavior is fully described by its inputs and outputs.</li><li class="ql-indent-1">No mutable state</li><li class="ql-indent-1">No input or output (text, file system, network, ...)</li><li class="ql-indent-1">No random or non-deterministic choices</li><li><strong>Effectful programming: </strong>side-effects are the norm. Monads are also effectful.</li></ul><p><br></p><ul><li><strong>Currying: </strong>converting a function that takes multiple arguments into a sequence of functions that each take a single argument</li></ul><p><br></p><h3 id="basic-type-classes">Basic type classes</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>class&nbsp;Eq&nbsp;a&nbsp;where&nbsp;
  -- Eq laws 
  -- Reflexivity: x == x = True
  -- Symmetry: (x == y) = (y == x) 
  -- Transitivity: If (x == y &amp;&amp; y == z) = True then x == z = True
  -- Substitutivity: If x == y = True then f x == f y = True 1
  -- Negation: x /= y = not (x == y)
  (==),&nbsp;(/=)&nbsp;::&nbsp;a&nbsp;-&gt;&nbsp;a&nbsp;-&gt;&nbsp;Bool&nbsp;
&nbsp;
class&nbsp;(Eq&nbsp;a)&nbsp;=&gt;&nbsp;Ord&nbsp;a&nbsp;where&nbsp;
&nbsp;&nbsp;compare&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;::&nbsp;a&nbsp;-&gt;&nbsp;a&nbsp;-&gt;&nbsp;Ordering&nbsp;
&nbsp;&nbsp;(&lt;),&nbsp;(&lt;=),&nbsp;(&gt;=),&nbsp;(&gt;)&nbsp;::&nbsp;a&nbsp;-&gt;&nbsp;a&nbsp;-&gt;&nbsp;Bool&nbsp;
&nbsp; max,&nbsp;min&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;::&nbsp;a&nbsp;-&gt;&nbsp;a&nbsp;-&gt;&nbsp;a


class&nbsp;Show&nbsp;a&nbsp;where&nbsp;
&nbsp;&nbsp;show ::&nbsp;a&nbsp;-&gt;&nbsp;String&nbsp;&nbsp;


class&nbsp;(Eq&nbsp;a,&nbsp;Show&nbsp;a)&nbsp;=&gt;&nbsp;Num&nbsp;a&nbsp;where&nbsp;
&nbsp;&nbsp;(+),&nbsp;(-),&nbsp;(⋆)&nbsp;::&nbsp;a&nbsp;-&gt;&nbsp;a&nbsp;-&gt;&nbsp;a&nbsp;
&nbsp;&nbsp;negate&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;::&nbsp;a&nbsp;-&gt;&nbsp;a&nbsp;
&nbsp;&nbsp;abs,&nbsp;signum&nbsp;&nbsp;&nbsp;::&nbsp;a&nbsp;-&gt;&nbsp;a&nbsp;
&nbsp;&nbsp;fromInteger&nbsp;&nbsp;&nbsp;::&nbsp;Integer&nbsp;-&gt;&nbsp;a&nbsp;
</code></pre>
</div><p><br></p><h3 id="list-comprehension">List comprehension</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>[x | x &lt;- [1..10], even x]
</code></pre>
</div><p><br></p><h2 id="week-2">Week 2</h2><h3 id="nice-little-syntax-thingies">Nice little syntax thingies</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>cylinder :: Double -&gt; Double -&gt; Double 
cylinder r h = 
  let sideArea = 2 * pi * r * h 
      topArea = pi * r ^2 
  in sideArea + 2 * topArea
</code></pre>
</div><p><br></p><h3 id="folds">Folds</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>foldr (-) 0 [1,2,3] = 1-(2-(3-0)) = 2


foldl (-) 0 [1,2,3] = ((0-1)-2)-3 = -6
foldl' -- strict version or foldl which doesn't evaluate its arg fully first (better for memory)
</code></pre>
</div><p><br></p><p>Can be used to express many recursive functions on lists, but not all (e.g. divide and conquer algorithms).</p><p><br></p><h3 id="quicktest">Quicktest</h3><p>We can do property based testing instead of regular testing because regular testing is:</p><ul><li>Boring because you need a lot of unit tests</li><li>Difficult because it is very easy to miss cases</li></ul><p><br></p><p><a href="https://hackage.haskell.org/package/QuickCheck-2.14.2/docs/Test-QuickCheck.html" target="_blank">More documentation</a></p><p><br></p><div style="white-space: normal;" class="markdown-body"><ul>
<li><strong>Roundtrip properties</strong>: applying two or more functions that together result in the original input, e.g.</li>
</ul>
<pre data-lang="text/x-haskell"><code>f (g (... (h x))) == x
</code></pre>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><ul>
<li><strong>Observationally equal</strong>: functions produce the same outputs for all inputs, e.g.</li>
</ul>
<pre data-lang="text/x-haskell"><code>f x == g x
</code></pre>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><ul>
<li><strong>Preconditions</strong>: <code>... ==&gt; ...</code> only tests cases that satisfy the condition</li>
</ul>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><ul>
<li><strong>Custom generators</strong>:</li>
</ul>
<pre data-lang="text/x-haskell"><code>arbitrary :: Arbitrary a =&gt; Gen a 
chooseInt :: (Int, Int) -&gt; Gen Int 
elements :: [a] -&gt; Gen a 
listOf :: Gen a -&gt; Gen [a] 
vectorOf :: Int -&gt; Gen a -&gt; Gen [a] 
shuffle :: [a] -&gt; Gen [a]
</code></pre>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><ul>
<li><strong>Properties</strong>: a generalization of the <code>Bool</code> type:</li>
</ul>
<pre data-lang="text/x-haskell"><code>(==&gt;) :: Property -&gt; Property -&gt; Property 
forAll :: Gen a -&gt; (a -&gt; Property) -&gt; Property 
(===) :: Eq a =&gt; a -&gt; a -&gt; Property 
(.&amp;&amp;.) :: Property -&gt; Property -&gt; Property 
(.||.) :: Property -&gt; Property -&gt; Property
</code></pre>
</div><p><br></p><h2 id="week-3">Week 3</h2><h3 id="adts">ADTs</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>-- Record syntax
-- Also generates the functions radius, width, height
data Shape 
  = Circle { radius :: Double } 
  | Rect { width :: Double , height :: Double }
</code></pre>
</div><p><br></p><p>A <strong>newtype</strong> declaration is a specialized kind of <strong>data</strong> declaration with exactly one constructor taking exactly one argument. It is a "forced" alias (so different than <strong>type</strong>). It is also more efficient than <strong>data.</strong></p><p><br></p><h3 id="set-and-map">Set and Map</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>-- Set
empty :: Set a 
singleton :: a -&gt; Set a 
fromList :: Ord a =&gt; [a] -&gt; Set a 
insert :: Ord a =&gt; a -&gt; Set a -&gt; Set a 
delete :: Ord a =&gt; a -&gt; Set a -&gt; Set a 
member :: Ord a =&gt; a -&gt; Set a -&gt; Bool 
size :: Set a -&gt; Int
union :: Ord a =&gt; Set a -&gt; Set a -&gt; Set a 
difference :: Ord a =&gt; Set a -&gt; Set a -&gt; Set a 
intersection :: Ord a =&gt; Set a -&gt; Set a -&gt; Set a


-- Map
empty :: Map k a 
singleton :: k -&gt; a -&gt; Map k a 
insert :: Ord k =&gt; k -&gt; a -&gt; Map k a -&gt; Map k a 
delete :: Ord k =&gt; k -&gt; Map k a -&gt; Map k a 
lookup :: Ord k =&gt; k -&gt; Map k a -&gt; Maybe a 
size :: Map k a -&gt; Int 
union :: Ord k =&gt; Map k a -&gt; Map k a -&gt; Map k a 
difference :: Ord k =&gt; Map k a -&gt; Map k a -&gt; Map k a 
intersection :: Ord k =&gt; Map k a -&gt; Map k a -&gt; Map k a
</code></pre>
</div><h3 id=""><br></h3><h3 id="type-vs-type-class-vs-instance">Type vs type class vs instance</h3><div style="white-space: normal;" class="markdown-body"><ul>
<li><strong>Type:</strong> a kind of label that every expression has (e.g. <code>Char</code>)</li>
<li><strong>Type class:</strong> &nbsp;a family of types that implement a common interface (= set of functions), e.g. <code>Eq a</code>. Some type classes are a subclass of another class: each instance must also be an instance of the base class.</li>
<li><strong>Instance of typeclass</strong>: a type that belongs to a typeclass</li>
</ul>
</div><p><br></p><p>A new type can be declared as such:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>newtype Sum a = Sum { getSum :: a }
</code></pre>
</div><p><br></p><p>See the next section about declaring new type classes.</p><p><br></p><p>A new instance can be declared as such:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>instance Eq TrafficLight where 
  Red == Red = True
  Green == Green = True 
  Yellow == Yellow = True 
  _ == _ = False
</code></pre>
</div><p><br></p><p>The compiler will forbid all overlapping instances to provide <strong>global coherence </strong>(the result of a program at run time should not depend on which instances were chosen at compile time).</p><p><br></p><h3 id="semigroup-&amp;-monoid">Semigroup &amp; monoid</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>class Semigroup a where 
  -- Semigroup law:
  -- (x &lt;&gt; y) &lt;&gt; z = x &lt;&gt; (y &lt;&gt; z)
  (&lt;&gt;) :: a -&gt; a -&gt; a 


class Semigroup a =&gt; Monoid a where 
  -- Monoid laws:
  -- mempty `mappend` x = x
  -- x `mappend` mempty = x 
  -- (x `mappend` y) `mappend` z = x `mappend` (y `mappend` z)
  mempty :: a 
  mappend :: a -&gt; a -&gt; a 
  mconcat :: [a] -&gt; a 
  mappend = (&lt;&gt;) 
  mconcat = foldr mappend mempty
</code></pre>
</div><p><br></p><h3 id="wrapper-types">Wrapper types</h3><p>You can use wrapper types to give several instances of a type class for the same type, you may want different implementations of monoids for lists.</p><p><br></p><p>This is done as such:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>newtype Sum a = Sum { getSum :: a }
</code></pre>
</div><p><br></p><p>Note the first <em>Sum </em>is the name of the type and the second is the name of the constructor. Now we can implement instances of this type.</p><p><br></p><h2 id="week-4">Week 4</h2><h3 id="io">IO</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>putChar :: Char -&gt; IO () 
putStr :: String -&gt; IO () 
putStrLn :: String -&gt; IO () 
print :: Show a =&gt; a -&gt; IO () 


getChar :: IO Char 
getLine :: IO String
readLn :: Read a =&gt; IO a
</code></pre>
</div><p><br></p><h3 id="do">Do</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>f :: IO a 
f = do 
  v1 &lt;- a1 
  ... 
  vn &lt;- an 
  f v1 ... vn


f = a1 &gt;&gt;= (\v1 -&gt; ... an &gt;&gt;= (\vn -&gt; ...))
</code></pre>
</div><p><br></p><h3 id="functor,-applicative-and-monad">Functor, Applicative and Monad</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>class Functor f where 
  -- Functor laws:
  -- fmap id = id
  -- fmap (g . h) = fmap g . fmap h
 
  -- If the type parameter a occurs to the left of a function arrow (e.g. newtype Endo a = Endo (a -&gt; a)), the type cannot be made into a Functor&nbsp;
  fmap :: (a -&gt; b) -&gt; f a -&gt; f b


class Functor f =&gt; Applicative f where
  -- Applicative laws:
  -- pure id &lt;*&gt; x = x 
  -- pure (f x) = pure f &lt;*&gt; pure x 
  -- mf &lt;*&gt; pure y = pure (\g -&gt; g y) &lt;*&gt; mf 
  -- x &lt;*&gt; (y &lt;*&gt; z) = (pure (.) &lt;*&gt; x &lt;*&gt; y) &lt;*&gt; z
  pure :: a -&gt; f a 
  (&lt;*&gt;) :: f (a -&gt; b) -&gt; f a -&gt; f b
</code></pre>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>Until now, we have viewed (applicative) functors as containers holding values of some type <code>a</code>. Another way to view them is as an effect that may occur while computing the result <code>a</code>. E.g. <code>Maybe</code> captures the possible failure (<code>Nothing</code>).</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>class Applicative m =&gt; Monad m where 
  -- Monad laws:
  -- return x &gt;&gt;= f = f x
  -- mx &gt;&gt;= (\x -&gt; return x) = mx
  -- (mx &gt;&gt;= f) &gt;&gt;= g = mx &gt;&gt;= (\x -&gt; (f x &gt;&gt;= g))
  -- 
  return :: a -&gt; m a 
  (&gt;&gt;=) :: m a -&gt; (a -&gt; m b) -&gt; m b
</code></pre>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p><code>&gt;&gt;</code> executes one action after the other, ignoring the output of the first</p>
</div><p><br></p><h3 id="encoding-a-side-effect">Encoding a side-effect</h3><div style="white-space: normal;" class="markdown-body"><ul>
<li><strong>Failing computation</strong>: <code>Maybe</code></li>
</ul>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><ul>
<li><strong>Throwing exceptions</strong>: <code>Either</code></li>
</ul>
<pre data-lang="text/x-haskell"><code>-- Right x = Just x
-- Left err = informative version of Nothing
instance Monad (Either e) where 
  return x = Right x 
  Left err &gt;&gt;= f = Left err 
  Right x &gt;&gt;= f = f x
</code></pre>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><ul>
<li><strong>Making non-deterministic choices</strong>: <code>[]</code></li>
</ul>
<pre data-lang="text/x-haskell"><code>-- [x] = Just x
-- [] = Nothing
instance Monad [] where 
  return x = [x] 
  xs &gt;&gt;= f = [y | x &lt;- xs, y &lt;- f x]
</code></pre>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><ul>
<li><strong>Modifying global state</strong>: <code>State</code></li>
</ul>
<pre data-lang="text/x-haskell"><code>-- oldState -&gt; (someReturnValue, newState)
newtype State s a = State (s -&gt; (a,s))


-- Returns the current state by setting a to the current state
-- Doesn't update the state because the new state is the input state
get = State (\st -&gt; (st,st)) 


-- Updates the state and returns nothing
put st = State (\_ -&gt; ((),st))
</code></pre>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><ul>
<li><strong>Performing IO</strong>: <code>IO</code></li>
</ul>
</div><p><br></p><h3 id="other-monads">Other monads</h3><div style="white-space: normal;" class="markdown-body"><ul>
<li><strong>Reader</strong>: gives access to extra input of type <code>r</code>:</li>
</ul>
<pre data-lang="text/x-haskell"><code>newtype Reader r a = Reader (r -&gt; a)
</code></pre>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><ul>
<li><strong>Writer</strong>: allows writing some output of type <code>w</code>:</li>
</ul>
<pre data-lang="text/x-haskell"><code>newtype Writer w a = Writer (w, a)
</code></pre>
</div><p><br></p><h3 id="monad-functions">Monad functions</h3><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>when</code>: executes an action only when the condition is <code>True</code></li>
</ul>
<pre data-lang="text/x-haskell"><code>when :: Applicative f =&gt; Bool -&gt; f () -&gt; f ()
</code></pre>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>sequence</code>: runs a list of actions and collect the results</li>
</ul>
<pre data-lang="text/x-haskell"><code>sequence :: Monad m =&gt; t (m a) -&gt; m (t a)
</code></pre>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>mapM</code>: a monadic version of <code>map</code></li>
</ul>
<pre data-lang="text/x-haskell"><code>mapM :: (Traversable t, Monad m) =&gt; (a -&gt; m b) -&gt; t a -&gt; m (t b)
mapM f xs = sequence (map f xs)
</code></pre>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>forM</code>: a monadic version of <code>for</code> (i.e. <code>mapM</code> with flipped arguments`)</li>
</ul>
<pre data-lang="text/x-haskell"><code>forM :: (Traversable t, Monad m) =&gt; t a -&gt; (a -&gt; m b) -&gt; m (t b)
forM = flip mapM
</code></pre>
</div><p><br></p><h2 id="week-5">Week 5</h2><h3 id="evaluation-strategies">Evaluation strategies</h3><ul><li>A <strong>reducible expression</strong> (or redex) is a function application that can be ‘reduced’</li><li>An evaluation strategy gives a general way to pick a redex to reduce next</li><li class="ql-indent-1"><strong>Innermost reduction</strong>: pick a redex that contains no other redex, <em>call-by-value</em></li><li class="ql-indent-1"><strong>Outermost reduction</strong>: pick a redex that is not contained in another redex, <em>call-by-name</em></li><li>Haskell can only apply lambda's, so it can't select redexes within lambdas</li></ul><p><br></p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>-- Call-by-value
    (\x -&gt; 1 + 2) (3 + 4) 
--&gt; (\x -&gt; 1 + 2) 7 
--&gt; 1 + 2 
--&gt; 0


-- Call-by-name
(\x -&gt; 1 + 2) -/-&gt; (no reduction)
</code></pre>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>For functions that don’t (always) use their arguments, <em>call-by-value</em> will do useless work:</p>
<pre data-lang="text/x-haskell"><code>(\x -&gt; 42) (2+3) --&gt; (\x -&gt; 42) 5 --&gt; 42 
</code></pre>
<p>For functions that use their arguments more than once, <em>call-by-name</em> will do useless work:</p>
<pre data-lang="text/x-haskell"><code>(\x -&gt; x * x) (2+3) --&gt; (2+3) * (2+3) --&gt; 5 * (2+3) --&gt; 5 * 5 --&gt; 25
</code></pre>
<p>The best of both worlds is a thunked version of <em>call-by-name</em>: <strong>call-by-need</strong>. The first time the argument is used, the thunk is evaluated and the result is stored in the thunk. The next time the value stored in the thunk is used:</p>
<pre data-lang="text/x-haskell"><code>(\x -&gt; x * x) (1 + 2) [            ] 
--&gt; x * x             [ x := 1 + 2 ] 
--&gt; 3 * x             [ x := 3     ] 
--&gt; 3 * 3             [ x := 3     ] 
--&gt; 9                 [ x := 3     ]
</code></pre>
</div><p><br></p><p>+  always terminates if possible, smallest number of steps, allows us to work with infinite data structures</p><p>-  more memory usage, runtime overhead, harder to predict execution plan</p><p><br></p><h3 id="forcing-evaluation">Forcing evaluation</h3><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>seq</code>: the expression <code>seq u v</code> will evaluate <code>u</code> to <strong>head normal form</strong> before returning <code>v</code></li>
</ul>
<pre data-lang="text/x-haskell"><code>seq :: a -&gt; b -&gt; b
(1+2) `seq` 5 --&gt; 3 `seq` 5 --&gt; 5
</code></pre>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>($!)</code>: the expression <code>f $! x</code> evaluates <code>x</code> before applying <code>f</code> (call-by-value)</li>
</ul>
<pre data-lang="text/x-haskell"><code>($!) :: (a -&gt; b) -&gt; a -&gt; b 
f $! x = x `seq` f x
</code></pre>
</div><p><br></p><h3 id="lazy-vs-strict">Lazy vs strict</h3><ul><li><strong>Lazy evaluation</strong> is often more efficient when working with small expressions that produce big data structures.</li><li><strong>Strict evaluation</strong> is often more efficient when working with big expressions that produce small data structures.</li></ul><p><br></p><div style="white-space: normal;" class="markdown-body"><pre data-lang="hs"><code>foldl' (+) 0 [1..1000]
</code></pre>
</div><p><br></p><ul><li>Second argument becomes big expression but computes to small Int ⇒ strict is better</li><li>Third argument is small expression but computes to long [Int] ⇒ lazy is better</li></ul><p><br></p><h3 id="laziness-in-folds">Laziness in folds</h3><div style="white-space: normal;" class="markdown-body"><p><code>foldr</code> is often the better choice is that the folding function can short-circuit, that is, terminate early by yielding a result which does not depend on the value of the accumulating parameter. When such possibilities arise with some frequency in your problem, short-circuiting can greatly improve your program's performance. <strong>Left folds can never short-circuit.</strong></p>
</div><p><br></p><p>The reason is illustrated here:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>-- foldr would unpack as such
-- This would be fine!
foldr (&amp;&amp;) True (repeat False)
= False &amp;&amp; (foldr (&amp;&amp;) True (repeat False))
= False


-- foldl would unpack as such
-- This would yield an out of memory
foldl (&amp;&amp;) True (repeat False)
= foldl (&amp;&amp;) (True &amp;&amp; False) (repeat False)
= foldl (&amp;&amp;) ((True &amp;&amp; False) &amp;&amp; False) (repeat False)
= foldl (&amp;&amp;) (((True &amp;&amp; False) &amp;&amp; False) &amp;&amp; False) (repeat False)
= ...


-- foldl' would unpack as such
-- This would loop infinitely
foldl' (&amp;&amp;) True (repeat False)
= foldl' (&amp;&amp;) False (repeat False)
= foldl' (&amp;&amp;) False (repeat False)
= foldl' (&amp;&amp;) False (repeat False)
= ...
</code></pre>
</div><p><br></p><h2 id="week-6">Week 6</h2><h3 id="pure-vs-total-functional-language">Pure vs total functional language</h3><p>Agda is a total language:</p><ul><li>NO runtime errors</li><li>NO incomplete pattern matches</li><li>NO non-terminating functions (every input is mapped to an output)</li></ul><p><br></p><p>It uses a <strong>coverage check </strong>to ensure all definitions by pattern matching are complete</p><p>It uses a <strong>termination check </strong>to ensure all recursive definitions are terminating</p><p>It only accepts functions that are <strong>structurally recursive: </strong>the argument of each recursive call must be a subterm of the argument on the left of the clause</p><p><br></p><h3 id="unicode-characters">Unicode characters</h3><div style="white-space: normal;" class="markdown-body"><p>→ <code>\to</code></p>
<p>λ <code>\lambda</code></p>
<p>× <code>\times</code></p>
<p>Σ <code>\Sigma</code></p>
<p>⊤ <code>\top</code></p>
</div><div style="white-space: normal;" class="markdown-body"><p>⊥ <code>\bot</code></p>
<p>≡ <code>\equiv</code></p>
</div><p><br></p><h3 id="data-types">Data types</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>-- The basic form of a datatype is
data D : Setᵢ where
&nbsp;c₁ : A₁
&nbsp;...
&nbsp;cₙ : Aₙ


-- E.g.
data BinTree : Set where
 -- These are constructors and MUST end in a BinTree
&nbsp;leaf&nbsp;&nbsp;: Nat → BinTree
&nbsp;branch : BinTree → BinTree → BinTree


-- They can also be parameterized:
data List (A : Set) : Set where
&nbsp;[]&nbsp;: List A
&nbsp;_∷_ : A → List A → List A


-- In&nbsp;contrast to parameters which are required to be the same for all constructors, indices can vary from constructor to constructor
data Vector (A : Set) : Nat → Set where
&nbsp;[]&nbsp;: Vector A zero
&nbsp;_∷_ : {n : Nat} → A → Vector A n → Vector A (suc n)
```w
</code></pre>
</div><p><br></p><h3 id="natural-numbers">Natural numbers</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>-- To not just have to work with suc zero etc, we can enable Agda support for machine integers:
{-# BUILTIN NATURAL Nat #-}
</code></pre>
</div><p><br></p><h3 id="dependent-types">Dependent types</h3><p>A <strong>dependent type</strong> is a type whose definition depends on a value. It can be expressed as such:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>data Food : Flavour → Set where 
  pizza : Food cheesy 
  cake : Food chocolatey 
  bread : (f : Flavour) → Food f
</code></pre>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>The argument of a <strong>parametrized type</strong> (e.g. <code>a</code> in <code>Maybe a</code>) in Haskell is a type, while the argument of a dependent type is an expression of some type. All types <code>Maybe a</code> have the same constructors (<code>Nothing</code> and <code>Just</code>) no matter what <code>a</code> is, while <code>Food f</code> has different constructors depending on <code>f</code></p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>A dependent function type is a type of the form <code>(x : A) → B x</code> where the type of the output depends on the value of the input:</p>
<pre data-lang="text/x-haskell"><code>zeroes : (n : Nat) → Vec Nat n 
zeroes zero = [] 
zeroes (suc n) = 0 :: zeroes n
</code></pre>
</div><p><br></p><h3 id="vec">Vec</h3><div style="white-space: normal;" class="markdown-body"><p><code>Vec A n</code> is the type of vectors with exactly <code>n</code> arguments of type <code>A</code>. Now we can use this to check the actual length:</p>
<pre data-lang="text/x-haskell"><code>data Vec (A : Set) : Nat → Set where 
  [] : Vec A 0 
  _::_ : {n : Nat} → A → Vec A n → Vec A (suc n)


-- Can be used as:
myVec4 : Vec Nat (2 + 2) 
myVec4 = 1 :: 2 :: 3 :: 4 :: []
</code></pre>
</div><p><br></p><h3 id="fin">Fin</h3><div style="white-space: normal;" class="markdown-body"><p><code>Fin n</code> is a type that denotes we have a number between 0 and n-1. <code>Fin 0</code> is an empty type.</p>
<pre data-lang="text/x-haskell"><code>data Fin : Nat → Set where 
  zero : {n : Nat} → Fin (suc n) 
  suc : {n : Nat} → Fin n → Fin (suc n)
</code></pre>
<p>To denote a case that can never happen, we can use the <strong>absurd pattern</strong> <code>()</code>:</p>
<pre data-lang="text/x-haskell"><code>lookupVec : {A : Set} {n : Nat} → Vec A n → Fin n → A 
lookupVec [] () 
lookupVec (x :: xs) zero = x 
lookupVec (x :: xs) (suc i) = lookupVec xs i
</code></pre>
</div><p><br></p><h3 id="function-into-set">Function into Set</h3><div style="white-space: normal;" class="markdown-body"><p>Since Set is just another type, we can use pattern matching to define new types:</p>
<pre data-lang="text/x-haskell"><code>pickType : Bool → Set 
pickType true = Nat 
pickType false = Bool → Bool
</code></pre>
<p>Now <code>pickType true</code> is an alias for Nat, and <code>pickType false</code> is an alias for Bool:</p>
<pre data-lang="text/x-haskell"><code>test2 : pickType true 
test2 = suc zero
</code></pre>
</div><p><br></p><h3 id="dependent-pairs">Dependent pairs</h3><div style="white-space: normal;" class="markdown-body"><p>The type <code>Σ A B1</code> is the type of dependent pairs <code>(x, y)</code> where the type of y can change depending on the value of <code>x </code>:</p>
<pre data-lang="text/x-haskell"><code>data Σ (A : Set) (B : A → Set) : Set where 
  _,_ : (x : A) → B x → Σ A B


pair1 : Σ Nat (λ n → Vec Bool n) 
pair1 = (2 , (true :: false :: [])) 


pair2 : Σ Nat (λ n → Vec Bool n) 
pair2 = (0 , [])
</code></pre>
<p>We can define regular pairs (where the type of the second component doesn’t actually depend on the first) as a special case of the <code>Σ</code> type:</p>
<pre data-lang="text/x-haskell"><code>_×’_ : (A B : Set) → Set 
A ×’ B = Σ A (λ _ → B)
</code></pre>
</div><p><br></p><h2 id="week-7">Week 7</h2><h3 id="curry-howard-correspondance">Curry-Howard correspondance</h3><div style="white-space: normal;" class="markdown-body"><p>We can interpret logical propositions (<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>A</mi><mo>∧</mo><mi>B</mi><mo separator="true">,</mo><mi mathvariant="normal">¬</mi><mi>A</mi><mo separator="true">,</mo><mi>A</mi><mo>⇒</mo><mi>B</mi><mo separator="true">,</mo><mo>…</mo></mrow><annotation encoding="application/x-tex">A ∧ B, ¬A, A ⇒ B, \dots</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">∧</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="mord mathdefault" style="margin-right:0.05017em;">B</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord">¬</span><span class="mord mathdefault">A</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord mathdefault">A</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">⇒</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="mord mathdefault" style="margin-right:0.05017em;">B</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="minner">…</span></span></span></span>) as the types of all their possible proofs. A <code>false</code> proposition has no proofs, so it corresponds to an <code>empty</code> type:</p>
<ol>
<li>Propositions are types</li>
<li>Proofs are programs</li>
<li>Simplifying a proof is evaluating a program</li>
</ol>
<p>We can only use this in a total language because we must have a way to express false propositions, without infinitely looping or having any uncovered cases.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><table>
<thead>
<tr>
<th>Propositional logic</th>
<th></th>
<th>Type system</th>
</tr>
</thead>
<tbody>
<tr>
<td>proposition</td>
<td><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi></mrow><annotation encoding="application/x-tex">P</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathdefault" style="margin-right:0.13889em;">P</span></span></span></span></td>
<td>type</td>
</tr>
<tr>
<td>proof of a proposition</td>
<td><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>p</mi><mo>:</mo><mi>P</mi></mrow><annotation encoding="application/x-tex">p: P</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="mord mathdefault">p</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">:</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathdefault" style="margin-right:0.13889em;">P</span></span></span></span></td>
<td>program of a type</td>
</tr>
<tr>
<td>conjunction (<code>AND</code>)</td>
<td><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mo>×</mo><mi>Q</mi></mrow><annotation encoding="application/x-tex">P\times Q</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.76666em;vertical-align:-0.08333em;"></span><span class="mord mathdefault" style="margin-right:0.13889em;">P</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">×</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="mord mathdefault">Q</span></span></span></span></td>
<td>pair type</td>
</tr>
<tr>
<td>disjunction (<code>OR</code>)</td>
<td><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mtext>Either</mtext><mi>P</mi><mi>Q</mi></mrow><annotation encoding="application/x-tex">\text{Either} P Q</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord text"><span class="mord">Either</span></span><span class="mord mathdefault" style="margin-right:0.13889em;">P</span><span class="mord mathdefault">Q</span></span></span></span></td>
<td>either type</td>
</tr>
<tr>
<td>implication</td>
<td><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mo>→</mo><mi>Q</mi></mrow><annotation encoding="application/x-tex">P\to Q</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathdefault" style="margin-right:0.13889em;">P</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">→</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="mord mathdefault">Q</span></span></span></span></td>
<td>function type</td>
</tr>
<tr>
<td>truth</td>
<td><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="normal">⊤</mi></mrow><annotation encoding="application/x-tex">\top</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord">⊤</span></span></span></span></td>
<td>unit type</td>
</tr>
<tr>
<td>falsity</td>
<td><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="normal">⊥</mi></mrow><annotation encoding="application/x-tex">\bot</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord">⊥</span></span></span></span></td>
<td>empty type</td>
</tr>
<tr>
<td>negation (<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi></mrow><annotation encoding="application/x-tex">\not P</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mrel"><span class="mord"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.69444em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="rlap"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="inner"><span class="mrel"></span></span><span class="fix"></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.19444em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathdefault" style="margin-right:0.13889em;">P</span></span></span></span>)</td>
<td><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mo>→</mo><mi mathvariant="normal">⊥</mi></mrow><annotation encoding="application/x-tex">P\to \bot</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathdefault" style="margin-right:0.13889em;">P</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">→</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord">⊥</span></span></span></span></td>
<td>-</td>
</tr>
<tr>
<td>equivalence (<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mtext>  </mtext><mo>⟺</mo><mtext>  </mtext><mi>Q</mi></mrow><annotation encoding="application/x-tex">P\iff Q</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.70733em;vertical-align:-0.024em;"></span><span class="mord mathdefault" style="margin-right:0.13889em;">P</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">⟺</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="mord mathdefault">Q</span></span></span></span>)</td>
<td><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo stretchy="false">(</mo><mi>P</mi><mo>→</mo><mi>Q</mi><mo stretchy="false">)</mo><mo>×</mo><mo stretchy="false">(</mo><mi>Q</mi><mo>→</mo><mi>P</mi><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">(P\to Q)\times (Q\to P)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord mathdefault" style="margin-right:0.13889em;">P</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">→</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathdefault">Q</span><span class="mclose">)</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">×</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord mathdefault">Q</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">→</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathdefault" style="margin-right:0.13889em;">P</span><span class="mclose">)</span></span></span></span></td>
<td>-</td>
</tr>
<tr>
<td>universal quantification (for all)</td>
<td><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo stretchy="false">(</mo><mi>x</mi><mo>:</mo><mi>A</mi><mo stretchy="false">)</mo><mo>→</mo><mi>P</mi><mi>x</mi></mrow><annotation encoding="application/x-tex">(x: A)\to P x</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord mathdefault">x</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">:</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathdefault">A</span><span class="mclose">)</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">→</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathdefault" style="margin-right:0.13889em;">P</span><span class="mord mathdefault">x</span></span></span></span></td>
<td>dependent function type</td>
</tr>
<tr>
<td>existential quantification (there exists)</td>
<td><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="normal">Σ</mi><mi>A</mi><mo stretchy="false">(</mo><mi>λ</mi><mi>x</mi><mo>→</mo><mi>P</mi><mi>x</mi><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">\Sigma A(\lambda x \to P x)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord">Σ</span><span class="mord mathdefault">A</span><span class="mopen">(</span><span class="mord mathdefault">λ</span><span class="mord mathdefault">x</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">→</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathdefault" style="margin-right:0.13889em;">P</span><span class="mord mathdefault">x</span><span class="mclose">)</span></span></span></span></td>
<td>dependent pair type</td>
</tr>
<tr>
<td>equality</td>
<td><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo>≡</mo></mrow><annotation encoding="application/x-tex">\equiv</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.46375em;vertical-align:0em;"></span><span class="mrel">≡</span></span></span></span></td>
<td>identity type</td>
</tr>
</tbody>
</table>
</div><p><br></p><h3 id="constructive-vs-classical-logic">Constructive vs classical logic</h3><p>In classical logic we can prove <span class="ql-formula" data-value="P\vee\left(\neg P\right)">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>P</mi><mo>∨</mo><mrow><mo fence="true">(</mo><mi mathvariant="normal">¬</mi><mi>P</mi><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">P\vee\left(\neg P\right)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.13889em;" class="mord mathdefault">P</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span><span class="mbin">∨</span><span class="mspace" style="margin-right: 0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="minner"><span class="mopen delimcenter" style="top: 0em;">(</span><span class="mord">¬</span><span style="margin-right: 0.13889em;" class="mord mathdefault">P</span><span class="mclose delimcenter" style="top: 0em;">)</span></span></span></span></span></span>﻿</span> (law of excluded middle) and <span class="ql-formula" data-value="\neg\neg P\Rightarrow P">﻿<span contenteditable="false"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mi mathvariant="normal">¬</mi><mi>P</mi><mo>⇒</mo><mi>P</mi></mrow><annotation encoding="application/x-tex">\neg\neg P\Rightarrow P</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord">¬</span><span class="mord">¬</span><span style="margin-right: 0.13889em;" class="mord mathdefault">P</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span><span class="mrel">⇒</span><span class="mspace" style="margin-right: 0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span style="margin-right: 0.13889em;" class="mord mathdefault">P</span></span></span></span></span>﻿</span> (double negation elimination). However, Agda uses <strong>constructive logic</strong>, so these problems are unprovable.</p><p><br></p><div style="white-space: normal;" class="markdown-body"><p><code>((A × B) → ⊥) → Either (A → ⊥) (B → ⊥)</code> cannot be proven because if <code>((A × B) → ⊥)</code> holds, it is unknown whether this is because of <code>A</code>, <code>B</code> or both. Thus we don't know which case to pick on the right hand side.</p>
</div><p><br></p><h3 id="proving-evenness">Proving evenness</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>data IsEven : Nat → Set where
  e-zero : IsEven zero -- Note this is an existing type and thus true
  e-suc2 : {n : Nat} → IsEven n → IsEven (suc (suc n)) -- This type will only exist if there are two successors


-- We can prove that every double of any number n is even:
double-even : (n : Nat) → IsEven (double n) 
double-even zero = e-zero 
double-even (suc m) = e-suc2 (double-even m)
</code></pre>
</div><p><br></p><h3 id="istrue">IsTrue</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>-- if b = true, isTrue b has one element
-- if b = false, it has no elements =&gt; empty type
data IsTrue : Bool → Set where 
  is-true : IsTrue true


-- We can prove that any number is equal to itself
n-equals-n : (n : Nat) → IsTrue (n =Nat n) 
n-equals-n zero = is-true 
n-equals-n (suc m) = n-equals-n m
</code></pre>
</div><p><br></p><h3 id="identity">Identity</h3><div style="white-space: normal;" class="markdown-body"><p>We can generalize <code>IsTrue</code> to some elements being equal to each other:</p>
<pre data-lang="text/x-haskell"><code>-- If x and y are equal x ≡ y has one constructor, refl
-- If they are not equal, x ≡ y is an empty type
data _≡_ {A : Set} : A → A → Set where 
  refl : {x : A} → x ≡ x


not-not : (b : Bool) → not (not b) ≡ b 
not-not true = refl 
not-not false = refl
</code></pre>
</div><p><br></p><h3 id="properties-of-equality">Properties of equality</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>-- Symmetry: if x is equal to y, y is equal to x
sym : {A : Set} {x y : A} → x ≡ y → y ≡ x 
sym refl = refl


-- Transitivity: if x is equal to y and y is equal to z, x is equal to z
trans : {A : Set} {x y z : A} → x ≡ y → y ≡ z → x ≡ z 
trans refl refl = refl


-- Congruence: if f: A → B is a function and x is equal to y, then f x is equal to f y
cong : {A B : Set} {x y : A} → (f : A → B) → x ≡ y → f x ≡ f y 
cong f refl = refl
</code></pre>
</div><p><br></p><h3 id="equational-reasoning">Equational reasoning</h3><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>reverse-singleton : {A : Set} (x : A) → reverse [ x ] ≡ [ x ] 
reverse-singleton x = 
  begin 
    reverse [ x ] = 
  &lt;&gt; -- definition of [_] 
    reverse (x :: []) 
  &lt;&gt; -- applying reverse (second clause) 
    reverse [] ++ [ x ] 
  &lt;&gt; -- applying reverse (first clause) 
    [] ++ [ x ] 
  &lt;&gt; -- applying 
   _++_ [ x ]
  end
</code></pre>
</div><p><br></p><p>Sometimes we also need to provide an <strong>explicit proof:</strong></p><p><br></p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-haskell"><code>add-n-zero : (n : Nat) → n + zero ≡ n 
  ...
    suc (n + zero)
  &lt; cong suc (add-n-zero n) &gt;
    suc n
  end
</code></pre>
</div>