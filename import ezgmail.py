import ezgmail


email = 'samer.rafid@gmail.com'
subject = 'EZGmail Test'
text = 'This is the body of the mail.'
ezgmail.send(email, subject, text)

