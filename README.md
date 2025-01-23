# My Python Project

## Overview
This project is designed to facilitate the collection and processing of data from various types of routers, including vEdge and IOS devices. It provides a structured approach to logging in, managing credentials, processing data, and executing commands through a command-line interface.

## Project Structure
```
my-python-project
├── src
│   ├── main.py               # Entry point for the application
│   ├── vedge_login.py        # Handles login for vEdge routers
│   ├── ios_login.py          # Handles login for IOS devices
│   ├── cred.py               # Manages user credentials
│   ├── loggs.py              # Implements logging functionality
│   ├── data_processing.py     # Processes data collected from routers
│   ├── command.py            # Defines CLI commands
│   └── collect.py            # Reference program for collecting OMP routes
├── requirements.txt          # Lists project dependencies
└── README.md                 # Documentation for the project
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd my-python-project
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
python src/main.py
```

## Components
- **main.py**: Initializes the application and orchestrates the execution of various components.
- **vedge_login.py**: Contains the `VedgeLogin` class for connecting and authenticating with vEdge routers.
- **ios_login.py**: Contains the `IosLogin` class for connecting and authenticating with IOS devices.
- **cred.py**: Manages user credentials securely.
- **loggs.py**: Implements logging functionality with different log levels.
- **data_processing.py**: Processes and analyzes data collected from routers.
- **command.py**: Sets up command-line interface commands for user interaction.
- **collect.py**: Collects OMP routes from SD-WAN routers and manages asynchronous tasks.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.# my-python-project
