#! /usr/bin/python3
import sys
import json
import collections
import hashlib
from buildmtree import merkleTree

def consistency(newHashes,oldRoot,newRoot):
	num=len(newHashes)-2
	temp=oldRoot+newHashes[num]
	tempHash=hashlib.sha256(temp.encode('utf-8')).hexdigest()
	return tempHash==newRoot

if __name__=="__main__":
	oldHashes=[]
	newHashes=[]
	# names=['alice', 'bob', 'carlol', 'david']
	# names2=['alice', 'bob', 'carlol', 'david', 'eve', 'fred']
	# names2=['alice', 'bob', 'carlol', 'rutul', 'fred','charlie','monitor']

	#Old MTree
	tree=merkleTree()
	# tree.listTrans=names
	tree.listTrans=sys.argv[1].split(',')
	tree.createMerkle()
	pastTrans=tree.getPTrans()

	#New MTree
	tree2=merkleTree()
	# tree2.listTrans=names2
	tree2.listTrans=sys.argv[2].split(',')
	tree2.createMerkle()
	pastTrans2=tree2.getPTrans()

	with open('merkle.trees', 'w') as f:
		data=[pastTrans, pastTrans2]
		f.write(json.dumps(data))

	# print(sys.argv[1])
	# print(json.dumps(pastTrans,indent=1))
	# print(type(pastTrans))

	with open('merkle.trees', 'r') as read_file:
		loaded_dictionaries = json.loads(read_file.read(),object_pairs_hook=collections.OrderedDict)
		# print(loaded_dictionaries['alice'])
		# print(type(loaded_dictionaries))
		print("Older version merkle tree")
		for i in loaded_dictionaries[0]:
			oldHashes.append(loaded_dictionaries[0][i])
			print ("Hash: "+ loaded_dictionaries[0][i])

		print("New version merkle tree")
		for i in loaded_dictionaries[1]:
			newHashes.append(loaded_dictionaries[1][i])
			print ("Hash: "+ loaded_dictionaries[1][i])

	oldnum=len(oldHashes)-1
	num=len(newHashes)-1
	# print(consistency(newHashes,oldHashes[oldnum],newHashes[num]))

	if(consistency(newHashes,oldHashes[oldnum],newHashes[num])==True):
		print("yes ")
		print("Hash " + oldHashes[oldnum])
		print("Hash "+ newHashes[num-1])
		print("Hash " + newHashes[num])
	else:
		print("no ")