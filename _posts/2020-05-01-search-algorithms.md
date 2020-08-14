---
title: Pathfinding in Pacman domain
description: Pathfinding / Graph Search Algorithms
categories:
  - AI
tags:
toc: true
toc_sticky: true
comments: true
excerpt: |
  AI / Pathfinding / Search Algorithms / Applications
# header:
#   image: /assets/images/logos/logo-text-8c3ba8a6.svg
---

# Introduction

Pathfinding builds on top of graph search algorithms and explore routes between nodes, traversing from the start node to the destination. These algorithms are used to identify optimal routes through a graph for uses such as logistics planning (Vehicle routing/logistics), least cost call or IP routing, and gaming simulation (AI movements or user assistance). The following figures are applications of pathfinding; logistics planning, robotics, and game-playing.

<p float="left">
  <img src="/assets/images/Pathfinding/logistics_path.png" width="150" height="100" />
  <img src="/assets/images/Pathfinding/robotics_path.png" width="300" height="100"/>
</p>
<p float="left">
  <img src="/assets/images/Pathfinding/game_path.png" width="150" height="100"/>
  <img src="/assets/images/Pathfinding/game-playing.png" width="300" height="100"/>
</p>

I applied pathfinding to Pacman domain (gaming-play application) to compare which algorithms are suitable in the case.

# Graphs
A graphs can represent networks of communication, data organization, computational devices, the flow of computation, etc, depending on how you set up nodes and edges.

For instance, we can set an input as a graph of the map like a set of locations (nodes) and the connections (edges) can be input. The following figures shows how a map is represented as a graph. The shaded path is the shortest path in the graph, the blue dots are nodes, and the green lines are edges.

<p float="left">
  <img src="/assets/images/Pathfinding/map_1.png" width="200" height="100"/>
  <img src="/assets/images/Pathfinding/map_2.png" width="200" height="100"/>
  <img src="/assets/images/Pathfinding/map_3.png" width="200" height="100"/>
</p>
| Fig1. Applications of pathfinding |

This map can represent in many different ways. One can be doorways as edges (left in the Fig2) or another can be a grid mapping.

<p float="left">
  <img src="/assets/images/Pathfinding/doorways_edges.png" width="200" height="100"/>
  <img src="/assets/images/Pathfinding/grid_map.png" width="200" height="100"/>
</p>
| Fig2. The map represented as a graph|

A pathfinding graph can vary, depending on how you define. In the Pacman domain, the map is designed as a grid.

# Shortest Path

The Shortest Path algorithm calculates the shortest (weighted) path between a pair of nodes. One of the most popular shortest path algorithms is Dijkstra's.
> **NOTE** Dijkstra's is known as Uniform Cost Search.



The goal of this project is to see how the behaviors of graph search algorithms in the Pacman domain and how heuristic affects them while finding the shortest path.
> ** NOTE** You can think of heuristic an approximate measure of how close you are to the target.

![scrapy_archit_all](/assets/images/Data-Crawling-Scrapy/scrapy_archit_all.png){:height="800px" width="600px"}  
| Fig3. Pathfinding in Pacman Domain |

There are various search algorithms, but we can categorize them into two: blind searches and heuristic searches.

<div class="side-by-side">
  <figure id="diagram-contour-unweighted">
  <figcaption>Breadth First Search</figcaption>
  <canvas width="568" height="568" style="touch-action: none; cursor: crosshair;">
  </canvas>
  </figure>
  <figure id="diagram-contour-weighted">
  <figcaption>Dijkstra’s Algorithm</figcaption>
  <canvas width="568" height="568" style="touch-action: none; cursor: crosshair;"></canvas>
  </figure>
</div>

 but in this project, BFS (Breadth-First Search), DFS (Depth-First Search), A* (A* Search), USC (Uniform Cost Search), and BiS (Bi-directional Search).

If you are not familiar with those algorithms, check this [tutorial](https://cs.stanford.edu/people/abisee/tutorial/).

https://github.com/pnut2357/Bidirectional_Pacman
