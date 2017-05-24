# From haloes to model galaxies: using SQL queries and python 

Use the Millennium DataBase (http://virgo.dur.ac.uk) to retrive data using SQL queries and analyse the data using python. The material builds on each other, so this is the recommended order:

* **virgoDB.ipynb**: Introduction to the Virgo Data Base. Simple SQL are used to retrive data from the millimil Data Base for which no registration is needed.

* **halo_mass.ipynb**: Measure the halo mass function from the millimil Database.

* **halo2stellar.ipynb**: Generate a galaxy stellar mass function using simple empirical models and a semi-analytical model, and compare it to observations. To understand better the modelling of galaxies have a look to **images/modelling_galaxies.pdf**. Supplementary information on going from photons to mass can by found in **l2mass.ipynb**.

* **on_halotools.ipynb**: Populate the millimil haloes with galaxies, using and halo occupation distribution model through 'halotools' (https://halotools.readthedocs.io/en/latest/).