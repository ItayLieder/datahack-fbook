
import os
import json
import requests
from bs4 import BeautifulSoup

PEOPLE_JSON = "\\data\\people-linkedin.json"
HTML_OUT = "\\data\\html"

client = requests.Session()

HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

html = client.get(HOMEPAGE_URL).content
soup = BeautifulSoup(html)
csrf = soup.find(id="loginCsrfParam-login")['value']

login_information = {
    'session_key': ?,
    'session_password': ?,
    'loginCsrfParam': csrf,
}

client.post(LOGIN_URL, data=login_information)

people = json.load(open(PEOPLE_JSON, 'r'))
for person in people.keys():
    linkedin_url = people[person]
    print person, linkedin_url
    if not "https" in linkedin_url:
        continue
    else:
        linkedin_url = linkedin_url.replace("il.link", "www.link")
        linkedin_url = linkedin_url.replace("th.link", "www.link")
        linkedin_url = linkedin_url.replace("ru.link", "www.link")
        linkedin_url = linkedin_url.replace("uk.link", "www.link")

        page = client.get(linkedin_url)
        html = page.content
        output_file = linkedin_url.split("/")[-1]
        with open(os.path.join(HTML_OUT, "{}.html".format(output_file)), "w") as out:
            out.write(html)
