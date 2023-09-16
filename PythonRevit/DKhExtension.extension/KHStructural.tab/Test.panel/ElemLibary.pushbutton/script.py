# -*-coding: utf-8 -*-

__title__ = "Libary Elements" #Name of the button displayed in Revit UI
__doc__   ="""This is simple tool for Elements Library """ #Button Description shown in Revit UI
__version__ = "Version = 1.0"
__doc__ = """ Version = 1.0
Date    = 28.08.2023
_____________________________________________________________________
Description:

Test code about Get all Furniture and Plumbing elements and write Room's name
if available to a comment Parameter.
______________________________________
Author: Dmytro Khom"""
# __context__ =  'active-floor-plan' #Disover more this type. It gives error message!
__highlight__ = "new"


# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# =======================================================================

# Regular + Autodesk
from Autodesk.Revit.DB import *    #Import everything from DB (Very good for beginners and development)


# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ===========================================================================
doc    = __revit__.ActiveUIDocument.Document   #type: UIDocument
uidoc  = __revit__.ActiveUIDocument            #type: Document
app    = __revit__.Application                 #type: UIApplication

active_view = doc.ActiveView
active_level = doc.ActiveView.GenLevel

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
# ===========================================================================
def create_text(origin, text_type):
    """Function to create TextNote at the given location.
    TextType Name is going to be used as Text."""
    text         = text_type.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_NAME).AsString()

    # CREATE TEXT NOTE
    txt = TextNote.Create(doc, active_view.Id, origin, text, text_type.Id)
    return txt

def create_wall(origin, wall_type):
    """Function to create WallType at the given location."""
    pt1   = origin
    pt2   = XYZ(origin.X + 2, origin.Y, origin.Z)
    curve = Line.CreateBound(pt1, pt2)

    # # # CREATE WALL
    H = 10
    O = 0
    flip = False
    struct = False

    wall = Wall.Create(doc, curve, wall_type.Id, active_level.Id, H, O, flip, struct)
    return wall

def create_floor(origin, floor_type):
    """Function to create WallType at the given location."""

    # # POINTS
    pt_0 = XYZ(origin.X, origin.Y,origin.Z)
    pt_1 =  XYZ(origin.X+1, origin.Y,origin.Z)
    pt_2 =  XYZ(origin.X+1, origin.Y+1,origin.Z)
    pt_3 =  XYZ(origin.X, origin.Y+1,origin.Z)
    #
    # # LINES
    l_0 = Line.CreateBound(pt_0, pt_1)
    l_1 = Line.CreateBound(pt_1, pt_2)
    l_2 = Line.CreateBound(pt_2, pt_3)
    l_3 = Line.CreateBound(pt_3, pt_0)
    #
    # # BOUNDARY
    boundary = CurveArray()
    boundary.Append(l_0)
    boundary.Append(l_1)
    boundary.Append(l_2)
    boundary.Append(l_3)
    #
    #
    # # CREATE FLOOR
    new_floor = doc.Create.NewFloor(boundary, floor_type, active_level, False)
    return new_floor

# ╔═╗╦  ╔═╗╔═╗╔═╗╔═╗╔═╗
# ║  ║  ╠═╣╚═╗╚═╗║╣ ╚═╗
# ╚═╝╩═╝╩ ╩╚═╝╚═╝╚═╝╚═╝ CLASSES
# ===========================================================================


# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
# ===========================================================================


# 1️⃣ Get Elements Types
all_walls_types  =  FilteredElementCollector(doc).OfClass(WallType).ToElements()
all_floors_types =  FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).OfClass(FloorType).ToElements()
all_text_types   =  FilteredElementCollector(doc).OfClass(TextNoteType).ToElements()

#🔵 ORIGIN
X = 0
Y = 0
Z = 0

name = "item1"
# 🔓 Start Transaction
t = Transaction(doc, name)
t.Start()


# ✔ Create TextTypes
for txt_type in all_text_types:
    origin  = XYZ(X,Y,Z)
    create_text(origin, txt_type)
    Y -= 2


X += 15
Y = 0


# ✔ Create WallType
for wall_type in all_walls_types:
    origin  = XYZ(X,Y,Z)
    create_wall(origin, wall_type)
    Y -= 2

X += 15
Y = 0

# ✔ Create Floor
for floor_type in all_floors_types:
    origin  = XYZ(X,Y,Z)
    create_floor(origin, floor_type)
    Y -= 2


# 🔒 End Transaction
t.Commit()

