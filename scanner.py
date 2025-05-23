import datetime
from zapv2 import ZAPv2
from .utils import wait

class ZAPScanner:
    def __init__(self, target_url, zap_proxy, api_key, logger):
        self.target_url = target_url
        self.zap = ZAPv2(proxies={'http': zap_proxy}, apikey=api_key)
        self.logger = logger

    def access_target(self):
        try:
            self.logger.info(f'Accessing target {self.target_url}')
            self.zap.urlopen(self.target_url)
            wait(2)
        except Exception as e:
            self.logger.error(f'Error accessing target: {e}')

    def start_passive_scan(self):
        try:
            self.logger.info('Starting Passive Scan')
            wait(5)
        except Exception as e:
            self.logger.error(f'Error starting passive scan: {e}')

    def start_active_scan(self):
        try:
            self.logger.info(f'Starting Active Scan on {self.target_url}')
            scan_id = self.zap.ascan.scan(self.target_url)
            while int(self.zap.ascan.status(scan_id)) < 100:
                self.logger.info(f'Scan progress: {self.zap.ascan.status(scan_id)}%')
                wait(5)
            self.logger.info('Scan completed')
        except Exception as e:
            self.logger.error(f'Error starting active scan: {e}')

    def retrieve_alerts(self, user_id, scan_id):
        try:
            self.logger.info('Retrieving alerts')
            alerts = self.zap.core.alerts(baseurl=self.target_url)
            vuln_infos = []
            for alert in alerts:
                vuln_info = {
                    "@timestamp": datetime.datetime.utcnow().isoformat(),
                    "user_id": user_id,
                    "scan_id": scan_id,
                    "module": "zap_scan",
                    "title": alert['alert'],
                    "severity": alert['risk'],
                    "tool_name": 'ZAP',
                    "data": {
                        "alert": alert['alert'],
                        "risk": alert['risk'],
                        "url": alert['url'],
                        "param": alert['param'],
                        "attack": alert['attack'],
                        "evidence": alert['evidence'],
                        "description": alert['description'],
                        "solution": alert['solution'],
                        "reference": alert['reference'],
                    }
                }
                vuln_infos.append(vuln_info)
            return vuln_infos
        except Exception as e:
            self.logger.error(f'Error retrieving alerts: {e}')
            return []

    def generate_report(self, report_path, report_saver):
        try:
            self.logger.info('Generating report')
            html_report = self.zap.core.htmlreport()
            report_saver(html_report, report_path, self.logger)
        except Exception as e:
            self.logger.error(f'Error generating report: {e}')

    def execute(self, user_id, scan_id, report_path, report_saver):
        try:
            self.access_target()
            self.start_passive_scan()
            self.start_active_scan()
            vuln_infos = self.retrieve_alerts(user_id, scan_id)
            self.generate_report(report_path, report_saver)
            return vuln_infos
        except Exception as e:
            self.logger.error(f'Error occurred: {e}')
            return []
