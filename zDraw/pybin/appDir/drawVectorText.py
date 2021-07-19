


def make_text_vectors(Text,XY,Anchor,Size):
    if Anchor=='left':
        X0=XY[0]
        Y0=XY[1]
    elif Anchor=='right':
        X0=XY[0]-len(Text)*FontSize*Size
        Y0=XY[1]
    elif Anchor=='middle':
        X0=XY[0]-(len(Text)*FontSize*Size)/2
        Y0=XY[1]
    Res=[]
    for Chr in Text:
        Part=make_vector_letter(Chr,X0,Y0,Size)
        X0 += FontSize*Size
        Res.extend(Part)
    return Res

def make_vector_letter(Chr,X0,Y0,Size):
    if Chr in Font1:
        List=Font1[Chr][:]
    else:
        List = Font1['joker'][:]
    Res=[]
    while '|' in List:
        Ind = List.index('|')
        Head = List[:Ind]
        List = List[Ind+1:]
        Part=mark_vector_segment(Head,X0,Y0,Size)
        Res.extend(Part)
    Part=mark_vector_segment(List,X0,Y0,Size)
    Res.extend(Part)
    return Res

def mark_vector_segment(List,X0,Y0,Size):
    Res=[]
    while len(List)>1:
        (X1,Y1) = List.pop(0)
        (X2,Y2) = List[0]
        Xa = X0 + X1*Glbs.fontShrink*Size
        Xb = X0 + X2*Glbs.fontShrink*Size
        Ya = Y0 + Y1*Size
        Yb = Y0 + Y2*Size
        Res.append([(Xa,Ya),(Xb,Yb)])
    return Res


    

FontSize=2
Font1 = {}

Font1[' '] = []
Font1['.'] = [(0.5,0.0),(0.5,0.5),(1.0,0.5),(1.0,0.0),(0.5,0.0)]
Font1['+'] = [(0,1),(1.8,1),'|',(1,0),(1,2)]
Font1['"'] = [(0.4,1.2),(0.6,2),'|',(0.8,1.2),(1.0,2)]
Font1['-'] = [(0,1),(1.8,1)]
Font1['_'] = [(0,0),(1.8,0)]
Font1['='] = [(0,0.5),(1.8,0.5),'|',(0,1.2),(1.8,1.2)]
Font1['>'] = [(0,0.4),(1.8,0.7),'|',(0,1.4),(1.8,0.7)]
Font1['<'] = [(1.8,0.4),(0,0.7),'|',(1.8,1.4),(0,0.7)]
Font1["0"]=[(0.4,0.0),(1.4,0.0),(1.7,0.5),"|",(0.4,0.0),(0.0,0.5),(0.0,1.4),(0.4,2.0),(1.4,2.0),(1.8,1.4),(1.7,0.5),"|",(1.8,1.4),(0.0,0.5)]
Font1['*'] = [(0.5,0.5),(1.5,1.5),'|',(0.5,1.5),(1.5,0.5),'|',(0.5,1),(1.5,1),'|',(1,1.5),(1,0.5)]

