+++
title = "SQL"
date = 2020-02-15
+++
<h1 id="sql">SQL</h1><h2 id="requirements-of-a-database-language">Requirements of a database language</h2><p><strong>Functional</strong></p><ul><li>Create database and relation structures</li><li>Perform data management tasks (CRUD)</li><li>Perform simple and complex queries</li></ul><p><br></p><p><strong>Non-functional requirements</strong></p><ul><li>Structure and syntax easy to learn</li><li>Portability across systems</li></ul><p><br></p><h2 id="sql-language">SQL Language</h2><ul><li><strong>S</strong>tructured <strong>Q</strong>uery <strong>L</strong>anguage</li><li>Far richer than a query language: a <strong>DML (Data Manipulation Languag</strong><strong>e)</strong><span style="background-color: rgba(0, 0, 0, 0);">, a </span><strong style="background-color: rgba(0, 0, 0, 0);">DDL (Data DefinitionLanguage) </strong><span style="background-color: rgba(0, 0, 0, 0);">/ </span><strong style="background-color: rgba(0, 0, 0, 0);">VD</strong><strong>L </strong><strong>(Visualization Description Language)</strong></li><li><strong>Set-based </strong>language, operators work on relations (tables) and results are always relations</li><li>SQL is declarative, it describes <strong>what </strong>to do, not how to do it</li><li>SQL is standardized, with different vendors supporting different versions</li></ul><p><br></p><h1 id="querying"><strong>Querying</strong></h1><h2 id="select-clause">Select clause</h2><p>Used with a FROM clause, lists the attributes (columns) that will be returned from the queried relation (table) specified in the FROM clause. </p><p><br></p><div style="white-space: normal;" class="markdown-body"><p>Find the code of <strong>all</strong> products in the DB:</p>
<pre data-lang="text/x-sql"><code>SELECT CodeP
FROM Products
</code></pre>
<p>A wildcard (*) can be used to select all the columns, for example, find all the information relating to employees named “Brown”</p>
<pre data-lang="text/x-sql"><code>SELECT *
FROM Employee
WHERE Surname = "Brown"
</code></pre>
<p>The keyword <code>AS</code> allows the definition of an alias. Used in attribute expressions, it defines a new temporary column per the calculated expression. For example, find the monthly salary of the employees named "White"</p>
<pre data-lang="text/x-sql"><code>SELECT Salary / 12 AS MonthlySalary
FROM Employee
WHERE Surname = "White"
</code></pre>
<p>No duplicates results can be obtained using the <code>DISTINCT</code> keyword. For example, find the code of the products supplied at least by one supplier</p>
<pre data-lang="text/x-sql"><code>SELECT DISTINCT CodeP
FROM Supply
</code></pre>
</div><p><br></p><h2 id="where-clause">Where clause</h2><ul><li>Selection conditions apply to each single tuple resulting form the evaluation of the <strong>FROM</strong> clause</li><li>Defined as a boolean expression of simple predicates (comparison between attributes, set membership, NULL values, text matching etc)</li></ul><p><br></p><div style="white-space: normal;" class="markdown-body"><p>Find the first names and surnames of the employees who work in office number 20 of the "Administration" department</p>
<pre data-lang="text/x-sql"><code>SELECT FirstName, Surname
FROM Employee
WHERE Office = "20" AND Dept = "Administration"
</code></pre>
<p>More complex logical operators can also be used. For example, Find the first names of the employees named "Brown" who work in the "Administration" department or the "Production" department</p>
<pre data-lang="text/x-sql"><code>SELECT FirstName
FROM Employee
WHERE Surname = "Brown" AND (Dept = "Administration" OR Dept = "Production")
</code></pre>
<p>The like operator can be used to match string patterns. The <code>_</code> is matching a term for a single character, <code>%</code> for zero or more characters. For example, find the employees with surnames that have "r" as the second letter and that end in "n"</p>
<pre data-lang="text/x-sql"><code>SELECT *
FROM Employee
WHERE Surname LIKE "_r%n"
</code></pre>
</div><p><br></p><h2 id="null-values">NULL values</h2><div style="white-space: normal;" class="markdown-body"><p>Using the <code>IS NULL</code> operator. For example, find the code and the name of products having size greater than 44, or that <strong>might</strong> have size greater than 44 (so unknown)</p>
<pre data-lang="text/x-sql"><code>SELECT CodeP, NameP
FROM Products
WHERE Size IS NULL
</code></pre>
</div><p><br></p><h2 id="ordering">Ordering</h2><ul><li>The <strong>ORDER BY</strong> clause, at the end of the query, orders the rows of the results</li><li>Last operator applied by the database in the query execution plan</li><li>The default ordering is <strong>ASC</strong></li></ul><p><br></p><div style="white-space: normal;" class="markdown-body"><p>Find all the information about products, in ascending order of name and descending order of size</p>
<pre data-lang="text/x-sql"><code>SELECT *
FROM Products
ORDER BY NameP, Size DESC
</code></pre>
<p>Find the code and the american size of all the products, in ascending order of size</p>
<pre data-lang="text/x-sql"><code>SELECT CodeP, Size - 14 AS AmericanSize
FROM Products
ORDER BY AmericanSize
</code></pre>
</div><p><br></p><h2 id="joining-tables">Joining tables</h2><p>Sometimes we want to match data from different tables, for example getting all the suppliers of a single product, which can be done using a couple of techniques.</p><p><br></p><div style="white-space: normal;" class="markdown-body"><p>Using a simple join: find the name of all the suppliers of product "P2"</p>
<pre data-lang="text/x-sql"><code>SELECT NameS
FROM Supplier, Supply
WHERE Supplier.CodeS = Supply.CodeS AND CodeP = "P2"
</code></pre>
<p>The <code>WHERE Supplier.CodeS = Supply.CodeS AND CodeP = "P2"</code> statement is a <strong>join condition</strong></p>
<p>But in SQL-2 a newer (better) version of JOINs arrived, using the following syntax:</p>
<pre data-lang="text/x-sql"><code>SELECT TargetList
FROM Table [[AS] Alias]
	{ [JoinType] JOIN Table [[AS] Alias] [ON BooleanExpression || USING JoinColumns]}
