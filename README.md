# ChaoticAttractors


A simple library to simulate the trajectories of a various chaotic dynamical systems.
# Examples
Rabinovich–Fabrikant equations

```
from attractors import RabFab_attractor
RabFab_attractor(init = (-1,0,0.5), a = 1.1, g = 0.87, speed = 0.001, steps = 150000)
```

![Rabinovich Fabrikant](https://github.com/goolulusaurs/ChaoticAttractors/blob/master/example_images/Rabinovich_Fabrikant_oscillator_1.png)

Rossler Attractor

```
from attractors import Rossler_attractor
Rossler_attractor(init = (0.1,0.1,0.1), a = 0.35, b = 0.5, c = 12, speed = 0.01, steps = 15000)
```

![Rossler Attractor](https://github.com/goolulusaurs/ChaoticAttractors/blob/master/example_images/Rossler_attractor.png)

Lorenz Attractor

```
from attractors import Lorenz_attractor
Lorenz_attractor(init = (10,10,10), sigma = 10, rho = 28, beta = 8/3, speed = 0.001, steps = 30000)
```

![Lorenz Attractor](https://github.com/goolulusaurs/ChaoticAttractors/blob/master/example_images/Lorenz_attractor.png)


Skew Tent Map

```
from attractors import Skew_Tent_map
Skew_Tent_map(init = 0.5, b = 0.68, steps = 250)
```

![Skew Tent Map](https://github.com/goolulusaurs/ChaoticAttractors/blob/master/example_images/Skew_Tent_Map.png)
