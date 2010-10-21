from pyx import *

files = ["f4a.eps", "f4b.eps"]
newfile = "f4"  # omit .eps

c = canvas.canvas()
c.insert(epsfile.epsfile(0,0,files[0]))
c.insert(epsfile.epsfile(20.5,0,files[1]))
c.writeEPSfile(newfile)
