from bs4 import BeautifulSoup
import requests
from datetime import datetime
import re

class ParseSite:
    def __init__(self, url):
        self.url_to_parse = url

    def parse_html(self, site_data):
        soup = BeautifulSoup(site_data, 'html.parser')
        return soup

    def get_html(self):
        try:
            r = requests.get(self.url_to_parse)
            return (r.status_code, r.content)
        except Exception as e:
            print(e)

    def get_text(self, soup):
        return " ".join(str(re.sub('(\n|\r|\t)', '', soup)).split())


    def process(self):
        (status_code, site_data) = self.get_html()
        if status_code != 200:
            return "Error in parsing the given site"
        parsed_data = self.parse_html(site_data)
        events_list = parsed_data.find_all(class_="entry")
        all_events = []
        for event in events_list:
            try:
                event_date = event['data-date']
                event_time = datetime.strptime(event.find(class_="time").string, '%H.%M').time() 
                event_location = self.get_text(event.find(class_="location").find('a').text)
                event_title = event.find(class_="title").find(class_="detail").text
                event_subtitle = self.get_text(event.find(class_="subtitle").text)
                all_events.append({
                    "event_date": event_date,
                    "event_time": event_time,
                    "event_location": event_location,
                    "event_title": event_title,
                    "event_subtitle": event_subtitle
                })
            except Exception as e:
                print(e)
        return all_events