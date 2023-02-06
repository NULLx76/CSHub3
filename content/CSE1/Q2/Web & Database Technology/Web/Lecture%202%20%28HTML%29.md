+++
title = "Lecture 2 (HTML)"
date = 2019-09-29
+++
<div style="white-space: normal;" class="markdown-body"><h1 id="lecture-2">Lecture 2</h1>
<p>HTML: The language of the web</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h2 id="w3c">W3C</h2>
<p>The W3C has many working groups, among them the "Web Platform Working Group" whose goal it is to move us closer towards the vision of <em>the browser as the operating system</em>.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h2 id="electron">Electron</h2>
<p>Electron is an open-source project that uses web technologies for building <strong>cross-platform</strong> desktop applications.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>Electron uses a combination of Node.js, a server-side JavaScript runtime together with Chromium, the open-source variant of Google's chrome.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>The main selling point of Electron is its cross-platform nature which ensures you only have to develop the application once and can deploy on multiple platforms.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>The downside of Electron is the overhead of bundling a whole browser (Chromium). For example, a simple <code>Hello World</code> application will 30MiB at a minimum.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h2 id="web-design-basics">Web design basics</h2>
<p>Web design is not trivial. However, a few basic rules go a long way.</p>
<ul>
<li>Don't make me think, The way websites work should be self-evident.</li>
<li>If you cannot make it self-evident, make it self-explanatory. Make sure to add a small explanation if it is not self-evident.</li>
<li>Minimize noise and clutter</li>
</ul>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>For example, pictures look at the original <a href="https://github.com/chauff/Web-Teaching/blob/master/Lecture-2.md#web-design-basics">here</a>.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h3 id="expectations-vs.-reality:-usability-testing">Expectations vs. reality: usability testing</h3>
<p>We must realize that our users will not always act rational, attentive and with a clear goal in mind.  A web application should be designed on <strong>user reality</strong>.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>Therefore <strong>usability testing</strong> is an important step in web design and follows the <em>designing-testing-reviewing</em> development cycle. A test in such a cycle will have the user perform various actions available in the Web App, and the actions the user performs will be kept track of and translated into Performance Metrics (Such as the number of elements clicked and total time taken).</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>A typical usability setup has the following</p>
<ul>
<li>The participant (our tester) sits in front of the device</li>
<li>The facilitator sits next to them and guides them through the test</li>
<li>The observers (developers of the app, managers, etc.) watch the usability test and discuss the tester's performance (and how to improve it) afterwards.</li>
</ul>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>The results of a test are then translated into issues and assigned a priority.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h3 id="site-navigation:-the-trunk-test">Site navigation: the trunk test</h3>
<p>In order to determine whether a web site's navigation scheme is useful, Krug developed the so-called trunk test. Given a website, pick a random page in it, print it and give it to a user who has never seen the site.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>As quickly as possible, the user should find:</p>
<ul>
<li>The name of the website</li>
<li>The name of the page she currently views</li>
<li>Major sections of the page</li>
<li>Possible navigation options at this point and you are here indicators.</li>
</ul>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>If the user is not able to find those elements, the site navigation scheme is considered sub-optimal.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h3 id="entry-page-checklist">Entry page checklist</h3>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>The home page of a web application should answer these questions:</p>
<ul>
<li>What is this?</li>
<li>What can I do here?</li>
<li>Why should I be here?</li>
<li>What do they have here?</li>
</ul>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h2 id="html5">HTML5</h2>
<p>HTML5 is a set of related technologies (core HTML5, CSS, JavaScript) that together enable rich web content:</p>
<ul>
<li>Core HTML5: mark up content;</li>
<li>CSS: control the appearance of marked-up content;</li>
<li>Client-side JavaScript: manipulate the contents of HTML documents and respond to user interactions.</li>
</ul>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>Modern web development requires knowledge of at least those three technologies but in practice of many more, such as frameworks, build tools, transpilers and so on (e.g. Webpack, Vue, Angular, React, Typescript, Babel).</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>XHTML and HTML4 are the predecessors of HTML5 and were abandoned in favour of HTML5 because the rules were too strict and thus it became a hassle to write valid XHTML and browser could render invalid XHTML anyways so there was no incentive to write valid XHTML. Another reason for abandonment was that HTML5 added a slew of new features.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>However, with the introduction of newer features <strong>browser compatibility</strong> issues returned as certain vendors are quicker in implementing new features.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h3 id="the-move-towards-html5">The move towards HTML5</h3>
<p>The initial list of HTML tags was static and limited. Therefore Javascript was created (in only ten days) as to make the web more extensible. Plugins were also created but quickly abandoned due to their security vulnerabilities, Adobe Flash as an example.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>HTML5 introduced the notion of <strong>semantic</strong> elements which have no implicit style and are to be used to make the document clearer and styling in CSS easier.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><h3 id="who-decides-the-html-standard">Who decides the HTML Standard</h3>
<p>The HTML standard is defined by W3C (which has many stakeholders such as Microsoft, Google, Mozilla, Baidum, etc.). The standardization process is slow and elaborate as a wide range of stakeholder needs to build consensus. The HTML Recommendation Track Process goes as follows:</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><ol>
<li>Working Draft: a document that W3C has published for review by the community, including W3C Members, the public, and other technical organizations.</li>
<li>Candidate Recommendation: a document that W3C believes has been widely reviewed and satisfies the Working Group's technical requirements. W3C publishes a Candidate Recommendation to gather implementation experience.</li>
<li>Proposed Recommendation: a mature technical report that, after wide review for technical soundness and implementability, W3C has sent to the W3C Advisory Committee for final</li>
<li>W3C Recommendation: a specification or set of guidelines that, after extensive consensus-building, has received the endorsement of W3C Members and the Director. W3C recommends the wide deployment of its Recommendations.</li>
</ol>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>The last step is a <strong>recommendation</strong> as W3C does not enforce anything and is only a standard.</p>
</div><p><br></p><div style="white-space: normal;" class="markdown-body"><p>The W3C almost never removes anything from the standard and most of the time merely suggests not using it. An exception to this is the AppCache which is slowly being removed from the standard (but this takes a very long time).</p>
</div>