Font1["y"]=[(0.0,2.0),(1.0,0.7),"|",(1.0,0.7),(1.8,2.0),"|",(1.0,0.7),(0.1,0.0)]
Font1["w"]=[(0.0,2.0),(0.5,0.0),"|",(0.5,0.0),(0.9,0.7),"|",(1.0,1.8),(0.9,0.7),"|",(0.9,0.7),(1.2,0.0),"|",(1.2,0.0),(1.8,1.8)]
Font1["a"]=[(0.0,0.0),(0.7,1.1),"|",(1.2,2.0),(0.7,1.1),"|",(1.2,2.0),(1.4,1.1),"|",(1.8,0.0),(1.4,1.1),"|",(0.7,1.1),(1.4,1.1)]
Font1["g"]=[(1.6,1.6),(1.4,2.0),"|",(1.4,2.0),(0.4,2.0),"|",(0.4,2.0),(0.0,1.6),"|",(0.0,1.6),(0.1,0.3),"|",(0.1,0.3),(0.5,0.0),"|",(0.5,0.0),(1.5,0.0),"|",(1.5,0.0),(1.8,0.4),"|",(1.8,0.4),(1.4,1.0),"|",(1.4,1.0),(0.5,1.0)]
Font1["f"]=[(0.1,0.0),(0.1,1.0),"|",(0.0,1.7),(0.6,2.0),"|",(0.0,1.7),(0.1,1.0),"|",(0.6,2.0),(1.8,2.0),"|",(0.1,1.0),(1.2,1.0)]
Font1["c"]=[(1.8,2.0),(0.8,2.0),"|",(0.8,2.0),(0.0,1.7),"|",(0.0,1.7),(0.0,0.4),"|",(0.0,0.4),(0.4,0.0),"|",(0.4,0.0),(1.6,0.0)]
Font1["o"]=[(0.5,0.0),(0.0,0.4),"|",(0.5,0.0),(1.5,0.1),"|",(0.0,0.4),(0.0,1.7),"|",(0.0,1.7),(0.4,2.0),"|",(0.4,2.0),(1.4,2.0),"|",(1.4,2.0),(1.8,1.7),"|",(1.8,1.7),(1.8,0.6),"|",(1.8,0.6),(1.5,0.1)]
Font1["e"]=[(1.8,1.7),(1.3,1.9),"|",(1.3,1.9),(0.5,2.0),"|",(0.0,1.7),(0.1,1.0),"|",(0.0,1.7),(0.5,2.0),"|",(0.1,1.0),(0.9,1.0),"|",(0.1,1.0),(0.0,0.2),"|",(0.0,0.2),(0.6,0.0),"|",(0.6,0.0),(1.6,0.0),"|",(1.6,0.0),(1.8,0.4)]
Font1["z"]=[(0.0,1.5),(0.4,1.9),"|",(0.4,1.9),(1.8,2.0),"|",(1.8,2.0),(0.0,0.0),"|",(0.0,0.0),(1.4,0.0),"|",(1.4,0.0),(1.8,0.5)]
Font1["x"]=[(0.1,2.0),(0.9,1.0),"|",(0.9,1.0),(1.8,0.0),"|",(0.9,1.0),(1.6,2.0),"|",(0.9,1.0),(0.0,0.1)]
Font1["k"]=[(0.1,1.9),(0.2,1.0),"|",(0.0,0.0),(0.2,1.0),"|",(1.8,2.0),(0.8,1.2),"|",(0.2,1.0),(0.8,1.2),"|",(0.8,1.2),(1.7,0.1)]
Font1["l"]=[(0.1,2.0),(0.0,0.3),"|",(0.0,0.3),(0.4,0.0),"|",(0.4,0.0),(1.8,0.0)]
Font1["i"]=[(0.0,1.9),(0.8,1.9),"|",(1.5,2.0),(0.8,1.9),"|",(0.0,0.0),(0.8,0.0),"|",(1.8,0.1),(0.8,0.0),"|",(0.8,0.0),(0.8,1.9)]
Font1["s"]=[(1.8,1.6),(1.5,2.0),"|",(1.5,2.0),(0.3,2.0),"|",(0.3,2.0),(0.0,1.6),"|",(0.0,1.6),(0.1,1.2),"|",(1.4,0.9),(1.7,0.7),"|",(1.4,0.9),(0.1,1.2),"|",(1.7,0.7),(1.7,0.2),"|",(1.7,0.2),(1.3,0.0),"|",(1.3,0.0),(0.0,0.2)]
Font1["j"]=[(0.8,2.0),(1.6,2.0),"|",(1.6,2.0),(1.8,0.8),"|",(1.8,0.8),(1.4,0.0),"|",(1.4,0.0),(0.5,0.0),"|",(0.5,0.0),(0.0,0.5)]
Font1["h"]=[(0.0,2.0),(0.1,1.1),"|",(0.0,0.0),(0.1,1.1),"|",(1.8,2.0),(1.7,1.1),"|",(1.7,0.1),(1.7,1.1),"|",(0.1,1.1),(1.7,1.1)]
Font1["v"]=[(0.0,2.0),(0.9,0.0),"|",(0.9,0.0),(1.8,1.9)]
Font1["t"]=[(0.0,1.7),(0.2,2.0),"|",(0.2,2.0),(0.9,2.0),"|",(0.9,2.0),(1.6,2.0),"|",(0.9,2.0),(0.9,0.0),"|",(1.6,2.0),(1.8,1.7)]
Font1["p"]=[(0.1,0.0),(0.1,0.9),"|",(0.0,1.6),(0.4,2.0),"|",(0.0,1.6),(0.1,0.9),"|",(0.4,2.0),(1.5,2.0),"|",(1.5,2.0),(1.8,1.6),"|",(1.8,1.6),(1.8,1.1),"|",(1.8,1.1),(1.0,0.9),"|",(1.0,0.9),(0.1,0.9)]

