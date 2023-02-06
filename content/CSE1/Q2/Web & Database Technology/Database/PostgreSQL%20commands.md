+++
title = "PostgreSQL commands"
date = 2019-01-20
+++
<h1>To access PostgreSQL from any location:</h1><ol><li data-list="bullet"><span class="ql-ui" contenteditable="false"></span>right click this computer (windows explorer) and select properties</li><li data-list="bullet"><span class="ql-ui" contenteditable="false"></span>click advanced system settings</li><li data-list="bullet"><span class="ql-ui" contenteditable="false"></span>click environment variables</li><li data-list="bullet"><span class="ql-ui" contenteditable="false"></span>select the 3rd line which says PATH and click edit</li><li data-list="bullet"><span class="ql-ui" contenteditable="false"></span>click new</li><li data-list="bullet"><span class="ql-ui" contenteditable="false"></span>in the new line paste `C:\Program Files\PostgreSQL\10\bin` (or if different, the location of psql but default is this)</li><li data-list="bullet"><span class="ql-ui" contenteditable="false"></span>click ok</li><li data-list="bullet"><span class="ql-ui" contenteditable="false"></span>click exit etc etc</li><li data-list="bullet"><span class="ql-ui" contenteditable="false"></span>restart cmd.</li></ol><p><br></p><p>Now the <em>psql </em>command works everywhere</p><p><br></p><h1>Useful CMD commands:</h1><div class="markdown-body" style="white-space: normal;"><p><code>psql -U postgres -c "";</code></p>
</div><p><br></p><p>For example:</p><p><br></p><p>Creating a database:</p><div class="markdown-body" style="white-space: normal;"><p><code>psql -U postgres -c "CREATE DATABASE {name}";</code></p>
</div><p>	</p><p>Deleting a database (Watch out):</p><div class="markdown-body" style="white-space: normal;"><p><code>psql -U postgres -c "DROP DATABASE {name}";</code></p>
</div><p><br></p><p>Restore a database from backup (afaik the database has to be empty for this, might be wrong)</p><div class="markdown-body" style="white-space: normal;"><p><code>pg_restore -U postgres --dbname "{name}" --clean "C:/path/to/your/backupfile";</code></p>
</div><p><br></p><p>Create a backup from a database:</p><div class="markdown-body" style="white-space: normal;"><p><code>pg_dump -U postgres -F c -b -v -f "C:/path/to/your/backupfile";</code></p>
</div><p><br></p><p>Connect to database:</p><div class="markdown-body" style="white-space: normal;"><p><code>psql -U postgres -d "{name}";</code></p>
</div><p><br></p><p>All commands above can be used with the following extra options:</p><div class="markdown-body" style="white-space: normal;"><ul>
<li><code>-h</code>, to pass the hostname</li>
<li><code>-p</code>, to pass the port</li>
</ul>
</div><p><br></p><p><br></p><h1>Useful Postgres commands</h1><p>(use this once you are in a Postgres environment, for example after opening a database with the -d option)</p><p><br></p><p>Switch/connect to database</p><div class="markdown-body" style="white-space: normal;"><p><code>\c dbname [username] [host] [port]</code></p>
</div><p><br></p>