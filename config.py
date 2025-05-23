import os

def get_config():
    return {
        "target_url": os.getenv('TARGET_URL', 'http://testphp.vulnweb.com'),
        "zap_proxy": os.getenv('ZAP_PROXY', 'http://localhost:8080'),
        "api_key": os.getenv('ZAP_API_KEY', 'change-me-9203935709'),
        "user_id": os.getenv('USER_ID', 'user_123'),
        "scan_id": os.getenv('SCAN_ID', 'scan_123'),
    }
