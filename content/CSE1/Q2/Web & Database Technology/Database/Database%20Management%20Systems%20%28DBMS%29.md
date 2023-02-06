+++
title = "Database Management Systems (DBMS)"
date = 2019-01-19
+++
<div class="markdown-body" style="white-space: normal;"><h2>Main functions of a DBMS</h2>
<p>The main functions of a DBMSs are generally described as the <strong>CRUD</strong> operations (Create, read, update and delete), and more specifically a DBMS should at least be able to do the following</p>
<h4>Queries</h4>
<ul>
<li>Retrieve data that match certain selection criteria expressed in the</li>
<li>Queries do not change the state of the database</li>
</ul>
<h4>Transactions</h4>
<ul>
<li>To insert, delete, and update data in the database.</li>
<li>Transactions change the state of the database</li>
</ul>
<h4>Security</h4>
<ul>
<li>Authentication, i.e. verification of the identity of a client application</li>
<li>Authorization, i.e. the enforcement of access and execution rules for
queries and transactions</li>
</ul>
<h3>Typical features of DBMSs</h3>
<h4>Data Integrity and Evolution</h4>
<ul>
<li>Durability, Integrity, Correctness, Evolvability</li>
</ul>
<h4>Performance</h4>
<ul>
<li>Scalability,, Elasticity, Latency, Throughput, Partition Tolerance</li>
</ul>
<h4>Security and Privacy</h4>
<ul>
<li>Security, Confidentiality, Non-Repudiation</li>
</ul>
<h3>Additional advantages of DBMSs</h3>
<ul>
<li>Reduced application development time</li>
<li>Economies of scale</li>
<li>Efficient query processing</li>
<li>Several (built-in or external) user interfaces</li>
<li>Self-describing nature
<ul>
<li>DBMSs might contain complete definition of structure (Meta-data) and rules of validity</li>
</ul>
</li>
</ul>
<h2>Classification of DMBSs</h2>
<h3>by Type of usage</h3>
<h4>Operational Databases or OnLine Transaction processing (OLTP)</h4>
<p>These databases have as main function the management of dynamic data in real-time.</p>
<h4>Analytical databases or OnLine Analytical Processing (OLAP)</h4>
<p>These databases that meant to support
tactical or strategic decision making by means of interactive analysis of multi-dimensional data.
In OLAP systems the emphasis is on the integration of data, possibly from
difterent databases, to allow for complex analytical and ad hoc queries with a rapid execution
time.</p>
<h3>by Distribution</h3>
<h4>Centralized</h4>
<p>A database that is located, stored, and maintained in a single location. In most cases, a centralised database would be used by an organisation or an institution.</p>
<h5>Advantages</h5>
<ul>
<li>Data integrity is maximized</li>
<li>Data redundancy is minimized</li>
</ul>
<h5>Disadvantages</h5>
<ul>
<li>Dependence on network and hardware therefore hard to scale</li>
<li>Single point of
failure for hardware and security.</li>
</ul>
<h4>Distributed or Decentralised</h4>
<p>Database systems where the DBMS software is distributed from various
sites that are connected by a computer network. We
can also distinguish between <em>heterogeneous</em> distributed database system – where different sites
might use different DBMS software, but there is additional common software to support data
exchange between these sites – and <em>homogeneous</em> distributed database systems: use the same
DBMS software at multiple sites. Data is also stored in multiple computers, these computers can be centralized or distributed.</p>
<p>Distributed RDMS allow for replication and duplication. Replication is obtained in a continuous
incremental manner, by propagating changes in each node. Duplication is performed by first selecting a master node, and then regularly copy its content into slave nodes; the master node is the only one accepting changes.</p>
<h5>Advantages</h5>
<ul>
<li>Increase reliability and availability.</li>
<li>Increased scalability and elasticity.</li>
<li>Cheaper (commodity) hardware.</li>
</ul>
<h5>Disadvantages</h5>
<ul>
<li>Complex w.r.t maintaining integrity, security, and just multiple systems in general</li>
<li>Data modelling and querying are also more challenging
<ul>
<li>e.g. joins become prohibitively expensive when
performed across multiple systems.</li>
</ul>
</li>
</ul>
<h3>by Data model</h3>
<p>Roughly speaking, we distinguish two big classes of DBMS.
The so called relational database management systems and the non-relational database management
systems, now commonly know as No-SQL. Notice that No-SQL stands for “not-only SQL”, and not as a
negation for SQL, as commonly assumed.</p>
<h4>Relation model</h4>
<p>The most common and predominant model for storing data is based on the idea of a <strong>relational model</strong>.
seventies. The model stores data as tuples, forming an ordered set of
attributes. In turn, a relation consists of sets of tuples. In terms of relational database systems, a tuple
is a row, an attribute is a column and a relation forms a table. SQL has established itself as generic
data definition, manipulation and query language for relational data. Relational database implementations typically rely on
sophisticated transaction and locking mechanisms in order to ensure <strong>A</strong>tomicity, <strong>C</strong>onsistency, <strong>I</strong>solation,
and <strong>D</strong>urability (the so-called properties ACID, described in <a href="https://cshub.nl/post/487433115">this</a> post)</p>
<h4>Dimensional model</h4>
<p>Dimensional models adopt the relational model, but are specialized for analytical operations. In dimensional models, the concepts of facts, and dimensions are separated. Facts are typically (but not always) numeric values that can be aggregated, and
dimensions are groups of hierarchies and descriptors that define the facts. Every dimensional model is
composed of one table with a multipart key, called the fact table, and a set of smaller tables called
dimension tables. Each dimension table has a single-part primary key that corresponds exactly to one
of the components of the multipart key in the fact table.  This characteristic “star-like”
structure is often called a star join.</p>
<h4>Key/Value store</h4>
<p>The idea of <strong>key/value-based</strong> storage system is very old. The storages allow to record tuples only containing a key and
a value. While the key uniquely identifies an entry, the value is an arbitrary chunk of data and in most
cases opaque for the database.</p>
<h4>Document stores</h4>
<p>Document stores are similar to key/value stores. However, they require structured data as values
using formats like XML or JSON. There are often no fixed schema definitions.</p>
<h4>Wide-column</h4>
<p>Database systems that store data by columns rather than by rows.
A major benefit is the efficiency of I/O operations during data access, when the column-oriented layout speeds up aggregation
or column-based search/filter operations.</p>
<h4>Graph database</h4>
<p>Use graph structures for data modeling,
thus nodes and edges represent and contain data. Nodes are often used for the main data entities,
while edges between nodes are used to describe relationships.</p>
<h2>History of DBMSs</h2>
<p>If you want to know more about the history of DBMSs I refer you to page 17 of the DB1-Lecture9 Lecture notes.</p>
<h6>For information about Database languages or Data Abstraction and Modelling please refer to the relevant CSHub posts</h6>
</div>