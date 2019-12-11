import configparser
from datetime import timezone, datetime
from dateutil import parser

def initializeConfig(date_str):
	config = configparser.ConfigParser()
	config['DEFAULT']['CITR_URL'] = 'citr.ca/radio/democracy-watch/'
	config['DEFAULT']['BASE_DIR'] = '/media/arman/Data1/CITR/DemocracyWatch/'
	config['DEFAULT']['EXT_INPUT_AUDIO'] = '.mp3'
	config['DEFAULT']['EXT_OUTPUT_VIDEO'] = '.mkv'
	config['DEFAULT']['IMAGE'] = 'democracy_watch.jpg'
	config['DEFAULT']['START_DATE'] = date_str
	with open('/home/arman/projects/rss_to_youtube/config.ini', 'w') as configfile:
		config.write(configfile)
		
def getConfig():
	config = configparser.ConfigParser()
	config.read('config.ini')
	return config

def updateDate(date):
	config = configparser.ConfigParser()
	config.read('config.ini')
	date = max(parser.parse(config['DEFAULT']['START_DATE']), date)
	config['DEFAULT']['START_DATE'] = str(date)
	with open('/home/arman/projects/rss_to_youtube/config.ini', 'w+') as configfile:
		config.write(configfile)

	