[ WHERE Conditions ]
</code></pre>
<p>The <code>JoinType</code> can be one of the following:</p>
<ul>
<li><code>INNER</code>, default type of join in a joined table. A tuple is included in the results only if a matching tuple exists in the other relation</li>
<li><code>RIGHT (OUTER)</code>, every tuple in left table must appear in result. If no matching tuple: values for attributes in the right table set to <code>NULL</code></li>
<li><code>LEFT (OUTER)</code>, every tuple in right table must appear in result. If no matching tuple: values for attributes in the left table set to <code>NULL</code></li>
<li><code>FULL (OUTER)</code>, if no matching tuple: values for attributes in the left and/or right tables set to NULL
The <code>JoinType</code> also can preceded by <code>NATURAL</code>, meaning that no join condition is specified</li>
</ul>
<p>Find the name of supplier of at least one red product</p>
<pre data-lang="text/x-sql"><code>SELECT DISTINCT NameS
FROM Products 
INNER JOIN Supply ON Products.CodeP = Supply.CodeP
INNER JOIN Supplier USING (CodeS) # Both syntaxes are equal
WHERE Color = "Red"
</code></pre>
<p>Find the code and name of Supplier, and the code of the supplied Products, showing also suppliers of no products</p>
<pre data-lang="text/x-sql"><code>SELECT Supply.CodeS, Supplier.NameS, Supply.CodeP
FROM Supplier 
LEFT OUTER JOIN Supply ON Supplier.CodeS = Supply.CodeS
</code></pre>
</div><p><br></p><h2 id="aggregation">Aggregation</h2><ul><li>Aggregate query: query in which the result depends on the consideration of sets of rows. Result is a single (aggregated) value</li><li>Five aggregate operations: <em>COUNT, SUM, MAX, MIN, MAX, </em>which all return <em>NULL </em>when no rows are selected</li></ul><p><br></p><p><strong>Count</strong></p><p>COUNT returns the number of rows or distinct values. Syntax:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-sql"><code>COUNT (&lt;* | [DISTINCT | ALL] TargetList &gt;)
</code></pre>
<p>Find the number of suppliers in the database:</p>
<pre data-lang="text/x-sql"><code>SELECT COUNT (*)
FROM Supplier
</code></pre>
<p>Count the number of suppliers that supply the product "P2":</p>
<pre data-lang="text/x-sql"><code>SELECT COUNT(*)
FROM Supply
WHERE CodeP = "P2"
</code></pre>
</div><p><br></p><p><strong>Operators</strong></p><p>For all operators (sum, max, min, avg) allowed arguments are attributes (columns) or expressions. </p><p>Sum and avg can only handle numeric types, while max and min apply on sortable types (numeric, strings, timestamps)</p><p><br></p><h2 id="null-values-and-aggregates"><strong>Null values and aggregates</strong></h2><p>All aggregate operations ignore tuples with <em>NULL</em> values on the aggregated attributes</p><ul><li><strong>COUNT</strong>: number of input rows for which the value of expression is not <em>NULL</em></li><li><strong>SUM, AVG, MAX, MIN</strong>: <em>NULL </em>values are not considered</li></ul><p><br></p><p>The <strong>COALESCE </strong>function (returns the first non-null value in a list) can be used to force a value for <em>NULL</em>, like so:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="sql"><code>SELECT AVG(COALESCE(season_nr,1))
FROM title_100k
</code></pre>
</div><p><br></p><h2 id="group-by-clause">Group by clause</h2><p>The order of the grouping attributes does not matter. </p><p>The SELECT clause can contain:</p><ul><li> Attributes specified in the GROUP BY clause</li><li> Aggregated functions</li><li> Attributes univocally determined by attributes already specified in the GROUP BY clause.</li></ul><div style="white-space: normal;" class="markdown-body"><p>For each product sold by suppliers in Den Haag, find the total amount of supplied items</p>
<pre data-lang="sql"><code>SELECT CodeP, SUM(Amount)
FROM Supply JOIN Supplier ON Supply.CodeS = Supplier.CodeS
WHERE Office = ‘Den Haag’
GROUP BY CodeP
</code></pre>
</div><p><br></p><h2 id="having-clause">Having clause</h2><p>Conditions on the result of an aggregate operator require the HAVING clause. Only predicates containing aggregate operators should appear in the argument of the HAVING clause</p><div style="white-space: normal;" class="markdown-body"><p>Find the departments in which the average salary of employees working in office number 20 is higher than 25</p>
<pre data-lang="sql"><code>SELECT Dept
FROM Employee
WHERE Office = ‘20’
GROUP BY Dept
HAVING AVG(Salary) &gt; 25
</code></pre>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>Find the total number of supplied items for products that count at least 600 total supplied items</p>
<pre data-lang="sql"><code>SELECT CodeP, SUM(Amount)
FROM Supply
GROUP BY CodeP
HAVING SUM(Amount) &gt;= 600
</code></pre>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>Find the code of red products supplied by more than one supplier</p>
<pre data-lang="sql"><code>SELECT Supply.CodeP
FROM Supply JOIN Products ON Supply.CodeP = Product.CodeP
WHERE Color = ‘Red’
GROUP BY Supply.CodeP
HAVING COUNT(*) &gt; 1
</code></pre>
</div><p><br></p><h2 id="nested-queries">Nested queries</h2><p>A parenthesized SELECT-FROM-WHERE statement can be used as a value in a number of places, including FROM, WHERE, and HAVING clauses.</p><p><br></p><p>A common use of subqueries is to perform tests for <strong>set membership</strong>, <strong>set</strong></p><p><strong>comparisons</strong>, and <strong>set cardinality</strong></p><p><br></p><p>The use of nested queries may produce less declarative queries, but they often improve readability (Complex queries can become very difficult to understand)</p><p><br></p><p><strong>The IN operator</strong></p><div style="white-space: normal;" class="markdown-body"><pre data-lang="sql"><code>&lt;tuple&gt; IN &lt;relation&gt;
</code></pre>
<p>is true iff the tuple is a member of the relations, <code>IN</code> can be negated with the <code>NOT</code> operator.</p>
</div><p><br></p><p><strong>Nested queries examples:</strong></p><div style="white-space: normal;" class="markdown-body"><p>Problem: "Find the name of all the suppliers of product "P2"
Solution with join:</p>
<pre data-lang="sql"><code>SELECT Names
FROM Supplier, Supply
WHERE Supplier.Codes = Supply.Codes AND CodeP = "P2"
</code></pre>
<p>Solution with <code>IN</code> nested query:</p>
<pre data-lang="text/x-sql"><code>SELECT Names
FROM Supplier
WHERE Codes IN (SELECT Codes
				FROM Supply
				WHERE CodeP = `P2`)
