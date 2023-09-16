# -*-coding: utf-8 -*-

__title__ = "Simple FilterElementColector" #Name of the button displayed in Revit UI
__doc__   ="""This is simple tool to filter an element """ #Button Description shown in Revit UI

__doc__ = """ Version = 1.0
Date    = 20.04.2022
_____________________________________________________________________
Description:
Function to add Elevation in meters to all Level names
as a prefix/suffix.

There is an option to Add/Update or Remove them.
_____________________________________________________________________
How-to:

-> Click on the Button 
-> Change Settings (Optional)
-> Rename Levels

_____________________________________________________________________
Last update:
- [02.04.2022] - 1.0 RELEASE
_____________________________________________________________________
Author: Dmytro Khom"""

__author__ = "Dmytro Khom"




# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# =======================================================================

# Regular + Autodesk

import clr
clr.AddReference('System')
from System.Collections.Generic import List

#
from Autodesk.Revit.DB import *    #Import everything from DB (Very good for beginners and development)
#
# # from Autodesk.Revit.DB import Transaction, Element, ElementId, FilteredElementCollector, Level, BuiltInCategory
#
# # pyRevit
# from pyrevit import revit, forms






# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ===========================================================================
# from pyrevit.revit import uidoc, doc, app #Alternative
doc    = __revit__.ActiveUIDocument.Document
uidoc  = __revit__.ActiveUIDocument
app    = __revit__.Application


active_view = doc.ActiveView

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
# ===========================================================================


# ╔═╗╦  ╔═╗╔═╗╔═╗╔═╗╔═╗
# ║  ║  ╠═╣╚═╗╚═╗║╣ ╚═╗
# ╚═╝╩═╝╩ ╩╚═╝╚═╝╚═╝╚═╝ CLASSES
# ===========================================================================


# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
# ===========================================================================
all_rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).ToElements()
all_walls = FilteredElementCollector(doc).OfClass(Wall).WhereElementIsNotElementType().ToElements()

all_rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_SWallRectOpening).WhereElementIsNotElementType().ToElements()


all_views = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Views).WhereElementIsNotElementType().ToElements()
all_legends = [view for view in all_views if view.ViewType == ViewType.Legend]

all_column_in_view = FilteredElementCollector(doc, active_view.Id).\
    OfCategory(BuiltInCategory.OST_StructuralColumns).WhereElementIsNotElementType().ToElements()

print (len(all_column_in_view))

categories = List[BuiltInCategory]([BuiltInCategory.OST_Walls,
                              BuiltInCategory.OST_Floors,
                              BuiltInCategory.OST_StructuralColumns,
                              BuiltInCategory.OST_SWallRectOpening])

custom_filter = ElementMulticategoryFilter(categories)
my_elements = FilteredElementCollector(doc).WherePasses(custom_filter).WhereElementIsElementType().ToElements()
print (my_elements)

# print (len(all_views))
# print (len(all_legends))


# print (all_rooms)
# print ("*"*40)
# print (all_walls)


