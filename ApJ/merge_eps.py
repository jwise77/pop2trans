from pyx import *

files = ["f3a.eps", "f3b.eps"]
newfile = "f3"  # omit .eps

c = canvas.canvas()
c.insert(epsfile.epsfile(0,0,files[0]))
c.insert(epsfile.epsfile(20.5,0,files[1]))
c.writeEPSfile(newfile)
