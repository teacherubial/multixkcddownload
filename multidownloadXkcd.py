# multidownloadXkcd.py
# Downloads XKCD comics using multipled threads

import requests, os, bs4, threading

# create or open a dir ./xkcd
os.makedirs('xkcd', exist_ok=True)

# TODO: Create function to download comic
def downloadXkcd(start_comic, end_comic):
    """ downloads all XKCD comics from start to end

    arguments:
    start_comic - the first comic you want to download
    end_comic - the last comic you want to download
    """

    for url_number in range(start_comic, end_comic + 1):
        pass
        # TODO: Download the page
        # TODO: Find the URL of the comic
        # TODO: Save the image if it exists

# TODO: Create and start the Threads

# TODO: Wait for all threads to end
