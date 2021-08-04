# MicroComp - Determining Environmental Compatibility Between Microbes and Root Microecosystems
Created by Daphne Fauber, Kyle Sander, Will Sharpless, & Adam Arkin

Work-in-Progress --- Made using Python 3.8.8

Notes for future development can be found in the Project section.

# PURPOSE:
MicroComp is a program designed to compare the compatibility between target microbes and the three distinct zones of the rhizopshere---the endorhizosphere, exorhizopshere, and rhizoplane---to inform the creation of more successful plant root system microbiomes. The main idea behind this thought process is that microbes that survive and propagate together in a closed, consistent lab environment may not do so in a real-world plant rhizosphere due to the variable and flucuating conditions throughout. Therefore, by checking microbial compatibility with different environmental conditions that would appear in a specific plant's root system, and cross-referencing that compatibility with the other microbes of interest, a more holistic view of both target environmental conditions and possible species distribution is created.

# INPUTS/OUTPUTS:
Briefly the inputs are currently designed to be a variable number of csv files---one that contains the maximum and minimum of parameter values that the target microbes can survive at and the rest of the files representing an environment per file that contains data for each parameter as time passes in the given environment. In its current condition, the program is hard-coded to accept three envrionmental files that contain data over the course of 15 days (with one data measure per parameter per day), as seen in the testData.csv files and microbeData.csv file. Currently, the program should theoretically accept any number of parameters however was created with the 7 parameters of temperature, pH, exudate volume, humidity, carbon availability, nitrogen availability, and oxygen availability in mind. In its current state using more or less than 7 parameters may result in errors.

The output of the model is currently a text output that prints out when the program is run. The printout is a compatibility analysis that expresses for which days in each environment that the microbe was compatible according to the data input. Alongside this, it also prints for each other microbe, which days there was shared compatibility. 

# HOW TO USE:
In order to use this program, first input data files need to be generated. Input data files should follow the general formatting of the example files provided for the best results. Spreadsheets that contain the target should be saved in .csv format and placed into the same folder as this downloaded code so they can easily be accessed by the program.

For repeated testing, directly type the names of the filenames for the environmental data as string items in the file_names array on line 24 and comment out lines 76 through 86 (the code is currently setup with this mode in mind and the array is populated with the names of the test environmental files). Alternatively, uncomment lines 76 through 86 and delete the current entries in the array on line 24 to populate the array via inputting file names as the program runs. 

Once it is decided how the system will recieve the file names, the program can be run by pressing the run button and the program will conduct the analysis. Since the analysis is a text output, it might be benenficial to copy the output and paste it into a text file as a means of saving the output more permanently. 

# LICENSING:
MicroComp follows the MIT License. 

# LONGTERM VISION:
This program is a work-in-progress that is currently in an unsophisticated state. Long term, the idea is to use Dynamic Energy Budget (DEB) theory as a form of mechanistic species distribution modeling for the purposes of determining the species distribution of target microbes across the rhizosphere. That information in turn would be used to identify which target microbes have the highest chance of success when paired together from the perspective of complementary physical and spatial needs. In its current state, the program does not include any DEB-related algorithmns, but DEB-related parameters could be utilized in the input.

# INSPIRED BY:
This work was inspired by pydeb (https://github.com/jornbr/pydeb) and DEBplant (https://github.com/rafaqz/DEBplant)

# ACKNOWLEDGMENTS:
This work was supported in part by the U.S. Department of Energy, Office of Science, Office of Workforce Development for Teachers and Scientists (WDTS) under the Science Undergraduate Laboratory Internship (SULI) program with Purdue Unversity, Lawrence Berkeley National Laboratory, University of California Berkeley, and the Center for the Utilization of Biological Engineering in Space (CUBES).

This material is based upon work supported by NASA under grant or cooperative agreement award number NNX17AJ31G. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Aeronautics and Space Administration (NASA).
