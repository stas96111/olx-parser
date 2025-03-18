# Olx Scraper
A tool to parse OLX.UA in the console

## Install

1. Create a virtual enviroment
```bash
python -m venv venv
venv\Scripts\activate.bat
```
2. Install requirements
```bash
pip install -r requirements.txt
```

## Usage
> 'Output' must be without file extension
```bash
> python.exe -m olx_parser -h
usage: olx_parser [-h] [-u URL] [-p PAGES] [-o OUTPUT] [-j]

options:
  -h, --help  show this help message and exit
  -u URL      url to parse
  -p PAGES    pages to parse (default: 1)
  -o OUTPUT   output file name (default: output.csv)
  -j          output in json format
```