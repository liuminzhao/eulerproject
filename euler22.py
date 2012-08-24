print sum ( [ (pos+1) * nv for pos, nv in enumerate([ sum ( [ ord(char) - 64 for char in name ] ) for name in sorted([name.strip('"') for name in open('names.txt','r').readline().split(",")]) ]) ] )
