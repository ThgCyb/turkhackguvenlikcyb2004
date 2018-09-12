import os

def menu():

    print(""" 
###########################################################################

 BU SCRİPT 
 WWW.TURKHACKGUVENLİK.COM'DAN Cyb2004
 TARAFINDAN KODLANMIŞTIR 
 EDİTLENMESİ KESİNLİKLE YASAKTİR
 
AKSİ HALDE OLACAKLARDAN BEN SORUMLU DEYİLİM





###########################################################################
Olusturan Kisi: Cyb2004
Web Site: www.turkhackguvenlik.com
Web Site Kullan?c? Ad?: Cyb2004
Facebook: facebook.com/BySusmaz
Version: v1
----
Sadece Termux İcin! 
----
==========================================
00. Termuxunuzu Bir Canavara Donusturun. 
------------------------------------------
1. Nmap Yukle
2. Hydra Yukle
3. SQLMap Yukle
4. Metasploit Yukle
5. ngrok Yukle
6. Kali Nethunter Yukle
7. angryFuzzer Yukle
8. Red_Hawk Yukle
9. Weeman Yukle
10.IPGeoLocation Yukle
11.Cupp Yukle
12. Instagram Bruteforcer (instahack)
13. Twitter Bruteforcer   (TwitterSniper)
14. Ubuntu Yukle
15. Fedora Yukle
16. viSQL Yukle
17. Hash-Buster Yukle
18. D-TECT Yukle
19. routersploit Yukle
------------------------------------------
99. C?K?S
==========================================
""")

loop = True

