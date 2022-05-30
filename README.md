# PythonEpochML
Python code which sends the EPOCH via UART to the new multilogger base

Execute using command prompt:

cd C:/yourdirectory
python multilogger_init.py

Scans for serial devices connected. In the future it will send if only one device is connected. 
Now, for test purposes, it sends to the first device it scans, even if it says it sees multiple devices.
This is because the CC13x0 devices have two COM ports. 
