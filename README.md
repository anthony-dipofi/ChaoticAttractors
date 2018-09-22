# Chaotic Attractors


A library to simulate trajectories of various systems of differential and difference equations, built primarily for the purpose of exploring the dynamics of chaotic attractors. Requires Numpy and Matplotlib.

# Examples
Rabinovich–Fabrikant equations

https://en.wikipedia.org/wiki/Rabinovich%E2%80%93Fabrikant_equations
```
from attractors import RabFab_attractor
RabFab_attractor(init = (-1,0,0.5), a = 1.1, g = 0.87, speed = 0.001, steps = 150000)
```

![Rabinovich Fabrikant](https://github.com/goolulusaurs/ChaoticAttractors/blob/master/example_images/Rabinovich_Fabrikant_oscillator_1.png)

```
RabFab_attractor(init = (-1,0,0.5), a = 1.1, g = 0.87, speed = 0.001, steps = 150000)
```

![Rabinovich Fabrikant](https://github.com/goolulusaurs/ChaoticAttractors/blob/master/example_images/Rabinovich_Fabrikant_oscillator_2.png)

Rossler Attractor

https://en.wikipedia.org/wiki/R%C3%B6ssler_attractor

```
from attractors import Rossler_attractor
Rossler_attractor(init = (0.1,0.1,0.1), a = 0.35, b = 0.5, c = 12, speed = 0.01, steps = 15000)
```

![Rossler Attractor](https://github.com/goolulusaurs/ChaoticAttractors/blob/master/example_images/Rossler_attractor.png)

Lu Chen Attractor

https://en.wikipedia.org/wiki/Multiscroll_attractor
```
from attractors import Lu_Chen_attractor
Lu_Chen_attractor(init = (0.1, 0.3, -0.5), a = 29, b = 3, c = 22, u = -1, speed = 0.001, steps = 25000) 

```

![Lu Chen Attractor](https://github.com/goolulusaurs/ChaoticAttractors/blob/master/example_images/Lu_Chen_attractor.png)


Skew Tent Map

https://infoscience.epfl.ch/record/52235/files/IC_TECH_REPORT_199704.pdf

```
from attractors import Skew_Tent_map
Skew_Tent_map(init = 0.5, b = 0.68, steps = 250)
```

![Skew Tent Map](https://github.com/goolulusaurs/ChaoticAttractors/blob/master/example_images/Skew_Tent_Map.png)


Logistic Map

https://en.wikipedia.org/wiki/Logistic_map
```
from attractors import Logistic_map
Logistic_map(init = 0.5, p = 3.99, steps = 150)
```

![Logistic Map](https://github.com/goolulusaurs/ChaoticAttractors/blob/master/example_images/Logistic_Map.png)

Gingerbread Map

http://mathworld.wolfram.com/GingerbreadmanMap.html
```
from attractors import GingerBread_map
GingerBread_map(init = (3.5, 3.5), steps = 250)
```
![Gingerbread Map](https://github.com/goolulusaurs/ChaoticAttractors/blob/master/example_images/GingerBread_Map.png)

Van der Pol Oscillator

https://arxiv.org/abs/0803.1658

```
from attractors import VanDerPol_oscillator
VanDerPol_oscillator(init = (0.5, 0.5), p = 1.614, speed = 0.001, steps = 15250)

```
![Van der Pol Oscillator](https://github.com/goolulusaurs/ChaoticAttractors/blob/master/example_images/VanderPol_Oscillator.png)



Bogdanov Map

https://arxiv.org/abs/chao-dyn/9402006

```
from attractors import Bogdanov_map
Bogdanov_map(init=(0.1,0), epsilon = 0.0000, k = 0.0001, mu = 0.020, steps = 10450)
```

![Bogdanov Map](https://github.com/goolulusaurs/ChaoticAttractors/blob/master/example_images/Bogdanov_Map.png)


Lorenz Attractor

https://en.wikipedia.org/wiki/Lorenz_system

```
from attractors import Lorenz_attractor
Lorenz_attractor(init = (10,10,10), sigma = 10, rho = 28, beta = 8/3, speed = 0.001, steps = 30000)
```

![Lorenz Attractor](https://github.com/goolulusaurs/ChaoticAttractors/blob/master/example_images/Lorenz_attractor.png)

