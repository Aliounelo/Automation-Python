import getpass

import email
import imaplib

import os

import mailfunc as mf


host = 'outlook.live.com' 
username = ''
password = getpass.getpass()

#-- Output directory
outputDir = os.getcwd() + '/mailTest'
inbox = 'INBOX/'

with mf.connect_to_inbox(host,username,password) as conn :
    conn = mf.switch_inbox(conn, inbox)

    mailids = mf.get_emailids_inbox(conn)
    #print(sorted(str(mailids), reverse=True))

    for ii in mailids : 
        mailbody = mf.get_emailbody(conn, ii)
	
	#-- From receiver 
        print(mailbody['From '])

        mf.download_attachments_email(mailbody, outputDir)


