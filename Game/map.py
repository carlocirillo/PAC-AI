from . nodes import node
#DEFINING PIXELS FOR THE GRID

rows = [15,93,151,208,267,324,382,440,497,554]
cols = [12,51,108,167,225,281,340,397,455,494]

a1 = node("A1",cols[0],rows[0])
a2 = node("A2",cols[0],rows[1])
a3 = node("A3",cols[0],rows[2])
a7 = node("A7",cols[0],rows[6])
a8 = node("A8",cols[0],rows[7])
a9 = node("A9",cols[0],rows[8])
a10 = node("A10",cols[0],rows[9])

b8 = node("B8",cols[1],rows[7])
b9 = node("B9",cols[1],rows[8])

c1 = node("C1",cols[2],rows[0])
c2 = node("C2",cols[2],rows[1])
c3 = node("C3",cols[2],rows[2])
c5 = node("C5",cols[2],rows[4])
c7 = node("C7",cols[2],rows[6])
c8 = node("C8",cols[2],rows[7])
c9 = node("C9",cols[2],rows[8])

d2 = node("D2",cols[3],rows[1])
d3 = node("D3",cols[3],rows[2])
d4 = node("D4",cols[3],rows[3])
d5 = node("D5",cols[3],rows[4])
d6 = node("D6",cols[3],rows[5])
d7 = node("D7",cols[3],rows[6])
d8 = node("D8",cols[3],rows[7])
d9 = node("D9",cols[3],rows[8])

e1 = node("E1",cols[4],rows[0])
e2 = node("E2",cols[4],rows[1])
e3 = node("E3",cols[4],rows[2])
e4 = node("E4",cols[4],rows[3])
e7 = node("E7",cols[4],rows[6])
e8 = node("E8",cols[4],rows[7])
e9 = node("E9",cols[4],rows[8])
e10 = node("E10",cols[4],rows[9])

f1 = node("F1",cols[5],rows[0])
f2 = node("F2",cols[5],rows[1])
f3 = node("F3",cols[5],rows[2])
f4 = node("F4",cols[5],rows[3])
f7 = node("F7",cols[5],rows[6])
f8 = node("F8",cols[5],rows[7])
f9 = node("F9",cols[5],rows[8])
f10 = node("F10",cols[5],rows[9])

g2 = node("G2",cols[6],rows[1])
g3 = node("G3",cols[6],rows[2])
g4 = node("G4",cols[6],rows[3])
g5 = node("G5",cols[6],rows[4])
g6 = node("G6",cols[6],rows[5])
g7 = node("G7",cols[6],rows[6])
g8 = node("G8",cols[6],rows[7])
g9 = node("G9",cols[6],rows[8])

h1 = node("H1",cols[7],rows[0])
h2 = node("H2",cols[7],rows[1])
h3 = node("H3",cols[7],rows[2])
h5 = node("H5",cols[7],rows[4])
h7 = node("H7",cols[7],rows[6])
h8 = node("H8",cols[7],rows[7])
h9 = node("H9",cols[7],rows[8])

i8 = node("I8",cols[8],rows[7])
i9 = node("I9",cols[8],rows[8])

j1 = node("J1",cols[9],rows[0])
j2 = node("J2",cols[9],rows[1])
j3 = node("J3",cols[9],rows[2])
j7 = node("J7",cols[9],rows[6])
j8 = node("J8",cols[9],rows[7])
j9 = node("J9",cols[9],rows[8])
j10 = node("J10",cols[9],rows[9])

starting_node = node("start",254,440)

ghosts_starting_node = node("ghosts",254,209)

#********* BLOCCO A **********#
a1.add_right_node(c1)
a1.add_down_node(a2)

a2.add_up_node(a1)
a2.add_right_node(c2)
a2.add_down_node(a3)

a3.add_up_node(a2)
a3.add_right_node(c3)

a7.add_right_node(c7)
a7.add_down_node(a8)

a8.add_up_node(a7)
a8.add_right_node(b8)

a9.add_right_node(b9)
a9.add_down_node(a10)

a10.add_up_node(a9)
a10.add_right_node(e10)

#********* BLOCCO B **********#
b8.add_left_node(a8)
b8.add_down_node(b9)

b9.add_up_node(b8)
b9.add_left_node(a9)
b9.add_right_node(c9)

#********* BLOCCO C **********#
c1.add_left_node(a1)
c1.add_down_node(c2)
c1.add_right_node(e1)

c2.add_up_node(c1)
c2.add_left_node(a2)
c2.add_down_node(c3)
c2.add_right_node(d2)

c3.add_up_node(c2)
c3.add_left_node(a3)
c3.add_down_node(c5)

c5.add_up_node(c3)
c5.add_left_node(h5) 
c5.add_down_node(c7)
c5.add_right_node(d5)

