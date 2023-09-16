# -*-coding: utf-8 -*-

__title__ = "Furniture Room" #Name of the button displayed in Revit UI
__doc__   ="""This is simple tool to Copy Elemement With Revit API """ #Button Description shown in Revit UI
__version__ = "Version = 1.0"
__doc__ = """ Version = 1.0
Date    = 26.08.2023
_____________________________________________________________________
Description:

Test code about Get all Furniture and Plumbing elements and write Room's name
if available to a comment Parameter.
______________________________________
Author: Dmytro Khom"""
__author__ = "Dmytro Khom"




# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# =======================================================================

# Regular + Autodesk
from Autodesk.Revit.DB import *    #Import everything from DB (Very good for beginners and development)
from Autodesk.Revit.UI import UIDocument, UIApplication

# .NET IMPORT
import clr
clr.AddReference('System')


# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ===========================================================================
# from pyrevit.revit import uidoc, doc, app #Alternative
doc    = __revit__.ActiveUIDocument.Document   #type: UIDocument
uidoc  = __revit__.ActiveUIDocument            #type: Document
app    = __revit__.Application                 #type: UIApplication

all_phases = list(doc.Phases)
phase = all_phases[-1]

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


# 1️⃣ Get Elements
all_furniture =  FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Furniture).WhereElementIsNotElementType().ToElements()
all_f_system  =  FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_FurnitureSystems).WhereElementIsNotElementType().ToElements()
all_plumbing   =  FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_PlumbingFixtures).WhereElementIsNotElementType().ToElements()

all_elements  =  list(all_furniture) + list(all_f_system) + list(all_plumbing)

# 🔓 Start Transaction
t = Transaction(doc, __title__)
t.Start()

# 2️ Iterate and get Rooms

for el in all_elements:
    room = el.Room[phase]

    if room:
        # 3️⃣ Read Room Name and Number
        # room_name   = room.Name
        # room_name   = Element.Name.GetValue(room)
        room_name   = room.get_Parameter(BuiltInParameter.ROOM_NAME).AsString()
        room_number = room.Number


        # 4️⃣ Get Element Parameters
        p_room_name    = el.LookupParameter('Room Name')
        p_room_number  = el.LookupParameter('Room Number')

        # 5️⃣ Write Room Name and Number to Parameters
        if p_room_name:
            p_room_name.Set(room_name)
        if p_room_number:
            p_room_number.Set(room_number)

# 🔒 End Transaction
t.Commit()

