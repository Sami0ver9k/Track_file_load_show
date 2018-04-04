from tkinter import *
from tkinter import filedialog
import numpy as np
from nibabel import trackvis
from dipy.tracking.utils import length
from dipy.viz import fvtk
import vtk.util.colors as colors



class Window(Frame):
   
   def show_tract(self,segmented_tract, color):
          """Visualization of the segmented tract.
          """ 
          ren = fvtk.ren()           
          fvtk.add(ren, fvtk.line(segmented_tract.tolist(),
                                    colors=color,
                                    linewidth=2,
                                    opacity=0.3))
          fvtk.show(ren)
          fvtk.clear(ren)

   def load(self,T_filename, threshold_short_streamlines=10.0):
          """Load tractogram from TRK file and remove short streamlines with
          length below threshold.
          """
          print("Loading %s" % T_filename)
          T, hdr = trackvis.read(T_filename, as_generator=False)
          T = np.array([s[0] for s in T], dtype=np.object)
          print("%s: %s streamlines" % (T_filename, len(T)))
          
          return T, hdr
          #Removing short artifactual streamlines
          #print("Removing (presumably artifactual) streamlines shorter than %s" % threshold_short_streamlines)
          #T = np.array([s for s in T if length(s) >= threshold_short_streamlines], dtype=np.object)
          #print("%s: %s streamlines" % (T_filename, len(T)))
          #return T, hdr

    
   def Insert_work(self):
        self.fileName = filedialog.askopenfilename( filetypes= ( ("only trk files", ".trk"),("trk files","*.trk*")) )
        print(self.fileName)
        #np.random.seed(0)
        # test tractogram
   	    #test_tractogram = "100307"
        T_A_filename = self.fileName
        T_A, hdr = self.load(T_A_filename, threshold_short_streamlines=10.0)
        print("Show the tract")
        color= colors.green
        self.show_tract( T_A,color)
    

   def init_window(self):
          self.master.title("Tractogram")
          self.pack(fill=BOTH,expand=1)
          button1=Button(self,text='Insert',command=self.Insert_work)
          button1.place(x=0,y=0)

   def __init__(self, master=None):
         Frame.__init__(self, master,bg='black')

         self.master = master

         self.init_window()

if __name__ == '__main__':
    root=Tk() 
    root.geometry("800x600")
    app=Window(root)
    root.mainloop()
    
    
