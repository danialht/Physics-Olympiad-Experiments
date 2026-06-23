# Experiment 4: Charged Projectile in a Rotating Field

You are in a room shaped like a rectangular cuboid. It has a ceiling of unknown height $H$, but its walls are far enough out of reach that they can be ignored.

The acceleration of gravity is $g=9.81\pm0.01\ \frac{m}{s^{2}}$. Consider a coordinate system whose z-axis is parallel to, and points opposite, gravity.

You can throw a ball of mass $m=1.500\pm0.001\ \text{kg}$ from an arbitrary height $h<H$ with an arbitrary initial velocity vector $\vec{v}_{0}$. The ball carries a charge $q$.

Everywhere in the room there is an electric field of constant magnitude $E$, making an angle $\theta$ with the z-axis. At $t=0$ this field lies in the zx-plane, and its direction then rotates about the z-axis with angular velocity $\omega$. You may also superimpose your own constant electric field, in any direction you choose.

### The Problem

Find the following quantities, in any order and by any correct method:

**a)** Charge $q$

**b)** Magnitude of the field $E$

**c)** Angle $\theta$ of the field with the z-axis

**d)** Ceiling height $H$

**e)** Period of the field's rotation

### Program Guide

The program takes the initial height of the projectile $h$, its initial velocity vector, and the constant field vector you choose to add (on top of the room's rotating field). It then returns the projectile's time of flight and landing location.

- The x and y coordinates of the projectile at the initial moment are 0.
- Consider the error of the numbers you give to the program as zero.
- Consider the error of the numbers you receive from the program as **0.0001 m** for X and Y, and **0.0001 s** for T.

### Downloads

- [Program (exp4ver2.exe)](/experiments/exp4/exp4ver2.exe)
- [Source code (exp4.py)](/experiments/exp4/exp4.py)
- [Solution (exp4_solution.xlsx)](/experiments/exp4/exp4_solution.xlsx)