</code></pre>
<p>Find the total number of supplied items for product "P2"</p>
<pre data-lang="text/x-sql"><code>SELECT SUM(Amount)
FROM Supply
WHERE CodeP = "P2"
</code></pre>
<p>Nested queries that return one tuple, if a subquery is guaranteed to produce one tuple, then the result of the subquery can be used as a value. A runtime error will occur when no or more than one tuple is returned.</p>
<p>Find the code of suppliers with less shareholders than the supplier having the maximum number of shareholders.</p>
<pre data-lang="sql"><code>SELECT Codes
FROM Supplier
WHERE Shareholders &lt; (SELECT MAX(Shareholders)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	  FROM Supplier)
</code></pre>
</div><p><br></p><h2 id="the-exists-operator">The exists operator</h2><p>This operator allows a nested query as a parameter and returns the TRUE value only if the query does not produce an empty result. This operator can be usefully employed only if there is a binding transfer between the external query and the nested query as can be seen by this example:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="sql"><code>SELECT Names
FROM Supplier
WHERE EXISTS (SELECT *
			  FROM Supply
              WHERE CodeP=‘P2’ AND Supplier.Codes = Supply.Codes)
</code></pre>
</div><p>A limitation of the exists operator is that a query cannot refer to attributes in a subquery, or in a query at the same level of nesting</p><p><br></p><h2 id="the-any/all-operator">The ANY/ALL operator</h2><p>The ANY operator returns TRUE if any of the subquery values meet the condition.</p><p><br></p><p>The keyword ALL can also be combined with each comparison operators, and returns TRUE if a value meets the condition with ALL the values in a set (or multiset).</p><p><br></p><div style="white-space: normal;" class="markdown-body"><p>So this:</p>
<pre data-lang="sql"><code>SELECT Dept
FROM Employee
WHERE Salary &gt;= ALL (SELECT Salary
FROM Employee)
</code></pre>
<p>is equal to</p>
<pre data-lang="sql"><code>SELECT Dept
FROM Employee
WHERE Salary IN (SELECT MAX(Salary)
                 FROM Employee)
