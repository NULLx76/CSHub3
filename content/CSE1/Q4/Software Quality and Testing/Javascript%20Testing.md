+++
title = "Javascript Testing"
date = 2019-06-20
+++
<h2 id="web-testing">Web testing</h2><p>What should we test if testing web applications (the ones in bold will be discussed here):</p><ul><li>Security testing</li><li>Load testing</li><li>Functionality testing</li><li class="ql-indent-1"><strong>End-to-end testing (testing the entire application)</strong></li><li class="ql-indent-1"><strong>Unit testing</strong></li><li>Non-functional testing</li><li class="ql-indent-1">Performance testing</li><li class="ql-indent-1"><strong>User interface testing</strong></li><li class="ql-indent-1"><strong>Accessibility </strong></li><li>Acceptance testing</li></ul><p><br></p><h2 id="javascript-unit-testing">JavaScript unit testing</h2><p>Tips for writing testable JavaScript code:</p><ul><li>Use a purely logical coding style</li><li>Separate logic from UI</li><li>Use modules to organize your code and allow for easy mocking</li></ul><p><br></p><p>Tips for UI testing (using components):</p><ul><li>Create small, independent components</li><li>Use component tests to save work</li><li>Snapshot tests can save you a lot of work, but use them with care</li></ul><p><br></p><h2 id="end-to-end-testing">End-to-end testing</h2><p>There are a couple of applications which can do automated end-to-end tests. E.g.:</p><ul><li>Selenium, works as a "remote control" for browsers and can be done for any type of automation across multiple browsers</li><li>Cypress: integrates with your browser and is specifically targeted at end-to-end testing</li></ul><p><br></p><p>When end-to-end testing we find specific elements on the page after rendering based on the input data.</p><p><br></p><h2 id="accessibility-testing">Accessibility testing</h2><p>You should make sure your web application is accessible to everyone.</p><p><br></p><p>This means that content should be:</p><ul><li>Perceivable</li><li>Operable</li><li>Understandable</li><li>Robust</li></ul><p>for all types of people with certain disabilities etc. </p><p><br></p><p>In order to make your web application accessible, you should:</p><ul><li>Start early, if you only start thinking about accessibility during the testing phase, you are far too late</li><li>Start with <em>inclusive design. </em>Inclusive design emphasizes the contribution that understanding user diversity makes to informing these decisions, and thus to including as many people as possible.</li><li>Write proper HTML, that already resolves many accessibility issues.</li></ul>