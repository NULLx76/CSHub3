+++
title = "MongoDB querying"
date = 2019-01-17
+++
<h2>Syntax note</h2><div style="white-space: normal;" class="markdown-body"><p><code>$</code> and <code>$$</code> characters are used to indicate that the value should be interpreted as a field path</p>
</div><p><br></p><h2><strong>Find</strong></h2><div style="white-space: normal;" class="markdown-body"><ul>
<li>The <code>find({QUERY}, {PROJECTION})</code> method selects document from collection
<ul>
<li><code>{QUERY}</code> retrieves documents based on filtering conditions</li>
<li><code>{PROJECTION}</code> enumerates fields to be included and excluded (also in subdocuments)</li>
<li>allows for modifiers (sorting, limit, and skip operations)</li>
<li>the order of matchers in the query is important, if a collection has some property listed in a certain order it must be queried in that order (otherwise no data will be returned)</li>
</ul>
</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><ul>
<li>The <code>findOne({QUERY}, {PROJECTION})</code> method selects the first document that matches the query</li>
</ul>
</div><p><br></p><h2>Operators</h2><div style="white-space: normal;" class="markdown-body"><ul>
<li>Equality
<ul>
<li><code>$eq</code>: equals</li>
</ul>
</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><ul>
<li>Inequality
<ul>
<li><code>$ne</code>: not equals (or not exists)</li>
<li><code>$lt</code> / <code>$lte</code>: less than / less than or equal to</li>
<li><code>$gt</code> / <code>$gte</code>: greater than / greater than or equal to</li>
</ul>
</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><ul>
<li>Set membership
<ul>
<li><code>$in</code>: equal to at least one of the provided values</li>
<li><code>$nin</code>: <code>$not: {$in}</code></li>
</ul>
</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><ul>
<li>Logical operators
<ul>
<li><code>$and</code></li>
<li><code>$or</code></li>
<li><code>$not</code></li>
<li><code>$nor</code></li>
</ul>
</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><ul>
<li>Element operators
<ul>
<li><code>$exists</code></li>
<li><code>$type</code></li>
</ul>
</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><ul>
<li>String matching
<ul>
<li><code>$regex</code>: regex machine (with <code>$options</code> for regex options)</li>
</ul>
</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><ul>
<li>Evaluation operators
<ul>
<li><code>$expr</code>: for comparison among fields in the same document, conditional statements and more</li>
<li><code>$all</code>: tests whether all specified items are present</li>
<li><code>$size</code>: tests the size of an array</li>
<li><code>$elemMatch</code>: tests whether an array contains at least one item that satisfies the query</li>
</ul>
</li>
</ul>
</div><p><br></p><h2>Projection</h2><div style="white-space: normal;" class="markdown-body"><p>Specifies the fields returned in the result:</p>
<ul>
<li><code>true</code> or <code>1</code> to show the field</li>
<li><code>false</code> or <code>0</code> to hide the field</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><p>You can't have both a <code>1</code> and <code>0</code> (unless that <code>0</code> is to hide the <code>_id</code>, "Projection cannot have a mix of inclusion and exclusion." @ MongoDB error log (but why tho))</p>
</div><div style="white-space: normal;" class="markdown-body"><p>This projection also works with sub-documents.</p>
</div><p><br></p><h2>Sorting</h2><div style="white-space: normal;" class="markdown-body"><ul>
<li>The order of documents is undefined, unless explicitly sorted</li>
<li>Use <code>.sort({field: value}, ...)</code> syntax where <code>value</code> is <code>1</code> (ascending) or <code>-1</code> (descending)</li>
<li>Sorting happens before projection phase</li>
</ul>
</div><p><br></p><h2>Aggregation framework</h2><p>The MongoDB aggregation framework is based on a <strong>pipeline, </strong>there are different stages which are performed sequentially. The order of execution matters in a pipeline. A few pipeline operators:</p><div style="white-space: normal;" class="markdown-body"><ul>
<li><code>$match</code>: filters the document to match specified conditions (use ASAP)</li>
<li><code>$lookup</code> (<code>LEFT JOIN</code>): like a join in SQL, can have sub-pipelines for more complex operations (e.g. filtering, join conditions etc).</li>
<li><code>$unwind</code>: produces one output for each element specified in an array field. There are also some flags that can be set (<code>preserveNullAndEmptyArrays</code>, which makes sure that also empty / null arrays have one entry and <code>includeArrayIndex</code> which is a field that will include the index for example)</li>
<li><code>$group</code>: similar to SQL <code>GROUP BY</code>, aggregation based on comon properties, it is important to define the <code>_id</code> of grouped documents</li>
<li><code>$graphLookup</code>: recursive lookup</li>
<li><code>$sortByCount</code>: groups based on value, then counts and sorts in descending order</li>
<li><code>$replaceRoot</code>: promotes a specified document to top level and replaces all other fields</li>
</ul>
</div><div style="white-space: normal;" class="markdown-body"><p><strong>Accumulators</strong>: calculate values from field values in multiple documents, can be used in group and project stages</p>
</div><p><br></p><p><br></p>