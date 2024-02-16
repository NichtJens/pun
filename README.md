# pun — python unused

![pun](https://github.com/NichtJens/pun/assets/1607379/2c87fa02-c55d-4c0d-9633-ebbaa305471b)

## overview

pun searches for unused parts of a python codebase via statically analysing imports.

Just point it to the folder containing the code and set one or more targets (i.e., the scripts you'd actually run). The ignore list can be used to skip imports of built-in or external libraries that are not of interest.

## usage

```
usage: pun.py [-h] [-i [IGNORE [IGNORE ...]]] [-t [TARGETS [TARGETS ...]]]
              folder

positional arguments:
  folder

optional arguments:
  -h, --help            show this help message and exit
  -i [IGNORE [IGNORE ...]], --ignore [IGNORE [IGNORE ...]]
  -t [TARGETS [TARGETS ...]], --targets [TARGETS [TARGETS ...]]
```