</code></pre>
<h2 id="set-queries">Set queries</h2>
<p>Union, intersection, and difference of relations are expressed by the following forms, each involving subqueries:</p>
<ul>
<li><code>(subquery)INTERSECT[ALL] (subquery)</code></li>
<li><code>(subquery)EXCEPT[ALL](subquery)</code></li>
<li><code>(subquery)UNION[ALL](subquery)</code></li>
</ul>
<p>A thing to keep in mind is that while the SELECT-FROM-WHERE statement uses <strong>bag semantics</strong> the <em>default</em> for union, intersection, and difference is <strong>set semantics</strong>
meaning that duplicates are eliminated as the operation is applied. This is done because of efficiency:</p>
<ul>
<li>When projecting attributes, it is easier to avoid  eliminating duplicates, just work tuple-by-tuple</li>
<li>When doing set operations it is most efficient to sort first and then you can just as well eliminate the duplicates</li>
</ul>
<h3 id="union">Union</h3>
<p>The operator executes the union of two relational expressions which are generated by SELECT clauses. This can only be done however if the tables are <strong>union compatible</strong> (i.e. have a compatible schema)</p>
<h3 id="intersection">Intersection</h3>
<p>The intersection of two subqueries, as with the union operator the tables must be <strong>union compatible</strong></p>
<pre data-lang="sql"><code>(SELECT Office FROM Supplier) INTERSECT (SELECT Storehouse FROM Product)
</code></pre>
<p>this is the equivalent of</p>
<pre data-lang="sql"><code>SELECT DISTINCT Office
FROM Supplier, Product
WHERE Office = Storehouse
</code></pre>
<h3 id="except">Except</h3>
<p>The difference set operator, it returns all rows that are in the result of the first (multi)set but not in the result of the second (multi)set.</p>
<p>Find cities hosting suppliers’ offices, but not products’ storehouses</p>
<pre data-lang="sql"><code>SELECT Office
FROM Supplier
EXCEPT
SELECT Storehouse
FROM Products
</code></pre>
<p>Can also be represented with a nested query using the NOT IN operator:</p>
<pre data-lang="sql"><code>SELECT DISTINCT Office
FROM Supplier
WHERE Office NOT IN (SELECT Storehouse
					 FROM Products)
