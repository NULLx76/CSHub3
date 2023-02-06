+++
title = "Lecture 4 (Node.js)"
date = 2019-09-29
+++
<div style="white-space: normal;" class="markdown-body"><h1 id="lecture-4">Lecture 4</h1>
<p>Node.js is a server-side javascript runtime.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h2 id="event-driven-and-non-blocking">Event-driven and non-blocking</h2>
<p>One of the core concepts of Node is the event loop. Node.js is a single-threaded application that executes callbacks in response to an occurring event (though it is single-threaded, it's easily possible to cluster Node.js to spread load over multiple processes). Developers write those callbacks. The event loop waits for events to enter the event queue and once they have, the events are processed in their order of arrival, i.e. their respective callbacks are executed.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>Node.js can make use of asynchronous operations, therefore, having a kind of faux parallelism. Async operations mainly I/O. Node.js often provides different methods for the same action depending on if you want it to block or not. Non-blocking operations make use of callbacks to signal when they are finished.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h2 id="node.js-in-examples">Node.js in examples</h2>
<p>For examples of how to write node.js you can take a look at the transcript <a href="https://github.com/chauff/Web-Teaching/blob/master/Lecture-4.md">here</a></p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h2 id="express">Express</h2>
<p>Express is a minimalistic web framework for Node.js that provides a thin abstraction layer on top of HTTP to simplify making Node.js web applications. Node.js also has a package repo and manager: npmjs.org which provides many packages so you don't have to re-invent the wheel.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>Example code and a detailed explanation of how to use npm I'll again refer to the <a href="https://github.com/chauff/Web-Teaching/blob/master/Lecture-4.md#express">transcript</a>.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h2 id="json">JSON</h2>
<p>JSON (JavaScript Object Notation) is a text format for Javascript objects (as the name suggests). The main difference between JSON and normal javascript objects is that JSON does not have functions, only data and that all property names must be enclosed in quotes.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h2 id="ajax">Ajax</h2>
<p>Ajax stands for Asynchronous JavaScript and XML. XML is in the name and only that as nowadays JSON is almost exclusively used instead. Ajax is a javascript <strong>mechanism</strong> that enables the dynamic loading of content without having to reload the page manually. Ajax is a technology that injects new data into an existing web page.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>As for how to use Ajax through jQuery look at the <a href="https://github.com/chauff/Web-Teaching/blob/master/Lecture-4.md#ajax-dynamic-updating-on-the-client">transcript</a> this will not be discussed here as it is considered bad practice (one of the most popular ways is by using axios).</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>On how to use Ajax without jQuery you can look at the <a href="https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX/Getting_Started#Step_3_%E2%80%93_A_Simple_Example">MDN</a></p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>The general steps to making an Ajax request are:</p>
<ol>
<li>Creating an XMLHttpRequest Object</li>
<li>The object request data from the server</li>
<li>Receiving data and processing it</li>
</ol>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>Ajax has a <strong>same-origin</strong> policy meaning that data can only be requested and received the origins match (protocol, port and host), there are ways around this but this is not recommended.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h2 id="websockets">WebSockets</h2>
<p>WebSockets are an alternative to Ajax which aims to resolve these issues of it:</p>
<ul>
<li>Ajax requires polling, WebSocket servers can push to their clients</li>
<li>Ajax has a lot of HTTP overhead, WebSocket re-uses the same connection.</li>
<li>The client-side script has to track the mapping from outgoing connections to the incoming connection (in cases where a client make requests to multiple servers).</li>
</ul>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>The WebSocket protocol itself is a TCP-based protocol, the handshake is interpreted by HTTP servers as an upgrade request. Once a connection between a client and server is established (this requires a handshake as the client requests an upgrade to the connection and the server responds to that upgrade before data transfer is possible), data (called messages in this protocol) can be sent back and forth. Both the client and the server can now send messages and we thus no longer need to simulate a single connection, we actually have a single connection.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>In order to close an established connection, a closing handshake is required: both the client and the server can initiate the closing of the connection Also important to know is that WebSocket servers can share a port with HTTP servers due to the HTTP upgrade request ability</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>An example of how to implement WebSockets can be found <a href="https://github.com/chauff/Web-Teaching/blob/master/Lecture-4.md#bangbang-a-first-websocket-example">here</a> and how to do so regarding multi-player games can be found <a href="https://github.com/chauff/Web-Teaching/blob/master/Lecture-4.md#websockets-for-multi-player-games">here</a></p>
</div><p><br></p>