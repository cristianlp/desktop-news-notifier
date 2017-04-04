"""
-*- coding: utf-8 -*-
========================
Python Desktop News Notifier
========================

Developed by: Chirag Rathod (Srce Cde)
Email: chiragr83@gmail.com

========================
"""

import feedparser
import notify2
import time
import os


def Parsefeed():
    f = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
    ICON_PATH = os.getcwd() + "/icon.ico"
    notify2.init('News Notify')

    for newsitem in f['items']:
        print(newsitem['title'])
        print(newsitem['summary'])
        print('\n')

        n = notify2.Notification(newsitem['title'],
                                 newsitem['summary'],
                                 icon=ICON_PATH
                                 )

        n.set_urgency(notify2.URGENCY_NORMAL)
        n.show()
        n.set_timeout(10000)
        time.sleep(1200)


if __name__ == '__main__':
    Parsefeed()
