#!/usr/bin/env python

import numpy as np
import itertools as it
from genice import yaplotlib as yp
import random

#no threshold; draw contour at zero.
class Contour():
    def __init__(self, values, center=False, pbc=False):
        self.values = values
        if center:
            x,y,z = values.shape
            self.values = np.roll(self.values, x//2, axis=0)
            self.values = np.roll(self.values, y//2, axis=1)
            self.values = np.roll(self.values, z//2, axis=2)
        if pbc:
            self.pbc()
    def tetrahedron(self, points, values):
        parity = values > 0.0
        n = np.sum(parity)
        if n in (0,4):
            return
        elif n == 1:
            apex = np.where(values > 0.0)[0][0] #single point
            base = np.where(values <= 0.0)[0]   #three points
            return [(values[apex]*points[v]-values[v]*points[apex])/(values[apex]-values[v]) for v in base]
        elif n == 3:
            apex = np.where(values <= 0.0)[0][0] #single point
            base = np.where(values > 0.0)[0]   #three points
            return [(values[apex]*points[v]-values[v]*points[apex])/(values[apex]-values[v]) for v in base]
        else: # n==2
            top = np.where(values > 0.0)[0]  #two points
            bot = np.where(values <= 0.0)[0] #two points
            combi = ((top[0],bot[0]),(top[1],bot[0]),(top[1],bot[1]),(top[0],bot[1]))
            return [(values[i]*points[j]-values[j]*points[i])/(values[i]-values[j]) for i,j in combi]
    def facets(self):
        values = self.values
        sx,sy,sz = values.shape
        # values: 3-dim values on the grid
        for ix,iy,iz in it.product(range(sx-1),range(sy-1),range(sz-1)):
            # confirmed the order
            # always range in -0.5 .. +0.5
            qp = np.array([((ix+dx-sx//2)/(sx-1),
                            (iy+dy-sy//2)/(sy-1),
                            (iz+dz-sz//2)/(sz-1)) for dx in range(2) for dy in range(2) for dz in range(2)])
            qv = values[ix:ix+2, iy:iy+2, iz:iz+2].reshape([8])
            if (ix+iy+iz)%2 == 0:
                for i,j,k,l in ((0,1,2,4), (1,4,5,7), (1,2,3,7), (2,4,6,7), (1,2,4,7)):
                    face = self.tetrahedron(qp[[i,j,k,l]], qv[[i,j,k,l]])
                    if face is not None:
                        yield face
            else:
                for i,j,k,l in ((0,1,3,5), (3,5,6,7), (0,4,5,6), (0,2,3,6), (0,3,5,6)):
                    face = self.tetrahedron(qp[[i,j,k,l]], qv[[i,j,k,l]])
                    if face is not None:
                        yield face
    def double(self):
        """
        double the mesh
        """
        values = self.values
        x,y,z = values.shape
        newvalues = np.zeros((x*2-1,y*2-1,z*2-1))
        newvalues[::2,::2,::2] = values[:,:,:]
        newvalues[1::2,::2,::2] = (newvalues[0:x*2-2:2,::2,::2]+newvalues[2::2,::2,::2])/2
        newvalues[:,1::2,::2] = (newvalues[:,0:y*2-2:2,::2]+newvalues[:,2::2,::2])/2
        newvalues[:,:,1::2] = (newvalues[:,:,0:z*2-2:2]+newvalues[:,:,2::2])/2
        self.values = newvalues
        
    def pbc(self):
        """
        extend the array
        """
        values = self.values
        x,y,z = values.shape
        newvalues = np.zeros((x+1,y+1,z+1))
        newvalues[:x,:y,:z] = values
        newvalues[x,:y,:z] = values[0,:y,:z]
        newvalues[:x,y,:z] = values[:x,0,:z]
        newvalues[:x,:y,z] = values[:x,:y,0]
        newvalues[x,y,z] = values[0,0,0]
        self.values = newvalues
        
        

def main():
    points  = np.array([(x,y,z) for z in range(-2,3) for y in range(-2,3) for x in range(-2,3)])
    values = np.array([np.dot(x,x)-1.7 for x in points]).reshape((5,5,5))
    cnt = Contour(values)
    #print(values)
    #cnt.double()
    #cnt.double()
    #cnt.double()
    s = yp.Layer(1)
    for face in cnt.facets():
        s += yp.Polygon(face)

    points  = np.array([(x,y,z) for z in range(-2,3) for y in range(-2,3) for x in range(-2,3)])
    values = np.array([random.random()-0.5 for x in points]).reshape((5,5,5))
    cnt = Contour(values)
    cnt.double()
    s += yp.Layer(2)
    for face in cnt.facets():
        s += yp.Polygon(face)

    print(s)

if __name__ == "__main__":
    main()
