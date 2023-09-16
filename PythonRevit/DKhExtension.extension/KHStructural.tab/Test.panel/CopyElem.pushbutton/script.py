# -*-coding: utf-8 -*-

__title__ = "Copy Elemement" #Name of the button displayed in Revit UI
__doc__   ="""This is simple tool to Copy Elemement With Revit API """ #Button Description shown in Revit UI
__version__ = "Version = 1.0"
__doc__ = """ Version = 1.0
Date    = 26.08.2022
_____________________________________________________________________
Description:

Test code about Copying Elements 
using Revit API
______________________________________
Author: Dmytro Khom"""
__author__ = "Dmytro Khom"



# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# =======================================================================

# Regular + Autodesk
from Autodesk.Revit.DB import *    #Import everything from DB (Very good for beginners and development)
from Autodesk.Revit.DB.Structure import StructuralType
# .NET IMPORT
import clr
clr.AddReference('System')

# # pyRevit
from pyrevit import revit, forms
from pyrevit.forms import select_views

from System.Collections.Generic import List
# # from Autodesk.Revit.DB import Transaction, Element, ElementId, FilteredElementCollector, Level, BuiltInCategory



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

# 🟢 ╔═╗╔═╗╔═╗╦ ╦  ╦ ╦╦╔╦╗╦ ╦  ╦  ╦╔═╗╔═╗╔╦╗╔═╗╦═╗
# 🟢 ║  ║ ║╠═╝╚╦╝  ║║║║ ║ ╠═╣  ╚╗╔╝║╣ ║   ║ ║ ║╠╦╝
# 🟢 ╚═╝╚═╝╩   ╩   ╚╩╝╩ ╩ ╩ ╩   ╚╝ ╚═╝╚═╝ ╩ ╚═╝╩╚═ COPY WITH VECTOR

# ===========================================================================
# #👉 Get Walls
# wallsToCopy = FilteredElementCollector(doc)\
#     .OfCategory(BuiltInCategory.OST_Walls)\
#     .WhereElementIsNotElementType()\
#     .ToElementIds()
#
# # 📐Vector
# vector = XYZ(250, 500, 0)
#
# # 🔓 Start Transaction
# t = Transaction(doc, __title__)
# t.Start()
#
# # ✔ Copy Elements
# ElementTransformUtils.CopyElements(doc, wallsToCopy, vector)
#
# #for wall in wallsToCopy:
# #         ElementTransformUtils.CopyElement(doc, wall, vector)
#
#
# # 🔒 End Transaction
# t.Commit()




# 🟡 ╔═╗╔═╗╔═╗╦ ╦  ╔╗ ╔═╗╔╦╗╦ ╦╔═╗╔═╗╔╗╔  ╦  ╦╦╔═╗╦ ╦╔═╗
# 🟡 ║  ║ ║╠═╝╚╦╝  ╠╩╗║╣  ║ ║║║║╣ ║╣ ║║║  ╚╗╔╝║║╣ ║║║╚═╗
# 🟡 ╚═╝╚═╝╩   ╩   ╚═╝╚═╝ ╩ ╚╩╝╚═╝╚═╝╝╚╝   ╚╝ ╩╚═╝╚╩╝╚═╝ COPY BETWEEN VIEWS
# ===========================================================================
# # 👉 Get TextNotes
# textToCopy = FilteredElementCollector(doc, doc.ActiveView.Id)\
#     .OfCategory(BuiltInCategory.OST_TextNotes)\
#     .WhereElementIsNotElementType()\
#     .ToElementIds()
#
# # 👁 Get Views
# src_view =  doc.ActiveView
# dest_view = select_views(__title__,multiple=False)
#
# # ⚙ Transform & Options
# transform = Transform.Identity
# opts      = CopyPasteOptions()
#
# # # 🔓 Start Transaction
# t = Transaction(doc, __title__)
# t.Start()
#
# # ✔ Copy Elements
# ElementTransformUtils.CopyElements(src_view, textToCopy, dest_view, transform, opts)
#
# # # 🔒 End Transaction
# t.Commit()


# 🟠 ╔═╗╔═╗╔═╗╦ ╦  ╔╗ ╔═╗╔╦╗╦ ╦╔═╗╔═╗╔╗╔  ╔═╗╦═╗╔═╗ ╦╔═╗╔═╗╔╦╗╔═╗
# 🟠 ║  ║ ║╠═╝╚╦╝  ╠╩╗║╣  ║ ║║║║╣ ║╣ ║║║  ╠═╝╠╦╝║ ║ ║║╣ ║   ║ ╚═╗
# 🟠 ╚═╝╚═╝╩   ╩   ╚═╝╚═╝ ╩ ╚╩╝╚═╝╚═╝╝╚╝  ╩  ╩╚═╚═╝╚╝╚═╝╚═╝ ╩ ╚═╝ COPY BETWEEN PROJECTS
# # ===========================================================================
# #👉 Get Walls
# wallsToCopy = FilteredElementCollector(doc)\
#     .OfCategory(BuiltInCategory.OST_Walls)\
#     .WhereElementIsNotElementType()\
#     .ToElementIds()
#
# #🏠Get all Docs
# all_docs = list(app.Documents)
# doc_A = all_docs[0]
# doc_B = all_docs[1]
#
# # ⚙ Transform & Options
# transform = Transform.Identity
# opts      = CopyPasteOptions()
#
#
# # # 🔓 Start Transaction
# t = Transaction(doc_B, __title__)
# t.Start()
#
# # ✔ Copy Elements
# ElementTransformUtils.CopyElements(doc_A, wallsToCopy, doc_B, transform, opts)
#
# # # 🔒 End Transaction
# t.Commit()



