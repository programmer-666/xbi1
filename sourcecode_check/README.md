# Source Code Check - SCC [ ⚠️ ]

This code is on alpha version. Still under developing and not recommended for
production or serious projects.

## Purpose
This is a code that I decided to write out of simple need. A code that collects
data about the source code of the roughly written application.

## Working Logic
The source code files to be recorded in SCC are determined in advance.
A special code with a specific format is written in the first 10 lines of 
these files. I will include information about the details of the code in the
description later with any necessary updates. Source codes with this special
code are included in the data collection process. When SCC is first run
(that is, the application you wrote), it creates a SQLite3 database for itself.
It keeps the data from the source codes you specify here.

SCC first generates a working code for itself. This code also includes data on
how many times the application was run and on what date and time it was run.
Along with this data, it reads the details about the source codes and includes
them in the database. This process repeats every time the code runs and the
data is stored in the database.
