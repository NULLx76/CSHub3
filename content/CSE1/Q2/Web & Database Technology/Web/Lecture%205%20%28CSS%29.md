+++
title = "Lecture 5 (CSS)"
date = 2019-03-10
+++
<h1>Lecture 5</h1><p><a href="https://github.com/chauff/Web-Teaching/blob/master/Lecture-5.md" target="_blank" style="color: rgb(0, 166, 216);"><em>This is a list of things copied from the transcripts that seem most important to me</em></a></p><p><br></p><h2>About CSS</h2><p>There have been multiple versions of CSS, starting from CSS1 becoming a W3C recommendation in 1996, CSS2 in 1998, CSS2.1 in 2011 and CSS3 is in use nowadays. <span style="background-color: rgb(255, 255, 255); color: rgb(36, 41, 46);">Any CSS module developed after CSS2.1 can be considered as CSS3. Polyfills are used to support features that are not natively supported. In the transcript they state there are 3 different stylesheets, but that really depends on the browser, in Chrome this was removed (</span><a href="https://\sup eruser.com/questions/52967/change-default-css-of-google-chrome" target="_blank" style="background-color: rgb(255, 255, 255); color: rgb(0, 102, 204);">see here</a>). Also, Sass is much better than normal CSS, in CSS you can use some weird --<em>varname </em>and then <em>property: var(--varname) </em>syntax, but that is ugly and SASS can do much more than that.</p><p><br></p><h2>Selectors</h2><p>In CSS, you can select different parts of the DOM, using selectors. This is the syntax:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/css">.class:hover {
  color: red;
}
</pre>
</div><p>If you understand this, great, otherwise it would be handy to <a href="https://www.w3schools.com/css/default.asp" target="_blank">read up online</a>.</p><p><br></p><p><strong>Selector combinations: </strong>You can combine selectors to select something more specifically :</p><div style="white-space: normal;" class="markdown-body"><table>
<thead>
<tr>
<th>Selector</th>
<th>Selects all elements that...</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>s1</code></td>
<td>match the selector <code>s1</code></td>
</tr>
<tr>
<td><code>s1s2</code></td>
<td>match both the selector <code>s1</code> and <code>s2</code></td>
</tr>
<tr>
<td><code>s1 s2</code></td>
<td>match the selector <code>s2</code> and are within an element which matches selector <code>s1</code></td>
</tr>
<tr>
<td><code>s1,s2</code></td>
<td>match the selector <code>s1</code> or <code>s2</code></td>
</tr>
<tr>
<td><code>s1&gt;s2</code></td>
<td>match the selector <code>s2</code> and have an element which matches selector <code>s1</code> as parent</td>
</tr>
<tr>
<td><code>s1+s2</code></td>
<td>match the selector <code>s2</code> and that are placed immediately after an element which matches selector <code>s1</code></td>
</tr>
</tbody>
</table>
</div><p>A decent list of many selectors can be found <a href="https://www.w3schools.com/csSref/css_selectors.asp" target="_blank">here</a></p><p><br></p><p><strong>Pseudo-classes: </strong><span style="background-color: rgb(255, 255, 255); color: rgb(36, 41, 46);">A </span><strong style="background-color: rgb(255, 255, 255); color: rgb(36, 41, 46);">pseudo-class </strong><span style="background-color: rgb(255, 255, 255); color: rgb(36, 41, 46);">is a keyword added to a </span><strong style="background-color: rgb(255, 255, 255); color: rgb(36, 41, 46);">selector</strong><span style="background-color: rgb(255, 255, 255); color: rgb(36, 41, 46);"> that indicates </span><em style="background-color: rgb(255, 255, 255); color: rgb(36, 41, 46);">a particular state or type </em><span style="background-color: rgb(255, 255, 255); color: rgb(36, 41, 46);">of the corresponding element. In practice, you'll only really use :hover but they talk about more than that:</span></p><p><br></p><div style="white-space: normal;" class="markdown-body"><table>
<thead>
<tr>
<th>Pseudo-class</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>:hover</code></td>
<td>On hover</td>
</tr>
<tr>
<td><code>:active</code></td>
<td>When active (clicked)</td>
</tr>
<tr>
<td><code>:enabled</code></td>
<td>When enabled (which is an HTML property)</td>
</tr>
<tr>
<td><code>:disabled</code></td>
<td>When disabled (which is an HTML property)</td>
</tr>
<tr>
<td><code>:not</code></td>
<td>Not</td>
</tr>
<tr>
<td><code>:first-child</code></td>
<td>The first child of an element</td>
</tr>
<tr>
<td><code>:last-child</code></td>
<td>The last child of an element</td>
</tr>
<tr>
<td><code>:first-of-type</code></td>
<td>The first element of that type</td>
</tr>
<tr>
<td><code>:last-of-type</code></td>
<td>The last element of that type</td>
</tr>
<tr>
<td><code>:nth-child(X)</code></td>
<td>The nth child of an element</td>
</tr>
<tr>
<td><code>:nth-last-child(X)</code></td>
<td>The nth child of an element from behind</td>
</tr>
<tr>
<td><code>:nth-last-child(X)</code></td>
<td>The nth child of an element from behind</td>
</tr>
<tr>
<td><code>:nth-last-of-type(X)</code></td>
<td>The nth child from behind of type</td>
</tr>
<tr>
<td><code>:nth-of-type(X)</code></td>
<td>The nth child of type</td>
</tr>
<tr>
<td><code>:valid</code></td>
<td>Only shown when a form is valid</td>
</tr>
<tr>
<td><code>:invalid</code></td>
<td>Only shown when a form is invalid</td>
</tr>
<tr>
<td><code>:root</code></td>
<td>Alias of &lt;html&gt;</td>
</tr>
<tr>
<td><code>::fist-letter</code> (2 colons due to pseudo-content instead of selector)</td>
<td>The first letter of text</td>
</tr>
<tr>
<td><code>::first-line</code></td>
<td>The first line of text</td>
</tr>
<tr>
<td><code>::before</code></td>
<td>Placed before that selected element</td>
</tr>
<tr>
<td><code>::after</code></td>
<td>Placed after that selected element</td>
</tr>
</tbody>
</table>
</div><p><br></p><h2>Element positioning</h2><div style="white-space: normal;" class="markdown-body"><ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/float"><code>float</code></a> defines how an element floats in the containing element (which in turn determines how other elements flow around it), but don't use it, use flexbox.</li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position"><code>position</code></a> defines how an element is positioned in a document:</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>position:static</code></td>
<td>the default</td>
</tr>
<tr>
<td><code>position:relative</code></td>
<td>the element is positioned relatively to its normal position</td>
</tr>
<tr>
<td><code>position:absolute</code></td>
<td>positioned relative to the nearest positioned ancestor (instead of positioned relative to the viewport, like <code>position: fixed</code>).</td>
</tr>
<tr>
<td><code>position:fixed</code></td>
<td>positioned relative to the viewport</td>
</tr>
<tr>
<td><code>position:sticky</code></td>
<td>positioned relative until a given offset position is met in the viewport - then it "sticks" in place (like <code>position: fixed</code>).</td>
</tr>
</tbody>
</table>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/display"><code>display</code></a> defines the display type of an element.</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>display:inline</code></td>
<td>Displays an element as an inline element (like <code>&lt;span&gt;</code>). Any height and width properties will have no effect.</td>
</tr>
<tr>
<td><code>display:block</code></td>
<td>Displays an element as a block element (like <code>&lt;p&gt;</code>). It starts on a new line, and takes up the whole width</td>
</tr>
<tr>
<td><code>display:none</code></td>
<td>The element (and its descendents) are hidden from view; no space is reserved in the layout.</td>
</tr>
</tbody>
</table>
</div><div style="white-space: normal;" class="markdown-body"><p>Some additional concepts:</p>
<ul>
<li><strong>Block-level elements</strong> are surrounded by line-breaks. They can contain block-level and inline elements. <strong>The width is determined by their containing element.</strong> Examples of block-level elements are <code>&lt;main&gt;</code> or <code>&lt;p&gt;</code>.</li>
<li><strong>Inline elements</strong> can be placed within block-level or inline elements. They can contain other inline elements. <strong>The width is determined by their content.</strong> Examples are <code>&lt;span&gt;</code> or <code>&lt;a&gt;</code>.</li>
</ul>
</div><p><br></p><p>But, much better alternatives that won't leave you annoyed are the new <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout" target="_blank">CSS grid</a> and <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox" target="_blank">flexbox </a>technologies. </p><p><br></p><h2>Media queries</h2><div style="white-space: normal;" class="markdown-body"><p><strong>CSS media queries</strong> enable the use of <strong>device</strong>/<strong>media-type dependent</strong> style sheets. While the HTML document is written once, the CSS is written once per device type. There are four device types currently in use:</p>
</div><div style="white-space: normal;" class="markdown-body"><table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>media all</code></td>
<td>Suitable for all device types.</td>
</tr>
<tr>
<td><code>media print</code></td>
<td>Suitable for documents in print preview.</td>
</tr>
<tr>
<td><code>media screen</code></td>
<td>Suitable for screens.</td>
</tr>
<tr>
<td><code>media speech</code></td>
<td>Suitable for speech synthesizers.</td>
</tr>
</tbody>
</table>
</div><p><br></p><h2>Animations and transitions</h2><p>The rendering engine takes care of the transition between styles. A rendering engine - also known as browser engine or layout engine - is responsible for translating HTML+CSS to the screen.</p><p><br></p><p><strong style="color: rgb(36, 41, 46);">CSS animations </strong><span style="color: rgb(36, 41, 46);">consist of:</span></p><ul><li><span style="color: rgb(36, 41, 46);">an animation style (e.g.</span><code style="color: rgb(36, 41, 46); background-color: rgba(27, 31, 35, 0.05);">linear</code><span style="color: rgb(36, 41, 46);">);</span></li><li>a number of <strong style="color: rgb(36, 41, 46);">keyframes </strong><span style="color: rgb(36, 41, 46);">that act as transition waypoints. You assign a name of animation to these keyframes which will be referenced by the animation in CSS.</span></li></ul><p><br></p><p><strong style="color: rgb(36, 41, 46);">CSS transitions </strong><span style="color: rgb(36, 41, 46);">are animations with a simpler syntax. They consist of exactly </span><strong style="color: rgb(36, 41, 46);">two states</strong><span style="color: rgb(36, 41, 46);">: start and end state.</span></p><p><br></p><p>For examples and specific properties of these see the <a href="https://github.com/chauff/Web-Teaching/blob/master/Lecture-5.md#bangbang-animations" target="_blank">transcript</a>.</p><p><br></p><p><span style="color: rgb(36, 41, 46);">You could also do animations with JavaScript, which is a lot better if you want to do anything remotely complex as you can do much more with it.</span></p>