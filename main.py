# OSINT By FajarTheGGman For Google Code-in 2019©

import urllib3 as url

class GCI:
	def banner():
		print("[---- OSINT By FajarTheGGman ----]\n")

	def main():
		user = str(input("[!] Input Name Victim ? "))
		init = url.PoolManager()
		a = init.request("GET", "https://facebook.com/" + user)
		b = init.request("GET", "https://instagram.com/" + user)
		c = init.request("GET", "https://twitter.com/" + user)
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

x = GCI
x.banner()
x.main()