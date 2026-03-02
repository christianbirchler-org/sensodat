# SensoDat: Simulation-based Sensor Dataset of Self-driving Cars

Testing self-driving cars (SDCs) is crucial for maintaining high security levels and minimizing potential threats to humans.
While infield SDC testing is costly, simulation technologies offer a safer alternative.
However, conducting simulation-based tests demands increased computational resources, particularly GPUs for accelerated computation of physical dynamics (Toni Mancini and Igor Melatti and Enrico Tronci, 2023, Aitor Arrieta and Shuai Wang and Ainhoa Arruabarrena and Urtzi Markiegi and Goiuria Sagardui and Leire Etxeberria, 2018).

To address the challenge of minimizing the costs of simulation-based testing, recent research focused on various regression testing techniques for simulation-based tests.
Those techniques aim to test SDCs cost-effectively while maintaining the system&rsquo;s safety.
For instance, by test prioritization (Aitor Arrieta and Shuai Wang and Goiuria Sagardui and Leire Etxeberria, 2019, Christian Birchler and Sajad Khatiri and Pouria Derakhshanfar and Sebastiano Panichella and Annibale Panichella, 2023), in which the tests of the test suite are prioritized, i.e., sorted in a way so that the testing phase reveals faults of the system earlier.

However, to conduct research on optimizing simulation-based testing, researchers rely on expensive test executions in simulation environments (Toni Mancini and Igor Melatti and Enrico Tronci, 2023, Aitor Arrieta and Shuai Wang and Ainhoa Arruabarrena and Urtzi Markiegi and Goiuria Sagardui and Leire Etxeberria, 2018).
These additional computational costs are mainly due to the expensive computation simulating the physics of the environment, which is not the case when testing traditional software systems.
Thus, those tests are expensive and often not affordable when a large amount of data is required, e.g., for ML and DNNs.

To overcome the issue of running simulations to obtain the execution data of simulations, researchers can use existing datasets of executed simulation-based tests.
There are only a few datasets available consisting of simulation data for SDCs (Chengjie Lu and Tao Yue and Shaukat Ali, 2023, Birchler Christian and Khatiri Sajad and Derakhshanfar Pouria and Panichella Sebastiano and Panichella Annibale, 2021).
Despite the existence of those datasets, in most cases, the simulators used are not maintained anymore.
Popular simulators like Udacity (Udacity Inc., 2017), Apollo (Apollo Auto, 2023), SVL (LGSVL, 2023), and DeepDrive (Deepdrive, 2023) were used in the past for research purposes, but unfortunately, the active development of these simulators has been stopped by the maintainers or have long release cycles.

