import requests
from bs4 import BeautifulSoup

def extract_job(i):
  try :     
    title_link = i.find("a",{"class":"preventLink"})
    title = title_link.get_text(strip=True)   
    company = i.find("span",{"class":"companyLink"}).get_text(strip=True)
    location = i.find("div",{"class":"location tooltip"}).get_text()
    apply_link = f"https://remoteok.com/{title_link['href']}"   
  except AttributeError  as e :
    return None  
  return {'title':title,'company':company,'location':location,"apply_link":apply_link}

def extract_jobs(url):
  jobs=[] 
  headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Whale/3.12.129.46 Safari/537.36'}
  result = requests.get(url,headers = headers)
  soup = BeautifulSoup(result.text,"html.parser",)
  soup = soup.select('#jobsboard > .job > .company_and_position')
  for i in soup :  
    job = extract_job(i)
    if job is not None:
      print("Scrapping remoteok")
      jobs.append(job)   
  return jobs

def get_rt_jobs(job):
  url = f"https://remoteok.com/remote-{job}-jobs"
  jobs = extract_jobs(url)
  return jobs