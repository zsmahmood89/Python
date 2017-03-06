# Python

### Correlates of War country-coding

This file allows me to country-code csv files using Python.

My goal with this file was to allow for user-flexibility. The script will cowcode only using the inputted source file. The remaining errors will be exported as a CSV file for you (the user) to update manually. After you have updated it, you can simply input "yes" and the code will re-run to update with your additions. This interactive approach is useful when you have noisy data where you want to code as much as you can while minimizing false-positives. 

This script will use the source file (COWsource.csv) included to cow-code. This file is generated almost directly from the COW data originally on the website. You can simply add additional rows identifying new spellings as you see fit.

Files:
	cowcoding.py
	COWsource.csv

### Functions

I keep my pet functions here. They're stuff I use a lot in python, such as Region coding for COW; writing a CSV row to a file; making month numbers or checking whether a date falls within a boundary; etc. Really, I don't recommend downloading and using them since these kinds of functions are best written by the end-user themselves (so you can troubleshoot as you see fit). If you do use them and there's a problem, let me know.

