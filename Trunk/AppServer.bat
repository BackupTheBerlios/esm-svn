@echo off
:restart
rem python Launch.py ThreadedAppServer %1 %2 %3 %4 %5
python Launch.py NewThreadedAppServer %1 %2 %3 %4 %5
if errorlevel 3 goto restart
