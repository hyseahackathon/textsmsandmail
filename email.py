import smtplib 
  
# list of email_id to send the mail 
li = ["niharikajaincs@gmail.com", "kajaljaiswal24@gmail.com"] 
  
for i in range(len(li)): 
    try:
        s = smtplib.SMTP_SSL('smtp.gmail.com', 587) 
        # s.ehlo()
        s.starttls() 
        s.login("aiswaryapai.mec@gmail.com", "allu@1996") 
        message = "hello thanku :*"
        s.sendmail("aiswaryapai.mec@gmail.com", li[i], message) 
        s.quit() 
    except:
        print("test")