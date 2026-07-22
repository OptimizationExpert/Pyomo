# 🧮 Optimization Expert — Pyomo & OR-Tools Notebook Library

> *A hands-on, open-source collection of solved optimization problems using Pyomo, OR-Tools (CP-SAT), and MILP — from supply chain to puzzles, routing to scheduling.*

[![Stars](https://img.shields.io/github/stars/OptimizationExpert/Pyomo?style=social)](https://github.com/OptimizationExpert/Pyomo/stargazers)
[![Forks](https://img.shields.io/github/forks/OptimizationExpert/Pyomo?style=social)](https://github.com/OptimizationExpert/Pyomo/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![LinkedIn Newsletter](https://img.shields.io/badge/LinkedIn-Newsletter-blue?logo=linkedin)](https://www.linkedin.com/newsletters/optimization-in-open-source-6874020019009859585/)
[![Telegram](https://img.shields.io/badge/Telegram-Channel-2CA5E0?logo=telegram)](https://t.me/PyomoChannel)

---

## 🚀 What Is This Repository?

This repository is a **living library** of optimization models — each one a fully solved, self-contained Jupyter notebook. Problems range from real-world supply chain challenges to classic combinatorial puzzles, all tackled using the power of mathematical programming.

Whether you're a student stepping into Operations Research, a practitioner solving real business problems, or a puzzle enthusiast who thinks in constraints — there's something here for you.

**Tools used across the notebooks:**
- 🐍 [Pyomo](http://www.pyomo.org/) — algebraic modeling in Python
- ⚙️ [Google OR-Tools CP-SAT](https://developers.google.com/optimization) — constraint programming solver
- 🔢 Solvers: Gurobi, CBC, GLPK, NEOS Server

---

## 📂 What's Inside

Each notebook includes:

1. **Problem Description** — a clear, intuitive explanation of the challenge
2. **Mathematical Formulation** — the model written out properly (sets, variables, constraints, objective)
3. **Python Implementation** — clean code in Pyomo or OR-Tools CP-SAT
4. **Solution & Visualization** — results displayed with charts, tables, and maps where relevant
5. **Analysis** — interpretation of the solution and key insights

---

## 🗂️ Solved Problems

### 🚛 Routing & Logistics
| Problem | Notebook |
|---|---|
| Capacitated VRP (CVRP) | [CVRP_CP.ipynb](CVRP_CP.ipynb) |
| CVRP with Time Windows | [CVRPTW_CP.ipynb](CVRPTW_CP.ipynb) |
| Clustered CVRP | [CCVRP_CP.ipynb](CCVRP_CP.ipynb) |
| TSP with AddCircuit | [AddCircuit_Advanced_CP.ipynb](AddCircuit_Advanced_CP.ipynb) |
| Large-scale TSP | [Large_TSP_CP.ipynb](Large_TSP_CP.ipynb) |
| TSP with Precedence Constraints | [precedence_AddCircuit_Advanced_CP.ipynb](precedence_AddCircuit_Advanced_CP.ipynb) |
| VRP Wiring (no crossings) | [VRP_Circuit_CP_Wiring_nocross.ipynb](VRP_Circuit_CP_Wiring_nocross.ipynb) |
| Boat Tour Optimization | [BoatTour.ipynb](BoatTour.ipynb) |
| Optimal Order Pickup from Inventory | [storage_routing.ipynb](storage_routing.ipynb) |
| Conquering All Metro Stations | [Metro map -V3-github.ipynb](Metro%20map%20-V3-github.ipynb) |

### 📅 Scheduling
| Problem | Notebook |
|---|---|
| Job Shop Scheduling (with idle time) | [JobShop_CP_ORTools_Idle_time.ipynb](JobShop_CP_ORTools_Idle_time.ipynb) |
| RCPSP with Cumulative Constraints | [RCPSP_Cummulative_CP.ipynb](RCPSP_Cummulative_CP.ipynb) |
| Airline Crew Scheduling (Two-Stage) | [Airliner-twostage.ipynb](Airliner-twostage.ipynb) |
| Movie Shooting Sequence | [Movie_shooting.ipynb](Movie_shooting.ipynb) |
| Team Meeting Scheduling | [TeamMeeting.ipynb](TeamMeeting.ipynb) |
| Hospital Staff Scheduling | [Hospital_CP.ipynb](Hospital_CP.ipynb) |
| Tourist Trip Scheduling (TTP) | [TTP_CP.ipynb](TTP_CP.ipynb) |
| Project Scheduling (MOO) | [Project-Class-module-github-MOO.ipynb](Project-Class-module-github-MOO.ipynb) |

### 🔗 Graph Theory & Networks
| Problem | Notebook |
|---|---|
| Critical Node Detection | [CND-github.ipynb](CND-github.ipynb) |
| Graph Island Detection | [Graph-Island.ipynb](Graph-Island.ipynb) |
| Edge Coloring | [Edgecoloring.ipynb](Edgecoloring.ipynb) |
| Total Coloring | [Totalcoloring.ipynb](Totalcoloring.ipynb) |
| Routing & Wavelength Assignment | [Routin_Wavelength_Assignment_CP.ipynb](Routin_Wavelength_Assignment_CP.ipynb) |
| 2D No-Overlap Placement | [2d_no_overlap.ipynb](2d_no_overlap.ipynb) |
| Max Independent Set | [April Fools day max independent set.ipynb](April%20Fools%20day%20max%20independent%20set.ipynb) |

### 🧩 Puzzles & Combinatorics
| Problem | Notebook |
|---|---|
| N-Queens | [N-Queen.ipynb](N-Queen.ipynb) |
| Magic Square | [MagicSquare.ipynb](MagicSquare.ipynb) |
| Knight's Tour (MILP) | [Knight tour MILP.ipynb](Knight%20tour%20MILP.ipynb) |
| Hidato Puzzle | [Hidato-git.ipynb](Hidato-git.ipynb) |
| Hashi (Bridges) Puzzle | [HAshi puzzle-git.ipynb](HAshi%20puzzle-git.ipynb) |
| Hitori Puzzle | [Hitori_CP.ipynb](Hitori_CP.ipynb) |
| Bonairo Puzzle | [Bonairo puzzle .ipynb](Bonairo%20puzzle%20.ipynb) |
| Shikaku Puzzle | [Shikaku-puzzle-github.ipynb](Shikaku-puzzle-github.ipynb) |
| Suguru Puzzle | [Suguru_CP.ipynb](Suguru_CP.ipynb) |
| Numberlink | [Numberlink-V3-Git.ipynb](Numberlink-V3-Git.ipynb) |
| Slitherlink | [slitherlink_puzzle.py](slitherlink_puzzle.py) |
| A Puzzle A Day | [A_Puzzle_A_Day_git.ipynb](A_Puzzle_A_Day_git.ipynb) |
| LinkedIn Queens Puzzle | [Linkedin_CP_Puzzle.ipynb](Linkedin_CP_Puzzle.ipynb) |
| LinkedIn Tango Puzzle | [TANGO_of_Linkedin_CP_Puzzle.ipynb](TANGO_of_Linkedin_CP_Puzzle.ipynb) |
| LinkedIn ZIP Puzzle | [ZIP_LInkedin_CP.ipynb](ZIP_LInkedin_CP.ipynb) |
| ROGO Puzzle | [ROGO_of_AddCircuit_Advanced_CP.ipynb](ROGO_of_AddCircuit_Advanced_CP.ipynb) |
| Master Mind Game | [game_Master_Mind_CP_Pyomo.ipynb](game_Master_Mind_CP_Pyomo.ipynb) |
| Social Golfer Problem | [Social golfer.ipynb](Social%20golfer.ipynb) |
| Secret Santa Assignment | [Secret_Santa_Circuit_Advanced_CP.ipynb](Secret_Santa_Circuit_Advanced_CP.ipynb) |
| 15-Puzzle IBM Challenge | [15_Puzzle_IBM_Git.ipynb](15_Puzzle_IBM_Git.ipynb) |
| Prime Sequence IBM Challenge | [Prime_IBM_sequence_March2024.ipynb](Prime_IBM_sequence_March2024.ipynb) |
| IBM Max Army Challenge | [IBM_max_Army.ipynb](IBM_max_Army.ipynb) |

### 🏭 Supply Chain & Operations
| Problem | Notebook |
|---|---|
| Cutting Stock Problem (CSP) | [CSP-git-V1.ipynb](CSP-git-V1.ipynb) |
| Bilevel Optimization | [bilevel-github-single-bilevel-multi-EX2.ipynb](bilevel-github-single-bilevel-multi-EX2.ipynb) |
| Gerrymandering (District Design) | [Final_Gerrymandering_CP.ipynb](Final_Gerrymandering_CP.ipynb) |
| Farmer Resource Allocation | [Farmer_CP_V1.ipynb](Farmer_CP_V1.ipynb) |
| Stable Marriage Problem | [stable_marriage_CP.ipynb](stable_marriage_CP.ipynb) |
| Student–Professor Assignment | [StudenttoProf.ipynb](StudenttoProf.ipynb) |
| Christmas Gift Happiness Maximization | [Gift-Christmas.ipynb](Gift-Christmas.ipynb) |
| Pairing Optimization | [Pairing CP.ipynb](Pairing%20CP.ipynb) |
| 7-Seen Modeling | [7seenPyomo.ipynb](7seenPyomo.ipynb) |
| Pyomo with NEOS Server | [NEOS Pyomo.ipynb](NEOS%20Pyomo.ipynb) |
| Pyomo on Google Colab | [Pyomo_on_Google_Colab.ipynb](Pyomo_on_Google_Colab.ipynb) |

### 📐 Geometry & Machine Learning
| Problem | Notebook |
|---|---|
| Largest Box (CP) | [Largest_box_CP.ipynb](Largest_box_CP.ipynb) |
| Biggest Circle with Equal Points | [blue-green-points-biggest_circle.ipynb](blue-green-points-biggest_circle.ipynb) |
| Max Distance Between Points | [MaxDistance-Github-V2.ipynb](MaxDistance-Github-V2.ipynb) |
| Shape Placement (CP) | [shape_placement.ipynb](shape_placement.ipynb) |
| SVM Primal & Dual (Classification) | [EXample_SVM_Primal_Dual_Classification_.ipynb](EXample_SVM_Primal_Dual_Classification_.ipynb) |
| SVM with Kernel | [Class_kernel_Dual_of_SVM_hard_constraint.ipynb](Class_kernel_Dual_of_SVM_hard_constraint.ipynb) |
| K-Means Clustering (Optimization) | [Clustering_Kmean_class.ipynb](Clustering_Kmean_class.ipynb) |
| Multi-Curve Regression | [regression-multiline-V4.ipynb](regression-multiline-V4.ipynb) |
| Longest Common Subsequence | [LCS-git.ipynb](LCS-git.ipynb) |

---

## ⚡ Quick Start

### Run Locally

```bash
# Clone the repository
git clone https://github.com/OptimizationExpert/Pyomo.git
cd Pyomo

# Install dependencies
pip install pyomo ortools matplotlib pandas numpy

# Install a free solver (CBC)
conda install -c conda-forge coincbc

# Launch Jupyter
jupyter notebook
```

### Run on Google Colab ☁️

No local setup needed — open any notebook directly in Colab using the badge at the top of each notebook, or start with the dedicated Colab setup notebook:

👉 [Pyomo_on_Google_Colab.ipynb](Pyomo_on_Google_Colab.ipynb)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Pyomo** | Algebraic modeling language for LP, MILP, NLP, Bilevel |
| **OR-Tools CP-SAT** | Constraint programming for combinatorial problems |
| **Gurobi** | High-performance commercial solver (free academic license) |
| **CBC / GLPK** | Open-source solvers, zero setup required |
| **NEOS Server** | Free cloud-based solver access |
| **Jupyter Notebooks** | Interactive, documented problem-solving environment |

---

## 📡 Stay Connected

| Platform | Link |
|---|---|
| 📰 LinkedIn Newsletter | [Optimization in Open-Source](https://www.linkedin.com/newsletters/optimization-in-open-source-6874020019009859585/) |
| 💬 Telegram Channel | [t.me/PyomoChannel](https://t.me/PyomoChannel) |
| 🎓 Udemy Course | [Optimization in Python](https://www.udemy.com/course/optimization-in-python/?couponCode=36C6F6B228A087695AD9) |
| 👤 LinkedIn Profile | [Alireza Soroudi](https://www.linkedin.com/in/soroudi/) |

---

## 🤝 Contributing

Contributions are warmly welcome! To add a new notebook or improve an existing one:

1. Fork the repository and create a new branch
2. Write clean, well-documented code with problem description and formulation
3. Test your notebook end-to-end
4. Submit a pull request with a clear description of what you've added

Let's build the most comprehensive open-source optimization library together! 🌍

---

## 📖 How to Cite

If this repository has been useful in your research or work, please cite it:

```bibtex
@misc{soroudi2024pyomo,
  author       = {Alireza Soroudi},
  title        = {Optimization Expert — Pyomo \& OR-Tools Notebook Library},
  year         = {2024},
  publisher    = {GitHub},
  url          = {https://github.com/OptimizationExpert/Pyomo}
}
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — use it, fork it, build on it freely.

---

<p align="center">
  <i>If this repo helped you solve a hard problem or learn something new — consider giving it a ⭐ star. It helps others find it too!</i>
</p>
