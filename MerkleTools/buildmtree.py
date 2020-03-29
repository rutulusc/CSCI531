#! /usr/bin/python3
import sys
import json
import collections
import hashlib

class merkleTree:
	
	def __init__(self,listTrans=None):
		self.listTrans=listTrans
		self.pastTrans=collections.OrderedDict()

	def createMerkle(self):
		listTrans=self.listTrans
		pastTrans=self.pastTrans
		tempTrans=[]

		for i in range(0,len(listTrans),2):
			currTrans=listTrans[i]
			currHash=hashlib.sha256(currTrans.encode('utf-8'))
			pastTrans[listTrans[i]]=currHash.hexdigest()

			if i+1 !=len(listTrans):
				currRight=listTrans[i+1]
				currRighthash=hashlib.sha256(currRight.encode('utf-8'))
				pastTrans[listTrans[i+1]]=currRighthash.hexdigest()
				tempTrans.append(currHash.hexdigest() + currRighthash.hexdigest())

			else:
				currRight=''
				tempTrans.append(currHash.hexdigest())

		#Recursive calls until root hash is obtained
		if len(listTrans) !=1:
			self.listTrans=tempTrans
			self.pastTrans=pastTrans
			self.createMerkle()

	def getPTrans(self):
		return self.pastTrans


if __name__=="__main__":

	# print(sys.executable)
	# names=['alice', 'bob', 'carlol', 'david']
	tree=merkleTree()
	# tree.listTrans=names
	tree.listTrans=sys.argv[1].split(',')
	tree.createMerkle()
	pastTrans=tree.getPTrans()

	with open('merkle.tree', 'w') as f:
		f.write(json.dumps(pastTrans))

	# print(sys.argv[1])
	# print(json.dumps(pastTrans,indent=1))
	# print(type(pastTrans))

	with open('merkle.tree', 'r') as read_file:
		loaded_dictionaries = json.loads(read_file.read(),object_pairs_hook=collections.OrderedDict)
		# print(loaded_dictionaries['alice'])
		# print(type(loaded_dictionaries))
		print("Hashes are printed from bottom to top in sequence.")
		print("The last one is the root hash. \n")
		for i in loaded_dictionaries:
			print ("Hash: "+ loaded_dictionaries[i])
