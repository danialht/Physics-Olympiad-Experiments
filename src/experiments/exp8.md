# Experiment 8: Potential of a Charged Disk

In this experiment, a non-conducting charged disk of radius $R$ and uniform surface charge density $\sigma$ lies in the plane $ax+by+cz=1$, centered at $C=(x_c, y_c, z_c)$. Your task is to find all of these unknown parameters.

> *Note:* The program allows infinite precision and includes no measurement error.

The experiment is simulated inside the cube $0 \le x,y,z \le 10$ meters; it is guaranteed that the entire disk lies within this cube.

### Program Guide

The program has two operating modes:

- **Mode A:** You input three coordinates, and the program returns the electric potential at that point.
- **Mode B:** You input three integers specifying how many points to divide each axis into ($n_x \times n_y \times n_z$ points total). This creates a discrete cubic lattice of the given dimensions and outputs the potential at every point in it. I recommend not exceeding 4000–8000 measurements in total (do not enter any number greater than 20 per axis).

The data is written to a file named `result.txt`, in the same folder as the `.exe` file or the folder just outside it. This text format can be imported into Excel directly.

### Downloads
- [Source code (Main.py)](/experiments/exp8/Main.py)

