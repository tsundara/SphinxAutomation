import os.path

def readfile():
	currdir = os.getcwd()
	tempfile = currdir + "\\" + "template.txt"
	input = open(tempfile,"r")
	data = input.read()
	return data

def createfiles():
	topicfile = open("topics.txt", "r")
	lines = topicfile.readlines()
	for topicname in lines:
		topicnamenew=topicname.rstrip('\n')
		newfilename = str(lines.index(topicname)).zfill(2) + "_" + topicnamenew + ".rst"
		newfilename_nospaces=newfilename.replace(' ','')
		print "Creating File :" + newfilename_nospaces
		target = open(newfilename_nospaces,"w")
		target.truncate()
		target.write(topicname)
		target.write("===========================\n")
		target.write(readfile())
		target.close()
		
			
		
		
createfiles()