c7.add_up_node(c5)
c7.add_left_node(a7)
c7.add_down_node(c8)
c7.add_right_node(d7)

c8.add_up_node(c7)
c8.add_down_node(c9)
c8.add_right_node(d8)

c9.add_up_node(c8)
c9.add_left_node(b9)

#********* BLOCCO D **********#
d2.add_left_node(c2)
d2.add_down_node(d3)
d2.add_right_node(e2)

d3.add_up_node(d2)
d3.add_right_node(e3)

d4.add_right_node(e4)
d4.add_down_node(d5)

d5.add_up_node(d4)
d5.add_left_node(c5)
d5.add_down_node(d6)

d6.add_up_node(d5)
d6.add_right_node(g6)
d6.add_down_node(d7)

d7.add_up_node(d6)
d7.add_left_node(c7)
d7.add_right_node(e7)

d8.add_left_node(c8)
d8.add_down_node(d9)
d8.add_right_node(e8)

d9.add_up_node(d8)
d9.add_right_node(e9)

#********* BLOCCO E **********#
e1.add_left_node(c1)
e1.add_down_node(e2)

e2.add_up_node(e1)
e2.add_left_node(d2)
e2.add_right_node(f2)

e3.add_left_node(d3)
e3.add_down_node(e4)

e4.add_up_node(e3)
e4.add_left_node(d4)
e4.add_right_node(f4)

e7.add_left_node(d7)
e7.add_down_node(e8)

e8.add_up_node(e7)
e8.add_left_node(d8)
e8.add_right_node(starting_node)

e9.add_left_node(d9)
e9.add_down_node(e10)

e10.add_up_node(e9)
e10.add_left_node(a10)
e10.add_right_node(f10)

#********* BLOCCO F **********#
f1.add_right_node(h1)
f1.add_down_node(f2)

f2.add_up_node(f1)
f2.add_left_node(e2)
f2.add_right_node(g2)

f3.add_right_node(g3)
f3.add_down_node(f4)

f4.add_right_node(g4)
f4.add_up_node(f3)
f4.add_left_node(e4)

f7.add_right_node(g7)
f7.add_down_node(f8)

f8.add_up_node(f7)
f8.add_left_node(starting_node)
f8.add_right_node(g8)

f9.add_down_node(f10)
f9.add_right_node(g9)

f10.add_up_node(f9)
f10.add_right_node(j10)
f10.add_left_node(e10)

#********* BLOCCO G **********#
g2.add_left_node(f2)
g2.add_down_node(g3)
g2.add_right_node(h2)

g3.add_up_node(g2)
g3.add_left_node(f3)

g4.add_left_node(f4)
g4.add_down_node(g5)

g5.add_up_node(g4)
g5.add_down_node(g6)
g5.add_right_node(h5)

g6.add_up_node(g5)
g6.add_left_node(d6)
g6.add_down_node(g7)

g7.add_up_node(g6)
g7.add_left_node(f7)
g7.add_right_node(h7)

g8.add_left_node(f8)
g8.add_right_node(h8)
g8.add_down_node(g9)

g9.add_left_node(f9)
g9.add_up_node(g8)

#********* BLOCCO H **********#
h1.add_left_node(f1)
h1.add_right_node(j1)
h1.add_down_node(h2)

h2.add_up_node(h1)
h2.add_left_node(g2)
h2.add_right_node(j2)
h2.add_down_node(h3)

h3.add_up_node(h2)
h3.add_right_node(j3)
h3.add_down_node(h5)

h5.add_left_node(g5)
h5.add_up_node(h3)
h5.add_right_node(c5) 
h5.add_down_node(h7)

h7.add_up_node(h5)
h7.add_left_node(g7)
h7.add_right_node(j7)
h7.add_down_node(h8)

h8.add_up_node(h7)
h8.add_left_node(g8)
h8.add_down_node(h9)

h9.add_up_node(h8)
h9.add_right_node(i9)

#********* BLOCCO I **********#
i8.add_right_node(j8)
i8.add_down_node(i9)

i9.add_up_node(i8)
i9.add_left_node(h9)
i9.add_right_node(j9)

#********* BLOCCO J **********#
j1.add_left_node(h1)
j1.add_down_node(j2)

j2.add_up_node(j1)
j2.add_left_node(h2)
j2.add_down_node(j3)

j3.add_up_node(j2)
j3.add_left_node(h3)

j7.add_left_node(h7)
j7.add_down_node(j8)

j8.add_up_node(j7)
j8.add_left_node(i8)

j9.add_left_node(i9)
j9.add_down_node(j10)

j10.add_up_node(j9)
j10.add_left_node(f10)

starting_node.add_right_node(f8)
starting_node.add_left_node(e8)

ghosts_starting_node.add_right_node(f4)
ghosts_starting_node.add_left_node(e4)
