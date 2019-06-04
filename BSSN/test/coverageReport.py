import time
import subprocess
import coverage

cov = coverage.Coverage()

# Starts coverage if bool == True, does nothing otherwise
def coverageStart():
    cov.start()

# Ends coverage, saves HTML report, opens html report in firefox, types [string] (used for automatic filtering) if
# bool == True, does nothing otherwise
def coverageEnd():
    # Stops coverage, saves report, creates HTML file
    cov.stop()
    cov.save()
    #cov.html_report()

    # Opens HTML report in firefox
    #subprocess.call('firefox htmlcov/index.html', shell=True)

    #cov.erase()

