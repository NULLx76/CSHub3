+++
title = "Fundamentals of Testing"
date = 2019-07-29
+++
<h2 id="why-test?">Why test?</h2><p>There are a few objectives for testing:</p><ul><li>Determine that software products satisfy specified requirements</li><li>Demonstrate that software products are fit for purpose</li><li>Detect defects</li><li>Try to make the program fail so you are able to fix it beforehand</li></ul><p><br></p><h3 id="when-do-flaws-arise?">When do flaws arise?</h3><p>There are a few stages in which software is built. If a flaw arises in one of the first three elements, the end result gets increasingly worse:</p><ul><li><strong>Requirements</strong>: A flaw in the requirements would mean that even testing won't help, and in the end you deliver a product which the client didn't ask for (but works, if tested well!)</li><li><strong>Design: </strong>A flaw in design would mean that testing the software also doesn't help much, but that the end product will have design flaws, which are hard to fix</li><li><strong>Build: </strong>A flaw in the build would give bugs, but are (easily) correctable</li></ul><p><br></p><h3 id="failure-vs-fault-vs-error">Failure vs fault vs error</h3><p><strong>Failure: </strong>a component or system behaves in a way that is not expected (requires a program to be executed!)</p><p><strong>Fault / bug / defect: </strong>a flaw in a (sub-)component that can cause the system to behave incorrectly. A fault, if encountered during execution, may cause a failure</p><p><strong>Error / mistake: </strong>a human action that produces an incorrect result</p><p><br></p><h3 id="quality">Quality</h3><p>Testing helps us to measure the quality of software in terms of the number of defects found, the tests run, and the system covered by the tests.  Quality can be defined from different standpoints, see appendix A.</p><p><br></p><h2 id="testing-principles">Testing principles</h2><ol><li>Testing shows <strong>presence of defects</strong>, not absence of them!</li><li><strong>Exhaustive testing</strong> (testing everything, all combinations of inputs and preconditions) <strong>is impossible</strong>, there are too many possibilities</li><li><strong>Test early</strong></li><li class="ql-indent-1">Let tests guide design</li><li class="ql-indent-1">Get feedback as early as possible</li><li class="ql-indent-1">Find bugs when they are easiest to find</li><li class="ql-indent-1"><span>Find bugs when they are easiest to fix</span></li><li><span>Defects are likely to be </span><strong>clustered</strong><span>, certain components have a lot of changes in code, leading to more defects</span></li><li><strong>Pesticide paradox</strong><span>: If the same tests are repeated over and over again, eventually the same set of test cases will no longer find any new defects. To overcome this “pesticide paradox”, test cases need to be regularly reviewed and revised, and new and different tests need to be written to exercise different parts of the software or system to find potentially more defects.</span></li><li>Testing is <strong>context-dependent</strong>, not all defects are as severe as others</li><li>There is <strong>more to quality</strong> than absence of defects</li></ol><p><br></p><h2 id="cognitive-bias">Cognitive bias</h2><p>Testers are people (are they?), thus they are naturally biased towards certain solutions. Though independence of testing is required: from self-testing to external approval with testers from different backgrounds.</p><p><br></p><p>(from the lecture, nowhere in the book:)</p><p>Cognitive bias is characterized into different systems; </p><p><strong>System 1</strong>: fast, instinctive, emotional</p><p><strong>System 2</strong>: slower, more deliberative and more logical. System 2 requires effort and is happy to let system 1 do the work</p><p><br></p><h1 id="appendix-">Appendix </h1><h2 id="a">A</h2><div style="white-space: normal;" class="markdown-body"><table>
<thead>
<tr>
<th>Viewpoint</th>
<th>Software</th>
<th>Tomatoes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Quality is measured by looking at the attributes of the product.</td>
<td>We will measure the attributes of software, e.g. its reliability in terms of mean time between failures (MTBF), and release when they reach a specified level e.g. MTBF of 12 hours.</td>
<td>The tomatoes are the right size and shape for packing for the supermarket. The tomatoes have a good taste and color.</td>
</tr>
<tr>
<td>Quality is fitness for use. Quality can have subjective aspects and not just quantitative aspects</td>
<td>We will ask the users whether they can carry out their tasks; if they are satisfied that they can we will release the software.</td>
<td>The tomatoes are right for our recipe.</td>
</tr>
<tr>
<td>Quality is based on good manufacturing processes, and meeting defined requirements. It is measured&nbsp;by testing, inspection, and analysis of faults and failures.</td>
<td>We will use a recognized software development process. We will only release the software if there&nbsp;are fewer than five outstanding high-priority defects once the planned tests are complete.</td>
<td>The tomatoes are organically farmed. The tomatoes have no blemishes and no pest damage.</td>
</tr>
<tr>
<td>Expectation of value for money. affordability, and a value-based trade-off between time, effort and&nbsp;cost aspects. We can afford to buy this software and we expect a return on investment.</td>
<td>We have time-boxed the testing to two weeks to stay in the project budget.</td>
<td>The tomatoes have a good shelf life. The tomatoes are cheap or good value for money.</td>
</tr>
<tr>
<td>Transcendent feelings - this is about the feelings of an individual or group of individuals towards&nbsp;a product or a supplier.</td>
<td>We like this software! It is fun and it's the latest thing! So what if it has a few problems? We&nbsp;want to use it anyway... We really enjoy working with this software team. So, there were a few problems - they sorted them&nbsp;out really quickly - we trust them.</td>
<td>We get our tomatoes from a small local farm and we get on so well with the growers.</td>
</tr>
</tbody>
</table>
</div>