Font1["q"]=[(0.4,0.1),(1.4,0.1),(1.7,0.5),"|",(0.4,0.1),(0.0,0.6),(0.0,1.4),(0.4,2.0),(1.3,2.0),(1.7,1.5),(1.7,0.5),"|",(1.3,0.8),(1.8,-0.2)]
Font1["Q"]=[(0.4,0.1),(1.4,0.1),(1.7,0.5),"|",(0.4,0.1),(0.0,0.6),(0.0,1.4),(0.4,2.0),(1.3,2.0),(1.7,1.5),(1.7,0.5),"|",(1.3,0.6),(1.8,0.0)]

Font1["d"]=[(0.1,2.0),(0.6,2.0),"|",(1.3,2.0),(1.8,1.7),"|",(1.3,2.0),(0.6,2.0),"|",(1.8,1.7),(1.7,0.3),"|",(1.7,0.3),(1.1,0.0),"|",(1.1,0.0),(0.5,0.0),"|",(0.0,0.0),(0.5,0.0),"|",(0.6,2.0),(0.5,0.0)]
Font1["n"]=[(0.0,0.0),(0.0,2.0),"|",(0.0,2.0),(1.8,0.1),"|",(1.8,0.1),(1.8,2.0)]
Font1["m"]=[(0.0,0.0),(0.0,1.9),"|",(0.0,1.9),(0.9,1.4),"|",(0.9,1.4),(1.8,2.0),"|",(1.8,2.0),(1.8,0.1)]
Font1["b"]=[(0.0,2.0),(1.2,2.0),"|",(0.0,2.0),(0.0,1.1),"|",(1.0,0.0),(0.0,0.0),"|",(1.0,0.0),(1.5,0.3),"|",(0.0,0.0),(0.0,1.1),"|",(1.2,2.0),(1.8,1.6),"|",(1.8,1.6),(1.7,1.2),"|",(1.7,1.2),(1.0,1.1),"|",(1.0,1.1),(0.0,1.1),"|",(1.0,1.1),(1.6,0.7),"|",(1.6,0.7),(1.5,0.3)]
Font1["r"]=[(0.1,0.0),(0.1,0.9),"|",(0.0,1.7),(0.4,2.0),"|",(0.0,1.7),(0.1,0.9),"|",(0.4,2.0),(1.5,2.0),"|",(1.5,2.0),(1.8,1.6),"|",(1.8,1.6),(1.8,1.1),"|",(1.8,1.1),(1.2,0.8),"|",(1.2,0.8),(0.1,0.9),"|",(0.1,0.9),(1.2,0.0),"|",(1.2,0.0),(1.6,0.1)]


