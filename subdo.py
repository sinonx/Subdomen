import requests
import re
from multiprocessing.dummy import Pool
import os
requests.packages.urllib3.disable_warnings()

def banner():
	print("""

           _         _       
          | |       | |      
 ___ _   _| |__   __| | ___  
/ __| | | | '_ \ / _` |/ _ \ 
\__ \ |_| | |_) | (_| | (_) |
|___/\__,_|_.__/ \__,_|\___/ 
                             
    Subdomain Scanner

    Author : Abdi Pranata
    API by Sonar Omnisint

		""")


def single():

	nama = input('Website -> ')
	if '://' in nama:
		oke = nama.split('/')
		web = oke[2]
	else:
		web = nama
	web = web.replace('www.', '')

	r = requests.get('https://sonar.omnisint.io/subdomains/{}'.format(web), verify=False)
	ambil = re.findall('"(.*?)"', r.text)

	if r.status_code == 200:
		print('=' * 30)
		print('Subdomains of', web)
		print('=' * 30)
		for a in ambil:
			print(a)
	else:
		print('No Record!')


def mass(hola):

	if '://' in hola:
		oke = hola.split('/')
		websit = oke[2]
	else:
		websit = hola
	websit = websit.replace('www.', '')

	r = requests.get('https://sonar.omnisint.io/subdomains/{}'.format(websit), verify=False)
	jupuk = re.findall('"(.*?)"', r.text)

	if r.status_code == 200:
		print(websit, '|', len(jupuk), 'Subdomains')
		for b in jupuk:
			le = b.strip()
			open('subdo.txt', 'a').write('\n'+le+'\n')
	else:
		print(websit, '| No records!')

def thread(ok):

	geh = open(ok, 'r').read().splitlines()
	p = Pool(50)
	p.map(mass, geh)


if __name__ == "__main__":

	os.system('cls' if os.name == 'nt' else 'clear')
	banner()
	print('1. Single Scan')
	print('2. Mass Scan'+'\n')

	pilih = input('Select Options! -> ')

	if pilih == '1':
		single()
	elif pilih == '2':
		webmu = input('Website List -> ')
		thread(webmu)
	else:
		print('No Options!')