#https://github.com/nickdenardis/edu-inventory/blob/master/edu-list.txt
#quick and dirty way to build possible canvas urls

import requests,time

inFile = open("in.txt","r")

inLines = inFile.readlines()
inFile.close()
print(len(inLines))

outfile = open("out.txt","a")

for line in inLines:

    #print(line)

    try:
        url = requests.get(line)
        print(line)
        print(url.status_code)
        formattedString = '"https://canvas.'+line.strip()+'/*",\n'

        outfile.write(formattedString)
    except:
        continue
outfile.close()