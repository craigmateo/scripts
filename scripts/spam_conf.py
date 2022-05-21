# Reads file and calculates spam confidence. 

fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.rstrip()
    line = line.strip("X-DSPAM-Confidence: ")
    number = float(line)
    count = count + 1
    total = total + number
    avg = total/count
print "Average spam confidence:",avg