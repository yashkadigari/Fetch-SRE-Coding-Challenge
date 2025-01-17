# HTTP Endpoint Health Monitor

This Python script monitors the health of HTTP endpoints specified in a YAML configuration file. The script periodically checks the availability of the endpoints and logs their uptime percentage.

## Features
- Monitors HTTP/HTTPS endpoints using custom configuration.
- Logs availability percentage for each endpoint's domain.
- Supports retries for failed requests with configurable retry counts.
- Handles GET, POST, and other HTTP methods.

## Prerequisites
- Python 3.8 or later
- `pip` (Python package installer)
- YAML configuration file specifying endpoints

## Installation
1. Clone this repository or download the script directly.
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, install the dependencies manually:
   ```bash
   pip install requests pyyaml
   ```

## Usage
Run the script using the following syntax:

```bash
python3 monitor.py <path_to_yaml_config> [<retry_count>]
```

### Arguments
- `<path_to_yaml_config>`: Path to the YAML configuration file specifying the endpoints to monitor.
- `[<retry_count>]`: (Optional) Number of retries for failed requests. Must be a positive integer. Default is 3.

### Example
To monitor endpoints defined in `config.yaml` with a retry count of 5:
```bash
python3 monitor.py config.yaml 5
```

### Example YAML Configuration File
```yaml
- name: Example Index Page
  url: https://example.com
  method: GET
  headers:
    user-agent: custom-monitor

- name: Example API Endpoint
  url: https://api.example.com/health
  method: POST
  headers:
    content-type: application/json
  body: '{"key": "value"}'
```

### Default Configuration
If no configuration file is provided, the script uses a built-in default configuration:
- Monitors `https://example.com`, `https://api.example.com/health`, and other sample endpoints.

## Logs and Output
- The script prints availability percentages for each domain to the console after every monitoring cycle.
- Logs include detailed error messages for failed requests and retries.

## Error Handling
- Provides detailed messages for missing or malformed configuration files.
- Validates YAML configuration schema and HTTP method correctness.
- Handles common network errors gracefully.

## Cross-Platform Usage
The script is platform-independent and should work on Windows, macOS, and Linux. Ensure Python 3.8+ is installed on your system.

### Installing Python
1. [Download Python](https://www.python.org/downloads/).
2. Follow the instructions for your operating system.

### Verifying Python Installation
Run the following command to check the installed Python version:
```bash
python3 --version
```

## Testing the Script
You can test the script using the provided example configuration file or create your own.

### Testing Invalid Inputs
- Run without arguments to see usage instructions:
  ```bash
  python3 monitor.py
  ```
- Pass an invalid retry count to test validation:
  ```bash
  python3 monitor.py config.yaml 0
  ```
