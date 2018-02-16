# findrefs

This is just a simple project to demonstrate that the Microsoft Visual Studio Code Python extension
does not correctly find references in certain scenarios. In the project, if you right click on the
function definition for "configure_params" in the contrived.py file, and click "Find All References",
it will not find any references outside of the current file. However, if you click "Find All References"
in the prove_its_broken.py, it will find two references - one from prove_its_broken.py and the other 
from contrived.py. Note that you must put PyCommons on the PYTHONPATH for the example to work.
