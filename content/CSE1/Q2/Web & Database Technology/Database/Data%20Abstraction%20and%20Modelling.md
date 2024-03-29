+++
title = "Data Abstraction and Modelling"
date = 2019-09-29
+++
<div style="white-space: normal;" class="markdown-body"><h2 id="data-abstraction-and-modelling">Data Abstraction and Modelling</h2>
<p>The major purpose of a database system is to provide users with an abstract view of the system. Complexity should be hidden from database users. Understanding improved by highlighting only the essential features of data.</p>
<p><strong>Program-Data Independence</strong>: The system hides certain details of how data is created, stored, maintained, and accessed.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h3 id="three-schema-architecture">Three schema architecture</h3>
<p>Goals is to separate the user application from the physical database.</p>
<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/4-2_ANSI-SPARC_three_level_architecture.svg/320px-4-2_ANSI-SPARC_three_level_architecture.svg.png" alt=""></p>
<p><em>Image taken from slides by Alessandro Bozzon</em></p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p><strong>External/View Level</strong>: describe part of the database that is of interest for a category of users</p>
<p><strong>Internal/Physical Schema</strong>: description of the physical structure of the database, including details
about data storage and access paths</p>
<p><strong>Conceptual Level</strong>: hides the details of the physical storage and focus on entities, data types,
relationships, user operations, and constraints.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h3 id="data-independence">Data independence</h3>
<p>Guaranteed by the multi-level architecture. The two forms of data independence</p>
<ul>
<li>Logical: Change the conceptual schema without changing external schema or application programs</li>
<li>Physical: Change the internal schema without changes the conceptual schema.</li>
</ul>
<h3 id="functional-independence">Functional independence</h3>
<p>Capacity to change the implementation of a function (method) without impact on software applications.
This is often referred to as <strong>information hiding</strong></p>
<h5>Function</h5>
<ul>
<li>Interface name of the function, and its arguments</li>
<li>Method: how the functions is executed</li>
</ul>
</div>