# Experiment 6

## Advanced C++ Computational Physics
High-performance computing for physics simulations.

## Electromagnetism
Maxwell's equations describe electromagnetic phenomena:

$$\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}$$
$$\nabla \cdot \mathbf{B} = 0$$
$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$
$$\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}$$

## Simulation Details
- Domain size: 1m × 1m
- Grid points: 256 × 256
- Time duration: 10 microseconds
- Solver: FDTD (Finite-Difference Time-Domain)

## Performance Metrics
- Computation time: ~5 minutes
- Memory usage: 512 MB

## Visualization
Field distributions at different time steps.
