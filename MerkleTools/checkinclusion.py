#! /usr/bin/python3
import sys
import json
import collections
import hashlib

# validation function for 4 leafs in merkle tree
def validation(testHash, hashes, rootHash,i,j):
	if(j==5):
		if(i==1):
			temp=testHash+hashes[i]
		elif(i==0):
			temp=hashes[i]+testHash
		tempHash=hashlib.sha256(temp.encode('utf-8')).hexdigest()
		temp=tempHash+hashes[j]
		tempHash=hashlib.sha256(temp.encode('utf-8')).hexdigest()
		return tempHash==rootHash
	elif(j==4):
		if(i==3):
			temp=testHash+hashes[i]
		elif(i==2):
			temp=hashes[i]+testHash
		tempHash=hashlib.sha256(temp.encode('utf-8')).hexdigest()
		temp=hashes[j]+tempHash
		tempHash=hashlib.sha256(temp.encode('utf-8')).hexdigest()
		return tempHash==rootHash
	else:
		return False


if __name__=="__main__":

	hashes=[]
	with open('merkle.tree', 'r') as read_file:
		loaded_dictionaries = json.loads(read_file.read(),object_pairs_hook=collections.OrderedDict)
		for i in loaded_dictionaries:
			hashes.append(loaded_dictionaries[i])
			# print merkle tree hashes from previous transactions
			#print (" Hash:"+ loaded_dictionaries[i])

	# test='david'
	test=sys.argv[1]
	testHash=hashlib.sha256(test.encode('utf-8')).hexdigest()
	print("Test String Hash: " + testHash)
	print("Checking inclusion..........")

	if(validation(testHash, hashes, hashes[6], 1, 5)==True):
		print("yes ")
		print("Hash " + hashes[1])
		print("Hash " + hashes[5])
		print("Old Root Hash " +hashes[6])
	elif(validation(testHash, hashes, hashes[6], 0, 5)==True):
		print("yes ")
		print("Hash " + hashes[0])
		print("Hash " + hashes[5])
		print("Old Root Hash " +hashes[6])
	elif(validation(testHash, hashes, hashes[6], 3, 4)==True):
		print("yes ")
		print("Hash " + hashes[3])
		print("Hash " + hashes[4])
		print("Old Root Hash " +hashes[6])
	elif(validation(testHash, hashes, hashes[6], 2, 4)==True):
		print("yes ")
		print("Hash " + hashes[2])
		print("Hash " + hashes[4])
		print("Old Root Hash " +hashes[6])
	else:
		print("no ")