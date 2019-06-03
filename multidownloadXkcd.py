# multidownloadXkcd.py
# Downloads XKCD comics using multipled threads

import requests
import os
import bs4
import threading

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
        print(f'Downloading the page http://xkcd.com/{url_number}...')
        res = requests.get(f'http://xkcd.com/{url_number}')
        res.raise_for_status()

        # Find the URL of the comic
        soup = bs4.BeautifulSoup(res.content, 'html.parser')

        comic_elem = soup.select('#comic img')


        # Save the image if it exists
        if comic_elem == []:
            print('Could not find comic.')
        else:
            comic_url = 'http:' + comic_elem[0].get('src')

            # Download the image
            print(f'Downloading image {url_number}...')
            res = requests.get(comic_url)
            res.raise_for_status()

            # Save the image
            image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()


def main():
    downloadXkcd(1, 5)


if __name__ == "__main__":
    main()


# TODO: Create and start the Threads

# TODO: Wait for all threads to end
