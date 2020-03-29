# CSCI531
Applied Cryptography

# MerkleTools

## Overview
Merkle Hash Tree is a simple binary tree consisting of hashed leaves and nodes. Leaves are the hashes of individual nodes that have been appended to the next node. Nodes are the hashes of paired child leaves or paired child nodes. The root hash, from which all nodes and leaves stem, is known as the merkle tree hash.

## Tree Generation Samples

         ROOT=Hash(E+F)        
          /       \          
         /         \       
     E=Hash(A+B)    F=Hash(C+D)    
       /     \        /     \       
      /       \      /       \       
     A         B    C         D       
  
*Note that A, B, C, D are the hashes of the individual transactions


		  ROOT=Hash(I+J)
                  /        \
                 /          \
          I=Hash(F+G)        J=Hash(H)
          /       \           \
         /         \           \
    F=Hash(A+B)    G=Hash(C+D)    H=Hash(E)
       /     \        /     \        \
      /       \      /       \        \
     A         B    C         D        E
 
*Note that A, B, C, D, E are the hashes of the individual transactions

## Commands and Usage

Merkle tree transaction validation is the missing node hashes required to compute all the nodes between the leaf and the tree root. If the root hash you compute from the audit path matches the currently advertised merkle tree root hash, then the leaf exists in the tree. The consistency proof lets you verify that any two versions of a tree are consistent: that is, the later version includes everything in the earlier version, in the same order, and all new entries come after the entries in the older version.


```
./buildmtree.py alice,bob,carlol,david
cat merkle.tree
./checkinclusion.py richard
./checkinclusion.py david
./checkconsistency.py alice,bob,carlol,david alice,bob,carlol,david,eve,fred
cat merkle.trees
./checkconsistency.py alice,bob,carlol,david alice,bob,carol,eve,fred,davis
cat merkle.trees
```


