# CoreTemp
a simple python app to check CPU temperatures on linux and notify if above 80°C

# Requirements
* Python3:
  * install python3 go to the project folder open a command window and type: `pip install -r requirements.txt`
* lm-sensors:
  * install lm-sensors using your linux package manager e.g: `sudo apt install lm-sensors`
  
# Running
Simply go to the project folder open a command window and type: `python3 ct.py` although i recommend using `nohup python3 ct.py &` so that you can close the command window afterwards
