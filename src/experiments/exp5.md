# Experiment 5

Consider a 1000-meter by 1000-meter environment in which a mountain exists. You provide the program with $x$ and $y$, and it gives you $h(x,y)$, which is the elevation above sea level at the coordinates $(x,y)$.

**Program Notes:** The numbers you enter into the program are rounded to a multiple of 10. The output error is 1 meter.

**a)** We want to find the peak. By collecting data, find the coordinates that yield the maximum $h$ ($h_{max}$). Now, also measure the four coordinates that are 10 meters away and surrounding it. From these, find the minimum ($h_{min}$). Take the error of $h$ as the difference between $h_{max}$ and $h_{min}$, and report it. What is the error of the peak's coordinates?

**b)** Assume the following equation describes this mountain (though it may not describe everywhere on the mountain perfectly):

$$h(x,y)=He^{-ar^{2}}$$

where $r$ is the distance to the peak. Based on this equation, find $a$, $H$, and their errors.

**c)** At distances further away from the peak, the land has a gentle slope. Find the angle of the slope.

**d)** Draw a topographic map along with the topographic contour lines. The consecutive contour lines should have a 300-meter interval between their $h$ values. Use interpolation to find points with your desired $h$.

> *Hint:* For interpolation, always use two points whose connecting line is parallel to either the $x$ or $y$ axis.

**e)** Using the 5 points you measured in part (a), find the height of the peak using a parabolic model once in the $y$-direction for three points, and once in the $x$-direction for three points.

### Downloads

- [Program .exe file](/experiments/exp5/exp5%28edited%29.exe)
- [Source code in Python](/experiments/exp5/exp5%28edited%29.py)
- [Answer key (in Persian)](/experiments/exp5/%D9%BE%D8%A7%D8%B3%D8%AE%D9%86%D8%A7%D9%85%D9%87%20%D8%A2%D8%B25.xlsx)