Font1["Y"]=[(0.0,2.0),(1.0,0.7),"|",(1.0,0.7),(1.8,2.0),"|",(1.0,0.7),(0.1,0.0)]
Font1["W"]=[(0.0,2.0),(0.5,0.0),"|",(0.5,0.0),(0.9,0.7),"|",(1.0,1.8),(0.9,0.7),"|",(0.9,0.7),(1.2,0.0),"|",(1.2,0.0),(1.8,1.8)]
Font1["A"]=[(0.0,0.0),(0.7,1.1),"|",(1.2,2.0),(0.7,1.1),"|",(1.2,2.0),(1.4,1.1),"|",(1.8,0.0),(1.4,1.1),"|",(0.7,1.1),(1.4,1.1)]
Font1["G"]=[(1.6,1.6),(1.4,2.0),"|",(1.4,2.0),(0.4,2.0),"|",(0.4,2.0),(0.0,1.6),"|",(0.0,1.6),(0.1,0.3),"|",(0.1,0.3),(0.5,0.0),"|",(0.5,0.0),(1.5,0.0),"|",(1.5,0.0),(1.8,0.4),"|",(1.8,0.4),(1.4,1.0),"|",(1.4,1.0),(0.5,1.0)]
Font1["F"]=[(0.1,0.0),(0.1,1.0),"|",(0.0,1.7),(0.6,2.0),"|",(0.0,1.7),(0.1,1.0),"|",(0.6,2.0),(1.8,2.0),"|",(0.1,1.0),(1.2,1.0)]
Font1["C"]=[(1.8,2.0),(0.8,2.0),"|",(0.8,2.0),(0.0,1.7),"|",(0.0,1.7),(0.0,0.4),"|",(0.0,0.4),(0.4,0.0),"|",(0.4,0.0),(1.6,0.0)]
Font1["O"]=[(0.5,0.0),(0.0,0.4),"|",(0.5,0.0),(1.5,0.1),"|",(0.0,0.4),(0.0,1.7),"|",(0.0,1.7),(0.4,2.0),"|",(0.4,2.0),(1.4,2.0),"|",(1.4,2.0),(1.8,1.7),"|",(1.8,1.7),(1.8,0.6),"|",(1.8,0.6),(1.5,0.1)]
Font1["E"]=[(1.8,1.7),(1.3,1.9),"|",(1.3,1.9),(0.5,2.0),"|",(0.0,1.7),(0.1,1.0),"|",(0.0,1.7),(0.5,2.0),"|",(0.1,1.0),(0.9,1.0),"|",(0.1,1.0),(0.0,0.2),"|",(0.0,0.2),(0.6,0.0),"|",(0.6,0.0),(1.6,0.0),"|",(1.6,0.0),(1.8,0.4)]
Font1["Z"]=[(0.0,1.5),(0.4,1.9),"|",(0.4,1.9),(1.8,2.0),"|",(1.8,2.0),(0.0,0.0),"|",(0.0,0.0),(1.4,0.0),"|",(1.4,0.0),(1.8,0.5)]
Font1["X"]=[(0.1,2.0),(0.9,1.0),"|",(0.9,1.0),(1.8,0.0),"|",(0.9,1.0),(1.6,2.0),"|",(0.9,1.0),(0.0,0.1)]
Font1["K"]=[(0.1,1.9),(0.2,1.0),"|",(0.0,0.0),(0.2,1.0),"|",(1.8,2.0),(0.8,1.2),"|",(0.2,1.0),(0.8,1.2),"|",(0.8,1.2),(1.7,0.1)]
Font1["L"]=[(0.1,2.0),(0.0,0.3),"|",(0.0,0.3),(0.4,0.0),"|",(0.4,0.0),(1.8,0.0)]
Font1["I"]=[(0.0,1.9),(0.8,1.9),"|",(1.5,2.0),(0.8,1.9),"|",(0.0,0.0),(0.8,0.0),"|",(1.8,0.1),(0.8,0.0),"|",(0.8,0.0),(0.8,1.9)]
Font1["S"]=[(1.8,1.6),(1.5,2.0),"|",(1.5,2.0),(0.3,2.0),"|",(0.3,2.0),(0.0,1.6),"|",(0.0,1.6),(0.1,1.2),"|",(1.4,0.9),(1.7,0.7),"|",(1.4,0.9),(0.1,1.2),"|",(1.7,0.7),(1.7,0.2),"|",(1.7,0.2),(1.3,0.0),"|",(1.3,0.0),(0.0,0.2)]
Font1["J"]=[(0.8,2.0),(1.6,2.0),"|",(1.6,2.0),(1.8,0.8),"|",(1.8,0.8),(1.4,0.0),"|",(1.4,0.0),(0.5,0.0),"|",(0.5,0.0),(0.0,0.5)]
Font1["H"]=[(0.0,2.0),(0.1,1.1),"|",(0.0,0.0),(0.1,1.1),"|",(1.8,2.0),(1.7,1.1),"|",(1.7,0.1),(1.7,1.1),"|",(0.1,1.1),(1.7,1.1)]

