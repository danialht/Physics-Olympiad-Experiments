# Experiment 3: The Fall

*Program Manual* — Developed by **Mohammad Amin Haghjoo**, February 2025

In this experiment a hypothetical ball of mass $m$ is released from a height of $h$ in the presence of gravity $g$ and linear air drag.

$$F_{drag}=-\alpha v \quad (1)$$

The provided .exe file will input the height and mass from you and return the time that the ball hits the ground. Your task is to find the values of $g$ and $\alpha$.

> `Enter a height in meters between 0.00 and 10.00.`

*Fig 1, Program Interface*

The times given to you include random error; therefore, standard statistical methods are required here.

### Program Guide

**Notes:**

1. ALWAYS enter data in the requested format, DO NOT enter characters when numbers are asked for.
2. The program keeps running until you shut it down by using the EXIT command when prompted.
3. If your PC tells you that the program is from an unknown publisher and gives a warning, ignore it. There is no matter of concern.
4. Perform your calculations in Microsoft Excel.
5. Note that you can copy numbers from the program; to do so, select that part and use ctrl + c to copy it. You can also use ctrl + v to paste.
6. To close the program by other means, use ctrl + c when no text is selected, closing the window is also possible.

### The Problem

**a)** Derive an equation relating the quantities $g$, $h$, $t$, $\gamma=\frac{\alpha}{m}$.

**b)** Construct a table to document your data points and their errors, and any other quantities you may have defined.

**c)** From your data and regressional analysis, find the values of $\alpha$ and $g$.

### Mathematical Reference

**Integrals:**

$$\int e^{x}dx=e^{x}+C \qquad C\in\mathbb{R} \quad (2)$$

$$\int x^{n}dx=\frac{x^{n+1}}{n+1}+C \qquad C\in\mathbb{R} \text{ and } n\ne-1 \quad (3)$$

**Differential Equations:**

$$\frac{dy}{dx}+P(x)y=Q(x)\Rightarrow y=e^{-\int P(x)dx}\left(\int Q(x)e^{\int P(x)dx}dx+C\right) \quad (4)$$

### Downloads

- [Program (experiment3.exe)](/experiments/exp3/experiment3.exe)
- [Source code (experiment3.cpp)](/experiments/exp3/experiment3.cpp)
- [Answers header (answers.hpp)](/experiments/exp3/answers.hpp)
- [Guide source (ex3guide.tex)](/experiments/exp3/ex3guide.tex)

Good Luck! *-Mohammad Amin Haghjoo*
