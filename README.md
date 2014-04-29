swc-wordcount
=============

Converting wordcount script to use argparse

#### Objectives
*  Explain how to create a Python script that can take command line arguments
so the code doesn't need to be modified each time it is run
*  Provides some examples to show how a script that can use command line
arguments can be much more useful than a script that requires modification
each time in order to read a new input file

Lindsy Norman, a graduate student in Information and Library Science wants
to generate word frequency counts on various texts. She has written a Python
script that can generate a frequency count on an individual file but the
location of the file is hard coded into the script and so is the value of the
number of results in decending order is returned. She also many many text files
that she wants counts on and editing the script or renaming the input file
before running the script each time is tedious.

In this lesson we assume that you are familiar with basic Python scripting and
using the command line. We will be taking a Python script that can do word
frequency counts and use the Python module argparse to pass in values for the
text file we want to act on and how many of the top hits to report on.

#### Key Points
*  Argparse is part of the the standard Python language (it doesn't have to be installed in addition to installing Python)
*  Using just a few lines of Python code we can provide useful help messages
to someone using the script for the first time or for someone who has used the 
script but forgot what command line arguments are implemented
*  After adding the command line arguments to the script we can now use the 
word frequency script in a shell script to process thousands of files almost
as easy as it is to process a single file





 
