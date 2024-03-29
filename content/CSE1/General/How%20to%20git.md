+++
title = "How to git"
date = 2019-01-21
+++
<p>Thanks to <a href="https://github.com/CSEdelft/FAQ/tree/master/git" target="_blank">CSEDelft</a>!</p><p><br></p><div style="white-space: normal;" class="markdown-body"><h1>Quick video tutorial</h1>
</div><div style="white-space: normal;" class="markdown-body"></div><div style="white-space: normal;" class="markdown-body"><p>If you've got 30 minutes of time, these two videos will teach you how to work with git in the command line so that you can quickly start collaborating on github using git. Git and github will make more sense after this, promised.</p>
<ol>
<li><a href="https://www.youtube.com/watch?v=0fKg7e37bQE">Git and Source Control Basics</a></li>
<li><a href="https://www.youtube.com/watch?v=oFYyTZwMyAg">Pull requests, Branching, Merging &amp; Team Workflow</a></li>
</ol>
</div><div style="white-space: normal;" class="markdown-body"><h1>Essential git commands</h1>
</div><div style="white-space: normal;" class="markdown-body"><h2>How to make a new repository</h2>
</div><div style="white-space: normal;" class="markdown-body"><p>Go to <a href="https://github.com/new">https://github.com/new</a>
make a new repository</p>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-sh">cd &lt;folder of new repository&gt;
</pre>
</div><div style="white-space: normal;" class="markdown-body"><p>git init
git remote add origin https://github.com/username/repository</p>
<pre data-lang="">## How to upload local changes
</pre>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-sh">git add . # Add all files you added locally
git commit -am "tell here what you changed in a few words"
git push origin master
</pre>
</div><div style="white-space: normal;" class="markdown-body"><h2>How to commit local changes</h2>
</div><div style="white-space: normal;" class="markdown-body"><p>(this just saves your progress, does not actually upload it. <em><em>DO THIS OFTEN</em></em>)</p>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-sh">git add . #add all files you added locally
git commit -a -m "tell here what you changed in a few words"
</pre>
</div><div style="white-space: normal;" class="markdown-body"><h2>How to pull all changes from github</h2>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-sh">git pull origin master
</pre>
</div><div style="white-space: normal;" class="markdown-body"><h2>resolve conflicts</h2>
</div><div style="white-space: normal;" class="markdown-body"><p>do this if you get a message similar to this:</p>
</div><div style="white-space: normal;" class="markdown-body"></div><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-sh">&gt;&gt; git push
</pre>
</div><div style="white-space: normal;" class="markdown-body"><p>To https://github.com/username/repositoryname
! [rejected]        master -&gt; master (fetch first)
error: failed to push some refs to 'https://github.com/username/repositoryname'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.</p>
<pre data-lang=""></pre>
</div><div style="white-space: normal;" class="markdown-body"><p>this means other people have pushed things while you changed your version too.</p>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-sh">git branch &lt;name of feature you added&gt;
git push origin &lt;branchname you just made&gt;
</pre>
</div><div style="white-space: normal;" class="markdown-body"><p>now go to <code>https://github.com/username/repositoryname/pulls</code>
create new pull request</p>
</div><div style="white-space: normal;" class="markdown-body"><p>select <code>master</code> &lt;- <code>&amp;lt;branchname you just made&amp;gt;</code></p>
</div><div style="white-space: normal;" class="markdown-body"><p>Now you can type some text about why you think this feature should be added to master
and assign people for review on the right (optional but reccommended)</p>
</div><div style="white-space: normal;" class="markdown-body"><p>click create pull request.</p>
</div><div style="white-space: normal;" class="markdown-body"><p>now wait... until someone accepts it :)</p>
</div><div style="white-space: normal;" class="markdown-body"><p>(Or when you merge it if your the repo owner)</p>
</div><div style="white-space: normal;" class="markdown-body"><h2>Accepting a pull request</h2>
</div><div style="white-space: normal;" class="markdown-body"><p>There are 2 options:</p>
</div><div style="white-space: normal;" class="markdown-body"><p>either there are no conflicts and the branches can be merged or there are conflicts.</p>
</div><div style="white-space: normal;" class="markdown-body"><h3>No conflicts</h3>
</div><div style="white-space: normal;" class="markdown-body"></div><div style="white-space: normal;" class="markdown-body"><p>this is easy: just click merge. now to start working with this new version use</p>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-sh">git pull origin master
</pre>
</div><div style="white-space: normal;" class="markdown-body"></div><div style="white-space: normal;" class="markdown-body"><h3>Conflicts</h3>
</div><div style="white-space: normal;" class="markdown-body"><p>click resolve conflicts
you will get a list of all files that have conflicts. click each one and you'll see what changes are made in both branches. Edit the file until all &gt;&gt;&gt;&gt;&gt; and &lt;&lt;&lt;&lt;&lt; sections are gone. keep everything you want to keep and remove everything that can be removed from the files. when you're done and resolved all conflicts you can safely merge.</p>
</div><div style="white-space: normal;" class="markdown-body"></div><div style="white-space: normal;" class="markdown-body"><h2>.gitignore file</h2>
</div><div style="white-space: normal;" class="markdown-body"><p>it is not wise to have large files or folders on github. use a file called ".gitignore" in the root of your repository to exclude files from your project</p>
</div><div style="white-space: normal;" class="markdown-body"></div><div style="white-space: normal;" class="markdown-body"><p>this file can have a structure like this:</p>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="gitignore">*.java
secretpasswords.json
</pre>
</div><div style="white-space: normal;" class="markdown-body"><p>node_modules/</p>
<pre data-lang=""></pre>
</div><div style="white-space: normal;" class="markdown-body"><p>from the moment you make this gitignore file, any file that match these patterns and wasn't previously on the repository will not be pushed anymore.</p>
</div><div style="white-space: normal;" class="markdown-body"></div><div style="white-space: normal;" class="markdown-body"><h3>apply gitignore file on existing files in repositoryname</h3>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-sh">git rm -r --cached .
git add .
git commit -a -m "applied gitignore"
git push
</pre>
</div><div style="white-space: normal;" class="markdown-body"><h2>remove any changes you made after you last pulled (reset to whatever is in the remote repository)</h2>
</div><div style="white-space: normal;" class="markdown-body"><p><em><em>watch out. this removes anything you made since the last pull</em></em></p>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-sh">git fetch origin
git reset --hard origin/master
</pre>
</div><div style="white-space: normal;" class="markdown-body"><h3>Save current progress before reset</h3>
</div><div style="white-space: normal;" class="markdown-body"><p>if you want to reset but maybe later return to whatever you had before the reset, do this:</p>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-sh"></pre>
</div><div style="white-space: normal;" class="markdown-body"><p>git commit -a -m "saving my work"
git branch mysavedwork</p>
</div><div style="white-space: normal;" class="markdown-body"><pre data-lang=""></pre>
</div><div style="white-space: normal;" class="markdown-body"><p>now you can do the fetch and reset.</p>
</div><div style="white-space: normal;" class="markdown-body"></div><div style="white-space: normal;" class="markdown-body"></div><div style="white-space: normal;" class="markdown-body"></div><div style="white-space: normal;" class="markdown-body"></div><div style="white-space: normal;" class="markdown-body"></div><div style="white-space: normal;" class="markdown-body"></div><div style="white-space: normal;" class="markdown-body"></div>