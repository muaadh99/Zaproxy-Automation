import json
from .config import get_config
from .logger import get_logger
from .scanner import ZAPScanner
from .report import save_html_report

def main():
    config = get_config()
    logger = get_logger()
    scanner = ZAPScanner(config['target_url'], config['zap_proxy'], config['api_key'], logger)
    findings = scanner.execute(config['user_id'], config['scan_id'], 'zap_report_learnwdg.html', save_html_report)
    print(json.dumps(findings, indent=2))

if __name__ == "__main__":
    main()
