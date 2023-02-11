import datetime
from generateUrl import generate_url
from scrapePanchangam import scrape_panchangam
from displayPanchangam import print_panchangam

today = datetime.datetime.now().strftime("%d/%m/%Y")


if __name__ == '__main__':
    scrape_panchangam(today, generate_url(today))

    print_panchangam() 
