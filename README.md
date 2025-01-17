# HTTP Endpoint Health Monitor

## Overview
This Python program monitors the health of HTTP endpoints specified in a YAML configuration file. It periodically checks the endpoints' availability and logs the results to the console, including the availability percentage of each domain over the program's runtime.

## Features
- Supports `GET`, `POST`, and other HTTP methods.
- Logs the availability percentage of domains to the console after each test cycle.
- Retries failed requests up to 3 times by default.
- Runs continuously, checking endpoints every 15 seconds, until manually stopped.

## Requirements
- Python 3.6 or higher
- Internet access to perform health checks
- The `requests` and `PyYAML` Python libraries

## Installation
1. Clone this repository or download the script (`monitor.py`).
2. Ensure Python is installed on your system. To check:
   ```bash
   python3 --version
   ```
3. Install the required libraries:
   ```bash
   pip install requests pyyaml
   ```

## Usage
Run the script using the following command:
```bash
python3 monitor.py <path_to_yaml_config>
```

### Example:
```bash
python3 monitor.py config.yaml
```

### Input File Format
The configuration file must be a YAML file with a list of endpoints. Each endpoint entry should follow this schema:
- **`name`** (string, required): A descriptive name for the endpoint.
- **`url`** (string, required): The endpoint's URL.
- **`method`** (string, optional): HTTP method (`GET`, `POST`, etc.). Defaults to `GET`.
- **`headers`** (dictionary, optional): HTTP headers to include in the request.
- **`body`** (string, optional): HTTP body for the request (valid JSON string).

#### Sample Configuration (`config.yaml`):
```yaml
- name: Fetch homepage
  url: https://fetch.com/
  method: GET
  headers:
    user-agent: fetch-monitor

- name: Fetch careers
  url: https://fetch.com/careers
  method: GET

- name: Fetch API health
  url: https://api.fetch.com/health
  method: POST
  headers:
    content-type: application/json
    user-agent: fetch-monitor
  body: '{"check": "health"}'
```

## Output
After each cycle (15 seconds), the program logs availability percentages for each domain:
```plaintext
fetch.com has 75% availability percentage
api.fetch.com has 100% availability percentage
```

## Error Handling
1. **File Not Found:**
   If the provided YAML file is not found, the program exits with an error:
   ```plaintext
   Error: File 'config.yaml' not found.
   ```

2. **YAML Parsing Error:**
   If the YAML file is malformed, the program exits with an error:
   ```plaintext
   Error: Failed to parse YAML file. <details>
   ```

3. **Invalid Command:**
   If no file is provided, the program exits with usage instructions:
   ```plaintext
   Usage: python3 monitor.py <path_to_yaml_config>
   Example: python3 monitor.py config.yaml
   ```

## Limitations
- The program assumes the YAML file is valid and does not validate its schema beyond basic file parsing.
- Requests are retried up to 3 times with a fixed 1-second delay between retries.

## Stopping the Program
To stop the program, press `CTRL+C`. The program will log a termination message and exit gracefully:
```plaintext
Monitoring stopped. Exiting program.
```

## Notes for Reviewers
- The program is designed to run on any OS with Python installed.
- It does not persist data to disk; all state is maintained in memory.
- You can use the provided `config.yaml` sample or create your own configuration file for testing.
