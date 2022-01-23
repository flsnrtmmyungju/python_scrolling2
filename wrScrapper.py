import requests
from bs4 import BeautifulSoup

def extract_job(i):
  try : 
    class_company = i.select('.company')
    company = ''
    location = i.select('.region')
    num = 0
    for j in class_company :
      num += 1  
      if num == 1:
        company = j.text
    title = i.find("span",{"class":"title"}).get_text() 
    location = i.find("span",{"class":"region company"}).get_text() 
    apply_link = f"https://weworkremotely.com/{i['href']}"  
  except AttributeError  as e :
    return None  
  return {'title':title,'company':company,'location':location,"apply_link":apply_link}
  
def extract_jobs(url):
  jobs=[] 
  result = requests.get(url)
  soup = BeautifulSoup(result.text,"html.parser")
  soup = soup.select('.jobs > article > ul > li > a')
  for i in soup :  
    job = extract_job(i)
    if job is not None :
      print("Scrapping weworkremotely")
      jobs.append(job) 
  return jobs

def get_wr_jobs(job):
  url = f"https://weworkremotely.com/remote-jobs/search?term={job}"
  jobs = extract_jobs(url)
  return jobs