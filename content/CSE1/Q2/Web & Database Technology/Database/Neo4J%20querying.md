+++
title = "Neo4J querying"
date = 2019-02-04
+++
<h2>Cypher language</h2><ul><li><strong>Declarative </strong>graph query language</li><li>Allows for expressive and efficient querying and updates (inspired by SQL and SPARQL)</li><li>Many features stem from improving on SQL pain points (JOIN, GROUP)</li></ul><p><br></p><p><strong>Cypher principles</strong></p><div style="white-space: normal;" class="markdown-body"><ul>
<li>Specification by example</li>
<li>Patterns specified with ASCII-Art inspired syntax
<ul>
<li>Circles <code>()</code> for nodes</li>
<li>Arrows <code>&amp;lt;-</code>, <code>--</code>, <code>-&amp;gt;</code> and <code>[]</code> for relationships</li>
</ul>
</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><p>Example:</p>
<pre data-lang="cypher">MATCH 	(t:Title{
			title: 'The Matrix',
			production_year: 1999}
		)-[r:HAS_CAST]-&gt;(c:CastInfo)&lt;-[s:PARTICIPATES_IN]-(p:Person)
RETURN distinct p.name
</pre>
</div><p><br></p><h2>Query clauses</h2><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>MATCH</code>, specifies <strong>graph patterns</strong> to be searched for
<ul>
<li>Search for sub-graphs of the dadta graph that match <strong>all</strong> the <strong>patterns</strong> in the query (patterns can occur many times in the graph)</li>
<li>The query result is a set of <strong>variable bindings</strong>, each variable has to be bounded to a node/relationship</li>
<li>Queries can return a <strong>graph</strong> or a <strong>table</strong></li>
<li>Results are unordered</li>
</ul>
</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>WHERE</code>, <strong>filtering</strong> constraints on nodes and relationships
<ul>
<li>Add constraints to the pattern to be matched, evaluation is at matching time</li>
<li>Usual operations
<ul>
<li>Checking on existing properties</li>
<li>Range (<code>&amp;lt;</code>, <code>&amp;lt;=</code>, <code>&amp;gt;</code>, <code>&amp;gt;=</code>)</li>
<li>String matching (<code>starts with</code>, <code>ends with</code>, <code>contains</code>, regex)</li>
</ul>
</li>
<li>Boolean operations (<code>AND</code>, <code>OR</code>, <code>XOR</code>, <code>NOT</code>)</li>
<li>Filters on node labels, node properties, relationship types, relationship properties</li>
<li>Path patterns can also be predicates, <code>true</code> if at least one solution is found, no new variables</li>
<li>Path patterns in <code>MATCH</code> behave differently than path patterns in <code>WHERE</code>
<ul>
<li><code>MATCH</code>: patterns produce subgraph for every found path</li>
<li><code>WHERE</code>: filters any matched sub-path where connected nodes have no relationship</li>
</ul>
</li>
</ul>
</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>RETURN</code>, defines <strong>returned</strong> data
<ul>
<li>Defines what to include in the query result set</li>
<li>Projection of node and relationship variables</li>
<li>Literals, predicates, properties and functions can also be returned</li>
<li><code>DISTINCT</code> receives only unique rows depending on the column that have been selected to output</li>
</ul>
</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>ORDER BY</code>, describes how results should be <strong>ordered</strong>
<ul>
<li>By default, order of results is not defined</li>
<li>Multiple criteria can be specified (default direction is <code>ASC</code>)</li>
<li>Sorting is only allowed on properties, not on nodes and relationships</li>
</ul>
</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>UNION</code>, merges results from two or more queries
<ul>
<li>Combines the result of multiple queries</li>
<li>Number and names of columns must be identical in all queries</li>
<li><code>UNION ALL</code> keeps duplicates</li>
</ul>
</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>WITH</code>, chains subsequent query parts and forwards results from one to the next
<ul>
<li>Behaves analogously to the <code>RETURN</code> clause</li>
<li>Does not output anything to the user, just forwards the current result to the subsequent clause. The output of one part is passed as input to another.</li>
<li>Useful to filter on aggregate values (there is no <code>HAVING</code> clause in Cypher)</li>
<li>But it can also be used to decompose queries into "sub-queries"</li>
</ul>
</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>NULL</code>, missing value evaluates to <code>null</code>, checking for it in a node will make the condition <code>false</code>. The syntax is equal to SQL.</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>OPTIONAL MATCH</code>, when no solution is found, one specific solution with all the variables bound to <code>NULL</code> is generated
<ul>
<li>Pretty much a <code>LEFT JOIN</code></li>
<li>Either the whole pattern is matched or nothing is matched</li>
</ul>
</li>
</ul>
</div><p><br></p><h2>Node pattern</h2><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">(variable:Label:..:Label{key: expression, ..., key: expression})
</pre>
</div><ul><li>Matches nodes</li><li><strong>Variable: </strong>used to refer/access nodes</li><li><strong>Labels: </strong>all nodes labels to be matched</li><li><strong>Properties: </strong>properties of the nodes to be matched, order is not important</li></ul><p><br></p><h2>Path pattern</h2><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">()&lt;-|-[variable:type|...|type variableLength {key: expression, ..., key: expression}]-|-&gt;()
</pre>
</div><ul><li>Describe multiple nodes and one or more relationships among them</li><li>A series of connected nodes is called a <strong>path</strong></li><li class="ql-indent-1">A traversal of part of the graph</li><li class="ql-indent-1">Describes a single path, not a general sub-path</li><li class="ql-indent-1">Used as part of a query to specify patterns</li><li><strong>Variable: </strong>used to refer/access relationships</li><li><strong>Type: </strong>all relationship types to be matched</li><li><strong>VariableLength: </strong>describes paths of arbitrary lengths (not just one relationship)</li><li><strong>Properties: </strong>properties of the relationships to be matched</li></ul><p><br></p><h2>Aggregation functions</h2><p>Aggregation functions are analogous to SQL's <em>GROUP BY</em></p><ul><li>Compute over all matching subgraphs</li><li>Non-aggregate-expressions are used as group by, matching sub-graphs are divided in buckets according to the key value<em> </em></li></ul><p><br></p><p>Classic functions (<em>avg, count, max, min, sum)</em></p><p><br></p><div style="white-space: normal;" class="markdown-body"><p><code>collect</code> returns a list containing the values returned by an expression</p>
</div><p><br></p><h2>Improving performance</h2><ul><li>Use parameters instead of literals when possible, cypher can re-use queries</li><li>Set upper limit for variable length pattern</li><li>Return only the data you need, avoid returning whole nodes and relationships</li><li>Use <strong>PROFILE / EXPLAIN </strong>to analyse the performance of your queries</li><li>Know/learn the types of questions to answer, then create new relationships that speed up these questions</li><li>Use indexes</li></ul><p><br></p><h1>Examples</h1><h2>Nodes</h2><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">(t) // any node, referred by the variable 't'
</pre>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">(t:Title) // nodes with label 'Title'
</pre>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">(t:Title:Person) // nodes with labels 'Title' **and** 'Person'
</pre>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">(t:Title{title:'The Matrix', production_year: 1999}) // nodes with label 'Title' having properties with the specified values
</pre>
</div><p><br></p><h2>Path patterns</h2><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">(t)-[r:HAS_CAST]-(c) // matches relationships of type 'HAS_CAST' between all nodes
</pre>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">(t)-&gt;(c) // matches all relationships from 't' (any node) to 'c' (any node)
</pre>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">(t)--(c) // matches relationships in any direction between 't' to 'c'
</pre>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">(t:Title)-&gt;(c) // all relationships from nodes with label 'Title'
</pre>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">(t)&lt;-[HAS_CAST]-(c) // relationship of type 'HAS_CAST' from 'c' to 't'
</pre>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">(t)-[HAS_CAST|HAS_KEYWORD]-&gt;(c) // relationships of type 'HAS_CAST' or 'HAS_KEYWORD' from 't' to 'c'
</pre>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">(t)-[r]-(c) // binds the relationships to the variable 'r'
</pre>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">(t)-[*1..5]-(c) // variable length path, from 1 to 5 relationships between 't' and 'c'
</pre>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">(t)-[*]-(c) // variable path of any number of relationships, from 't' to 'c'
</pre>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">(t)-[HAS_CAST]-(c {movie_id:'2543774'}) // A relationship of type 'HAS_CAST' from a node 't' to a node 'c' having declared property
</pre>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">shortestPath((p1:Person)-[*..6]-((p2:Person)) // Find a single shortest path between any two nodes 'Person'
</pre>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">size((t)--&gt;()--&gt;()) // Count the paths matching the pattern
</pre>
</div><p><br></p><h2>Return clause</h2><div style="white-space: normal;" class="markdown-body"><p>Returns distinct people name, a <code>true/false/null</code> value if they are female, and a constant literal:</p>
<pre data-lang="cypher">MATCH (t:Title{
		title: 'The Matrix',
		production_year: 1999
	})-[r:HAS_CAST]-&gt;(c:CastInfo)&lt;-[s:PARTICIPATES_IN]-(p:Person)
