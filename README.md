# Validere_assginment

Please create a git repository and use commits to act as a chronological record of your implementation.  If you have any questions, please let us know.  When finished, please tarball/zip the repo or send a github link and email it back for review.

<h1>Sourcing and analyzing crude data </h1> <br />
When blending two different kinds of oil together, each of the oil's properties (e.g.: sulphur content, density, etc.) are combined via specific rules. One property of particular importance is density since it directly affects both the quantitative value of the crude as well as blending characteristics. Publicly available data can be leveraged to provide insights into historical quality trends.
<h1>Assignment</h1> <br />
Create a command line interface where a user can specify: crude acronym, start/end dates, operation e.g. ‘<’ or ‘greater_than’ .. etc and a numerical limit e.g. 830<br />

The script/function should:<br />

●	Fetch data from Crude Monitor for the specified crude acronym for the given start/end dates<br />

●	Filter the density data based on the specified operation<br />

●	Print the results to the user<br />


An example of the usage of the script would look like:<br />
![alt text](https://github.com/jeremy763/Validere_assginment/blob/master/Screen%20Shot%202021-09-25%20at%2012.25.58%20PM.png)



Bonus: subsequent runs of the script for the same crude should look to source data locally instead of re-requesting<br />
Additional comments:<br />
●	Include documentation about your implementation and assumptions <br />
●	Include instructions/files for environment management i.e. venv, requirements.txt, pipenv .. etc <br />
Program in Python (preferably Python 3), and submit as a .py file. Use any numerical/data packages you may think are useful, such as NumPy, Pandas, etc.<br />
<h1>To get started</h1> <br />
Please find the attached example.py file to get started on how to fetch data from the Crude Monitor website.<br />
The crude_monitor_parameters.csv will provide you with the additional parameters required to make a successful request.<br />
