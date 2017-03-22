import smtplib
import imaplib
import email

org_email = "@gmail.com"
smtp_server = "imap.gmail.com"
smtp_port = 993


def readmail():
    username = raw_input("Enter username : ")
    password = raw_input("Enter password : ")

    mail = imaplib.IMAP4_SSL(smtp_server)

    mail.login(username, password)
    mail.select('inbox')

    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()

    first_id = int(id_list[0])
    last_id = int(id_list[-1])

    # print first_id
    # print last_id

    for i in range(last_id, first_id, -1):
        typ, data = mail.fetch(i, '(RFC822)')

        for response in data:
            if isinstance(response, tuple):
                msg = email.message_from_string(response[1])
                email_subject = msg['subject']
                email_from = msg['from']
                print 'From : ' + email_from + '\n'
                print 'Subject : ' + email_subject + '\n'


readmail()