</code></pre>
</div><p><br></p><h2 id="database-schema">Database schema</h2><p>A database schema comprises: </p><ul><li>Declarations for the relations (“tables”) of the database</li><li>Domains associated with each attribute</li><li>Integrity constraints</li><li>Authorization: </li><li class="ql-indent-1">Name </li><li class="ql-indent-1">Owner</li></ul><p><br></p><p>Optionally a schema may also include:</p><ul><li>Privileges</li><li>Views</li><li>Indices</li><li>Triggers</li></ul><p><br></p><div style="white-space: normal;" class="markdown-body"><p>Creation syntax:</p>
<pre data-lang="sql"><code>CREATE SCHEMA [ SchemaName ] Authorisation ] { SchemaElementDefinition }
</code></pre>
</div><p><br></p><p><strong>Domains:</strong></p><p>Specify the content of attributes.</p><p>Two categories:</p><ul><li><strong>Elementary: </strong>Predefined by the standard</li><li><strong>User-defined: </strong>Not available in all RDBMs implementations</li></ul><p><br></p><p><strong>Elementary domains:</strong></p><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>BIT [varying] [(Length)]</code>: Single boolean values or strings of boolean values.</li>
<li>Exact numeric domains: Exact values, integer or with a fractional part
<ul>
<li>Four version:
<ul>
<li><code>NUMERIC/DECIMAL [(Precision [, Scale ])]</code>: fixed point number, with user-specified Precision digits, of which Scale digits to the right of decimal point.</li>
<li><code>INTEGER</code>: a finite subset of the integers that is machine-dependent</li>
<li><code>SMALLINT</code>: a machine-dependent subset of the integer domain type</li>
</ul>
</li>
</ul>
</li>
<li>Approximate real values: Based on floating point representation
<ul>
<li><code>FLOAT [(Precision)]</code>: floating point number, with user-specified precision of at least n digits. By default n is 53, but it can be less</li>
<li><code>REAL</code>: floating point numbers, with machine-dependent precision</li>
<li><code>Double Precision</code>: double-precision floating point numbers, with machine-dependent precision</li>
</ul>
</li>
<li>Temporal <strong>Instants</strong>
<ul>
<li><code>DATE</code>: format yyyy-mm-dd</li>
<li><code>TIME [(Precision)] [ with time zone ]</code>: format hh:mm:ss:p with an optional decimal point and fractions of a second following.</li>
<li><code>TIMESTAMP [(Precision)] [ with time zone ]</code>: format yyyy-mm-dd hh:mm:ss:p</li>
</ul>
</li>
<li>Temporal intervals</li>
<li>INTERVAL FirstUnitOfTime [ TO LastUnitOfTime ]
<ul>
<li>Units of time are divided into two groups:
<ul>
<li>year, month</li>
<li>day, hour, minute, second</li>
</ul>
</li>
</ul>
</li>
<li>In PotgreSQL the syntax is different: <code>interval '2 months ago'</code></li>
<li>Geometric Types: two-dimensional spatial object
<ul>
<li><code>point, line, lseg,box,path,Open path,polygon, circle</code></li>
</ul>
</li>
<li>Network Address Types: to store IPv4, IPv6, and MAC addresses
<ul>
<li><code>cidr, inet, macaddr, macaddr8</code></li>
</ul>
</li>
<li>JSON Types
<ul>
<li><code>json</code>: data is stored an exact copy of the input text</li>
<li><code>jsonb</code>: data is stored in a decomposed binary format</li>
</ul>
</li>
<li>XML Type, used to store XML data</li>
<li>Composite Types: represents the structure of a row or record</li>
<li>UUID, Array, Ranges, Text Search (to support full text search)</li>
</ul>
</div><p><br></p><p><strong>Table definition</strong></p><p>An SQL table consists of:</p><ul><li>an ordered set of attributes</li><li>a (possibly empty) set of constraints</li></ul><div style="white-space: normal;" class="markdown-body"><p>Can be created like so:</p>
<pre data-lang="sql"><code>CREATE TABLE TableName (
	AttributeName Domain [DefaultValue] [Constraints]
	{, AttributeName Domain [DefaultValue] [Constraints]}
	[OtherConstraints]
)
</code></pre>
<p>Example:</p>
<pre data-lang="sql"><code>CREATE TABLE Employee (
	RegNo 		CHARACTER(6) PRIMARY KEY,
	FirstName 	CHARACTER(20) NOT NULL,
	Surname		CHARACTER(20) NOT NULL,
	Dept 		CHARACTER(15)
				REFERENCES Department(DeptName)
					ON DELETE SET NULL
					ON UPDATE CASCADE
	Salary 		DECIMAL (9) DEFAULT 0,
	City		CHARACTER(15),
	UNIQUE(Surname, FirstName)
)
</code></pre>
</div><p><br></p><p><strong>Default domain values</strong></p><p>Define the value that the attribute must assume when a value is not specified during row insertion</p><p>Syntax:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="sql"><code>DEFAULT &lt; GenericValue | USER | CURRENT_USER | SESSION_USER | SYSTEM_USER | NULL &gt;
</code></pre>
</div><ul><li>GenericValue represents a value compatible with the domain, in the form of a constant or an expression</li><li>USER is the login name of the user who issues the command</li></ul><p><br></p><h2 id="constraints"><strong>Constraints</strong></h2><p>Constraints are conditions that must be verified by every database instance and are defined in the CREATE or ALTER TABLE operations.</p><p>These are automatically verified by the DB after each operation.</p><p><br></p><p><strong>Advantages</strong></p><ul><li>Declarative specification of constraints</li><li>Unique centralized verification</li></ul><p><br></p><p><strong>Disadvantages</strong></p><ul><li>Might slow down execution</li><li>Pre-defined type of constraints</li><li class="ql-indent-1">e.g. no constraint on aggregated data</li><li class="ql-indent-1">but triggers can help</li></ul><p><br></p><p>An operation that violates a constraints might cause two type of reactions:</p><ul><li> The operation is aborted, causing an application error</li><li> A compensation action is taken, to reach a new consistent state</li></ul><p><br></p><p>Three type of constraints (for more on this, see <a href="https://cshub.nl/post/235224984" target="_blank" style="background-color: rgb(255, 255, 255);">this</a> post)</p><ul><li> Intra-relational constraints (or table constraints)</li><li> Inter-relational constraints (or referential integrity constraints)</li><li> Generic integrity constraints and assertions</li></ul><p><br></p><p><strong>Intra-relational constraints</strong></p><ul><li>Involve a single relation</li><li>NOT NULL: upon tuple insertion, the attribute MUST be specified</li><li>UNIQUE</li><li class="ql-indent-1">for single attributes: UNIQUE, after the domain</li><li class="ql-indent-1">for multiple attributes: UNIQUE( Attribute , Attribute )</li><li>PRIMARY KEY: Implies NOT NULL, same syntax as unique</li></ul><p><br></p><p><strong>Primary key vs UNIQUE</strong></p><p>The SQL standard allows DBMS implementers to make their own distinctions between PRIMARY KEY and UNIQUE.</p><p>For example some DBMS might automatically create an index (data structure to speed search) in response to PRIMARY KEY, but not UNIQUE</p><p><br></p><p>However standard SQL requires only these distinctions:</p><ul><li>Only one primary key but there can be several UNIQUE attributes</li><li>Primary Key can never be NULL</li><li>UNIQUE attributes can be NULL</li></ul><p><br></p><p><strong>Inter-relational constraints</strong></p><p>Constraints that take into account several relations</p><ul><li>REFERENCES</li><li>FOREIGN KEY</li></ul><p><br></p><p><strong>Reaction policies for referential integrity constraints:</strong></p><p>Reactions operate on the referencing table, after changes to the referenced table.</p><p>Violations may be introduced by updates on the referred attribute or by row deletions</p><p><br></p><div style="white-space: normal;" class="markdown-body"><pre data-lang="sql"><code>ON &lt; DELETE | UPDATE &gt; &lt; CASCADE | SET NULL | SET DEFAULT | NO ACTION &gt;
</code></pre>
</div><p><br></p><p>Reactions:</p><ul><li>CASCADE: propagate the change</li><li>SET NULL: nullify the referring attribute</li><li>SET DEFAULT: assign the default value to the referring attribute</li><li>NO ACTION: forbid the change on the external table</li></ul><p><br></p><p><strong>Schema updates</strong></p><p>Two SQL statements:</p><ul><li><strong>ALTER</strong>: to modify a domain, the schema of a table, or a user</li><li><strong>DROP</strong>: to remove schema, domain, table, etc.</li></ul><p><br></p><p>Like so:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="sql"><code>ALTER TABLE Department ADD COLUMN NoOfOffices NUMERIC(4)
ALTER TABLE Department ADD CONSTRAINT UniqueAddress UNIQUE(Address)
DROP TABLE TempTable CASCADE
</code></pre>
</div><p><br></p><p><strong>Relational catalogues</strong></p><p>The catalog contains:</p><ul><li>The data dictionary</li><li>The description of the data contained in the data base (tables, etc)</li><li>Statistics about the data (distribution, access, growth)</li></ul><p>It is based on a relational structure (reflexive) and It can be queried!</p><p><br></p><p>The SQL92 standard describes a Definition Schema(composed of tables) and an Information Schema (composed of views)</p><p><br></p><h2 id="with-clause-(common-table-expression)">With clause (common table expression)</h2><p>Allows for the definition of a table (or multiple tables) that can be used only within a specific query (like a view). It also allows for deletion, insertion and updating with a WITH clause.</p><p><br></p><div style="white-space: normal;" class="markdown-body"><p>Retrieve pairs of titles from the 90s that have the same name of a title from the 80s</p>
<pre data-lang="sql"><code>WITH NinetiesMovies AS(
	SELECT title, production_year
	FROM title_100k, kind_type
	WHERE production_year BETWEEN 1990 AND 1999
	AND title_100k.kind_id = kind_type.id
	AND kind = 'movie'
), EightiesMovies AS (
	SELECT title, production_year
	FROM title_100k, kind_type
	WHERE production_year BETWEEN 1980 AND 1989
	AND title_100k.kind_id = kind_type.id
	AND kind = 'movie'
)
SELECT *
FROM NinetiesMoviepfSenses, EightiesMovies
WHERE NinetiesMovies.title = EightiesMovies.title
</code></pre>
<p>Remove all aliases containing the name Alessandro, but copy them in a log table</p>
<pre data-lang="sql"><code>WITH moved_rows AS (
	DELETE FROM aka_name_100k
	WHERE name LIKE "%Alessandro%"
	RETURNING *
)
INSERT INTO aka_name_log
SELECT * FROM moved_rows
</code></pre>
</div><p><br></p><p><strong>Recursive</strong></p><p>This notation also allows for recursive queries, you first specify a base query, on which is iterated, using the following structure:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="sql"><code>WITH RECURSIVE t(n) AS (
	VALUES (1)
UNION ALL
	SELECT n+1 FROM t WHERE n &lt; 100
)
SELECT sum(n) FROM t
</code></pre>
</div><p><br></p><h1 id="views">Views</h1><p>A view is any relation that is not of the conceptual model but is made visible to a user</p><p><br></p><p>It is</p><ul><li>a single table derived from other tables</li><li>considered to be a virtual relation</li><li>always up-to-date, the DBMS takes care of synchronization</li></ul><p><br></p><h2 id="why?">Why?</h2><p>Users <strong>should not be allowed</strong> to access the actual relations / data stored in the database</p><ul><li>Limits on row values</li><li>Aliases for column or table names</li></ul><p><br></p><p>Favor the reuse of queries that are frequently used just to denormalize the logical schema</p><p><br></p><p>Help simplifying complex queries, or enable the execution of queries that could not</p><p>be expressed otherwise</p><ul><li>Decompose the problem and produce a more readable solution</li><li>Combine and nest several aggregate operators</li></ul><p><br></p><h2 id="defining-a-view">Defining a view</h2><div style="white-space: normal;" class="markdown-body"><pre data-lang="sql"><code>CREATE [TEMPORARY] VIEW ViewName [(AttributeList)]
AS SelectSQL
   [WITH [CASCADED|LOCAL] CHECK OPTION]
