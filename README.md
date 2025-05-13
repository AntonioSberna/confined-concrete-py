# Concrete Confinement Models in Python

This repository contains Python functions for computing confined concrete properties based on analytical models. It is intended for researchers and engineers working in structural engineering, especially in the field of reinforced concrete modeling.

## ✅ Currently Implemented

### Eurocode 2 (EN 1992-1-1:2004 §3.1.9)

Implemented confinement model for concrete with transverse reinforcement (stirrups) as defined by the European standard:

> CEN (2004). *Eurocode 2: Design of concrete structures – Part 1-1: General rules and rules for buildings*. EN 1992-1-1, European Committee for Standardization.

The function `conf_concr_EC2` computes enhanced strength and strain parameters for confined concrete, suitable for use in nonlinear modeling (e.g., OpenSees `Concrete01` material).

## 🔜 Planned Additions

Upcoming implementations will include:

- **Mander et al. (1988)**
- **Kent & Park (1971)**
- **Saatcioglu & Razvi (1992)**
- **Steel Jacketing confinement models**
- **FRP confinement models**

## 📁 Repository Structure

```
.
├── conf_concr.py     # Core function: EC2 confinement model
├── tests.py          # Example and stress-strain visualization using EC2 model
```

## 🚀 Getting Started

Clone the repository and run the `tests.py` script to visualize the stress-strain curves of confined vs unconfined concrete:

```bash
git clone https://github.com/your-username/concrete-confinement.git
cd concrete-confinement
python tests.py
```

## 📈 Example Output

The `tests.py` file generates the EC2 parabola-rectangle stress-strain curve for both unconfined and confined concrete, visualized using Matplotlib.

## 📜 License

This project is released under the MIT License. See the LICENSE file for details.