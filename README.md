# CSCI531
Applied Cryptography

# MerkleTools

## Overview
Merkle Hash Tree is a simple binary tree consisting of hashed leaves and nodes. Leaves are the hashes of individual nodes that have been appended to the next node. Nodes are the hashes of paired child leaves or paired child nodes. The root hash, from which all nodes and leaves stem, is known as the merkle tree hash.

          ROOT=Hash(E+F)        
          /       \          
         /         \       
  E=Hash(A+B)    F=Hash(C+D)    
   /     \        /     \       
  /       \      /       \       
 A         B    C         D       

*Note that A, B, C, D are the hashes of the individual transactions
