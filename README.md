# Second-Order-Semidiscrete-Central-Upwind-Scheme
The second-order semidiscrete central-upwind scheme is used to model compressible flow systems. 
The equations governing the flow are the equation of mass conservation, energy conservation 
and the compressible Euler Equations. 
<br /> <br />
An OpenMP parallelized numerical framework written in C++, controlled through simple Python scripts 
by the use of pybind11, is in use to implement the semidiscrete central-upwind scheme. The implementation 
is tested through a number of classic examples with known solutions. 
<br /> <br /> 
The current form of the code is only featured for uniform, quadrilateral cells, with zero gradient
boundary conditions.

# <sub>Usage</sub>
# <sub><sub>Build Instructions</sub></sub>
Clone the GitHub repository 
```bash
git clone https://github.com/ErinSam/Second-Order-Semidiscrete-Central-Upwind-Scheme.git
```
Create the shared library 
```bash
make
```
# <sub><sub>Running a configuration</sub></sub>
To run the simulation, excecute run.sh with appropriate variables
```bash
./run.sh var1 var2 var3 var4 var5 var6
```
where,      
   var1: number of mesh cells  
   var2: dx, the size of each finite volume mesh cell  
   var3: dt, the size of a single time step  
   var4: the number of time steps for the simulation  
   var5: save frequency  
An example for 200x200 mesh, with dx = 0.0025, dt = 0.000025, numIterations = 125000, save frequency = 20
```bash
./run.sh 200 0.0025 0.000025 125000 20
```
# <sub><sub>Post Processing</sub></sub>
View the latest data with an interactive 3D plot
```bash
make plotLastest
```
Save density charts (distribution, surface plot, contour plot) for all the data saved
```bash
make saveAll
```
All the saved data is stored in the ./data/ directory and images in the ./data/img/. To 
change the location of the saved data, make appropriate changes to ./bin/postProcess.py

# <sub>Benchmarking</sub>


# <sub>Numerical Experiments</sub>


# <sub><sub>References</sub></sub>
[[1]] Alexander Kurganov; Eitan Tadmor (2002). _Solution of two-dimensional Riemann problems for gas dynamics 
    without Riemann problem solvers._ , 18(5), 584–608. 
<br />
[[2]] Kurganov, Alexander; Noelle, Sebastian; Petrova, Guergana (2001). _Semidiscrete Central-Upwind Schemes for Hyperbolic Conservation Laws and Hamilton--Jacobi Equations. SIAM Journal on Scientific Computing._, 23(3), 707–740.


[1]: https://doi.org/10.1002/num.10025
[2]: https://doi.org/10.1137/S1064827500373413