We propose a dataset consisting of simulation data of executed SDC test cases in the *BeamNG* simulation environment.
The *BeamNG* simulator is known in academia (Christian Birchler and Cyrill Rohrbach and Hyeongkyun Kim and Alessio Gambi and Tianhai Liu and Jens Horneber and Timo Kehrer and Sebastiano Panichella, 2023, Christian Birchler and Sajad Khatiri and Bill Bosshard and Alessio Gambi and Sebastiano Panichella, 2023, Sebastiano Panichella and Alessio Gambi and Fiorella Zampetti and Vincenzo Riccio, 2021, Alessio Gambi and Gunel Jahangirova and Vincenzo Riccio and Fiorella Zampetti, 2022, Matteo Biagiola and Stefan Klikovits and Jarkko Peltom{\\"{a}}ki and Vincenzo Riccio, 2023, Zohdinasab, Tahereh and Riccio, Vincenzo and Gambi, Alessio and Tonella, Paolo, 2023) and is based on the popular *BeamNG.drive* game, which is actively developed and maintained by *BeamNG GmbH*.
The availability of simulation data of SDCs enhances the research on SDC testing in simulation.
Researchers and practitioners do not rely on executing expensive test cases to develop and evaluate regression testing techniques.
Having the dataset publicly available eases the research for the domain of SDC software, especially for researchers and practitioners who can not afford expensive computing hardware.
Furthermore, the availability of an open dataset improves the reproducibility and comparability of research results in various areas.


We generated test cases that are based on three different test generators for the *BeamNG* simulator.
All of these test generators were developed in the context of tool competitions at the SBST  and SBFT workshop (Sebastiano Panichella and Alessio Gambi and Fiorella Zampetti and Vincenzo Riccio, 2021, Alessio Gambi and Gunel Jahangirova and Vincenzo Riccio and Fiorella Zampetti, 2022, Matteo Biagiola and Stefan Klikovits and Jarkko Peltom{\\"{a}}ki and Vincenzo Riccio, 2023).

    {
      "_id": {...},
      "OpenDRIVE": {
        "header": {
          "@name": "mt_set5/frenetic/test-440",
          "sdc_test_info": {
            "@test_id": "mt_set5/frenetic/test-440",
            "@test_outcome": "PASS",
            "@predicted_test_outcome": "null",
            "@test_duration": "11.067427158355713",
            "@is_valid": "True"
          },
          "run_config": {
            "@rf": "1.5",
            "@oob": "0.5",
            "@max_speed": "120",
            "@obstacles": "False",
            "@bump_dist": "20",
            "@delineator_dist": "None",
            "@tree_dist": "None",
            "@field_of_view": "120"
          }
        },
        "road": {...}
      },
      "execution_data": {...}
    }


### *Frenetic*

The *Frenetic* tool (Ezequiel Castellano and Ahmet Cetinkaya and C{\\'{e}}dric Ho Thanh and Stefan Klikovits and Xiaoyi Zhang and Paolo Arcaini, 2021) uses a genetic algorithm to minimize the distance between the SDC and the edge of the road.
For its computation, it leverages the concepts of frenet frames and curvature-based road representations.
Thus, it converts the solutions back to the Cartesian space, which is required for the simulator.


### *FreneticV*

The *FreneticV* tool (Ezequiel Castellano and Stefan Klikovits and Ahmet Cetinkaya and Paolo Arcaini, 2022) is an extension of *Frenetic*, which is able to reduce the amount of invalid roads.
For example, an invalid road has overly sharp turns, or if it intersects with itself.
This definition of road validity is given by the SBST tool competition (Alessio Gambi and Gunel Jahangirova and Vincenzo Riccio and Fiorella Zampetti, 2022), for which the tool was developed for.


### *AmbieGen*

The *AmbieGen* (Dmytro Humeniuk and Giuliano Antoniol and Foutse Khomh, 2022) tool is a test generator that uses a multi-objective approach using NSGA-II (Kalyanmoy Deb and Samir Agrawal and Amrit Pratap and T. Meyarivan, 2000).
Using the diversity preservation and the fault revealing power as the objectives, *AmbieGen* generates test cases that are more likely to reveal faults based on the OOB metric.

<table id="org9e21fea" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
<caption class="t-above"><span class="table-number">Table 1:</span> Database storage size</caption>

<colgroup>
<col  class="org-left" />

<col  class="org-right" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left"><b>Collection</b></th>
<th scope="col" class="org-right"><b># Documents</b></th>
<th scope="col" class="org-left"><b>Storage size</b></th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">campaign_2_ambiegen</td>
<td class="org-right">973</td>
<td class="org-left">108.36 MB</td>
</tr>

<tr>
<td class="org-left">campaign_2_frenetic</td>
<td class="org-right">928</td>
<td class="org-left">109.46 MB</td>
</tr>

<tr>
<td class="org-left">campaign_2_frenetic_v</td>
<td class="org-right">944</td>
<td class="org-left">41.93 MB</td>
</tr>

<tr>
<td class="org-left">campaign_3_ambiegen</td>
<td class="org-right">964</td>
<td class="org-left">109.85 MB</td>
</tr>

<tr>
<td class="org-left">campaign_3_frenetic</td>
<td class="org-right">954</td>
<td class="org-left">112.73 MB</td>
</tr>

<tr>
<td class="org-left">campaign_4_ambiegen</td>
<td class="org-right">965</td>
<td class="org-left">111.98 MB</td>
</tr>

<tr>
<td class="org-left">campaign_4_frenetic</td>
<td class="org-right">964</td>
<td class="org-left">113.87 MB</td>
</tr>

<tr>
<td class="org-left">campaign_4_frenetic_v</td>
<td class="org-right">525</td>
<td class="org-left">63.43 MB</td>
</tr>

<tr>
<td class="org-left">campaign_5_ambiegen</td>
<td class="org-right">958</td>
<td class="org-left">109.59 MB</td>
</tr>

<tr>
<td class="org-left">campaign_5_frenetic</td>
<td class="org-right">945</td>
<td class="org-left">112.29 MB</td>
</tr>

<tr>
<td class="org-left">campaign_5_frenetic_v</td>
<td class="org-right">940</td>
<td class="org-left">112.81 MB</td>
</tr>

<tr>
<td class="org-left">campaign_6_ambiegen</td>
<td class="org-right">959</td>
<td class="org-left">111.76 MB</td>
</tr>

<tr>
<td class="org-left">campaign_6_frenetic</td>
<td class="org-right">944</td>
<td class="org-left">111.11 MB</td>
</tr>

<tr>
<td class="org-left">campaign_6_frenetic_v</td>
<td class="org-right">764</td>
<td class="org-left">91.14 MB</td>
</tr>

<tr>
<td class="org-left">campaign_7_ambiegen</td>
<td class="org-right">963</td>
<td class="org-left">110.00 MB</td>
</tr>

<tr>
<td class="org-left">campaign_7_frenetic</td>
<td class="org-right">967</td>
<td class="org-left">114.09 MB</td>
</tr>

<tr>
<td class="org-left">campaign_7_frenetic_v</td>
<td class="org-right">47</td>
<td class="org-left">5.67 MB</td>
</tr>

<tr>
<td class="org-left">campaign_8_ambiegen</td>
<td class="org-right">952</td>
<td class="org-left">110.76 MB</td>
</tr>

<tr>
<td class="org-left">campaign_8_frenetic</td>
<td class="org-right">952</td>
<td class="org-left">112.25 MB</td>
</tr>

<tr>
<td class="org-left">campaign_9_ambiegen</td>
<td class="org-right">953</td>
<td class="org-left">109.20 MB</td>
</tr>

<tr>
<td class="org-left">campaign_9_frenetic</td>
<td class="org-right">964</td>
<td class="org-left">113.57 MB</td>
</tr>

<tr>
<td class="org-left">campaign_10_ambiegen</td>
<td class="org-right">971</td>
<td class="org-left">63.95 MB</td>
</tr>

<tr>
<td class="org-left">campaign_11_ambiegen</td>
<td class="org-right">973</td>
<td class="org-left">72.79 MB</td>
</tr>

<tr>
<td class="org-left">campaign_11_frenetic</td>
<td class="org-right">866</td>
<td class="org-left">66.44 MB</td>
</tr>

<tr>
<td class="org-left">campaign_11_frenetic_v</td>
<td class="org-right">953</td>
<td class="org-left">73.52 MB</td>
</tr>

<tr>
<td class="org-left">campaign_12_frenetic</td>
<td class="org-right">956</td>
<td class="org-left">110.11 MB</td>
</tr>

<tr>
<td class="org-left">campaign_12_freneticV</td>
<td class="org-right">942</td>
<td class="org-left">114.00 MB</td>
</tr>

<tr>
<td class="org-left">campaign_13_ambiegen</td>
<td class="org-right">954</td>
<td class="org-left">68.83 MB</td>
</tr>

<tr>
<td class="org-left">campaign_13_frenetic</td>
<td class="org-right">959</td>
<td class="org-left">72.52 MB</td>
</tr>

<tr>
<td class="org-left">campaign_13_frenetic_v</td>
<td class="org-right">951</td>
<td class="org-left">71.48 MB</td>
</tr>

<tr>
<td class="org-left">campaign_14_ambiegen</td>
<td class="org-right">959</td>
<td class="org-left">70.14 MB</td>
</tr>

<tr>
<td class="org-left">campaign_14_frenetic</td>
<td class="org-right">866</td>
<td class="org-left">64.05 MB</td>
</tr>

<tr>
<td class="org-left">campaign_14_frenetic_v</td>
<td class="org-right">934</td>
<td class="org-left">70.16 MB</td>
</tr>

<tr>
<td class="org-left">campaign_15_ambiegen</td>
<td class="org-right">952</td>
<td class="org-left">110.50 MB</td>
</tr>

<tr>
<td class="org-left">campaign_15_frenetic</td>
<td class="org-right">870</td>
<td class="org-left">102.61 MB</td>
</tr>

<tr>
<td class="org-left">campaign_15_freneticV</td>
<td class="org-right">949</td>
<td class="org-left">114.67 MB</td>
</tr>
</tbody>
<tbody>
<tr>
<td class="org-left"><b>Total</b></td>
<td class="org-right"><b>32,580</b></td>
<td class="org-left"><b>3.34 GB</b></td>
</tr>
</tbody>
</table>

<table id="orgab192eb" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
<caption class="t-above"><span class="table-number">Table 2:</span> Overview of available types of sensor data</caption>

<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">fuel</td>
<td class="org-left">steering_input</td>
<td class="org-left">oil</td>
</tr>

<tr>
<td class="org-left">low fuel</td>
<td class="org-left">rpm spin</td>
<td class="org-left">lowhighbeam</td>
</tr>

<tr>
<td class="org-left">gear</td>
<td class="org-left">airflow speed</td>
<td class="org-left">lowbeam</td>
</tr>

<tr>
<td class="org-left">odometer</td>
<td class="org-left">lights</td>
<td class="org-left">high beam</td>
</tr>

<tr>
<td class="org-left">brake</td>
<td class="org-left">horn</td>
<td class="org-left">brakelight_signal_R</td>
</tr>

<tr>
<td class="org-left">throttle</td>
<td class="org-left">hasABS</td>
<td class="org-left">brakelight_signal_L</td>
</tr>

<tr>
<td class="org-left">parking brake</td>
<td class="org-left">altitude</td>
<td class="org-left">lowhighbeam_signal_R</td>
</tr>

<tr>
<td class="org-left">throttle_input</td>
<td class="org-left">dseColor</td>
<td class="org-left">lowhighbeam_signal_L</td>
</tr>

<tr>
<td class="org-left">reverse</td>
<td class="org-left">virtualAirspeed</td>
<td class="org-left">turn signal</td>
</tr>

<tr>
<td class="org-left">exhaust_flow</td>
<td class="org-left">4x brakeCoreTemperature</td>
<td class="org-left">left_signal</td>
</tr>

<tr>
<td class="org-left">fog_lights</td>
<td class="org-left">4x brakeThermalEfficiency</td>
<td class="org-left">signal_r</td>
</tr>

<tr>
<td class="org-left">fuel_volume</td>
<td class="org-left">4x brakeSurfaceTemperature</td>
<td class="org-left">right_signal</td>
</tr>

<tr>
<td class="org-left">fuel_capacity</td>
<td class="org-left">engineRunning</td>
<td class="org-left">tcs_active</td>
</tr>

<tr>
<td class="org-left">gear_a</td>
<td class="org-left">running</td>
<td class="org-left">water_temperature</td>
</tr>

<tr>
<td class="org-left">gear_index</td>
<td class="org-left">low-pressure</td>
<td class="org-left">brake_lights</td>
</tr>

<tr>
<td class="org-left">gear_m</td>
<td class="org-left">rpm</td>
<td class="org-left">check_engine</td>
</tr>

<tr>
<td class="org-left">hazard_signal</td>
<td class="org-left">clutch</td>
<td class="org-left">clutch_ratio</td>
</tr>

<tr>
<td class="org-left">is_shifting</td>
<td class="org-left">parkingbrake_input</td>
<td class="org-left">engine_load</td>
</tr>

<tr>
<td class="org-left">airspeed</td>
<td class="org-left">brake_input</td>
<td class="org-left">signal_l</td>
</tr>

<tr>
<td class="org-left">abs</td>
<td class="org-left">tcs</td>
<td class="org-left">parking</td>
</tr>

<tr>
<td class="org-left">steering</td>
<td class="org-left">ignition</td>
<td class="org-left">hazard</td>
</tr>

<tr>
<td class="org-left">isYCBrakeActive</td>
<td class="org-left">gearboxMode</td>
<td class="org-left">clutch_input</td>
</tr>

<tr>
<td class="org-left">isTCBrakeActive</td>
<td class="org-left">lightbar</td>
<td class="org-left">abs_active</td>
</tr>

<tr>
<td class="org-left">driveshaft</td>
<td class="org-left">headlights</td>
<td class="org-left">engine_throttle</td>
</tr>

<tr>
<td class="org-left">wheelspeed</td>
<td class="org-left">oil_temperature</td>
<td class="org-left">esc_active</td>
</tr>

<tr>
<td class="org-left">esc</td>
<td class="org-left">radiator_fan_spin</td>
<td class="org-left">avg_wheel_av</td>
</tr>

<tr>
<td class="org-left">smoothShiftLogicAV</td>
<td class="org-left">rpm_tacho</td>
<td class="org-left">freezeState</td>
</tr>
</tbody>
</table>

## Bibliography

Aitor Arrieta and Shuai Wang and Ainhoa Arruabarrena and Urtzi Markiegi and Goiuria Sagardui and Leire Etxeberria (2018). *Multi-objective black-box test case selection for cost-effectively testing simulation models*, {ACM}.

Aitor Arrieta and Shuai Wang and Goiuria Sagardui and Leire Etxeberria (2019). *Search-Based test case prioritization for simulation-Based testing of cyber-Physical system product lines*, J. Syst. Softw..

Alessio Gambi and Gunel Jahangirova and Vincenzo Riccio and Fiorella Zampetti (2022). *SBST Tool Competition 2022*, {IEEE}.

Apollo Auto (2023). *apollo*.

Birchler Christian and Khatiri Sajad and Derakhshanfar Pouria and Panichella Sebastiano and Panichella Annibale (2021). *Dataset Package for the paper &ldquo;Single and Multi- objective Test Cases Prioritization for Self- driving Cars in Virtual Environments&rdquo;*, Zenodo.

Chengjie Lu and Tao Yue and Shaukat Ali (2023). *DeepScenario: An Open Driving Scenario Dataset for Autonomous Driving System Testing*, {IEEE}.

Christian Birchler and Cyrill Rohrbach and Hyeongkyun Kim and Alessio Gambi and Tianhai Liu and Jens Horneber and Timo Kehrer and Sebastiano Panichella (2023). *TEASER: Simulation-Based CAN Bus Regression Testing for Self-Driving Cars Software*, {IEEE}.

Christian Birchler and Sajad Khatiri and Bill Bosshard and Alessio Gambi and Sebastiano Panichella (2023). *Machine learning-based test selection for simulation-based testing of self-driving cars software*, Empir. Softw. Eng..

Christian Birchler and Sajad Khatiri and Pouria Derakhshanfar and Sebastiano Panichella and Annibale Panichella (2023). *Single and Multi-objective Test Cases Prioritization for Self-driving Cars in Virtual Environments*, {ACM} Trans. Softw. Eng. Methodol..

Deepdrive (2023). *Deepdrive*.

Dmytro Humeniuk and Giuliano Antoniol and Foutse Khomh (2022). *AmbieGen tool at the SBST 2022 Tool Competition*, {IEEE}.

Ezequiel Castellano and Ahmet Cetinkaya and C{\\'{e}}dric Ho Thanh and Stefan Klikovits and Xiaoyi Zhang and Paolo Arcaini (2021). *Frenetic at the SBST 2021 Tool Competition*, {IEEE}.

Ezequiel Castellano and Stefan Klikovits and Ahmet Cetinkaya and Paolo Arcaini (2022). *FreneticV at the SBST 2022 Tool Competition*, {IEEE}.

Kalyanmoy Deb and Samir Agrawal and Amrit Pratap and T. Meyarivan (2000). *A Fast Elitist Non-dominated Sorting Genetic Algorithm for Multi-objective Optimisation: NSGA-II*, Springer.

LGSVL (2023). *SVL Simulator: An Autonomous Vehicle Simulator*.

Matteo Biagiola and Stefan Klikovits and Jarkko Peltom{\\"{a}}ki and Vincenzo Riccio (2023). *SBFT Tool Competition 2023 - Cyber-Physical Systems Track*, {IEEE}.

Sebastiano Panichella and Alessio Gambi and Fiorella Zampetti and Vincenzo Riccio (2021). *SBST Tool Competition 2021*, {IEEE}.

Toni Mancini and Igor Melatti and Enrico Tronci (2023). *Optimizing Highly-Parallel Simulation-Based Verification of Cyber-Physical Systems*, {IEEE} Trans. Software Eng..

Udacity Inc. (2017). *A self-driving car simulator built with Unity*.

Zohdinasab, Tahereh and Riccio, Vincenzo and Gambi, Alessio and Tonella, Paolo (2023). *Efficient and Effective Feature Space Exploration for Testing Deep Learning Systems*, Association for Computing Machinery.
