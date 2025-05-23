# Automated Web Vulnerability Scanning with OWASP ZAP and Python

This guide explains how to install **OWASP ZAP** on Kali Linux (or any Debian-based Linux), run it in daemon mode, and use the provided Python script to automate vulnerability scanning and generate actionable reports.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installing OWASP ZAP](#installing-owasp-zap)
- [Running ZAP in Daemon Mode](#running-zap-in-daemon-mode)
- [Installing Python Dependencies](#installing-python-dependencies)
- [Using the Python Scanner Script](#using-the-python-scanner-script)
- [Understanding the Output](#understanding-the-output)
- [Best Practices & Next Steps](#best-practices--next-steps)
- [References](#references)

---

## Prerequisites

- **Kali Linux** or any Debian-based Linux distribution
- **Python 3** installed
- **Internet connection** (for installing packages and downloading dependencies)
- **Administrator (sudo) privileges**

---

## Installing OWASP ZAP

### Update Your System

sudo apt update
sudo apt upgrade


### Install ZAPROXY

sudo apt install zaproxy


This command will install OWASP ZAP and all required dependencies.

---

## Running ZAP in Daemon Mode

Daemon mode allows ZAP to run headlessly (no GUI), which is ideal for automation.

### Start ZAP in Daemon Mode

zaproxy -daemon -port 8080 -config api.key=YOUR_API_KEY

- Replace `YOUR_API_KEY` with a strong, random string.
- The default API port is `8080`, but you can change it if needed.

**Tip:**  
You can also create a systemd service to run ZAP in the background automatically.

---

## Installing Python Dependencies

### Install the ZAP Python API Client

pip install python-owasp-zap-v2.4

or

pip install zaproxy


This will provide the `zapv2` module required by the script.

---

## Using the Python Scanner Script

### Configure Environment Variables (Optional)

You can set these variables to customize the scan:

- `TARGET_URL` – The web application URL to scan (default: `http://testphp.vulnweb.com`)
- `ZAP_PROXY` – The proxy address for ZAP (default: `http://localhost:8080`)
- `ZAP_API_KEY` – Your ZAP API key (default: `change-me-9203935709`)
- `USER_ID` – (Optional) User identifier for tracking
- `SCAN_ID` – (Optional) Scan identifier for tracking

Example:

export TARGET_URL="http://your.target.site"
export ZAP_PROXY="http://localhost:8080"
export ZAP_API_KEY="your-actual-api-key"


### Run the Script

python3 zap_scanner.py


- The script will access the target, perform passive and active scans, retrieve alerts, and generate a detailed HTML report.

---

## Understanding the Output

- **JSON Output:**  
  The script prints a JSON array of detected vulnerabilities, including details like severity, affected URLs, and recommended solutions.

- **HTML Report:**  
  A comprehensive HTML report named `zap_report_learnwdg.html` is generated in the script directory. This report includes:
  - Overview of vulnerabilities
  - Detailed information for each alert (risk levels, affected URLs, descriptions, and solutions).

---

## Best Practices & Next Steps

- **Review Alerts Carefully:**  
  Not all findings are critical. Review each alert, prioritize remediation, and watch for false positives.

- **Update Regularly:**  
  Keep ZAP and its plugins up to date for the latest vulnerability checks.

- **Integrate with CI/CD:**  
  ZAP can be integrated into CI/CD pipelines for continuous security testing.

- **Ethical Use:**  
  Only scan applications you own or have explicit permission to test.

---

## References

- [OWASP ZAP Official Documentation](https://www.zaproxy.org/docs/)
- [ZAP Python API Client](https://pypi.org/project/python-owasp-zap-v2.4/)
- [Kali Linux Tools: zaproxy](https://tools.kali.org/web-applications/zaproxy)

---

*Happy and responsible testing!*
