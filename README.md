# HR CLI Tool

## Overview

The **HR ClI Tool** is a command-line utility designed to export a system's user information into formats suitable for sharing with other departments. It provides an easy way to extract user details such as username, user ID, home directory, and default shell into either **JSON** or **CSV** formats.

By default, the tool outputs the data in **JSON** format to the terminal, but it supports a `--format` flag to export the data in **CSV** format. Additionally, the `--path` flag allows the user to specify a file path to save the output.

This tool excludes system users from the exported information and only lists non-system users.

## Features

- Export system user information (name, ID, home directory, shell) in JSON or CSV format.
- Ability to export data directly to a file or display it in the terminal (stdout).
- Simple command-line interface with flexible options for format and file path.

## Installation

To install the tool, clone the repository and install any dependencies:

```bash
git clone clone https://github.com/AugustHottie/hr-cli-tool.git
cd hr-cli-tool
```

Since the tool uses Python’s standard libraries (`pwd`, `argparse`, `json`, and `csv`), no external dependencies are needed. Simply make the Python script executable:

```bash
chmod +x hr-cli-tool
```

You can now run the tool from the command line.

## Usage

The **HR CLI Tool** can be used in several ways to extract and export user data. Below are some examples of how to use the tool.

### Default JSON Output to Stdout

If no flags are specified, the tool will export the user information in **JSON** format to the terminal.

```bash
$ hr-cli-tool
```

Example output:

```json
[
  {
    "name": "cloud_user",
    "id": 1002,
    "home": "/home/cloud_user",
    "shell": "/bin/bash"
  },
  {
    "name": "kevin",
    "id": 1003,
    "home": "/home/kevin",
    "shell": "/bin/zsh"
  }
]
```

### Export to CSV Format

To export user information in **CSV** format, use the `--format` flag with the value `csv`:

```bash
$ hr-cli-tool --format=csv
```

Example output:

```csv
name,id,home,shell
cloud_user,1002,/home/cloud_user,/bin/bash
kevin,1003,/home/kevin,/bin/zsh
```

### Export to a File

To export the user data to a file, use the `--path` flag followed by the file path where the data should be saved. The format will be determined by the file extension if the `--format` flag is omitted (e.g., `.json` or `.csv`).

#### Export to JSON file:

```bash
$ hr-cli-tool --path=path/to/users.json
```

#### Export to CSV file:

```bash
$ hr-cli-tool --format=csv --path=path/to/users.csv
```

## Command-Line Options

- `--format [json|csv]`: Specify the output format (default is `json`).
- `--path`: Specify the file path to save the output. If not specified, the output is printed to the terminal (stdout).

### Example Commands

- Export user information in JSON format to a file:
  ```bash
  $ hr-cli-tool --path=/tmp/users.json
  ```

- Export user information in CSV format to stdout:
  ```bash
  $ hr-cli-tool --format=csv
  ```

- Export user information in CSV format to a file:
  ```bash
  $ hr-cli-tool --format=csv --path=/tmp/users.csv
  ```

## Internals

The tool leverages Python's built-in libraries for interacting with the system and generating the required output formats:

- **`pwd`**: Retrieves user account information from the system.
- **`argparse`**: Handles command-line parsing for flexible user interaction.
- **`json`**: Serializes user information into JSON format.
- **`csv`**: Serializes user information into CSV format.

### How It Works

1. The tool retrieves user information using the `pwd` library, which accesses the system's user database.
2. It filters out system users (i.e., users with IDs lower than 1000 on most systems) to ensure only relevant users are included in the export.
3. Based on the provided command-line arguments, it formats the user data as either JSON or CSV.
4. The data is either printed to the terminal or saved to a file if the `--path` flag is specified.

### Filtering System Users

By design, the tool filters out system users by excluding any users with a user ID (`UID`) lower than 1000. This threshold can be adjusted in the script if needed to accommodate different system configurations.

## Development

### Prerequisites

- Python 3.x

### Setting Up

1. Clone the repository:
   ```bash
   git clone https://github.com/AugustHottie/hr-cli-tool.git
   cd hr-cli-tool
   ```

2. Install the tool:
   ```bash
    pip install  -e .
   ```

3. You're ready to use the tool or contribute to its development!

### Contributing

I welcome contributions! Please open an issue or submit a pull request with your feature ideas or bug fixes.
