import time
import subprocess
import coverage
from myKeyboard import write

cov = coverage.Coverage()

# Starts coverage if bool == True, does nothing otherwise
def coverageStart(bool = False):
    if bool:
        cov.start()

# Ends coverage, saves html report, opens html report in firefox, types [string] (used for automatic filtering) if
# bool == True, does nothing otherwise
def coverageEnd(string, bool = False):
    if bool:
        cov.stop()
        cov.save()
        cov.html_report()

        subprocess.call("firefox htmlcov/index.html", shell=True)

        time.sleep(0.25)

        write(string)
        cov.erase()

