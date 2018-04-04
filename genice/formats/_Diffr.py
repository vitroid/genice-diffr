# coding: utf-8
"""
Structure factor from atomic arrangement.
"""



# system library
#from collections import defaultdict
#import itertools as it

# public library
import numpy as np
#import networkx as nx
#from countrings import countrings_nx as cr

# private library
from genice import yaplotlib as yp
#import pairlist as pl
from formats import contour


def hook1(lattice):
    lattice.logger.info("Hook1: Diffraction.")
    lattice.logger.info("  3D FFT.")
    cellmat = lattice.repcell.mat
    atoms = lattice.reppositions
    grid = [32,32,32]
    distrib = np.zeros(grid)
    grid = np.array(grid)
    iatoms = np.array(np.floor(lattice.reppositions * grid), dtype=int)
    for x,y,z in iatoms:
        distrib[x,y,z] += 1
    diffr = np.fft.fftn(distrib, axes=(0,1,2))
    power = np.real(diffr*np.conj(diffr)) / len(atoms)
    lattice.logger.info("  Rendering in Yaplot format.")
    s = ""
    for layer,threshold in enumerate(thresholds):
        s += yp.Color(layer+3)
        s += yp.Layer(layer+1)
        cnt = contour.Contour(power - threshold, pbc=True, center=True)
        cnt.double()
        nfacet = 0
        for face in cnt.facets():
            s += yp.Polygon(face)
            nfacet += 1
        lattice.logger.info("    {0} facets rendered for threshold {1}.".format(nfacet, threshold))
    print(s)
    
    lattice.logger.info("Hook1: end.")


thresholds = (5.0,)

def argparser(arg):
    global thresholds
    args = arg.split(":")
    thresholds = [float(v) for v in args[0].split(",")]

hooks = {1:hook1}
