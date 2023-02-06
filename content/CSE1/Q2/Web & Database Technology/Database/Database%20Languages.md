+++
title = "Database Languages"
date = 2019-01-17
+++
<div style="white-space: normal;" class="markdown-body"><h2>Database Languages</h2>
<h3>Language types</h3>
<h4>Data Definition Language (DDL)</h4>
<ul>
<li>Defines the logical and physical schema</li>
<li>Often used also for access authorisation specification</li>
</ul>
<h4>Data Manipulation Language (DML)</h4>
<p>Allows retrieval, insertion, deletion, modification of database
instances.</p>
<h4>Storage Definition Language (SDL)</h4>
<p>Specifies the internal schema.</p>
<h4>View Definition Language (VDL)</h4>
<ul>
<li>Specifies user views/mapping to conceptual schema</li>
<li>Typically the same as DDL</li>
</ul>
<h3>Languages</h3>
<h4>Various forms</h4>
<ul>
<li>Interactive textual and declarative language
<ul>
<li>SQL, Cypher, MongoDB QL</li>
</ul>
</li>
<li>Interactive commands embedded in a host language (Python, C++, Java)</li>
<li>By means of non-textual user-friendly interfaces:
<ul>
<li>GUIs</li>
<li>Natural Language interfaces</li>
</ul>
</li>
</ul>
<h3>DML Languages Classification</h3>
<h4>High-level or nonprocedural DML</h4>
<ul>
<li>Specifies what data should be retrieved, or what changes should be made</li>
<li>DBMS determines automatically the best way to retrieve or modify the data</li>
<li>Set-at-a-time or set-oriented</li>
</ul>
<h4>Low-level or procedural DML</h4>
<ul>
<li>Specifies how to navigate the database to locate and modify the data</li>
<li>Can be embedded in a general-purpose programming language</li>
<li>Record-at-a-time (usually starts by positioning on one specific record and navigate from there onwards to other records)</li>
</ul>
</div>