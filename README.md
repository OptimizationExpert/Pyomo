# 🧮 Optimization Expert — Pyomo & OR-Tools Model Library

> *A hands-on, open-source library of **129+ solved optimization models** in Pyomo and Google OR-Tools CP-SAT —
> routing, scheduling, supply chain, graphs, machine learning and puzzles.*

[![Stars](https://img.shields.io/github/stars/OptimizationExpert/Pyomo?style=social)](https://github.com/OptimizationExpert/Pyomo/stargazers)
[![Forks](https://img.shields.io/github/forks/OptimizationExpert/Pyomo?style=social)](https://github.com/OptimizationExpert/Pyomo/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![LinkedIn Newsletter](https://img.shields.io/badge/LinkedIn-Newsletter-blue?logo=linkedin)](https://www.linkedin.com/newsletters/optimization-in-open-source-6874020019009859585/)
[![Telegram](https://img.shields.io/badge/Telegram-Channel-2CA5E0?logo=telegram)](https://t.me/PyomoChannel)
[![Website](https://img.shields.io/badge/Website-optexpert.org-orange)](https://optexpert.org)

---

## 🚀 What Is This Repository?

A **living library** of optimization models. Each notebook or script is fully solved and self-contained: problem,
mathematical formulation, Python code, solution and visualization.

It is written for:

- **Students** learning operations research and mathematical programming
- **Practitioners** looking for working templates for real problems
- **Puzzle lovers** who like to think in constraints

**Modeling tools:** [Pyomo](http://www.pyomo.org/) (LP, MILP, NLP, bilevel, DAE) and
[Google OR-Tools](https://developers.google.com/optimization) (CP-SAT and the routing library).
**Solvers:** CP-SAT, CBC, GLPK, HiGHS, Ipopt, Gurobi and the free [NEOS Server](https://neos-server.org/).

Most notebooks open directly in **Google Colab** through the badge at the top of the notebook — no installation needed.

---

## 🗂️ Contents

- [🚛 Routing & Logistics](#-routing--logistics)
- [📅 Scheduling](#-scheduling)
- [🏭 Supply Chain & Resource Allocation](#-supply-chain--resource-allocation)
- [🤝 Assignment & Matching](#-assignment--matching)
- [🔗 Graphs & Networks](#-graphs--networks)
- [🧩 Logic Puzzles](#-logic-puzzles)
- [♟️ Chess & Board Puzzles](#️-chess--board-puzzles)
- [💼 LinkedIn Puzzles](#-linkedin-puzzles)
- [🧠 IBM Ponder This Challenges](#-ibm-ponder-this-challenges)
- [📐 Geometry & Packing](#-geometry--packing)
- [🤖 Machine Learning & Data Fitting](#-machine-learning--data-fitting)
- [🛠️ Pyomo & OR-Tools Techniques](#️-pyomo--or-tools-techniques)

---

## 📚 Solved Problems

### 🚛 Routing & Logistics

| Problem | File | Tool |
|---|---|---|
| Capacitated VRP (CVRP) | [CVRP\_CP.ipynb](CVRP_CP.ipynb) | CP-SAT |
| CVRP with OR-Tools routing library | [CVRP\_log.ipynb](CVRP_log.ipynb) | OR-Tools Routing |
| CVRP with distance limits — comparison | [Comparison\_Distance\_Exceed\_of\_CVRP\_CP.ipynb](Comparison_Distance_Exceed_of_CVRP_CP.ipynb) | CP-SAT |
| CVRP with Time Windows (CVRPTW) | [CVRPTW\_CP.ipynb](CVRPTW_CP.ipynb) | CP-SAT |
| Clustered CVRP | [CCVRP\_CP.ipynb](CCVRP_CP.ipynb) | CP-SAT |
| VRP with constraint programming | [CP\_VRP.ipynb](CP_VRP.ipynb) | CP-SAT |
| TDCPVRP | [TDCPVRP\_V2.ipynb](TDCPVRP_V2.ipynb) | CP-SAT |
| TSP with AddCircuit | [AddCircuit\_Advanced\_CP.ipynb](AddCircuit_Advanced_CP.ipynb) | CP-SAT |
| TSP with precedence constraints | [precedence\_AddCircuit\_Advanced\_CP.ipynb](precedence_AddCircuit_Advanced_CP.ipynb) | CP-SAT |
| Large-scale TSP | [Large\_TSP\_CP.ipynb](Large_TSP_CP.ipynb) | CP-SAT |
| Shortest path with waiting times | [routing\_shortest\_path\_waiting\_CP\_V3.ipynb](routing_shortest_path_waiting_CP_V3.ipynb) | CP-SAT |
| VRP wiring | [VRP\_Circuit\_CP\_Wiring.ipynb](VRP_Circuit_CP_Wiring.ipynb) | CP-SAT |
| VRP wiring without crossings | [VRP\_Circuit\_CP\_Wiring\_nocross.ipynb](VRP_Circuit_CP_Wiring_nocross.ipynb) | CP-SAT |
| Tourist trip planning (TTP) | [TTP\_CP.ipynb](TTP_CP.ipynb) | CP-SAT |
| Boat tour optimization | [BoatTour.ipynb](BoatTour.ipynb) | Pyomo |
| Order pickup from inventory | [storage\_routing.ipynb](storage_routing.ipynb) | CP-SAT |
| Conquering all metro stations | [Metro map -V3-github.ipynb](Metro%20map%20-V3-github.ipynb) | Pyomo |

### 📅 Scheduling

| Problem | File | Tool |
|---|---|---|
| Job shop scheduling with idle time | [JobShop\_CP\_ORTools\_Idle\_time.ipynb](JobShop_CP_ORTools_Idle_time.ipynb) | CP-SAT |
| Job shop with flexible preventive maintenance (6 jobs × 5 machines) | [maintenance\_CP.py](maintenance_CP.py) | CP-SAT |
| ↳ data for the maintenance example | [data\_maintenance\_CP.py](data_maintenance_CP.py) | Python |
| RCPSP with cumulative constraints | [RCPSP\_Cummulative\_CP.ipynb](RCPSP_Cummulative_CP.ipynb) | CP-SAT |
| Multi-mode RCPSP (MRCPSP) | [mrcpsp.ipynb](mrcpsp.ipynb) | Pyomo |
| Project scheduling | [Project-Class-module-github.ipynb](Project-Class-module-github.ipynb) | Pyomo |
| Project scheduling — multi-objective | [Project-Class-module-github-MOO.ipynb](Project-Class-module-github-MOO.ipynb) | Pyomo |
| Shift scheduling | [shift\_scheduling\_CP.ipynb](shift_scheduling_CP.ipynb) | CP-SAT |
| Nurse scheduling | [automation.py](automation.py) | CP-SAT |
| Hospital staff scheduling | [Hospital\_CP.ipynb](Hospital_CP.ipynb) | CP-SAT |
| Airline scheduling (two-stage) | [Airliner-twostage.ipynb](Airliner-twostage.ipynb) | Pyomo |
| Movie shooting sequence | [Movie\_shooting.ipynb](Movie_shooting.ipynb) | CP-SAT |
| Team meeting scheduling | [TeamMeeting.ipynb](TeamMeeting.ipynb) | CP-SAT |

### 🏭 Supply Chain & Resource Allocation

| Problem | File | Tool |
|---|---|---|
| Cutting stock problem | [CSP-git-V1.ipynb](CSP-git-V1.ipynb) | Pyomo |
| Farmer resource allocation | [Farmer\_CP\_V1.ipynb](Farmer_CP_V1.ipynb) | CP-SAT |
| Bilevel optimization (single and multi follower) | [bilevel-github-single-bilevel-multi-EX2.ipynb](bilevel-github-single-bilevel-multi-EX2.ipynb) | Pyomo |
| Gerrymandering (district design) | [Final\_Gerrymandering\_CP.ipynb](Final_Gerrymandering_CP.ipynb) | CP-SAT |
| Yield | [yield.ipynb](yield.ipynb) | Pyomo |

### 🤝 Assignment & Matching

| Problem | File | Tool |
|---|---|---|
| Stable marriage | [stable\_marriage\_CP.ipynb](stable_marriage_CP.ipynb) | CP-SAT |
| Student–professor assignment | [StudenttoProf.ipynb](StudenttoProf.ipynb) | Pyomo |
| Pairing | [Pairing CP.ipynb](Pairing%20CP.ipynb) | CP-SAT |
| Christmas gift happiness maximization | [Gift-Christmas.ipynb](Gift-Christmas.ipynb) | Pyomo |
| Secret Santa | [Secret\_Santa\_Circuit\_Advanced\_CP.ipynb](Secret_Santa_Circuit_Advanced_CP.ipynb) | CP-SAT |
| Social golfer problem | [Social golfer.ipynb](Social%20golfer.ipynb) | Pyomo |

### 🔗 Graphs & Networks

| Problem | File | Tool |
|---|---|---|
| Critical node detection | [CND-github.ipynb](CND-github.ipynb) | Pyomo |
| Graph island detection | [Graph-Island.ipynb](Graph-Island.ipynb) | Pyomo |
| Earthquake network | [earthquake.ipynb](earthquake.ipynb) | Pyomo |
| Max distance on a graph | [max distance.ipynb](max%20distance.ipynb) | Pyomo |
| Max independent set | [April Fools day max independent set.ipynb](April%20Fools%20day%20max%20independent%20set.ipynb) | Pyomo |
| Vertex coloring | [vertexcoloring.ipynb](vertexcoloring.ipynb) | Pyomo |
| Edge coloring | [Edgecoloring.ipynb](Edgecoloring.ipynb) | Pyomo |
| Total coloring | [Totalcoloring.ipynb](Totalcoloring.ipynb) | Pyomo |
| Routing & wavelength assignment | [Routin\_Wavelength\_Assignment\_CP.ipynb](Routin_Wavelength_Assignment_CP.ipynb) | CP-SAT |
| PCB routing | [PCB.py](PCB.py) | CP-SAT |

### 🧩 Logic Puzzles

| Problem | File | Tool |
|---|---|---|
| Zebra puzzle | [zebra\_CP.py](zebra_CP.py) | CP-SAT |
| Zebra puzzle — v2 | [zebra\_CP\_v2.py](zebra_CP_v2.py) | CP-SAT |
| Hidato | [Hidato-git.ipynb](Hidato-git.ipynb) | Pyomo |
| Hashi (bridges) | [HAshi puzzle-git.ipynb](HAshi%20puzzle-git.ipynb) | Pyomo |
| Hitori | [Hitori\_CP.ipynb](Hitori_CP.ipynb) | CP-SAT |
| Bonairo | [Bonairo puzzle .ipynb](Bonairo%20puzzle%20.ipynb) | Pyomo |
| Shikaku | [Shikaku-puzzle-github.ipynb](Shikaku-puzzle-github.ipynb) | Pyomo |
| Suguru | [Suguru\_CP.ipynb](Suguru_CP.ipynb) | CP-SAT |
| Numberlink | [Numberlink-V3-Git.ipynb](Numberlink-V3-Git.ipynb) | Pyomo |
| Slitherlink | [slitherlink\_puzzle.py](slitherlink_puzzle.py) | CP-SAT |
| Slitherlink — drone variant | [slitherlink\_puzzle\_Drone.py](slitherlink_puzzle_Drone.py) | CP-SAT |
| Slitherlink — drone variant v2 | [slitherlink\_puzzle\_Drone-V2.py](slitherlink_puzzle_Drone-V2.py) | CP-SAT |
| Tower (Skyscraper) puzzle | [tower\_puzzle.py](tower_puzzle.py) | CP-SAT |
| Tower puzzle — all solutions | [tower\_puzzle\_allsolutions.py](tower_puzzle_allsolutions.py) | CP-SAT |
| Snake | [Snake\_CP.ipynb](Snake_CP.ipynb) | CP-SAT |
| Snake with eggs | [snake\_egg.py](snake_egg.py) | CP-SAT |
| Snake with eggs — modular | [snake\_egg\_modular.py](snake_egg_modular.py) | CP-SAT |
| Magic square | [MagicSquare.ipynb](MagicSquare.ipynb) | CP-SAT |
| Mean square | [MeanSquare.ipynb](MeanSquare.ipynb) | CP-SAT |
| ROGO | [ROGO\_of\_AddCircuit\_Advanced\_CP.ipynb](ROGO_of_AddCircuit_Advanced_CP.ipynb) | CP-SAT |
| A puzzle a day | [A\_Puzzle\_A\_Day\_git.ipynb](A_Puzzle_A_Day_git.ipynb) | CP-SAT |
| Tiling puzzle | [Tiling.py](Tiling.py) | CP-SAT |
| Domino placement | [domino.ipynb](domino.ipynb) | CP-SAT |
| Maze | [maze.ipynb](maze.ipynb) | Pyomo |
| Clock puzzle | [Clock\_CP.ipynb](Clock_CP.ipynb) | CP-SAT |
| Calculator with two buttons | [calculator\_cp.py](calculator_cp.py) | CP-SAT |
| 1 Euro coin | [1EuroCoin.ipynb](1EuroCoin.ipynb) | CP-SAT |
| Pennies | [Pennies.py](Pennies.py) | Pyomo |
| Empty bucket | [Empty-Bucket-Github.ipynb](Empty-Bucket-Github.ipynb) | Pyomo |
| Family puzzle | [Project\_Family\_Advanced\_CP.ipynb](Project_Family_Advanced_CP.ipynb) | CP-SAT |
| Master Mind game | [game\_Master\_Mind\_CP\_Pyomo.ipynb](game_Master_Mind_CP_Pyomo.ipynb) | CP-SAT / Pyomo |
| Longest common subsequence | [LCS-git.ipynb](LCS-git.ipynb) | Pyomo |
| Maximum path sum (Project Euler 18 & 67) | [maxpasssum.py](maxpasssum.py) | CP-SAT |
| Maximum path sum — visual | [maxpasssum\_visual.py](maxpasssum_visual.py) | CP-SAT |
| Maximum path sum — visual, multiple paths | [maxpasssum\_visual\_multi.py](maxpasssum_visual_multi.py) | CP-SAT |
| Pizza | [Pizza.ipynb](Pizza.ipynb) | CP-SAT |
| Easter photo | [Easter Photo.ipynb](Easter%20Photo.ipynb) | Pyomo |

### ♟️ Chess & Board Puzzles

| Problem | File | Tool |
|---|---|---|
| N-Queens | [N-Queen.ipynb](N-Queen.ipynb) | Pyomo |
| Knight's tour (MILP) | [Knight tour MILP.ipynb](Knight%20tour%20MILP.ipynb) | Pyomo |
| One knight stands | [One\_Knight\_Stansd\_.ipynb](One_Knight_Stansd_.ipynb) | CP-SAT |
| Half chessboard | [half\_chess\_board.ipynb](half_chess_board.ipynb) | CP-SAT |
| Fill the chessboard | [fill\_chess-Github.ipynb](fill_chess-Github.ipynb) | Pyomo |
| Snake on a chessboard | [snake\_chess\_board.ipynb](snake_chess_board.ipynb) | CP-SAT |
| Board puzzle | [board-git.ipynb](board-git.ipynb) | Pyomo |
| Vertex rectangle | [vertex\_rectangle.ipynb](vertex_rectangle.ipynb) | CP-SAT |

### 💼 LinkedIn Puzzles

| Problem | File | Tool |
|---|---|---|
| Queens | [Linkedin\_CP\_Puzzle.ipynb](Linkedin_CP_Puzzle.ipynb) | CP-SAT |
| Queens on a multi-color board | [Queen\_Linkedin\_of\_multi\_color\_chess\_board\_CP.ipynb](Queen_Linkedin_of_multi_color_chess_board_CP.ipynb) | CP-SAT |
| Tango | [TANGO\_of\_Linkedin\_CP\_Puzzle.ipynb](TANGO_of_Linkedin_CP_Puzzle.ipynb) | CP-SAT |
| ZIP | [ZIP\_LInkedin\_CP.ipynb](ZIP_LInkedin_CP.ipynb) | CP-SAT |
| Patches | [patches\_puzzle\_CP\_final.py](patches_puzzle_CP_final.py) | CP-SAT |
| Patches — first version | [patches\_puzzle\_CP.py](patches_puzzle_CP.py) | CP-SAT |

### 🧠 IBM Ponder This Challenges

| Problem | File | Tool |
|---|---|---|
| Prime sequence (March 2024) | [Prime\_IBM\_sequence\_March2024.ipynb](Prime_IBM_sequence_March2024.ipynb) | CP-SAT |
| Solution callback (January 2024) | [callback\_CP\_IBM\_Ponder\_this\_Challenge\_Jan\_2024.ipynb](callback_CP_IBM_Ponder_this_Challenge_Jan_2024.ipynb) | CP-SAT |
| Max army | [IBM\_max\_Army.ipynb](IBM_max_Army.ipynb) | CP-SAT |

### 📐 Geometry & Packing

| Problem | File | Tool |
|---|---|---|
| 2D no-overlap placement | [2d\_no\_overlap.ipynb](2d_no_overlap.ipynb) | CP-SAT |
| Shape placement | [shape\_placement.ipynb](shape_placement.ipynb) | CP-SAT |
| Largest box | [Largest\_box\_CP.ipynb](Largest_box_CP.ipynb) | CP-SAT |
| Biggest circle with equal blue/green points | [blue-green-points-biggest\_circle.ipynb](blue-green-points-biggest_circle.ipynb) | Pyomo |
| Max points | [maxpoints-V2.ipynb](maxpoints-V2.ipynb) | Pyomo |
| Max distance between points | [MaxDistance-Github-V2.ipynb](MaxDistance-Github-V2.ipynb) | Pyomo |

### 🤖 Machine Learning & Data Fitting

| Problem | File | Tool |
|---|---|---|
| SVM — primal & dual classification | [EXample\_SVM\_Primal\_Dual\_Classification\_.ipynb](EXample_SVM_Primal_Dual_Classification_.ipynb) | Pyomo |
| SVM — primal & dual on corn seed data | [EXample\_SVM\_Primal\_Dual\_Classification\_Corn\_.ipynb](EXample_SVM_Primal_Dual_Classification_Corn_.ipynb) | Pyomo |
| SVM — why kernels are needed | [EX\_final\_SVM\_Primal\_Class\_Kernel\_Necessity\_.ipynb](EX_final_SVM_Primal_Class_Kernel_Necessity_.ipynb) | Pyomo |
| SVM — kernel dual, hard constraints | [Class\_kernel\_Dual\_of\_SVM\_hard\_constraint.ipynb](Class_kernel_Dual_of_SVM_hard_constraint.ipynb) | Pyomo |
| K-means clustering | [Clustering\_Kmean\_class.ipynb](Clustering_Kmean_class.ipynb) | Pyomo |
| K-means (class) | [Kmeans\_Class.ipynb](Kmeans_Class.ipynb) | Pyomo |
| Multi-curve regression | [regression-multiline-V4.ipynb](regression-multiline-V4.ipynb) | Pyomo |
| Projectile fitting from an image | [projectile- GitHub-V2.ipynb](projectile-%20GitHub-V2.ipynb) | Pyomo |

### 🛠️ Pyomo & OR-Tools Techniques

| Problem | File | Tool |
|---|---|---|
| Pyomo on Google Colab — setup | [Pyomo\_on\_Google\_Colab.ipynb](Pyomo_on_Google_Colab.ipynb) | Pyomo |
| Pyomo on Google Colab — example | [Pyomo\_example\_on\_Google\_Colab.ipynb](Pyomo_example_on_Google_Colab.ipynb) | Pyomo |
| Solving with the NEOS server | [NEOS Pyomo.ipynb](NEOS%20Pyomo.ipynb) | Pyomo |
| Mutable parameters | [mutable prarameter.ipynb](mutable%20prarameter.ipynb) | Pyomo |
| Indexed variables X[i,j] in Pyomo | [Xij\_Pyomo.ipynb](Xij_Pyomo.ipynb) | Pyomo |
| Indexed variables X[i,j] in CP-SAT | [Xij\_cp.ipynb](Xij_cp.ipynb) | CP-SAT |
| Pyomo.DAE — transient heat transfer | [Pyomo\_dae.ipynb](Pyomo_dae.ipynb) | Pyomo.DAE |
| Solving several instances in parallel (mpi4py) | [multiple\_instances.py](multiple_instances.py) | Pyomo |
| A simple CP model | [simple\_CP.py](simple_CP.py) | CP-SAT |
| Modeling with 7 cases | [7seenPyomo.ipynb](7seenPyomo.ipynb) | Pyomo |

---

## ⚡ Quick Start

### Run locally

```bash
git clone https://github.com/OptimizationExpert/Pyomo.git
cd Pyomo

pip install pyomo ortools matplotlib pandas numpy networkx
pip install highspy            # free LP/MILP solver usable from Pyomo
conda install -c conda-forge coincbc ipopt   # optional: CBC and Ipopt

jupyter notebook
```

### Run on Google Colab ☁️

Open any notebook with its **Open in Colab** badge, or start from
[Pyomo_on_Google_Colab.ipynb](Pyomo_on_Google_Colab.ipynb).

### Pick a tool

| Your problem has… | Start with |
|---|---|
| continuous variables, LP / MILP / NLP structure | **Pyomo** + HiGHS, CBC, Gurobi or Ipopt |
| sequencing, scheduling, logic, all-different, circuits | **OR-Tools CP-SAT** |
| vehicle routing with standard side constraints | **OR-Tools routing library** |

---

## 📡 Stay Connected

| Platform | Link |
|---|---|
| 🌐 Website | [optexpert.org](https://optexpert.org) |
| 📰 LinkedIn newsletter | [Optimization in Open Source](https://www.linkedin.com/newsletters/optimization-in-open-source-6874020019009859585/) |
| 💬 Telegram | [t.me/PyomoChannel](https://t.me/PyomoChannel) |
| 🎓 Udemy course | [Optimization in Python](https://www.udemy.com/course/optimization-in-python/?couponCode=36C6F6B228A087695AD9) |
| 👤 LinkedIn | [Alireza Soroudi](https://www.linkedin.com/in/soroudi/) |

---

## 🤝 Contributing

Contributions are welcome:

1. Fork the repository and create a branch.
2. Add a notebook with a problem description, the mathematical formulation, clean code and a visualization.
3. Run it end to end.
4. Open a pull request and say which section of this README it belongs to.

---

## 📖 How to Cite

```bibtex
@misc{soroudi2024pyomo,
  author       = {Alireza Soroudi},
  title        = {Optimization Expert — Pyomo \& OR-Tools Model Library},
  year         = {2024},
  publisher    = {GitHub},
  url          = {https://github.com/OptimizationExpert/Pyomo}
}
```

A [CITATION.cff](CITATION.cff) file is also included, so GitHub's **"Cite this repository"** button works.

---

## 📄 License

[MIT](LICENSE) — use it, fork it, build on it.

*If this library helped you, a ⭐ helps others find it.*
