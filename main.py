from datetime import datetime
import pdfkit

reunion_url = 'https://www.ipgp.fr/volcanoweb/reunion/Bulletin_quotidien/bulletin.html'
mayotte_url = 'https://www.ipgp.fr/volcanoweb/mayotte/Bulletin_quotidien/bulletin.html'

today = datetime.now()

pdfkit.from_url(f'{reunion_url}', 'reunion_{}.pdf')