Font1["U"]=[(0.4,0.0),(1.2,0.0),(1.7,0.5),"|",(0.4,0.0),(0.0,0.6),(0.0,1.3),(0.3,2.0),"|",(1.6,1.9),(1.8,1.2),(1.7,0.5)]
Font1["u"]=[(0.4,0.0),(1.2,0.0),(1.7,0.5),"|",(0.4,0.0),(0.0,0.6),(0.0,1.3),(0.3,2.0),"|",(1.6,1.9),(1.8,1.2),(1.7,0.5)]
Font1["V"]=[(0.0,2.0),(0.9,0.0),"|",(0.9,0.0),(1.8,1.9)]
Font1["T"]=[(0.0,1.7),(0.2,2.0),"|",(0.2,2.0),(0.9,2.0),"|",(0.9,2.0),(1.6,2.0),"|",(0.9,2.0),(0.9,0.0),"|",(1.6,2.0),(1.8,1.7)]
Font1["P"]=[(0.1,0.0),(0.1,0.9),"|",(0.0,1.6),(0.4,2.0),"|",(0.0,1.6),(0.1,0.9),"|",(0.4,2.0),(1.5,2.0),"|",(1.5,2.0),(1.8,1.6),"|",(1.8,1.6),(1.8,1.1),"|",(1.8,1.1),(1.0,0.9),"|",(1.0,0.9),(0.1,0.9)]
Font1["D"]=[(0.1,2.0),(0.6,2.0),"|",(1.3,2.0),(1.8,1.7),"|",(1.3,2.0),(0.6,2.0),"|",(1.8,1.7),(1.7,0.3),"|",(1.7,0.3),(1.1,0.0),"|",(1.1,0.0),(0.5,0.0),"|",(0.0,0.0),(0.5,0.0),"|",(0.6,2.0),(0.5,0.0)]
Font1["N"]=[(0.0,0.0),(0.0,2.0),"|",(0.0,2.0),(1.8,0.1),"|",(1.8,0.1),(1.8,2.0)]
Font1["M"]=[(0.0,0.0),(0.0,1.9),"|",(0.0,1.9),(0.9,1.4),"|",(0.9,1.4),(1.8,2.0),"|",(1.8,2.0),(1.8,0.1)]
Font1["B"]=[(0.0,2.0),(1.2,2.0),"|",(0.0,2.0),(0.0,1.1),"|",(1.0,0.0),(0.0,0.0),"|",(1.0,0.0),(1.5,0.3),"|",(0.0,0.0),(0.0,1.1),"|",(1.2,2.0),(1.8,1.6),"|",(1.8,1.6),(1.7,1.2),"|",(1.7,1.2),(1.0,1.1),"|",(1.0,1.1),(0.0,1.1),"|",(1.0,1.1),(1.6,0.7),"|",(1.6,0.7),(1.5,0.3)]
Font1["R"]=[(0.1,0.0),(0.1,0.9),"|",(0.0,1.7),(0.4,2.0),"|",(0.0,1.7),(0.1,0.9),"|",(0.4,2.0),(1.5,2.0),"|",(1.5,2.0),(1.8,1.6),"|",(1.8,1.6),(1.8,1.1),"|",(1.8,1.1),(1.2,0.8),"|",(1.2,0.8),(0.1,0.9),"|",(0.1,0.9),(1.2,0.0),"|",(1.2,0.0),(1.6,0.1)]


