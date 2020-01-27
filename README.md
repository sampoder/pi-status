
<h1 align="center"><img src="https://www.raspberrypi.org/wp-content/uploads/2011/10/Raspi-PGB001.png" alt="SwagLyrics" height=200 align="middle">Pi-Status</h1>

Pi-Status fetches basic statistics regarding your Raspberry Pi including network, CPU, RAM & storage stats it then displays the stats in the command-line, a GUI app or a browser tab. The program can be used for remote monitoring of headless deploys or simply to conveniently get stats on your Pi. The GUI app and browser tab refresh the stats on a timely basis. The lyrics are fetched from Genius.

## Installation
Requires Python 3.6+. Use pip or pip3 depending on your installation. You might want to use the `--user` flag on Linux to avoid using pip as root.
```
pip install pistatus
```

## Usage
`usage: pistatus [-g] [-w]`

To use the CLI output no arguments are required.

Arguments:
```
  -g, show the stats in the gui form       
  -w, start the web server on the local network      
```
You can quit the web server by pressing <kbd>Ctrl</kbd>+<kbd>C</kbd> and you will be able to see the IP address in the command line for reference. 

## Compiling PiStatus for Development

- Clone into this repo
- `cd` into the cloned repo.
- `pip install -e .` the -e flag installs it locally in editable mode.