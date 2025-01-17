# File: monitor.py

import sys
import time
import yaml
import requests
from collections import defaultdict

DEFAULT_RETRIES = 3

def parse_yaml(file_path):
    """Parse the YAML configuration file."""
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def check_health(endpoint, retries):
    """Perform a health check on a single endpoint with retry logic."""
    method = endpoint.get('method', 'GET').upper()
    url = endpoint['url']
    headers = endpoint.get('headers', {})
    body = endpoint.get('body', None)

    attempt = 0
    while attempt < retries:
        try:
            start_time = time.time()
            response = requests.request(method, url, headers=headers, data=body, timeout=5)
            latency = (time.time() - start_time) * 1000  # Convert to milliseconds

            if 200 <= response.status_code < 300 and latency < 500:
                return "UP"
            return "DOWN"
        except requests.RequestException as e:
            print(f"Request failed for endpoint '{endpoint['name']}' ({url}) on attempt {attempt + 1}/{retries}: {e}")
            attempt += 1
            time.sleep(1)  # Wait before retrying

    return "DOWN"

def main():
    """Main program to monitor endpoints."""
    if len(sys.argv) != 2:
        print("Usage: python3 monitor.py <path_to_yaml_config>")
        print("Example: python3 monitor.py config.yaml")
        sys.exit(1)

    config_path = sys.argv[1]

    try:
        endpoints = parse_yaml(config_path)
    except FileNotFoundError:
        print(f"Error: File '{config_path}' not found.")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error: Failed to parse YAML file. {e}")
        sys.exit(1)

    domain_stats = defaultdict(lambda: {"up": 0, "total": 0})

    try:
        while True:
            for endpoint in endpoints:
                domain = endpoint['url'].split('/')[2]  # Extract domain
                status = check_health(endpoint, DEFAULT_RETRIES)
                domain_stats[domain]['total'] += 1
                if status == "UP":
                    domain_stats[domain]['up'] += 1

            for domain, stats in domain_stats.items():
                total_checks = stats['total']
                up_checks = stats['up']
                availability = round(100 * (up_checks / total_checks))
                print(f"{domain} has {availability}% availability percentage")

            print("Waiting for the next cycle... Press CTRL+C to stop.")
            time.sleep(15)
    except KeyboardInterrupt:
        print("\nMonitoring stopped. Exiting program.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
