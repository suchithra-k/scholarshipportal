from datetime import datetime
import requests
from bs4 import BeautifulSoup

from django.utils.text import slugify
from ..models import Scholarship


def crawl_data():
    base_link = 'https://www.scholarshipportal.com'
    start_link = '{}/bachelor/scholarships/india'.format(base_link)

    count = 0
    try:
        while(True):
            page_response = requests.get(start_link, timeout=5)

            page_content = BeautifulSoup(page_response.content, "html.parser")

            scholarships = page_content.find_all('a', {'class': 'scholarship'})

            for scholarship in scholarships:
                title = scholarship.find('h3',{'class':'scholarship__title'}).text
                url = base_link + scholarship.attrs['href']
                contents = scholarship.find_all('li', {'class':'list__item'})
                waiver = None if len(contents) < 1 else contents[0].text
                deadline = None if len(contents) < 2 else contents[1].text

                count = save_data(title=title, url=url, deadline=deadline, count=count)

            nextPage = page_content.find('span', {'class','pagination__item pagination__item--right'}).find('a')
            if(nextPage == None) :
                break
            else:
                start_link = base_link + nextPage.attrs['href']
    except:
        pass

    return count


def save_data(title, url, deadline, count):
    try:
        slug = slugify(title)
        if deadline is not None:
            deadline = deadline.split(':')[1].strip()
            deadline = datetime.strptime(deadline, '%B %d, %Y') if isValidExpirytDate(deadline) else None
        if not Scholarship.objects.filter(slug=slug).exists():
            Scholarship(title=title, url=url, expiry_date=deadline).save()
            count+=1
    except:
        pass
    return count

def isValidExpirytDate(deadline):
    try:
        datetime.strptime(deadline, '%B %d, %Y')
        return True
    except:
        return False
