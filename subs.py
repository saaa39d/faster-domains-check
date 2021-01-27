import requests,re,socket,concurrent.futures,colorama,sys
colorama.init()
# This code was Writeed by saad_alhrby all my thx to "web_alive" my bro 1337r00t
def man():
	print(colorama.Fore.RED,"Usage :",colorama.Fore.BLUE," python3 subs.py site.com \r\n ")
	r=sys.argv[1]
	if len(r) <=5:
		print("Enter ur  hostname Again bitch")
	else:
		try:
			req=requests.get("https://api.linuxsec.org/api/subdomains?host="+r)
		except:
			print("Hostname Down")
		else:
			regex=re.findall("[\w\-\.]*%s"%r,req.text)
			for i in regex:
				s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				s.settimeout(0.1)

				try:
					s.connect_ex((i,80))
					print(colorama.Fore.BLUE,"Worked as well "+i)
				except:
					try:
						s.connect_ex((i,443))
					except:
						print(colorama.Fore.RED,"Bad url "+i)
				else:
					print("Works as well "+ i)
			
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pl:
	pl.submit(man)