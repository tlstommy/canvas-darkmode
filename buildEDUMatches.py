#https://github.com/nickdenardis/edu-inventory/blob/master/edu-list.txt
#quick and dirty way to build possible canvas urls

inFile = open("in.txt","r")

inLines = inFile.readlines()
inFile.close()
print(len(inLines))

outfile = open("out.txt","a")

for line in inLines:
    print(f"https://canvas.{line.strip()}/*")

    formattedString = '"https://canvas.'+line.strip()+'/*",\n'

    outfile.write(formattedString)
outfile.close()