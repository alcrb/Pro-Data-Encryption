# :page_with_curl:	_Encrypt File_ :lock: 
[![Python 3](https://img.shields.io/badge/Python-3-blue.svg)](https://www.python.org/downloads/release/python-381/)
![License](https://img.shields.io/badge/Code%20License-MIT-blue.svg)

CLI to encrypt or decrypt files with only one command
```bash
                                    __     _____ __   
  ___  ____  ____________  ______  / /_   / __(_) /__ 
 / _ \/ __ \/ ___/ ___/ / / / __ \/ __/  / /_/ / / _ \
/  __/ / / / /__/ /  / /_/ / /_/ / /_   / __/ / /  __/
\___/_/ /_/\___/_/   \__, / .___/\__/  /_/ /_/_/\___/ 
                    /____/_/                          

Encrypt or decrypt files with ONLY ONE COMMAND 
----------------------------------------------------------------------
PARAMETERS
func:		encrypt
password:	123456
file_path:	tests/plain_text.txt

Encrypting ...
Encrypted file at tests/plain_text.txt.enc
Execution time: 0.01 seconds                        
```
The _encrypt file_ is a **CLI** for encrypting and decrypting files.

## Why should I use the _encrypt file_?
- **No Code**: When there is no need to code something you can simply use _encrypt file_.
- **Abstraction of cryptographic algorithms**: you don't need to know what goes on behind the scenes in _encrypt file_ (but if you want, just see it on github).

## Requirements
This project is tested with:

| Requisite      | Version  |
|----------------|----------|
| Python         | 3.11.0   |
| Pip            | 22.3.1   |

## Install
```sh
pip install encrypt-file
```

## Usage
- :lock: Encrypt :lock:
```bash

          --func encrypt \
          --file plain_text.txt \
          --password 123456
```

- :unlock: Decrypt :unlock:
```bash

          --func decrypt \
          --file plain_text.txt.enc \
          --password 123456
```
