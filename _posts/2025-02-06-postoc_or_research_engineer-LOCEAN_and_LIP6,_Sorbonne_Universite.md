---
layout: post
title: Postoc or research engineer position in ocean model (Paris, France)
subtitle: Locean and lip6, sorbonne université
tags: [postoc or research engineer, ocean model, France]
comments: false
---
# Precision optimization in an ocean model
## Background
Numerical modelling has come to play a key role in climate research, particularly in the
generation of the different climate change scenarios that form the basis of the IPCC reports.
Climate models are extremely complex and require huge computational resources. Optimizing them is therefore both a necessity and a real challenge. The objective is to accelerate
the NEMO code, which is one of the most popular components of these climate models.
NEMO (Nucleus for European Modelling of the Ocean) is an Ocean General Circulation
Model (OGCM) designed to describe ocean dynamics, marine biogeochemistry, and sea ice
through its various modules. More than a thousand people use NEMO to work on a wide
range of topics: fundamental research into coastal and open ocean oceanography, studies of
past, present and future climates, operational oceanography, weather forecasts and climate
projections.
This work will be carried out in the framework of the European project ENMASSE (Enhancing Nemo for Marine Applications and Services). This project is appointed by Mercator Ocean International, which is implementing the European ocean-monitoring service
(the Copernicus Marine Service, CMEMS), as part of the European Earth observation programme, Copernicus.

## Research directions
Since its creation, NEMO has been designed to run in double precision, i.e. using 64-bit
floating-point numbers. Using lower precision can be beneficial in terms of performance by
reducing memory usage, execution time (by two) and energy consumption. However, lower
precision can also increase numerical instabilities. The main objective of this project is to
automatically identify and control sources of instabilities when running NEMO in single
precision.
To support this, the plan is to use the CADNA library [1, 2] which relies on Discrete Stochastic Arithmetic [3] to estimate rounding errors in numerical codes and detect numerical instabilities that may occur during their execution. The CADNA library will be used to control
the numerical quality of the results computed by NEMO and point out the possible numerical instabilities. By leveraging CADNA, we will automatically identify instability sources
and try to fix/bypass them by combining our expertise on NEMO algorithms with CADNA
developers’ knowledge of numerical precision/instabilities. Different physical configurations
of NEMO, either local or global, will be studied. We also plan to optimize the threshold
values in NEMO, taking into account the various precisions used.

## Location
The recruited person will be supervised by two laboratories of Sorbonne Université
• the Oceanography and Climate Science LOCEAN laboratory:
https://www.locean.ipsl.fr
• the Computer Science LIP6 laboratory:
https://www.lip6.fr
These two laboratories are settled on the Pierre & Marie Curie Campus of Sorbonne Université, in the Latin Quarter of Paris, France.
## Salary
The gross salary per month (including national health transport and lunch subsidies, insurance and employment insurance) varies from 2600 to 3700 euros depending on the experience.
## Duration
1 year, renewable 1 year
## Qualifications and skills
Candidates must have a PhD in Computer Science, Applied Physics, Applied Mathematics
or other relevant fields, with both good programming skills and good knowledge in numerical
algorithms.
## Application
Applications should be sent to Stef Graillat (Stef.Graillat@lip6.fr), Fabienne Jézéquel
(Fabienne.Jezequel@lip6.fr), and Sébastien Masson (Sebastien.Masson@locean.ipsl.fr).
They should include:
* a curriculum vitae;
* a motivation letter;
* at least two referees with their e-mail addresses;
* links to PhD thesis and publications;
* links to software contributions.

Useful links
* NEMO:
  * web site: https://www.nemo-ocean.eu/
  * gitlab forge: https://forge.nemo-ocean.eu/nemo/nemo
  * zenodo documentation: https://zenodo.org/records/14515373
* Mercator Ocean International: https://www.mercator-ocean.eu/en/
* Copercinus Marine Service: https://marine.copernicus.eu
* Copercinus: https://www.copernicus.eu/en
* CADNA: http://cadna.lip6.fr

References
[1] P. Eberhart, J. Brajard, P. Fortin, and F. Jézéquel. High performance numerical validation using stochastic arithmetic. Reliable Computing, 21:35–52, 2015.
[2] F. Jézéquel and J.-M. Chesneaux. CADNA: a library for estimating round-off error
propagation. Computer Physics Communications, 178(12):933–955, 2008.
[3] J. Vignes. Discrete Stochastic Arithmetic for validating results of numerical software.
Numerical Algorithms, 37(1–4):377–390, December 2004.

link to the announce: https://www-pequan.lip6.fr/~jezequel/OFFERS/Offer_ENMASSE.pdf

