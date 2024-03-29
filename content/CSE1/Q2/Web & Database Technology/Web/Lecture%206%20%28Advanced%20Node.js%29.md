+++
title = "Lecture 6 (Advanced Node.js)"
date = 2019-09-29
+++
<div style="white-space: normal;" class="markdown-body"><h1 id="lecture-6">Lecture 6</h1>
<h2 id="node.js-modules">Node.js modules</h2>
<p>In Node.js each file is its own module. This means that the code we write in a file does not pollute the <em>global namespace</em>. Modules can also be a directory of files with the entry point being an <code>index.js</code> file.</p>
<p>The module system works as follows: each Node.js file can access its so-called module definition through the module object. The module object is your entry point to modularize your code. To make something available from a module to the outside world, <code>module.exports</code> or its alias <code>exports</code> is used.</p>
<p>Once a module has been defined you can use the globally defined <code>require</code> function to import it (Note: <code>require</code> is blocking).</p>
<p><a href="https://github.com/chauff/Web-Teaching/blob/master/Lecture-6.md#bangbang-a-first-module-example">Example</a></p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h2 id="middleware">Middleware</h2>
<p>Middleware are pieces of code that can sit "in the middle" of other tasks.  Middleware functions have access to the <a href="https://expressjs.com/en/4x/api.html#req">request object</a> (<code>req</code>), the <a href="https://expressjs.com/en/4x/api.html#res">response object</a> (<code>res</code>) and the <code>next</code> middleware function in the application's request-response cycle.</p>
<p>Middleware functions can perform the following tasks:</p>
<ul>
<li>Execute any code.</li>
<li>Make changes to the request and the response objects.</li>
<li>End the request-response cycle.</li>
<li>Call the next middleware function in the stack.</li>
</ul>
<p>There exist multiple types of middleware with the most common being router middleware that sits between each request.</p>
<p><a href="https://expressjs.com/en/guide/using-middleware.html">More info</a></p>
<p><a href="https://github.com/chauff/Web-Teaching/blob/master/Lecture-6.md#bangbang-logger-example">Example</a></p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h3 id="configuring-middleware">Configuring middleware</h3>
<p>To make middleware functions more reusable you can wrap them in a setup function so that you can pass it parameters, you can do so like this:</p>
<pre data-lang="javascript"><code>function setup(options) {
    // setup logic
    return function(req, res, next) {
        // middleware logic
    }
}
app.use( setup({ param1 : 'value1' }) );
</code></pre>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h2 id="routing-in-express">Routing in Express</h2>
<p><strong>Routing</strong> refers to how an application’s endpoints (URIs) respond to client requests. In Express you define routes using the methods of the app object that correspond to HTTP methods (<code>app.get()</code> or <code>app.post</code> for GET and POST requests respectively). Route handlers are middleware.</p>
<p>Routing (in Express) is different to the standard <strong>filesystem-based</strong> routing in which each directory and file corresponds to a route in the sense that you define methods to handle your routes instead.</p>
<p><a href="https://expressjs.com/en/guide/routing.html">Examples of how to route in Express</a></p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h3 id="routing-paths-and-string-patterns">Routing paths and string patterns</h3>
<p>We specify a path (like <code>/todos</code>) in a route, the path is eventually converted into a regular expression (regex in short) by Express.
Regular expressions are patterns to match character combinations in strings. They are very powerful and allow us to specify matching patterns instead of hard-coding all potential routes. Express distinguishes three different types of route paths: strings, string patterns and regular expressions. So far, we have employed just strings to set route paths. String patterns are routes defined with strings and a subset of the standard regex meta-characters, namely: <code>+ ? * ( ) []</code>.</p>
<p>Express' string pattern meta-characters have the following interpretations:</p>
<table>
<thead>
<tr>
<th>Character</th>
<th>Description</th>
<th>Regex</th>
<th>Matched expressions</th>
</tr>
</thead>
<tbody>
<tr>
<td>+</td>
<td>one or more occurrences</td>
<td>ab+cd</td>
<td>abcd, abbcd, …</td>
</tr>
<tr>
<td>?</td>
<td>zero or one occurrence</td>
<td>ab?cd</td>
<td>acd, abcd</td>
</tr>
<tr>
<td>*</td>
<td>zero or more occurrences of any char (wildcard)</td>
<td>ab*cd</td>
<td>abcd, ab1234cd, …</td>
</tr>
<tr>
<td>[…]</td>
<td>match anything inside for one character position</td>
<td>ab[cd]?e</td>
<td>abe, abce, abde</td>
</tr>
<tr>
<td>(…)</td>
<td>boundaries</td>
<td>ab(cd)?e</td>
<td>abe, abcde</td>
</tr>
</tbody>
</table>
<p>It is important to realize that the use of <code>*</code> in Express' string patterns is somewhat unique. In most other languages/frameworks, whenever <code>*</code> is mentioned in relation to regular expressions, it refers to zero or more occurrences of the preceding element. In Express' string patterns, <code>*</code> is a wildcard.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h3 id="routing-parameters">Routing parameters</h3>
<p>Besides regular expressions, routing parameters can be employed to enable variable input as part of the route.
To do so you define a route string like so <code>"/route/:parameter"</code> (notice the colon before the parameter). This will match any parameter not containing a slash. These can then be accessed by <code>req.params.type</code> and if you have multiple they can be accessed like so <code>[req.params.type][req.params.level]</code></p>
<p><a href="https://github.com/chauff/Web-Teaching/blob/master/Lecture-6.md#routing-parameters">Examples</a></p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h3 id="organizing-routes">Organizing routes</h3>
<p>It is recommended to put all your routes in one file to maintain maintainability.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h2 id="templating-with-ejs">Templating with EJS</h2>
<p>Templating can be used to embed Javascript inside the HTML that is sent to the client (Normally you'd use a framework or a better templating engine like pug, however, we need to know EJS).</p>
<p>Basic EJS syntax:</p>
<pre data-lang="javascript"><code>const ejs = require('ejs');
const template = '&lt;%= message %&gt;'; //&lt;%= outputs the value into the template (HTML escaped)
const data = {message: 'Hello template!'};
console.log(ejs.render(template, data)); // Outputs "Hello template"
</code></pre>
<p>Be careful not to use <code>&lt;%-</code> as this enables XSS and is therefore considered insecure</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>Multiple examples can be found <a href="https://github.com/chauff/Web-Teaching/blob/master/Lecture-6.md#bangbang-a-first-ejs-example">here</a>.</p>
</div>