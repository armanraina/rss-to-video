import requests
from tqdm import tqdm
from util import getFeed, createVideo, getFilteredFeedEntries
from config_manager import getConfig, updateDate
from dateutil import parser



config = getConfig()
CITR_URL = config['DEFAULT']['CITR_URL']
BASE_DIR = config['DEFAULT']['BASE_DIR']
EXT = config['DEFAULT']['EXT_INPUT_AUDIO']
OUT_EXT = config['DEFAULT']['EXT_OUTPUT_VIDEO']
IMAGE = config['DEFAULT']['IMAGE']
START_DATE = config['DEFAULT']['START_DATE'] 
feed = getFeed(CITR_URL)
start_date = parser.parse(START_DATE)

IMAGE = 'divest.jpeg'

for episode in getFilteredFeedEntries(feed, start_date):
	response = requests.get(episode.link, stream=True)
	filename = "".join([c for c in episode.title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
	with open(BASE_DIR+filename+EXT, "wb") as handle:
		for data in tqdm(response.iter_content(chunk_size=1024*1024)):
			handle.write(data)
		createVideo(BASE_DIR+IMAGE, BASE_DIR+filename+EXT, BASE_DIR + filename +OUT_EXT, episode.summary+ ' ' + episode.published)
	updateDate(parser.parse(episode.published))
		
