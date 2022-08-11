#")

from xml.dom.minidom import Identified
import requests
import csv 
from requests_html import HTML
from requests_html import HTMLSession
with open('ratings.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'title','content', 'voteSum', 'voteCount', 'rating', 'updated', 'version']    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(1,10):
        url=f"https://itunes.apple.com/us/rss/customerreviews/page={i}/id=499597400/sortby=mostrecent/xml?urlDesc=/customerreviews/id=499597400/sortBy=mostRecent/xml"
        session = HTMLSession()
        response = session.get(url)
        with response as r:
            entries=r.html.find("entry", first=False)
            for entry in entries:
                title = entry.find('title', first=True).text
                id = entry.find('id', first=True).text
                content = entry.find('content', first=True).text
                voteSum = entry.find('voteSum', first=True).text
                
                voteCount = entry.find('voteCount', first=True).text
                rating = entry.find('rating', first=True).text
                updated = entry.find('updated', first=True).text
                version = entry.find('version', first=True).text
                writer.writerow(
                    {
                        'id':id,
                        'title':title,
                        'content':content,
                        'voteSum':voteSum,
                        'voteCount':voteCount,
                        'rating':rating,
                        'updated':updated,
                        'version':version
                        })
