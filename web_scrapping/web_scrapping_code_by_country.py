from urllib.request import urlopen
from bs4 import BeautifulSoup

header_url="https://www.tennisexplorer.com"
country_link="https://www.tennisexplorer.com/ranking/atp-men/?page=1"
request_page = urlopen(country_link)
page_html = request_page.read()
request_page.close()
html_soup = BeautifulSoup(page_html , 'html.parser')
filename1='current_male_tennis_players.csv'
f1=open(filename1, 'w')
filename2='current_female_tennis_players.csv'
f2=open(filename2, 'w')
headers= 'FIRST NAME , LAST NAME , PLAYS , GENDER , COUNTRY , AGE , DOB , HEIGHT , WEIGHT , CURRENT SINGLES RANKING , HEIGHEST SINGLES RANKING ,CURRENT DOUBLES RANKING , HEIGHEST DOUBLES RANKING , IMAGE \n'
f1.write(headers)
f2.write(headers)
while True:
  
  tablebody=html_soup.find('tbody',class_="flags")
  player_names=tablebody.find_all('td',class_="t-name")
  
  for player in player_names:
    
    k=player.find('a')
    if k==None:
        continue
    print(k.text)
    link=header_url+k['href']
    request_page = urlopen(link)
    html = request_page.read()
    request_page.close()
    soup = BeautifulSoup(html , 'html.parser')
    
    
    table= soup.find('table',class_="plDetail")
    image=header_url + table.find('img')['src']
    name=table.find('h3').text.split(' ')
    
    first_name=name[0].strip()
    last_name=''.join(name[1:]).strip()
    d={}
    d["Country"]=''
    d["Current/Highest rank - singles"]=''
    d["Current/Highest rank - doubles"]=''
    d['Age']=''
    d['Sex']=''
    d['Plays']=''
    d["Height / Weight"]=''
    age,dob='',''
    details_divs=table.find_all('div',class_="date")
    for info in details_divs:
        arrr=info.text.split(':')
        d[arrr[0]]=arrr[1].strip()
    if d["Current/Highest rank - singles"]=='':
        continue
    height,weight='-','-'
    if d["Height / Weight"]  != '':
        bb=d["Height / Weight"].split('/')
        height,weight=bb[0].strip().replace(' ',''),bb[1].strip().replace(' ','')
    
    cc=d["Current/Highest rank - singles"].split('/')
    Current_Singles,Heighest_Singles=cc[0].strip().strip('.'),cc[1].strip().strip('.')
    Current_Doubles,Heighest_Doubles='-','-'
    if d["Current/Highest rank - doubles"]!='':
        dd=d["Current/Highest rank - doubles"].split('/')
        Current_Doubles,Heighest_Doubles=dd[0].strip().strip('.'),dd[1].strip().strip('.')
    if d['Age']!='':
        vv=d['Age'].split('(')
        age=vv[0].strip().replace(' ','')
        dob=vv[1].replace(')','').strip().replace(' ','')
    
    
    wltab=soup.find('div',id="balMenu-2-data")
    wins_loses_doubles_a=wltab.find('a')
    wins_loses_doubles='-'
    if wins_loses_doubles_a != None:
        wins_loses_doubles=wins_loses_doubles_a.text.strip()
    wltabs=soup.find('div',id="balMenu-1-data")
    wins_loses_singles_a=wltab.find('a')
    wins_loses_singles='-'
    if wins_loses_singles_a != None:
        wins_loses_singles=wins_loses_singles_a.text.strip()
    
    
    single_titles_main='0'
    single_titles_lower='0'
    lists_s=soup.find('div',id="titMenu-1-data")
    tfootdata1=lists_s.find('tfoot')
    if tfootdata1!=None:
     single_titles=[ints.text.strip() for ints in tfootdata1.find_all('td',class_="titles-col")]
     if len(single_titles)!=0:
        single_titles_main=single_titles[0].replace(' ','')
        single_titles_lower=single_titles[1].replace(' ','')
    
    
    doubles_titles_main='0'
    doubles_titles_lower='0'
    lists_d=soup.find('div',id="titMenu-1-data")
    tfootdata2=lists_s.find('tfoot')
    if tfootdata2!=None:
     doubles_titles=[ints.text.strip() for ints in tfootdata2.find_all('td',class_="titles-col")]
     if len(doubles_titles)!=0:
        doubles_titles_main=doubles_titles[0].replace(' ','')
        doubles_titles_lower=doubles_titles[1].replace(' ','')
    print(first_name+','+last_name+','+d["Plays"]+','+d["Sex"]+','+d["Country"]+','+age+','+dob+','+height+','+weight+','+Current_Singles+','+Heighest_Singles+','+Current_Doubles+','+Heighest_Doubles+','+single_titles_main+','+single_titles_lower+','+doubles_titles_main+','+doubles_titles_lower+','+wins_loses_singles+','+wins_loses_doubles+','+image+'\n')
    if d["Sex"]=='man':
        f1.write(first_name+','+last_name+','+d["Plays"]+','+d["Sex"]+','+d["Country"]+','+age+','+dob+','+height+','+weight+','+Current_Singles+','+Heighest_Singles+','+Current_Doubles+','+Heighest_Doubles+','+single_titles_main+','+single_titles_lower+','+doubles_titles_main+','+doubles_titles_lower+','+wins_loses_singles+','+wins_loses_doubles+','+image+'\n')
    else:
        f2.write(first_name+','+last_name+','+d["Plays"]+','+d["Sex"]+','+d["Country"]+','+age+','+dob+','+height+','+weight+','+Current_Singles+','+Heighest_Singles+','+Current_Doubles+','+Heighest_Doubles+','+single_titles_main+','+single_titles_lower+','+doubles_titles_main+','+doubles_titles_lower+','+wins_loses_singles+','+wins_loses_doubles+','+image+'\n')
  
  next_page=html_soup.find('a' , title="Next page")
  if next_page == None:
      break
  url="https://www.tennisexplorer.com"+next_page['href']
  request_page = urlopen(url)
  page_html = request_page.read()
  request_page.close()
  html_soup = BeautifulSoup(page_html , 'html.parser')
f1.close()
f2.close()