import csv


hostname = input('please enter hostname:')
ip = input('please enter the ip address: ')
location = input('Please enter the location:')

router = [hostname, ip, location]
with open ('testing.csv', 'a') as data:  #testing.csv is an existing file in same folder as the python code.
    csv_writer= csv.writer(data)
    csv_writer.writerow(router)
    