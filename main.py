# OSINT By Caviar1998 For Google Code-in 2023©

import urllib3 as url

class GCI:
	def banner():
		print("[---- OSINT By FajarTheGGman ----]\n")

	def main():
		user = str(input("[!] Input Name Victim ? "))
                number = str(input("[!] Input Number Victim ? "))
		init = url.PoolManager()
		a = init.request("GET", "https://facebook.com/" + user)
		b = init.request("GET", "https://instagram.com/" + user)
		c = init.request("GET", "https://twitter.com/" + user)
                d = init.request("GET", "https://m.youtube.com/" + user)
                e = init.request("GET", "https://github.com" + user)
                f = init.request("GET", "https://www.tiktok.com/" + user)
                g = init.request("GET", "https://wa.mr/" + number)
  
  
		if a.status == 200:
			print("[+] " + user + " => Found In Facebook")
		else:
			print("[-] " + user + " => NotFound in Facebook")

		if b.status == 200:
			print("[+] " + user + " => Found In Instagram")
		else:
			print("[-] " + user + " => NotFound in Instagram")

		if b.status == 200:
			print("[+] " + user + " => Found In Twitter")
		else:
			print("[-] " + user + " => NotFound in Twitter")
                else:
			print("[-] " + user + " => NotFound in YouTube")
                else:
			print("[-] " + user + " => NotFound in Tiktok")
               else:
			print("[-] " + user + " => NotFound in Github")

                else:
			print("[-] " + number + " => NotFound in whatsapp")

x = GCI
x.banner()
x.main()
