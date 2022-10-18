# from pyrevit import forms
# import clr
# import pyrevit
# from pyrevit.forms import WPFWindow
# import math
# import System

# print(System)
# import sys
# print(sys.modules.keys())

# import Autodesk
# from Autodesk.DesignScript.Geometry
# import Autodesk

from Autodesk.Revit.DB import *

from pyrevit import revit

doc = revit.doc

all_doors =FilteredElementCollector(doc).OfCategory
