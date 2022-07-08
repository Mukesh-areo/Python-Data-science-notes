'''
# Company: iNeuron.ai
# Author: Sunny Bhaveen Chandra
# Contact: support@ineuron.ai
# dated: Aug, 13th, 2020
'''

import os
from sendDetailedEmail.email import MailAttachment

def sendMail(clientEmail):
    try:
        # send mail to the user 
        # d is a temp var can be used for debuging 
        d = MailAttachment(clientEmail=clientEmail).send()

    except Exception as e:
        raise e


if __name__ == "__main__":
    # clientEmail = input("input a valid client email ID: ")
    clientEmail = 'CLIENT_EMAIL@gmail.com'
    sendMail(clientEmail)