# -*-coding: utf-8 -*-

__title__ = "Element Info" #Name of the button displayed in Revit UI
__doc__   ="""This is simple tool to pick an element and 
print out some simple information about it.""" #Button Description shown in Revit UI

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

import sys

from Autodesk.Revit.DB import *    #Import everything from DB (Very good for beginners and development)

# from Autodesk.Revit.DB import Transaction, Element, ElementId, FilteredElementCollector, Level, BuiltInCategory

# pyRevit
from pyrevit import revit, forms






# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ===========================================================================
# from pyrevit.revit import uidoc, doc, app #Alternative
doc    = __revit__.ActiveUIDocument.Document
uidoc  = __revit__.ActiveUIDocument
app    = __revit__.Application




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

# print("Hello World")

# BONUS: pyRevit Input

# selected_views = forms.select_views()
# if selected_views:
#     print (selected_views)



# PICK ELEMENT



with forms.WarningBar(title='Pick an element'):
    element      = revit.pick_element()

element_type = type(element)

if element_type != Wall:
    forms.alert('You were supposed to pick a Wall', exitscript=True)


# print(element)
# print(element_type)



# GET INFORMATION

e_cat        = element.Category.Name
e_id = element.Id
e_level      = doc.GetElement(element.LevelId)



e_wall_type = element.WallType
e_width     = element.Width


# PRINT CONSOLE
print ('Element Category: {}'.format(e_cat))
print ('ElementId: {}'.format(e_id))
print ('ElementLevelId: {}'.format(e_level.Name))
print ('Wall WallType: {}'.format(e_wall_type))
print ('Wall Width: {}'.format(e_width))










# with forms.WarningBar(title='Pick an element'):
#     element = revit.pick_element()
#
# element_type = type(element)
#
# print(element)
# print(element_type)
#
# # GET INFORMATION
# attributes = ["Category", "Id", "LevelId", "WallType", "Width"]
#
# # PRINT CONSOLE
# values = [getattr(element, attr) for attr in attributes]
# print("Element: {}".format(values))
