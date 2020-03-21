# Downloading and running the latest server
- Download from aiwolf.org/en/server
- version 0.5.6

# Things that I have to translate
- AIWolf webpage: Developer, Resource, Support
- Official github repository:
  https://github.com/aiwolf/AIWolfPy/tree/master


# Starting GUI game
- Start and configure the server
./StartServer.sh
- Start the necessary number of players
./StartClient.sh -h localhost -p 10000 -c org.aiwolf.sample.player.SampleRoleAssignPlayer

- game gui shows up (Japanese)
- game log saved on ./log

# Starting noGUI multiple games
- Configure number of games in "Autostarter.ini" and run Autostarter:
./AutoStarter.sh

- Individual logs for each game is saved on "./log"
- Logs for the games, as well as overall stats, exported to the standard output.

# Using the AIWolfPy library
- Installed a pyenv for version 3.6.5 (same as server)

pyenv install 3.6.5
pyenv virtualenv 3.6.5 pywolf
pyenv local pywolf

## requirements.txt (libraries available at game server)
- requirements.txt file at: http://aiwolf.org/en/python_modules
pip install -r requirements.txt
- Following packages were not found with specific versions in requirements.txt: anaconda, blaze, cloudpickle, clyent, conda, datashape, llvmlite, mkl-fft, mkl-random, navigator-update, odo
- Needs to install some lib-devs for installation.

# Trivial agent:
- Clone from: https://github.com/aiwolf/AIWolfPy
- Run as ./python_sample.py -h localhost -p 10000
- Created copy of Autostart script that asks to specify the settings file.

## Goals:
- [X] Finds out its agent name, and set a priority list
- [X] Always vote on the first agent of the priority list
- [X] Remove agent from the priority list if they are dead

## self.baseinfo:
- agentIdx: (My id)
- myRole: string
- roleMap: dict - agent ids and roles that I know
- day:
- remainTalkMak: dict: How many talks each agent still has
- statusMap: dict: string: ALIVE/DEAD for each agent

## Updates:
- Updates are called every time the game state change (before new day, after new day, before talks, before end of day, etc). The "Request" field of update says what will be the next request from the player (a talk, the end of the day, a vote, etc.)
