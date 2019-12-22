#!/usr/bin/python3
#code by: Mr.Đ`HACK
#code date:22/12/2019

##########################################################
#                    import module                       #
##########################################################
import os
import re
import sys
##########################################################
#                  kesalahan module                      #
##########################################################
try:
        import requests
except ImportError:


        print ("[!] Kesalahan!")
        print ("[!] Anda Belum Menginstall 'requests'\n")
        print ("[+] Type 'pip2 install requests' to installing")

##########################################################
#                        banner                          #
##########################################################
print ('\033[32;1m')
banner = """

                |\___/|
                | sms |
               <Gratiss>
                \[ | ]/
             {Tanpa pulsa}
          {Code By Mr.D'HACK'}
          <--------X--------->
"""
##########################################################
#                      proses.....                       #
##########################################################
os.system('clear')
print (banner)


from requests import Session
s = Session()

try:             
	print(" * TOOLS SEND SMS GRATIS TANPA PULSA *\n* MASUKAN NO DENGAN (62/0) TANPA (+62) *\n")
	no = int(input("[+] Nomor: "))
	msg = input("[+] Pesan: ")
except:
	print("\n\t* [-] KESALAHAN! * \n")
	sys.exit()

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
    'Referer': 'http://sms.payuterus.biz/alpha/'
}

bypass = s.get("http://sms.payuterus.biz/alpha/?a=keluar", headers=headers).text
key = re.findall(r'value="(\d+)"', bypass)[0]           
jml = re.findall(r'<span>(.*?) = </span>', bypass)[0]  
captcha = eval(jml.replace("x", "*").replace(":", "/"))

data = {
	'nohp':no,
	'pesan':msg,
	'captcha':captcha,
	'key':key
}

send = s.post("http://sms.payuterus.biz/alpha/send.php", headers=headers, data=data).text

if '[+] SMS TELAH DI KIRIM!' in send:
	print(f"\n  [ Pengiriman sukses ]\n  [ {no} : {msg} ]\n")
elif '[+] MAAF....!' in send:
	print("\n  [ Mohon tunggu 15 menit untuk mengirim pesan yg sama ]\n")
else:
	print("\n  [-] PENGIRIMAN GAGAL! \n[ Silahkan cek no yang anda Masukan\natau sinyal anda lemah! ]\n")
############################################################################
#                          SENOGA BERGUNA                                  #
############################################################################