</code></pre>
</div><p>- `ViewName` is used by other queries / views as tablename</p><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>[(AttributeList)]</code> is used for projection / renaming / functions / operation</li>
<li><code>SelectSQL</code> is any <code>SELECT</code> query (with some limitations)</li>
<li><code>[WITH [CASCADED|LOCAL] CHECK OPTION]</code> constraints inserts or updates to rows in tables references by the view</li>
<li><code>[TEMPORARY]</code> defines if the view should be dropped at the end of the current user session</li>
</ul>
<p>Example:</p>
<pre data-lang="sql"><code>CREATE VIEW AdminEmployee (FirstName, Surname, Salary) AS
SELECT FirstName, Surname, Salary
FROM Employee
WHERE Dept = "Administration" AND Salary &gt; 10
</code></pre>
</div><p><br></p><h2 id="view-execution-approaches">View execution approaches</h2><p><strong>Query Modification</strong></p><ul><li><strong>Modify </strong>view query into a query on underlying base tables</li><li>Disadvantage: inefficient for views defined via complex queries that are time-consuming to execute</li><li><br></li></ul><p><strong>View Materialization</strong></p><ul><li><strong>Physically create </strong>a temporary view table when the view is first queried</li><li><strong>Keep that table</strong> on the assumption that other queries on the view will follow</li><li>Requires efficient strategy for <strong>automatically </strong>updating the view table when the base tables are updated</li></ul><p><br></p><h2 id="automatically-updatable-views">Automatically updatable views</h2><p><strong>Idea</strong>: Update the underlying base tables through CRUD operations on a VIEW</p><p><br></p><div style="white-space: normal;" class="markdown-body"><p><code>INSERT</code>, <code>UPDATE</code> or <code>DELETE</code> statements on the view are turned into corresponding statements on the base relation. This is possible when:</p>
<ul>
<li><code>VIEW</code> is defined on a single table</li>
<li>No <code>WITH</code>, <code>DISTINCT</code>, <code>GROUP BY</code>, <code>HAVING</code>, <code>LIMIT</code> or <code>OFFSET</code> clauses at top level</li>
<li>No set operations (<code>UNION</code>, <code>INTERSECT</code> or <code>EXCEPT</code>) at the top level</li>
<li>No aggregates or set-returning functions</li>
</ul>
<p>There might be a mix of updatable and non-updatable columns</p>
<ul>
<li>Updatable: simple reference to updatable column of the base relation</li>
<li>Non-updatable: error when <code>INSERT</code> or <code>UPDATE</code></li>
</ul>
<p>If <code>WHERE</code> statement in the query</p>
<ul>
<li>Only rows that are in the view can be deleted or updated</li>
<li><code>INSERT</code> can be executed on the view, but rows might not be in it</li>
</ul>
<p><code>CHECK OPTION</code></p>
<ul>
<li>Ensures that any rows changed through the view continue to match the view's <code>WHERE</code> clause after the changes</li>
<li><code>LOCAL</code>: check only the conditions defined directly in the view</li>
<li><code>CASCADE</code>: check also conditions of underlying base <code>VIEWs</code></li>
</ul>
</div><p><br></p><h2 id="limitations">Limitations</h2><div style="white-space: normal;" class="markdown-body"><ul>
<li>User, system, or local variables are <strong>not allowed</strong> in the SQL <code>SELECT</code> statement</li>
<li>If the base table schema changes, <code>VIEWS</code> won't be valid anymore</li>
<li><code>VIEWS</code> can have bad performance, but sometimes better through caching</li>
<li><code>MATERIALIZED</code> views add overhead, and it's hard to predict how such a view will impact performance</li>
</ul>
<table>
<thead>
<tr>
<th>Base table</th>
<th>View</th>
</tr>
</thead>
<tbody>
<tr>
<td>Tuples always physically stored in database</td>
<td>Tuples do not necessarily exist in physical form</td>
</tr>
<tr>
<td>CRUD operations are always allowed</td>
<td>CRUD operations are not always allowed</td>
</tr>
<tr>
<td>Always possible to defined tables of views</td>
<td>Can be used to create other views, but not in a mutually dependent way (though recursion on the same view is possible)</td>
</tr>
</tbody>
</table>
</div><p><br></p><h1 id="assertions-and-triggers">Assertions and triggers</h1><p>Semantic / business constraints are constraints that cannot be directly expressed in the schemas of the data model</p><p><br></p><p>In order to express these in the RDBMs, we can use assertions or triggers.</p><p><br></p><h2 id="assertions">Assertions</h2><p>Assertions permit the specification of constraints outside of table definitions, which is useful in many situations (e.g. to express generic inter- relational constraints)</p><p><br></p><p>An assertion associates a name to a check clause, the constraint is satisfied if no combination of tuples in that database violates this check clause.</p><p><br></p><p>The DBMS is responsible for the condition not to be violated</p><p><br></p><p>The syntax for creating such an assertion is</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="sql"><code>CREATE ASSERTION assertion_name CHECK (condition)
</code></pre>
</div><p><br></p><h2 id="triggers">Triggers</h2><p>Triggers (Active Rules): rules that are automatically triggered by database events, and that initiate certain <strong>action </strong>if certain conditions are met</p><p><br></p><p>A trigger has three logical components:</p><ul><li>The triggering event</li><li>The condition that determines whether the rule action should be executed (optional)</li><li>The action to be taken</li><li class="ql-indent-1">Notifying users about violations</li><li class="ql-indent-1">Manage advanced referential integrity</li><li class="ql-indent-1">Automatic maintenance of data</li></ul><p><br></p><p>G<strong>ranularity</strong></p><p><br></p><ul><li><strong>Row-level</strong>: the trigger is activated once for every tuple on which the event occurred</li><li><strong>Statement-level</strong>: the trigger is activated once for every SQL statement, referring to all the tuples on which the statement operated (set-oriented)</li></ul><p><br></p><p><strong>Execution mode</strong></p><ul><li><strong>Immediate</strong>: right after (or even before) the event</li><li class="ql-indent-1">Before: to perform actions prior to changes in the table. New /modified record can be changed</li><li class="ql-indent-1">After: to perform actions after changes in the table. Record written in the table cannot be changed</li><li><strong>Deferred</strong>: at transaction commit</li></ul><p><br></p><p>The syntax for creating such a trigger is (postgres)</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="sql"><code>CREATE TRIGGER name {BEFORE|AFTER}{event [OR ...]}
ON tableName
	[FOR [EACH] {ROW|STATEMENT}]
	[WHEN (condition)]
	EXECUTE PROCEDURE function_name (arguments)
