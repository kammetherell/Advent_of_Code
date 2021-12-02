# GWA Package

## Installation

Download and install the package on your machine:
```
cd <<working directory>>
pip install -e ./aoc_helpers
```

If you need to bypass SSL verification on your machine (if you are behind a proxy for example), you can use the following install command:
```
git -c http.sslVerify=false clone https://github.com/kamdickens/pypas.git
pip install -e ./aoc_helpers --trusted-host pypi.org --trusted-host files.pythonhosted.org
```

Import the package into your Python script:
```
import aoc_helpers
```

## Usage

### `pypas.ona`
