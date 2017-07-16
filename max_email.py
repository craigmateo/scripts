# The program reads through the mbox-short.txt and figures out who has the sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)

counts = dict()

for line in handle:
    line = line.strip()
    if not line.startswith('From ') : continue
    words = line.split()
    for word in words:
        if "@" in word:
        	counts[word] = counts.get(word,0) + 1

maxnum = None
email = None
for word,count in counts.items():
    if maxnum is None or count > maxnum:
        email = word
        maxnum = count
        
print email, maxnum