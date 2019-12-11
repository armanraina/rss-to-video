from feedsearch_crawler import search
import feedparser
import ffmpeg
from datetime import timedelta, timezone, datetime
from dateutil import parser


def getFeed(rss_url):
	feeds = search(rss_url)
	podcast_url = feeds[0].url.human_repr()
	feed = feedparser.parse(podcast_url)
	return feed

def createVideo(image_file, audio_file, out_dir, description):
	audio = ffmpeg.input(audio_file)
	image = ffmpeg.input(image_file, loop=1, framerate=1)
	out = ffmpeg.output(
	audio, image, out_dir, 
	shortest=None, preset='veryslow', crf=0,
	 **{'c:a': 'copy', 'c:v': 'libx264','metadata': f'description="{description}"'})
	out.run()

def getFilteredFeedEntries(feed, start_date=None):
	if start_date == None:
	 start_date =  datetime.min.replace(tzinfo=timezone.utc)
	for episode in feed.entries:
		published = parser.parse(episode.published)
		if published > start_date:
			yield episode  

def createVideoStream(image_stream, audio_stream, out_stream):
	audio = ffmpeg.input(audio_stream)
	image = ffmpeg.input(image_stream, loop=1, framerate=1)
	out = ffmpeg.output(
	audio, image, out_dir, 
	shortest=None, preset='veryslow', crf=0,
	 **{'c:a': 'copy', 'c:v': 'libx264'})
	out.run()
