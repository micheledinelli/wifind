# wifind

![python](https://img.shields.io/badge/Python-3776AB.svg?style=plain&logo=Python&logoColor=white)
![sklearn](https://img.shields.io/badge/scikitlearn-F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)
[![pypi downloads](https://img.shields.io/pypi/dw/wifind)](https://pypi.org/project/wifind/)

`wifind` is a cli tool that performs wifi fingerprinting and detect your position based on access points around you.

## Installation

```console
pip install wifind
```

## Usage

```console
# learn current location labelling it as kitchen
wifind learn -r kitchen

# print saved locations
wifind rooms
# ['kitchen', 'bedroom']

# predicts current location
wifind predict
# kitchen

wifind --watch
# 2024-06-08 12:31:24 - kitchen
# 2024-06-08 12:31:27 - bedroom
# 2024-06-08 12:31:31 - bedroom
# 2024-06-08 12:31:35 - bedroom

wifind predict -p
# {'kitchen': 0.68, 'bedroom': 0.32}

# clears data
wifind clear
```

## Acknowledgments

Inspired by amazing work of [`whereami`](https://github.com/kootenpv/whereami)
