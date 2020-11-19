![Python CI](https://github.com/NONVME/python-project-lvl2/workflows/Python%20CI/badge.svg?branch=main)
[![Maintainability](https://api.codeclimate.com/v1/badges/6647c43a188ac223b894/maintainability)](https://codeclimate.com/github/NONVME/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6647c43a188ac223b894/test_coverage)](https://codeclimate.com/github/NONVME/python-project-lvl2/test_coverage)

# GenDiff
(GENerator of DIFFerences) 
The cli package gives diff between two files.

This is a second level project. created as part of the [Hexlet](https://ru.hexlet.io/) training course to prepare a Python Web developer.

## Features

- Supported input formats: YAML, JSON
- Report generation as plain text, structured text and JSON
- Usage as CLI util or library function

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install GenDiff.

```bash
pip install --extra-index-url https://test.pypi.org/simple/ nonvme-gendiff
```

## Usage

### As library function

```python
from gendiff import generate_diff

diff = generate_diff(file_path1, file_path2)
print(diff)
```

### As CLI util

```bash
usage: gendiff [-h] [-f {prety,plain,json}] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f {prety,plain,json}, --format {prety,plain,json}
                        set format of output    
```

### Usage examples

#### Prety output
[![asciicast](https://asciinema.org/a/TkfGqaXzqJfv5vsoC7XOa4JJQ.svg)](https://asciinema.org/a/TkfGqaXzqJfv5vsoC7XOa4JJQ)

#### JSON output
[![asciicast](https://asciinema.org/a/dlN7oQx2KLQCz9HkCqiFRPlDK.svg)](https://asciinema.org/a/dlN7oQx2KLQCz9HkCqiFRPlDK)

#### Plain output
[![asciicast](https://asciinema.org/a/NNOVeaQFrGoOxQaGLyvJZ9KWK.svg)](https://asciinema.org/a/NNOVeaQFrGoOxQaGLyvJZ9KWK)

## License

[MIT](https://choosealicense.com/licenses/mit/)
