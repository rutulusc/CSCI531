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

		#Rerun the function again and agian untill root hash is calculated
		if len(listTrans) !=1:
			self.listTrans=tempTrans
			self.pastTrans=pastTrans
			self.createMerkle()

	def getPTrans(self):
		return self.pastTrans


	# def getRoot(self):
	# 	key=self.pastTrans.keys()[-1]
	# 	return self.pastTrans[key]


if __name__=="__main__":

	# names=[alice, bob, carlol, david]
	tree=merkleTree()
	tree.listTrans=sys.argv[1].split(',')
	tree.createMerkle()
	pastTrans=tree.getPTrans()

	print(sys.argv[1])
	print("----------------------------")
	# print(tree.getRoot())
	print(json.dumps(pastTrans,indent=1))
	# print(type(pastTrans))
	print("-----------------------------")










