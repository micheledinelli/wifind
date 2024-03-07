# wifind

[![Publish to PyPI](https://github.com/micheledinelli/wifind/actions/workflows/publish-to-pypi.yaml/badge.svg)](https://github.com/micheledinelli/wifind/actions/workflows/publish-to-pypi.yaml) [![pypi version](https://img.shields.io/pypi/v/wifind)](https://pypi.org/project/wifind/) [![pypi downloads](https://img.shields.io/pypi/dw/wifind)](https://pypi.org/project/wifind/)

`wifind` is a cli tool that performs wifi fingerprinting and detect your position based on access points around you.

## Results

`wifind` is in early stage development. I am trying to find a suitable model for the classification task considering only a few samples.

## Installation

```sh
pip install wifind
```

## Usage

```sh
# learn current location labelling it as kitchen
wifind learn -r kitchen

# print saved locations
wifind rooms
# ['kitchen', 'bedroom']

# predicts current location
wifind predict
# kitchen

wifind predict -p
# {'kitchen': 0.68, 'bedroom': 0.32}

# clears data
wifind clear
```

## Acknowledgments

Inspired by amazing work of [`whereami`](https://github.com/kootenpv/whereami)