Font1["2"]=[(0.2,0.0),(1.6,0.0),"|",(0.2,0.0),(1.8,1.2),"|",(0.0,1.4),(0.4,1.9),"|",(0.4,1.9),(1.2,2.0),"|",(1.2,2.0),(1.8,1.7),"|",(1.8,1.7),(1.8,1.2)]
Font1["1"]=[(0.0,1.5),(0.9,2.0),"|",(0.9,2.0),(1.0,0.0),"|",(1.0,0.0),(0.0,0.0),"|",(0.0,0.0),(1.8,0.0)]
Font1["8"]=[(0.6,1.0),(0.2,1.3),"|",(0.6,1.0),(1.5,1.0),"|",(0.6,1.0),(0.1,0.7),"|",(0.2,1.3),(0.2,1.8),"|",(0.2,1.8),(0.8,2.0),"|",(0.8,2.0),(1.7,1.8),"|",(1.7,1.8),(1.8,1.3),"|",(1.8,1.3),(1.5,1.0),"|",(1.5,1.0),(1.8,0.7),"|",(1.8,0.7),(1.8,0.3),"|",(1.8,0.3),(1.2,0.0),"|",(1.2,0.0),(0.4,0.0),"|",(0.4,0.0),(0.0,0.4),"|",(0.0,0.4),(0.1,0.7)]
Font1["9"]=[(1.7,1.0),(0.5,1.0),"|",(1.7,1.0),(1.8,1.6),"|",(1.7,1.0),(1.5,0.5),"|",(0.5,1.0),(0.1,1.2),"|",(0.1,1.2),(0.0,1.7),"|",(0.0,1.7),(0.5,2.0),"|",(0.5,2.0),(1.5,2.0),"|",(1.5,2.0),(1.8,1.6),"|",(1.5,0.5),(1.0,0.0),"|",(1.0,0.0),(0.2,0.0)]
Font1["6"]=[(1.8,1.6),(1.4,1.9),"|",(1.4,1.9),(0.5,2.0),"|",(0.5,2.0),(0.0,1.6),"|",(0.0,1.6),(0.0,0.9),"|",(0.0,0.9),(0.3,0.0),"|",(0.0,0.9),(0.8,1.1),"|",(0.3,0.0),(1.4,0.0),"|",(1.4,0.0),(1.8,0.5),"|",(1.8,0.5),(1.6,0.9),"|",(1.6,0.9),(0.8,1.1)]
Font1["5"]=[(1.6,2.0),(0.1,2.0),"|",(0.1,2.0),(0.2,1.1),"|",(0.2,1.1),(0.9,1.3),"|",(0.9,1.3),(1.6,1.2),"|",(1.6,1.2),(1.8,0.6),"|",(1.8,0.6),(1.4,0.1),"|",(1.4,0.1),(0.6,0.0),"|",(0.6,0.0),(0.0,0.2)]
Font1["3"]=[(0.0,1.4),(0.4,1.9),"|",(0.4,1.9),(1.3,2.0),"|",(1.3,2.0),(1.7,1.5),"|",(1.7,1.5),(1.0,0.9),"|",(1.0,0.9),(1.7,0.8),"|",(1.7,0.8),(1.8,0.3),"|",(1.8,0.3),(1.3,0.0),"|",(1.3,0.0),(0.2,0.1)]
Font1["4"]=[(0.6,2.0),(0.0,0.8),"|",(0.0,0.8),(1.8,0.8),"|",(1.8,0.8),(1.2,0.8),"|",(1.2,0.8),(1.3,1.4),"|",(1.3,1.4),(1.2,0.0)]
Font1["7"]=[(0.0,1.7),(0.2,1.9),"|",(0.2,1.9),(1.8,2.0),"|",(1.8,2.0),(1.3,0.9),"|",(1.3,0.9),(0.9,1.0),"|",(0.9,1.0),(1.2,0.8),"|",(0.7,0.0),(1.2,0.8)]



