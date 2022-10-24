import smtplib

HOST = "smtp.gmail.com"
SUBJECT = "testing"
TO = "samir.rafid@farukmedicalcity.com"
FROM = "samer.rafid@gmail.com"
TEXT = "Samer Rafid Saleem"
BODY = "\r\n".join((
    f"From: {FROM}",
    f"To: {TO}",
    f"Subject: {SUBJECT}",
    "",
    TEXT)
)
server = smtplib.SMTP('HOST:587')
server.ehlo()
server.starttls()
server.sendmail(FROM, [TO], BODY)
server.quit()

