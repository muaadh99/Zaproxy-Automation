def save_html_report(html_report, path, logger):
    try:
        with open(path, 'w') as f:
            f.write(html_report)
        logger.info(f'Report saved as {path}')
    except Exception as e:
        logger.error(f'Error saving report: {e}')
