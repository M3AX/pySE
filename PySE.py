#!/usr/bin/env python
import os
import sys
import time
import smtplib, sys, time, urllib2, io, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sys import platform
try:
    import google
    from google import search
    import pythonwhois
    import mechanize
    import requests
except ImportError as e:
    print "Error: {}".format(e)


installed1 = open("other/installed.txt", 'r')
if installed1 == "no":
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system("sudo su")
        os.system("easy_install pip")
        os.system("pip install requests")
        os.system("pip install google")
        os.system("pip install flask")
        os.system("pip install pythonwhois")
        os.system("pip install mechanize")
        os.system("curl -O https://bootstrap.pypa.io/get-pip.py")
        os.system("sudo python get-pip.py")
        installed = open("other/installed.txt", 'w')
        installed.write("yes")
        installed.close()
        os.system("clear")
    elif platform == "win32":
        print """Copy all the text from https://bootstrap.pypa.io/get-pip.py and save it into a .py file. From there just run it and when your done hit <enter>
        """
        raw_input("<enter when your done>")
        os.system("python -m pip install flask")
        os.system("python -m pip install google")
        os.system("python -m pip install requests")
        os.system("python -m pip install pythonwhois")
        os.system("python -m pip install mechanize")
        installed = open("other/installed.txt", 'w')
        installed.write("yes")
        installed.close()
        os.system("cls")
    elif platform == "android":
        os.system("pip install -r requirements.txt")
        installed = open("other/installed.txt", 'w')
        installed.write("yes")
        installed.close()
    else:
        print ""
else:
    print ""

banner = """
______      _____ _____ 
| ___ \    /  ___|  ___|
| |_/ /   _\ `--.| |__  
|  __/ | | |`--. \  __| 
| |  | |_| /\__/ / |___ 
\_|   \__, \____/\____/ 
       __/ |            
      |___/             

 -- Made by @_t0x1c aka Filip --                                                            
"""
options = """
1) Send email
2) Credential Harvester
3) Send HTML email
4) Send mass email
5) Clone website's source
6) Help and Advice
7) Search google for a query
8) Find info on a website
9) Send anonymous email
"""
while True:
    print banner + options 
    main = raw_input("PySE>")
    if main == "1":
        htmltext = raw_input("\n[?] Html or Text: ")
        if htmltext == "text":
            message = raw_input("[?] Message: ")
            html = message
        else:
            htmlfile = raw_input("\n[?] Html File: ")
            with open(htmlfile) as f:
                lines = f.readlines()
            html = ''.join(lines)
        subject = raw_input("[?] Subject: ")
        fromwho = raw_input("[?] Your email: ")
        towho = raw_input("[?] To email: ")
        password = raw_input("[?] Your password: ")
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = fromwho
        msg['To'] = towho
        part2 = MIMEText(html, 'html')
        msg.attach(part2)
        try:
            print "[+] Attempting to connect to server"
            s = smtplib.SMTP("smtp.gmail.com", 587)
            print "[+] Attempting to use STARTTLS"
            s.starttls()
            s.login(fromwho, password)
            print "[+] Attempting to send email"
            s.sendmail(fromwho, towho, msg.as_string())
            print "[+] Done!"
            s.quit()
        except:
            print "Error"
    elif main == "2":
        if platform == "linux" or platform == "linux2" or platform == "darwin":
            os.system("sudo python PhishingFlask.py")
        elif platform == "win32":
            os.system("PhishingFlask.py")
        elif platform == "android":
            os.system("python2 PhishingFlask.py")
        else:
            print ""
    elif main == "3":
        htmlfile = raw_input("\n[?] Html File: ")
        subject = raw_input("[?] Subject: ")
        fromwho = raw_input("[?] Your email: ")
        towho = raw_input("[?] To email: ")
        password = raw_input("[?] Your password: ")
        with open(htmlfile) as f:
            lines = f.readlines()
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = fromwho
        msg['To'] = towho
        html = ''.join(lines)
        part2 = MIMEText(html, 'html')
        msg.attach(part2)
        try:
            print "[+] Attempting to connect to server"
            s = smtplib.SMTP("smtp.gmail.com", 587)
            print "[+] Attempting to use STARTTLS"
            s.starttls()
            s.login(fromwho, password)
            print "[+] Attempting to send email"
            s.sendmail(fromwho, towho, msg.as_string())
            print "[+] Done!"
            s.quit()
        except:
            print "Error"
    elif main == "4":
        emailfile = raw_input('[?] Text file with all the emails: ')
        emailtosendfrom = raw_input('[?] Your email:  ')
        msgfile = raw_input('[?] Text file with message: ')
        subject = raw_input('[?] Subject: ')
        email = open(emailfile, 'r')
        toaddrs = email
        with open(msgfile) as msg:
            msgbody = 'Subject: {}\n\n{}'.format(subject, msg.read())

        password = raw_input('[?] Your email password: ')
        print "[+] Attempting to connect to server"
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        print "[+] Attempting to use STARTTLS"
        server.starttls()
        server.login(emailtosendfrom,password)
        print "[+] Attempting to send email"
        with open(emailfile) as f:
            emailsort = f.readlines()
            for user in emailsort:
                server.sendmail(emailtosendfrom, user, msgbody)
        print "[+] Done!"
        f.close()
        server.quit()
    elif main == "5":
        print ('Remember to put https:// in front of the website!')
        hey = raw_input('[?] Website: ')
        response = urllib2.urlopen(hey)
        page_source = response.read()

        with io.FileIO("websitesource.html", "w") as file:
            file.write(page_source)
        print ('[+] Finished!')
    elif main == "6":
        print "-- STUFF --"
        print """
1. Going to update pySE a lot
2. Contact me at toxicnull@gmail.com or @_t0x1c on IG for requests, bugs or feedback
3. Make sure you have "Less secure apps" turned on in gmail
4. Right now only Gmail is available
"""
        time.sleep(3)
        raw_input("<enter>")
        print "-- ADVICE --"
        print """
1. Always test before you attack
2. Get info on your target first before you attack him/her and make sure you understand how they react and more.
3. Make your attack look realistic
"""
        time.sleep(3)
        raw_input("<enter>")
    elif main == "7":
        lol = raw_input("[?] Query: ")
        for url in search(lol, tld='com', lang='es', stop=50):
            print("Site: " + url)

    elif main == "8":
        print('Example - example.com')
        h = raw_input('[?] Website: ')
        domains = [h]
        for dom in domains:
            details = pythonwhois.get_whois(dom)
            print details['contacts']['registrant']
    elif main == "9":
        br = mechanize.Browser()

        to = raw_input("[?] Enter the recipient address: ")
        subject = raw_input("[?] Subject: ")
        print "[?] Message: "
        message = raw_input(">")
        # If you have a proxy edit this and un-comment it
        #proxy = "http://127.0.0.1:8080"
        url = "http://anonymouse.org/anonemail.html"
        headers = "Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)"
        br.addheaders = [('User-agent', headers)]
        br.open(url)
        br.set_handle_equiv(True)
        br.set_handle_gzip(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.set_debug_http(False)
        br.set_debug_redirects(False)
        # Uncomment this too
        #br.set_proxies({"http": proxy})
        br.select_form(nr=0)
        br.form['to'] = to
        br.form['subject'] = subject
        br.form['text'] = message
        result = br.submit()
        response = br.response().read()


        if "The e-mail has been sent anonymously!" in response:
            print "The email has been sent successfully! \n The recipient will get it in up to 12 hours!"
        else:
            print "Failed to send email!"

    else:
        print "That is not an option! :/"
