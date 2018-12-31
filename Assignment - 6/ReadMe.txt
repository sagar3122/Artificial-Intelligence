Name: Sagar Sharma
UTA Id: 1001626958

Common to all problems of Towers of Hanoi:

The Actions and arguments are common for all the problems of Towers of Hanoi domain.

(disk1 Disk)
(disk2 Disk)
(disk3 Disk)
(disk4 Disk)
(disk5 Disk)
(A Peg)
(B Peg)
(C Peg)

(preconds
  (larger disk2 disk1) (larger disk3 disk1) (larger disk4 disk1) (larger disk5 disk1) (larger disk3 disk2) (larger disk4 disk2) (larger disk5 disk2) (larger disk4 disk3) (larger disk5 disk3) (larger disk5 disk4)



Common to all problems of 7puzzle: 

The Actions and arguments are common for all the problems of 7puzzle domain.

(tile1 Tile)
(tile2 Tile)
(tile3 Tile)
(tile4 Tile)
(tile5 Tile)
(tile6 Tile)
(tile7 Tile)
(pos1 Position)
(pos2 Position)
(pos3 Position)
(pos4 Position)
(pos5 Position)
(pos6 Position)
(pos7 Position)
(pos8 Position)
(pos9 Position)

(preconds
 (adjacent pos1 pos2) (adjacent pos1 pos4) (adjacent pos2 pos1) (adjacent pos2 pos3) (adjacent pos2 pos5) (adjacent pos3 pos2) (adjacent pos3 pos6)
 (adjacent pos4 pos1) (adjacent pos4 pos5) (adjacent pos4 pos7) (adjacent pos5 pos2) (adjacent pos5 pos4) (adjacent pos5 pos6) (adjacent pos5 pos8) (adjacent pos6 pos3) (adjacent pos6 pos5) (adjacent pos6 pos9)
 (adjacent pos7 pos4) (adjacent pos7 pos8) (adjacent pos8 pos5) (adjacent pos8 pos7) (adjacent pos8 pos9) (adjacent pos9 pos6) (adjacent pos9 pos8)

