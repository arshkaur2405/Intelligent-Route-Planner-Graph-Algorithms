# 🗺️ Intelligent Route Planner Using Graph Algorithms

## 📌 Project Overview

The Intelligent Route Planner is a Data Structures & Algorithms (DSA) project that finds the optimal route between locations using graph-based pathfinding algorithms.

The project models a city as a weighted graph where:

* Locations are represented as nodes (vertices)
* Roads are represented as edges
* Distance and travel time are represented as edge weights

Using graph algorithms such as BFS, DFS, and Dijkstra's Algorithm, the system calculates efficient routes between locations.

---

## 🎯 Problem Statement

Modern navigation systems need to determine the most efficient route between two locations.

Finding optimal routes is important for:

* Navigation systems
* Ride-sharing platforms
* Food delivery applications
* Logistics and supply chain management
* Public transportation systems

This project demonstrates how graph algorithms can be used to solve real-world route optimization problems.

---

## 🚀 Features

### Graph Representation

* Adjacency List Implementation
* Weighted Graph Structure
* Bidirectional Road Network

### Traversal Algorithms

* Breadth First Search (BFS)
* Depth First Search (DFS)

### Route Optimization

* Dijkstra's Shortest Path Algorithm
* Distance-Based Optimization
* Time-Based Optimization

### Route Analytics

* Route Reconstruction
* Total Distance Calculation
* Estimated Travel Time Calculation
* Route Summary Generation

### Visualization

* Interactive Streamlit Dashboard
* Graph Visualization using NetworkX
* Route Highlighting

---

## 🏗️ System Architecture

Location Data
↓
Graph Construction
↓
Adjacency List Storage
↓
Route Request
↓
Shortest Path Algorithm
↓
Optimized Route
↓
Route Summary
↓
Visualization

---

## 🧠 Data Structures Used

### Graph

Stores locations and roads.

### Adjacency List

Example:

Airport
→ Tech Park

Airport
→ Central Hospital

### Queue

Used in BFS Traversal.

### Recursion + Stack Behavior

Used in DFS Traversal.

### Priority Queue (Min Heap)

Used in Dijkstra's Algorithm for efficient shortest path calculation.

---

## 🔍 Algorithms Used

### Breadth First Search (BFS)

Purpose:

* Explore graph level by level
* Find path with minimum hops

Time Complexity:

O(V + E)

---

### Depth First Search (DFS)

Purpose:

* Explore graph deeply before backtracking

Time Complexity:

O(V + E)

---

### Dijkstra's Algorithm

Purpose:

* Find shortest path in weighted graph

Time Complexity:

O((V + E) log V)

Uses:

* Priority Queue
* Min Heap

---

## 📂 Project Structure

Intelligent-Route-Planner-Graph-Algorithms/

├── app.py

├── data/

├── docs/

├── images/

├── outputs/

├── src/

│   ├── **init**.py

│   ├── graph.py

│   ├── router.py

│   └── visualizer.py

├── README.md

├── requirements.txt

└── .gitignore

---

## ⚙️ Installation

### Clone Repository

git clone https://github.com/arshkaur2405/Intelligent-Route-Planner-Graph-Algorithms.git

cd Intelligent-Route-Planner-Graph-Algorithms

### Install Dependencies

pip install -r requirements.txt

---

## ▶️ Running the Project

### Streamlit Version

streamlit run app.py

After execution:

A local browser window opens automatically.

Example:

http://localhost:8501

---

## 📍 Sample Route Query

Source:

Airport

Destination:

Industrial Zone

Optimization:

Distance

---

## ✅ Sample Output

Optimized Route

Airport
→ Central Hospital
→ Industrial Zone

Total Distance:

22.3 km

Estimated Travel Time:

31.76 min

Optimization:

Distance

---

## 📊 Visualization

The application visualizes:

* City Graph
* Locations
* Roads
* Edge Weights
* Optimized Route

Highlighted shortest paths help users understand how Dijkstra's Algorithm works.

---

## 💡 Real World Applications

### Navigation Systems

* Google Maps
* GPS Navigation

### Ride Sharing

* Uber
* Ola
* Lyft

### Food Delivery

* Swiggy
* Zomato
* DoorDash

### Logistics

* Amazon Logistics
* DHL
* FedEx

### Smart Transportation

* Traffic Management Systems
* Public Transport Networks

---

## 🎓 Learning Outcomes

Through this project, I learned:

* Graph Data Structures
* Adjacency List Representation
* BFS Traversal
* DFS Traversal
* Dijkstra's Algorithm
* Priority Queues and Min Heaps
* Route Optimization Techniques
* Network Visualization
* Streamlit Application Development
* GitHub Project Management

---

## 🔮 Future Enhancements

* A* Search Algorithm
* Real-Time Traffic Data
* Multiple Route Suggestions
* Map API Integration
* Distance Matrix Optimization
* Logistics Route Planning
* Vehicle Routing Problem (VRP)
* Multi-City Route Planning

---

## 👩‍💻 Author

Arshdeep Kaur

B.Tech Student

Interested in:

* Software Development
* Data Structures & Algorithms
* Artificial Intelligence
* Route Optimization Systems
* Backend Engineering

---

## ⭐ If you found this project useful

Please consider giving it a Star on GitHub.
