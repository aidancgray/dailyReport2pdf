from datetime import datetime
import pdfkit
import logging
import sys
import os

src_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
rpt_dir = src_dir + '\\' + 'IPGP_Reports\\'

logging.basicConfig(datefmt = "%Y-%m-%d %H:%M:%S", 
                    format = '%(name)s | %(asctime)s.%(msecs)03d | %(levelname)s | %(message)s',
                    filename=rpt_dir + '\\' + 'report.log',
                    level=logging.INFO,
                    filemode='a'
                    )
logger = logging.getLogger('dailyReport2pdf')

reunion_url = 'https://www.ipgp.fr/volcanoweb/reunion/Bulletin_quotidien/bulletin.html'
mayotte_url = 'https://www.ipgp.fr/volcanoweb/mayotte/Bulletin_quotidien/bulletin.html'

today = datetime.now().strftime("%Y-%m-%d")
logger.info(f'Today\'s Date:  {today}')

try:
    if pdfkit.from_url(f'{reunion_url}', f'{rpt_dir}Reunion_{today}.pdf'):
        logger.info(f'Reunion Report OK')
    else:
        logger.warn(f'Reunion Report FAILED')
except OSError as e:
    logger.exception(e)
try:
    if pdfkit.from_url(f'{mayotte_url}', f'{rpt_dir}Mayotte_{today}.pdf'):
        logger.info(f'Mayotte Report OK')
    else:
        logger.warn(f'Mayotte Report FAILED')
except OSError as e:
    logger.exception(e)