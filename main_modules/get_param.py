import argparse

def createParser ():
	parser = argparse.ArgumentParser()
	parser.add_argument ('-injs','--injstring', default=-1)
	return parser