while loop:
    menu()
    what = input("#: ")
    if what == "00":
        print("================================")
        print("Yuklenecekler: nmap, hydra, sqlmap, metasploit, ngrok, angryFuzzer, red_hawk, weeman, IPGeoLocation, cupp, instahack, TwitterSniper, Hash-Buster, D-TECT, routersploit Ve Tek Tiklamayla viSQL")
        print("----------------")
        hm = input("[?] Devam Edilsin Mi? (y/n): ")
        print("================================")
        if hm == "y":
            print("========================================================")
            print("[+] Biraz Uyuya Bilirsin... ")
            print("Cunku Bu Baya Uzun Surecek... ")
            print("========================================================")
            os.system("pkg update")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y python2")
            os.system("pkg install -y wget")
            os.sysetm("pkg install -y nmap")
            os.system("plg install -y hydra ")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg install wget")
            os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
            os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
            os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
            os.system("cd /data/data/com.termux/files/home && bundle install")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
            os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
            os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home && pip2 install requests")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y php")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y python2")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
            os.system("cd /data/data/com.termux/files/home && cd weeman")
            os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
            os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
            os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y nano")
            os.system("pip install requests")
            os.system("pip install beautifulsoup4")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pip install mechanicalsoup")
            os.system("pkg install -y nano")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            os.system("clear")
            print("========================================")
            print("[+] everything Basariyla Yuklendi :)")
            print("[+] Mutlu Hacking <3")
            print("========================================")
        else:
            rmenu = input("[?] Menuye Donecekmisiniz?  (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
    if what == "1":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y nmap")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] nmap Basariyla Yuklendi:)")
        print("[+] Type 'nmap' Yazarak Calistirin.")
        print("====================================")
        rmenu = input("[?] Menuye Donecekmisiniz?  (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "2":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y hydra")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] hydra Basariyla Yuklendi:)")
        print("[+] Type 'hydra' Yazarak Calistirin.")
        print("====================================")
        rmenu = input("[?] Menuye Donecekmisiniz?  (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "3":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] SQLMap Basariyla Yuklendi:)")
        print("[+]  sqlmap Dosyasina Gidin Ve 'python2 sqlmap.py' Yazarak Calistirin.")
        print("====================================")
        rmenu = input("[?] Menuye Donecekmisiniz?  (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "4":
        os.system("pkg install -y wget")
        os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
        os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
        os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
        os.system("cd /data/data/com.termux/files/home && bundle install")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Metasploit Basariyla Yuklendi:)")
        print("[+] Type 'msfconsole' Yazarak Calistirin.")
        print("====================================")
        rmenu = input("[?] Menuye Donecekmisiniz?  (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "5":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] ngrok Basariyla Yuklendi:)")
        print("[+]  ngrok Dosyasina Gidin Ve './ngrok http 80' Yazarak Calistin")
        print("====================================")
        rmenu = input("[?] Menuye Donecekmisiniz?  (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "6":
        os.system("pkg update -y")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Nethunter-In-Termux.git")
        os.system("cd /data/data/com.termux/files/home && cd Nethunter-In-Termux && chmod +x kalinethunter")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Nethunter Basariyla Yuklendi:)")
        print("[+]  Nethunter-In-Termux Dosyasina Gidin Ve './kalinethunter' Yazarak Calistirin.")
        print("====================================")
        rmenu = input("[?] Menuye Donecekmisiniz?  (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "7":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
        os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
        os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home && pip2 install requests")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] angryFuzzer Basariyla Yuklendi:)")
        print("[+]  angryFuzzer Dosyasina Gidin Ve 'python2 angryFuzzer.py' Yazarak Calistirin.")
        print("====================================")
        rmenu = input("[?] Menuye Donecekmisiniz?  (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "8":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y php")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] RED_HAWK Basariyla Yuklendi:)")
        print("[+]  RED_HAWK Dosyasina Gidin Ve 'php rhawk.php' Yazarak Calistirin")
        print("====================================")
        rmenu = input("[?] Menuye Donecekmisiniz?  (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "9":
        os.system("pkg update -y")
        os.system("pkg install -y python2")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
        os.system("cd /data/data/com.termux/files/home && cd weeman")
        os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] weeman Basariyla Yuklendi:)")
        print("[+]  weeman Dosyasina Gidin Ve 'python2 weeman.py' Yazarak Calistirin")
        print("====================================")
        rmenu = input("[?] Menuye Donecekmisiniz?  (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "10":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
        os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
        os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] IPGeoLocation Basariyla Yuklendi:)")
        print("[+]  IPGeoLocation Dosyasina Gidin Ve 'python ipgeolocation.py' Yazarak Calistirin.")
        print("====================================")
        rmenu = input("[?] Menuye Donecekmisiniz?  (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "11":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
        print("====================================")
        print("[+] Cupp Basariyla Yuklendi:)")
        print("[+]  cupp Dosyasina Gidin Ve 'python cupp3.py' Yazarak Calistirin")
        print("====================================")
        rmenu = input("[?] Menuye Donecekmisiniz?  (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "12":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pkg install -y nano")
        os.system("pip install requests")
        os.system("pip install beautifulsoup4")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
        print("====================================")
        print("[+] Instahack Basariyla Yuklendi:)")
        print("[+]  instahack Dosyasina Gidin Ve 'python hackinsta.py' Yazarak Calistirin.")
        print("====================================")
        rmenu = input("[?] Menuye Donecekmisiniz?  (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "13":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pip install mechanicalsoup")
        os.system("pkg install -y nano")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
        print("====================================")
        print("[+] TwitterSniper Basariyla Yuklendi:)")
        print("[+]  TwitterSniper Dosyasina Gidin Ve 'python TwitterSniper.py' Yazarak Calistirin")
        print("====================================")
        rmenu = input("[?] Menuye Donecekmisiniz?  (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "14":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Neo-Oli/termux-ubuntu.git")
        os.system("cd /data/data/com.termux/files/home && cd termux-ubuntu && bash ubuntu.sh")
        print("====================================")
        print("[+] Ubuntu Basariyla Yuklendi:)")
        print("[+]  termux-ubuntu Dosyasina Gidin Ve './start.sh' Yazarak Calistirin")
        print("====================================")
        rmenu = input("[?] Menuye Donecekmisiniz?  (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "15":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y wget")
        os.system("apt update && apt install wget -y && /data/data/com.termux/files/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh")
        print("====================================")
        print("[+] Fedora Basariyla Yuklendi:)")
        print("[+]  'sh termux-fedora.sh f26_arm64 'veya' sh termux-fedora.sh f26_arm 'ba?l?yor.")
        print("====================================")
        rmenu = input("[?] Menuye Donecekmisiniz?  (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "16":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
        print("====================================")
        print("[+] viSQL Basariyla Yuklendi:)")
        print("[+]  viSQL Dosyasina Gidin Ve 'python2 viSQL.py --help' Yazarak Calistirin")
        print("====================================")
        rmenu = input("[?] Menuye Donecekmisiniz?  (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "17":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
        print("====================================")
        print("[+] Hash-Buster Basariyla Yuklendi:)")
        print("[+]  Hash-Buster Dosyasina Gidin Ve  'python2 hash.py' Yazarak Baslatin.")
        print("====================================")
        rmenu = input("[?] Menuye Doncekmisiniz? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "18":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
        print("====================================")
        print("[+] Hash-Buster Basariyla Yuklendi:)")
        print("[+] Hash-Buster Kalsorune Gidin Ve 'python2 hash.py' Yazarak Baslatin")
        print("====================================")
        rmenu = input("[?] Menuye Doncekmisiniz? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            print("====================================")
            print("[+] routersploit Basariyla Yuklendi :)")
            print("[+] routersploit Klasorune Gidin Ve  'python2 rsf.py' Yazarak Baslatin")
            print("====================================")
            rmenu = input("[?] Menuye Doncekmisiniz? (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
    elif what == "99":
        print("Baybay Görüsmek Uzere....")
        break