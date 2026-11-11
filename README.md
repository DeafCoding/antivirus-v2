# antivirus-v2

## What it does
Is A command line tool that scans a file against YARA rules, and tells you if the file is infected or clean.

## How to run
1. Create venv ``python3 -m venv venv``
2. Initiate it ``source venv/bin/activate``
3. Download the requirements: ``pip install -r requirements.txt``
4. Run it ``python scanner.py name_of_file ``
## Example
## Example
```bash
$ python scanner.py samples/infected.txt
samples/infected.txt has been reported as infected!!

$ python scanner.py samples/clean.txt
samples/clean.txt is clean
```
## Roadmap
- [ ] Show which rule matched
- [ ] Scan entire folders
- [ ] Multiple rule files
- [ ] Tests
