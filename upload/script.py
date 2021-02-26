
def openImage(imageName):
    print(imageName)

def programFPGA(file):
	import os
	os.system('djtgcfg prog -d Basys3 -i 1 -f bit')