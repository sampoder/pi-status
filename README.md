# 📈 pi-status



[![Downloads](https://pepy.tech/badge/pistatus)](https://pepy.tech/project/pistatus)

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

## Screenshots

**Web View**

<img src="https://github.com/sampoder/pi-status/blob/master/images/webserver.png?raw=true" alt="Web View" width = 50%>

**CLI View**

<img src="https://github.com/sampoder/pi-status/blob/master/images/cli.png?raw=true" alt="CLI View">

**GUI View**

<img src="https://github.com/sampoder/pi-status/blob/master/images/gui.png?raw=true" alt="GUI View">

## License

[MIT](https://choosealicense.com/licenses/mit/)
