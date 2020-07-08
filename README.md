# ULBStageMedServicePicker
Python helper to choose nicely the service for students in medicine at ULB (Affectation problem solved using SCIP)

You need to have obtained a licence for SCIP (https://www.scipopt.org/index.php#download) and installed it. 
You also need to have "scip" command added to your PATH.

This script has been tested with SCIP 7.0.1 on a Windows10 machine and seems to be working.

To run it simply launch:

`python3 main.py input.csv`

input csv file must have the following structure:

First line: List of all Possible services (first column skipped)

Second line: Maximum number of students per service (first column skipped)

All next lines: Student Name, preferences being in a range of 1-n 1 being the most preferred service. 

Empty values are considered as "least preferred"

preferences can be unique (e.g. only one of each number) or multiple (e.g. same preference level for two services)

For an example of input file see provided input.csv