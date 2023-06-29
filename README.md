## Description

`P5hellG3n.py` is a Python-based tool for security testers and penetration testers that automates the creation of a base64 encoded PowerShell reverse shell. It takes an IP address and port number as input arguments and generates a base64 encoded reverse shell command. This command, when executed on the target system's PowerShell (using `-exec bypass -enc`), establishes a reverse connection back to the provided IP and port, effectively giving control of the target system to the user. 

This script serves as an efficient utility for ethical hackers and cybersecurity professionals, easing the process of crafting a reverse shell command.

## Usage

```
python3 P5hellG3n.py [ip] [port]
```

Replace `[ip]` with the IP address you want the reverse shell to connect back to and `[port]` with the desired port number on the host machine.

Example usage:

```
python3 P5hellG3n.py 192.168.1.10 4444
```

This will generate a PowerShell command for a reverse shell to connect back to the IP address `192.168.1.10` on port `4444`.

## Prerequisites

To use this script, you need Python 3 installed on your machine.

## Warning

Please note that this tool is for educational purposes and authorized testing only. Always obtain proper permission before performing any kind of penetration testing.

## License

This project is licensed under the MIT License.

## Author

xbz0n

## Contributing

Please fork the project, create a new branch, and submit a pull request. For major changes, please open an issue first to discuss the proposed change.

## Disclaimer

This script is for educational purposes and for preparing for the OSEP certification exam. It should only be used in environments where you have permission to perform penetration testing.
