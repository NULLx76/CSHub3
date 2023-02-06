+++
title = "Admissible heuristics for sliding puzzle"
date = 2021-02-16
+++
<p>Given the following puzzle:</p><p><img src="https://i.imgur.com/bQEfeYh.png" width="378"></p><p>Some admissible heuristics would be:</p><ul><li><strong>Number of tiles misplaced: </strong>easy to compute but doesn't tell you much about whether you're close to the goal</li><li><strong>Total Manhattan distance: </strong>takes quite a bit of computation but is a bit informative</li><li><strong>Actual solution: </strong>you'd need to solve the problem to find this. Not very useful</li></ul>