</code></pre>
<p>Where:</p>
<ul>
<li>Event is <code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>, in postgres multiple can be specified using <code>OR</code></li>
<li><code>function_name(arguments)</code> is the function (procedure) to be executed</li>
<li><code>FOR EACH ROW</code> indicates it will be executed once for each of the affected records</li>
<li><code>FOR EACH STATEMENT</code> indicates it will be executed once for any given operations</li>
</ul>
</div><p><br></p><p><strong>Stored procedures</strong></p><p>Stored procedures are functions that are called by triggers, creating them can be done using the following syntax:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="sql"><code>CREATE FUNCTION name (arguments)
RETUNS returnType
local_declarations
function_body
</code></pre>
</div><p><br></p><p>These procedures can be written a couple of language, depending on the implementation. <strong>OLD </strong>and <strong>NEW </strong>keywords can be used to refer to data before and after the event.</p><p><br></p><p><strong>Properties of triggers</strong></p><ul><li>Termination: A rule set is guaranteed to terminate if, for any database state and initial modification, rule processing cannot continue forever</li><li>Confluence: A rule set is confluent if, for any database state and initial modification, the final database state after rule processing is unique, i.e. it is independent of the order in which activated rules are executed</li><li>Termination is assessed studying rules interaction (an important conceptual tool is the triggering graph)</li></ul><p><br></p><p><strong>Advantages of triggers</strong>: They provide <strong>complementary</strong>, and more <strong>robust</strong>, integrity checking mechanism to foreign keys, thus they are ale to catch every error in every change. You can also schedule tasks in the DB, simplify propagation of value changes across tables and enable the execution of calculation before inserting</p><p><br></p><p><strong>Disadvantages of triggers: </strong>They can't replace all types of validation, they are hard to create, debug and maintain and different vendors support different functionalities</p><p><br></p><h1 id="roles">Roles</h1><ul><li>Every component of the schema can be protected (tables, attributes, views, etc.) The owner of a resource (the creator) assigns privileges to the other users</li><li>A predefined role (postgres, or the name of the operating system user that initialized the cluster) represents the database administrator and has complete access to all the resources</li><li>A privilege is characterized by:</li><li class="ql-indent-1">The resource</li><li class="ql-indent-1">The user who grants the privilege</li><li class="ql-indent-1">The user who receives the privilege</li><li class="ql-indent-1">The action that is allowed on the resource</li><li class="ql-indent-1">Whether or not the privilege can be passed on to other users</li></ul><p><br></p><p>Creating a role and granting rights can be done using the following syntax:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="sql"><code>CREATE ROLE name
GRANT group_role TO role_name
</code></pre>
</div><p><br></p><p>For these roles, there are numerous authentication methods, depending on the DBMS.</p>