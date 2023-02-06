+++
title = "Visual Data Mining"
date = 2020-01-25
+++
<h1 id="visual-data-mining">Visual Data Mining</h1><p>We use Visual Data Mining as data becomes more clear to humans, which in the end need to actually interpret the data and do something with it.</p><p><br></p><p>Visual Data Mining approaches fall under 3 categories:</p><ul><li>Computationally enhanced Visualizations (V++)</li><li>Visually enhanced Mining (M++)</li><li>Integrated Visualization and Mining (VM)</li></ul><p><br></p><h2 id="enhanced-visualization-(v++)">Enhanced visualization (V++)</h2><p>Techniques in which visualization is the primary data analysis means and automatic computation (“++”) provides additional features to make the tool more effective.</p><p><br></p><p>Three main patterns in enhanced visualization</p><ul><li><strong>Intelligent data reduction</strong> (pattern matching, sampling, feature selection)</li><li><strong>Patterns Disclosure</strong> (configuring the visualization according to automatic methods, making visual patterns more prominent)</li><li><strong>Projections</strong> (providing an overview of the data by representing each object by a point in a low dimensional space)</li></ul><p><br></p><h2 id="enhanced-mining-(m++)">Enhanced Mining (M++)</h2><p>Techniques in which data mining is the primary data analysis means and visualization ( “++”) provides an advanced interactive interface to present the results.</p><p><br></p><p>Two major patterns in enhanced mining:</p><ul><li><strong>Model presentation</strong> (visualizing multi-dimensional decision boundaries in 2D)</li><li><strong>Pattern exploration and filtering</strong> (for association rules, example: time patterns are presented to understand how topics change in a stream of news)</li></ul><p><br></p><h2 id="integrated-visualization-and-mining-(vm)">Integrated Visualization and Mining (VM)</h2><p>Two major strategies:</p><ul><li><strong>Black-Box integration</strong> (algorithm is a black box, but user can steer its parameters in a tight visual loop environment. Changes in parameters are automatically reflected in the visualization)</li><li><strong>White-Box integration</strong> = Visual Analytics (feedback loop, human and machine cooperate during model building. Intermediary decisions in the algorithm are taken either by the algorithm or by the user):</li></ul><p><img src="https://media.discordapp.net/attachments/525297297798463489/669844881081892867/unknown.png?width=1090&amp;height=328" width="571"></p><p><em>Image taken from slides by Gosia Migut</em></p><p><br></p><p><strong>White-Box Integration: </strong>In this kind of integration the human and the machine cooperate during the model building process in a way that intermediary decisions in the algorithm can be taken either by the user or the machine. This kind of systems is quite rare. There are examples of cooperative construction of classification trees, where the user steers the construction process and at any stage can ask the computer to make one step in his or her place like splitting a node or expanding a sub-tree. These systems show the highest degree of collaboration between the user and the machine and go beyond the creation of accurate models. They help building trust and understanding, because the whole process is visible, and also they permit to directly exploit the user’s domain knowledge in the model construction process.</p><p><br></p><p><strong>Black-Box Integration</strong> (feedback loop): Integration between mining and visualization can also happen indirectly using the algorithm as a black box, but giving the user the possibility to “play” with parameters in a tight visual loop environment, where changes in the parameters are automatically reflected in the&nbsp;visualization. In this way the connection between parameters and model, even if not explicit, can be intuitively understood. Alternatively, the same integration can be obtained in a sort of “relevance feedback” fashion, where the system generates a set of alternative solutions and the user instructs the system on which are the most interesting ones and gives hints on how to generate a new set.</p><p><br></p><h2 id="summary">Summary</h2><ul><li>Not all problems are Visual Analytics problems!</li><li>Some problems/applications are best addressed by V++ or by M++ alone.</li><li>Some problems/applications are best addressed by integrated black-box approach (VM)</li><li>Fully integrates approaches are still rare, but very needed to exploit the knowledge (and gain trust) of the domain expert</li></ul>