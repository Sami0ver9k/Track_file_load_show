# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 12:12:02 2018

 
import numpy as np
from nibabel import trackvis
from dipy.tracking.utils import length
from dipy.viz import fvtk
import vtk.util.colors as colors

def show_tract(segmented_tract, color):
   """Visualization of the segmented tract.
   """ 
   ren = fvtk.ren()           
   fvtk.add(ren, fvtk.line(segmented_tract.tolist(),
                           colors=color,
                           linewidth=2,
                           opacity=0.3))
   fvtk.show(ren)
   fvtk.clear(ren)
   
def load(T_filename, threshold_short_streamlines=10.0):
    """Load tractogram from TRK file and remove short streamlines with
    length below threshold.
    """
    print("Loading %s" % T_filename)
    T, hdr = trackvis.read(T_filename, as_generator=False)
    T = np.array([s[0] for s in T], dtype=np.object)
    print("%s: %s streamlines" % (T_filename, len(T)))
    
    #Removing short artifactual streamlines
    #print("Removing (presumably artifactual) streamlines shorter than %s" % threshold_short_streamlines)
    #T = np.array([s for s in T if length(s) >= threshold_short_streamlines], dtype=np.object)
    #print("%s: %s streamlines" % (T_filename, len(T)))
    #return T, hdr

if __name__ == '__main__':
    
    print(__doc__)
    np.random.seed(0)

    # test tractogram
    test_tractogram = "100307" 
    T_A_filename = 'tracks_dti_100K.trk'
    
    T_A, hdr = load(T_A_filename, threshold_short_streamlines=10.0)  
    
    print("Show the tract")
    color= colors.green
    show_tract( T_A,color)       
    
    
    
    
    
    