Font1["@"]=[(0.6,0.1),(1.2,0.0),(1.8,0.2),"|",(1.8,0.8),(1.8,1.5),(1.4,2.0),(0.7,2.0),(0.2,1.7),(0.0,1.0),(0.2,0.5),(0.6,0.1),"|",(1.2,0.6),(1.6,0.5),(1.8,0.8),"|",(1.4,1.5),(1.2,0.6),(1.2,1.2),(0.9,1.4),(0.4,1.2),(0.4,0.8),(0.7,0.5),(1.2,0.6)]
Font1["?"]=[(1.0,1.0),(1.0,0.7),"|",(1.4,0.3),(1.3,0.0),(0.8,0.0),"|",(0.2,1.3),(0.0,1.6),"|",(1.0,0.4),(1.4,0.3),"|",(1.8,1.6),(1.6,1.2),(1.0,1.0),"|",(0.3,1.9),(1.0,2.0),(1.7,1.9),(1.8,1.6),"|",(0.0,1.6),(0.3,1.9),"|",(0.8,0.0),(0.6,0.2),(1.0,0.4)]
Font1[":"]=[(0.4,1.8),(0.6,1.8),(0.6,1.5),(0.4,1.5),(0.4,1.8),'|',(0.4,0.5),(0.6,0.5),(0.6,0.2),(0.4,0.2),(0.4,0.5)]
Font1[";"]=[(0.4,1.8),(0.6,1.8),(0.6,1.5),(0.4,1.5),(0.4,1.8),'|',(0.4,0.9),(0.6,0.9),(0.3,0.0),(0.4,0.9)]
Font1[","]=[(0.2,0.1),(0.2,0.3),(0.5,0.3),(0.2,0.1),(0.0,-0.3)]
Font1["/"]=[(1.8,2.0),(0.0,0.0)]
Font1["("]=[(0.5,2.0),(0.0,1.5),(0.0,0.5),(0.5,0.0)]
Font1[")"]=[(1.2,2.0),(1.8,1.5),(1.8,0.5),(1.2,0.0)]
Font1["["]=[(1.0,2.0),(0.5,2.0),(0.5,0.0),(1.0,0.0)]
Font1["]"]=[(0.8,2.0),(1.3,2.0),(1.3,0.0),(0.8,0.0)]
Font1["!"]=[(0.5,0.0),(0.4,0.5),(0.9,0.5),(0.9,0.0),(0.4,0.0),'|',(0.6,0.8),(0.3,2),(0.6,2.2),(0.9,2),(0.6,0.8)]
Font1["~"]=[(0.5,1.0),(0.8,1.3),(1.1,1.3),(1.4,1.0),(1.7,0.7),(2.0,0.7),(2.3,1.0)]
Font1['&'] = [(2,0),(0.2,1.6),(0.3,1.9),(0.6,2.0),(0.9,1.7),(1.0,1.4),(0.2,1.0),(0,0.4),(0.2,0),(1.0,0),(1.6,0.8)]
Font1['{'] = [(0.5,0),(0.3,0.3),(0.1,1.0),(0.3,1.7),(0.5,2),'|',(0.1,1),(0,1)]
Font1['}'] = [(0.1,0),(0.3,0.3),(0.5,1.0),(0.3,1.7),(0.1,2),'|',(0.5,1),(0.6,1)]
Font1['joker'] = [(0.5,0.5),(0.5,1.5),(1.5,1.5),(1.5,0.5),(0.5,0.5)]