RETURN distinct p.name, p.gender = ‘f’, ‘A Literal’
</pre>
</div><div style="white-space: normal;" class="markdown-body"><p>Returns a collection of nodes:</p>
<pre data-lang="cypher">MATCH (t:Title{
		title: 'The Matrix',
		production_year: 1999
	})-[r:HAS_CAST]-&gt;(c:CastInfo)&lt;-[s:PARTICIPATES_IN]-(p:Person)
RETURN t,p
</pre>
</div><div style="white-space: normal;" class="markdown-body"><p>Returns a graph:</p>
<pre data-lang="cypher">MATCH (t:Title{
		title: 'The Matrix',
		production_year: 1999
	})-[r:HAS_CAST]-&gt;(c:CastInfo)&lt;-[s:PARTICIPATES_IN]-(p:Person)
RETURN t,r,c,s,p
</pre>
</div><p><br></p><h2>Where clause</h2><div style="white-space: normal;" class="markdown-body"><p>Like a SQL <code>WHERE</code>:</p>
<pre data-lang="cypher">MATCH (p:Person)
WHERE p.name_pcode_cf='A1652' AND p.name_pcode_nf='J2165'
RETURN p.name, p.gender
</pre>
</div><div style="white-space: normal;" class="markdown-body"><p>Matching using regex:</p>
<pre data-lang="cypher">MATCH (t:Title)
WHERE t.title=~ 'S.*'
RETURN t.title, t.production_year
</pre>
</div><div style="white-space: normal;" class="markdown-body"><p>Path patterns with <code>WHERE</code>:</p>
<pre data-lang="cypher">MATCH (t:Title)
WHERE t.title=~ '.*Matrix.*' AND (t)-[:HAS_CAST]-({note:'(creator)'})
RETURN t.title, t.production_year
</pre>
</div><p><br></p><h2>NULL</h2><div style="white-space: normal;" class="markdown-body"><p>Null check:</p>
<pre data-lang="cypher">MATCH (t:Title)
WHERE t.production_year &gt; 2000 OR t.production_year IS NULL
RETURN t.title, t.production_year
</pre>
</div><p><br></p><h2>Aggregation functions</h2><div style="white-space: normal;" class="markdown-body"><p>Count:</p>
<pre data-lang="cypher">MATCH (cn:CharName{char_name:'Neo'})-[PERFORMED_AS]-(c:CastInfo)
RETURN COUNT(cn)
</pre>
</div><div style="white-space: normal;" class="markdown-body"><p>Collect:</p>
<pre data-lang="cypher">MATCH (t:Title)
WHERE t.title=~ '.*Matrix.*'
RETURN collect(t.title)
</pre>
</div><div style="white-space: normal;" class="markdown-body"><p>Group by:</p>
<pre data-lang="cypher">MATCH (t:Title)-[r:HAS_CAST]-&gt;(c:CastInfo)&lt;-[s:PARTICIPATES_IN]-(p:Person)
RETURN t.title, t.production_year, COUNT(c) AS Total
</pre>
</div><div style="white-space: normal;" class="markdown-body"><p>With:</p>
<pre data-lang="cypher">MATCH (t:Title)-[r:HAS_CAST]-&gt;(c:CastInfo)&lt;-[s:PARTICIPATES_IN]-(p:Person)
WITH p.name AS actor, avg(t.production_year) AS average_acting_year
WHERE average_acting_year &gt; 2000
RETURN actor, average_acting_year
</pre>
</div><div style="white-space: normal;" class="markdown-body"><p>Subqueries:</p>
<pre data-lang="cypher">MATCH (k:KindType{kind_name:'movie'})
WITH k.kind_id AS movie_kind
MATCH (t:Title)
WHERE t.kind_id = movie_kind
RETURN t.title
</pre>
</div><p><br></p><h2>Optional match</h2><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">MATCH (c:CastInfo)&lt;-[s:PARTICIPATES_IN]-(p:Person)
WHERE p.name = 'Reeves, Keanu'
OPTIONAL MATCH (c)-[pa:PERFORMED_AS]-&gt;(cn:CharName)
RETURN p.name, cn.char_name
</pre>
</div><p><br></p><h2>Order by</h2><div style="white-space: normal;" class="markdown-body"><pre data-lang="cypher">MATCH (t:Title)
RETURN t
ORDER BY t.production_year DESC, t.title ASC
</pre>
</div>