---
layout: post
title: Postdoc position in sea ice modelling and machine learning (Louvain-la-Neuve, Belgium)
subtitle: Université Catholique de Louvain
tags: [postdoc, Belgium, numerical modelling, sea ice, machine learning, data assimilation]
comments: false
---
Two-year post-doctoral scientist position at the UCLouvain, Belgium, focused on developing machine learning-based parameterizations of leads opening and closing in a sea ice model

Sea ice models rely on equations derived from our understanding of physical processes. However, some processes cannot be resolved explicitly due to the coarse spatial model resolution or to incomplete understanding of the processes involved, and thus must be parametrized. These parameterizations are a dominant source of uncertainty and contribute significantly to biases in climate models.
Parameterizations can be based on the system’s dynamics or rely on relatively simple hypotheses. For instance, some sea ice models include a minimum fraction of leads (open water areas within the ice pack) to account for opening mechanisms that are not captured by the model, preventing unphysically low simulated lead fractions to occur in winter.
Recently, machine learning techniques have been proposed to derive parameterizations directly from observations. The objective here is to develop a new parameterization of leads opening and closing in the sea ice model SI3 using this approach.
In this framework, applications are open for the following position:

Post-doctoral researcher

Starting date: Ideally in February 2025 but can be negotiated

Full time position for 24 months

Net monthly salary: 2900-3200 € (depending on seniority)

Social insurance and the transportation to and from the workplace are also covered. Location: Earth and Life Institute, Université catholique de Louvain, Belgium

The candidates must not have spent more than 2 years in Belgium over the last 3 years and should not have obtained their PhD more than 6 years before the starting date of the grant.

The development of the new parameterization will be guided by the analysis of existing outputs of the NEMO4.2-SI3 ocean—sea ice model that was constrained by data assimilation. Data assimilation combines model results and observations to obtain an optimal estimate of the state of the system. The increments, i.e. the difference between the initial sea ice model results and the updated values using the information derived from observations, provide important information on the model biases. On the basis of those increments, the applicant will propose to develop a new parameterization of leads opening and closing using machine learning. The advantage to use data assimilation increments compared to direct observations is that spatially complete fields at model resolution are available, only model biases need to be corrected, and the covariance between different variables, including those not directly observed, can be utilized in the development of the parameterization.
Specifically, the increments given by data assimilation in a reconstruction of the sea ice concentration and sea ice thickness performed with the model NEMO-SI3 will be analysed to derive the dominant patterns and dependencies in the corrections brought by the observations and their seasonal and spatial variability. Two machine learning techniques will then be assessed to obtain a parameterization of leads opening and closing that can be used without data assimilation. In the first type, equation discovery technique is applied to determine the dependence of leads opening and closing on quantities directly computed by the model such as shearing, divergence, heat balance. The goal is to find objectively the variables that control leads evolution and should be included in the parameterization. The second type of technique is based on Convolution Neural Networks (CNNs) that have shown promising results for parametrizations in atmospheric and oceanic models.

Required qualifications:
- To have a PhD in data science, climatology or related field;
- To have experience in machine learning or in numerical modelling
- To have published in peer-reviewed international journals;
- To have demonstrated good verbal and written communication skills in English; - To have interest in working in a multidisciplinary team environment.

Applicants should send an e-mail to Hugues Goosse (hugues.goosse@uclouvain.be) including (i) a statement of research experience, qualification and interest, (ii) a complete CV including a list of publications, and (iii) the name of two scientists who would agree to send a letter of recommendation
Review of the applications will start October 28 and the call will remain open until the position is filled.
