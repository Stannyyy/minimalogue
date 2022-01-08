# -*- coding: utf-8 -*-
'Spyder Editor'

def receive_gmail_by_subject_lifenode1994 (Keyword_subjects):

    #import packages
    import email
    import imaplib
    
    #email login info
    EMAIL = 'lifenode1994@gmail.com'
    PASSWORD = '3uqh13@N'
    SERVER = 'imap.gmail.com'
    
    #connect to server and inbox
    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(EMAIL,PASSWORD)
    
    # select the mail folder to search
    
    mail.select('inbox')
    
    #use "ALL" argument to retrieve every message in thee inbox
    
    # it will return it's status and a list of ids
    
    status, data = mail.search(None, 'All')
    
    # the data returned is a list of bytes separated by 
    #white spaces in this format" [b '1 2,3' , b '4 5 6']
    # so , to separate we create an empty list
    
    mail_ids = []
    
    #create an empty list to which you will add all the relevant email payloads
    collected_email = []
    
    # then we split each block of bytes and append it to the mail ids list
    
    for block in data:
        #split function called without a parameter
        # transforms the text or bytes into a list using
        # using the spaces between numbers to indicate a new item
        # b'1 2 3'.split() => [b '1', b '2', b '3']
        mail_ids += block.split()
        
    #fetch the email associated with the ids from above
    # also define format that you want to receive the mail in
    
    for i in mail_ids:
        #the fetch function fetches the email given it's id
        
        status, data = mail.fetch(i, '(RFC822)')
        
        #the '(RFC882)' format is a list with 
        # a tuple, containing (header,content,closing)
        
        for response_part in data:
            # check if it is a tuple before decomposing it
            
            if isinstance(response_part, tuple):
                # we are going to slice the content of the email to find if it contains
                # the name of one of our minimalouge lists 
                #not certain why we go fo the content and not the header, don't know what would happen
                # if header was chosen instead
                
                message = email.message_from_bytes(response_part[1])
                
                # from here we extract info such as who it is from and the subject
                
               # mail_from = message ['from']
                mail_subject = message['subject']
                
                #isolate the emails that have your desired subject keyword 
                if Keyword_subjects in mail_subject:
                    
                
                    # in case the email is not in plain text we want to separate
                    # the plain text from the rest of the email
                
                    if message.is_multipart():
                        mail_content = ''
                    
                    
                        # on multipart we loop through the mail payload appending the plain text to
                        # our Mail content
                        
                        for part in message.get_payload():
                            
                            # when content is plain text we extract it
                            
                            if part.get_content_type() == 'text/plain':
                                mail_content += part.get_payload()
                                
                                
                    else:
                        #if email is not multipart, just extract it
                        mail_content = message.get_payload()
                        
                   #add the email payload to the list if it has a Keyword subject
                   
                    collected_email += mail_content
                    
    return collected_email
                        
                        
  
                    