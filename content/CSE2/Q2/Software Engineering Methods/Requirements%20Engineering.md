+++
title = "Requirements Engineering"
date = 2019-12-11
+++
<h2 id="requirement-engineering">Requirement engineering</h2><p>Getting the requirements is done through the following process:</p><p><img src="https://i.imgur.com/WkSzzzF.png" width="437"></p><p><em>Image taken from slides by Annibale Panichella</em></p><p><br></p><p>The process will be:</p><ul><li><strong>Feasbility study: </strong>may user needs be satisfied using current software and hardware technologies? </li><li class="ql-indent-1">This will yield a <strong>feasibility report</strong>: the result should inform the decision of whether or not to go ahead with a more detailed analysis </li></ul><p><br></p><ul><li><strong>Requirement, elicitation &amp; analysis:</strong> understanding the problem </li><li class="ql-indent-1">This will yield <strong>system models</strong>: deriving the requirements through observation of existing systems, discussions with potential users and procedures, task analysis, etc. </li></ul><p><br></p><ul><li><strong>Requirement specification</strong>: describing what to deliver </li><li class="ql-indent-1">This will yield <strong>user and system requirements</strong>: translating the information gathered during the previous stages into a document that describes the set of requirements (and understandable to the customer)</li><li class="ql-indent-1">User requirements are abstract statements for the customer and end-user of the system. </li><li class="ql-indent-1">System requirements are a more detailed description of the functionality to be provided </li></ul><p><br></p><ul><li><strong>Requirement validation</strong>: reaching an agreement upon the nature of the problem </li><li class="ql-indent-1">This will yield a <strong>requirements document</strong>: checks the requirements for realism, consistency, and completeness. During this process, errors in the requirements document are inevitably discovered. The documents must then be modified to correct these problems.</li></ul><p><br></p><h2 id="requirement-analysis">Requirement analysis</h2><p><img src="https://i.imgur.com/jbTBUML.png" width="375"></p><p><em>Image taken from slides by Annibale Panichella</em></p><p><br></p><p>The process will be:</p><ul><li><strong>Requirements discovery: </strong>interacting with stakeholders to discover their requirements</li><li><strong>Requirements classification &amp; organization: </strong>take unstructured requirements and group them in coherent clusters</li><li><strong>Requirements prioritization &amp; negotiation: </strong>prioritize requirements based on importance and time to deliver each function. When there are conflicting requirements the should be identified and resolved with the stakeholders</li><li><strong>Requirement specification: </strong>the requirements are documented and the report is used as input for the next round of the spiral</li></ul><p><br></p><h3 id="common-problems">Common problems</h3><ul><li>Stakeholders don't know what they want</li><li>Stakeholders express requirements in their own terms</li><li>Different stakeholders may have conflicting requirements</li><li>Organizational and political factors may influence the system requirements</li><li>New stakeholders may emerge</li></ul><p><br></p><h3 id="verifiability">Verifiability</h3><p>Requirements must be written to be objectively verified: replace ‘easy to use’ (useless) to ‘should be usable after 2 hours of training’</p><h3 id=""><br></h3><h2 id="use-cases-and-scenarios">Use cases and scenarios</h2><p><strong>Use cases: </strong></p><ul><li>popular method to elicit requirements</li><li>a specification of <strong>actors</strong> that interact with the system and <strong>actions</strong> that a system can perform </li></ul><p><br></p><p><strong>Scenario</strong>: particular trace of action occurrences, starting from a known initial state e.g. go to google.com and click "images"</p><p><br></p><h2 id="uml">UML</h2><p>The Unified Modelling Language (UML) contains 4 types of diagrams:</p><ul><li><strong>Use case diagrams: </strong>show external <em>actors </em>and their <em>interactions </em>(use cases) with the system under development</li><li><strong>Sequence diagrams: </strong>visualize <em>temporal message ordering </em>of a concrete scenario of a use case</li><li><strong>Class diagrams: </strong>visualize the <em>logical structure</em> of the system regarding <em>classes</em>, <em>objects</em> and <em>relationships</em></li><li><strong>State diagrams: </strong>specify the <em>abstract states</em> of an object and the <em>transitions</em> between the states</li></ul><p><br></p><h2 id="functional-&amp;-non-functional-requirements">Functional &amp; non-functional requirements</h2><h3 id="functional-requirements"><strong>Functional requirements</strong></h3><p>Functional requirements describe what services the system should provide, how the system should react to particular inputs. They may also include what the system should not do. Functional requirements may be written at different levels of abstraction. </p><p><br></p><p>An example of a functional requirement is “When the player goes to a higher level, the speed is increased.” </p><p><br></p><p>Imprecision in the requirements specification is the cause of many software engineering problems. That's why functional requirements should be complete and consistent:</p><ul><li><strong>Complete: </strong>all services required by the user are defined</li><li><strong>Consistent: </strong>requirements should not have contradictory definitions</li></ul><p><br></p><p>For large, complex system it is practically impossible to achieve completeness and consistency.</p><p><br></p><h3 id="moscow">MoSCoW</h3><p>Using the MoSCoW method we can prioritize software requirements. We divide functional requirements into 4 categories:</p><ul><li><strong>Must have: </strong>critical to the delivery for a successful project</li><li><strong>Should have: </strong>are important but can be delivered in the future</li><li><strong>Could have: </strong>nice to haves, often to improve user experience</li><li><strong>Won't have: </strong>not critical, maybe for something in the future</li></ul><p><br></p><h3 id="non-functional-requirements"><strong>Non-functional requirements</strong></h3><p>Constraints on the services or functions offered by the system. They include the timing constraints, constraints on the development process, and constraint imposed by standards. </p><p><br></p><p>They can contain:</p><ul><li><strong>Product requirements</strong>: specify that the product must behave in a particular way. e.g. execution speed, security </li><li><strong>Organizational requirements</strong>: consequence of organizational policies and procedures. e.g. process standards used, implementation requirements </li><li><strong>External requirements</strong>: arise from factors which are external to the system and its development process e.g. interoperability requirements</li></ul><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p>