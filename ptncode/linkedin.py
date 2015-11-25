
import urllib2
from bs4 import BeautifulSoup
import json


PEOPLE_JSON = "c:\\datahack\\data\\people-linkedin.json"
people_json = json.load(open(PEOPLE_JSON, 'r'))

# all people go here
people = dict()

for person in people_json.keys():
    print person
    
    url_to_get = people_json[person]
    if not "www" in url_to_get:
        continue

    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36')]

    page = opener.open(url_to_get).read()
    soup = BeautifulSoup(page, "lxml")

    # Find all skills
    skills = []
    skill_elements = soup.findAll('li', attrs={'class':"skill"})
    for el in skill_elements:
        skills.append(el.getText())

    #GET SUMMARY
    try:
        summary_soup = soup.findAll('section', attrs={'id': "summary"})
        summary = summary_soup[0].findAll('div', attrs={'class': "description"})[0].get_text()
    except:
        summary = ""

    # GET JOBS
    job_positions_list = soup.findAll('li',attrs={'class':  "position"})
    job_dicts_list = []
    for job in job_positions_list:
        job_dict = {}
        job_title = job.findAll(attrs={'class': "item-title"})
        job_place =  job.findAll(attrs={'class': "item-subtitle"})
        job_descrip =  job.findAll(attrs={'class': "description"})
        job_dict["job_title"] = job_title[0].get_text()
        job_dict["job_place"] = job_place[0].get_text()
        if len(job_descrip)>0:
            job_dict["job_descrip"] = job_descrip[0].get_text()
        else:
            job_dict["job_descrip"] = None

        job_dicts_list.append(job_dict)

    #GET EDS
    edu_list = soup.findAll('li',attrs={'class':"school"})
    edu_dicts_list = []
    for ed in edu_list:
        ed_dict = {}
        ed_title = ed.findAll(attrs={'class':"item-title"})
        ed_place =  ed.findAll(attrs={'class':"item-subtitle"})
        ed_descrip =  ed.findAll(attrs={'class':"description"})
        ed_dict["ed_place"] = ed_title[0].get_text()
        ed_dict["ed_title"] = ed_place[0].get_text()
        if len(ed_descrip)>0:
            ed_dict["ed_descrip"] = ed_descrip[0].get_text()
        else:
            ed_dict["ed_descrip"] = None

        edu_dicts_list.append(ed_dict)


    this_person = {"LinkedIn": url_to_get,
                   "skills": skills,
                   "jobs": job_dicts_list,
                   "eds": edu_dicts_list,
                   "summary": summary}

    people[person] = this_person

json.dump(people, open("with_skills.json", "w"), indent=4)
