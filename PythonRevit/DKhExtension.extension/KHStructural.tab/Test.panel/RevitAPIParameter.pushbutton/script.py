# -*-coding: utf-8 -*-

__title__ = "RevitAPI: Parameters" #Name of the button displayed in Revit UI
__doc__   ="""This script is part of YouTube video.""" #Button Description shown in Revit UI

__doc__ = """ Version = 1.0
Date    = 20.08.2022
_________________________________________
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




# ╔═╗╔═╗╔╦╗  ╦ ╦╔═╗╦  ╦
# ║ ╦║╣  ║   ║║║╠═╣║  ║
# ╚═╝╚═╝ ╩   ╚╩╝╩ ╩╩═╝╩═╝ GET WALL
# ===========================================================================


wall_id = ElementId(563362)
wall    = doc.GetElement(wall_id)



# print(list(wall.Parameters))




# ╔═╗╔═╗╦═╗╔═╗╔╦╗╔═╗╔╦╗╔═╗╦═╗╔═╗
# ╠═╝╠═╣╠╦╝╠═╣║║║║╣  ║ ║╣ ╠╦╝╚═╗
# ╩  ╩ ╩╩╚═╩ ╩╩ ╩╚═╝ ╩ ╚═╝╩╚═╚═╝ PARAMETERS
# ===========================================================================

# print("*"*100)
# print('*** Parameters: ***')

# for p in wall.Parameters:
#     if p.Definition.Name == 'Comments':
#         print ("It's a comment parameter!")
#         print (p.Id)
    # print (p)
    # print('.Name:             {}'.format(p.Definition.Name))
    # print('.BuiltInParameter: {}'.format(p.Definition.BuiltInParameter))
    # print('StorageType:                  {}'.format(p.StorageType))
    # print('IsShared:                     {}'.format(p.IsShared))
    # print('IsReadOn0ly:                  {}'.format(p.IsReadOnly))
    # print ("-"*50)


# ╔═╗╔═╗╔╦╗  ╔╗ ╦ ╦╦╦ ╔╦╗  ╦╔╗╔  ╔═╗╔═╗╦═╗╔═╗╔╦╗╔═╗╔╦╗╔═╗╦═╗╔═╗
# ║ ╦║╣  ║   ╠╩╗║ ║║║  ║───║║║║  ╠═╝╠═╣╠╦╝╠═╣║║║║╣  ║ ║╣ ╠╦╝╚═╗
# ╚═╝╚═╝ ╩   ╚═╝╚═╝╩╩═╝╩   ╩╝╚╝  ╩  ╩ ╩╩╚═╩ ╩╩ ╩╚═╝ ╩ ╚═╝╩╚═╚═╝ GET BUILT-IN PARAMETERS
# ===========================================================================


# print("*"*100)
# print('*** BuiltInParameter: ***')
# wall_comments  = wall.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
# wall_type_name = wall.get_Parameter(BuiltInParameter.ELEM_TYPE_PARAM).AsValueString()
# # print (wall_comments.AsString())
# # print (wall_type_name)
#
# print('.Name:              {}'.format(wall_comments.Definition.Name))
# print('.BuiltInParameter:  {}'.format(wall_comments.Definition.BuiltInParameter))
# print('StorageType:        {}'.format(wall_comments.StorageType))
# print('IsShared:           {}'.format(wall_comments.IsShared))
# print('IsReadOn0ly:        {}'.format(wall_comments.IsReadOnly))
# print ("-"*50)
#
# print (wall_comments.AsString())

# # GET PROJECT/SHARED PARAMETER
#
# print('*** Getting Shared Parameters: ***')
#
# # sp_text = wall.LookupParameter('Option1')
# # print (sp_text.AsString())
#
# sp_mat_id = wall.LookupParameter('O_Material').AsElementId()
# sp_mat    = doc.GetElement(sp_mat_id)
# print (sp_mat)
# print (sp_mat.Name)
#
# sp_text = wall.LookupParameter('Option1')
# print (sp_text.AsString())

# GET TYPE PARAMETER

# print("*"*100)
# print('*** GET TYPE PARAMETERS ***')
#
# wall_type = wall.WallType
# wall_type_description = wall_type.get_Parameter(BuiltInParameter.ALL_MODEL_DESCRIPTION)
# wall_type_mark        = wall_type.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_MARK)
# print (wall_type_description.AsString())
# print (wall_type_mark.AsString())

# ╔═╗╔═╗╔╦╗  ╔═╗╔═╗╦═╗╔═╗╔╦╗╔═╗╔╦╗╔═╗╦═╗  ╦  ╦╔═╗╦  ╦ ╦╔═╗
# ╚═╗║╣  ║   ╠═╝╠═╣╠╦╝╠═╣║║║║╣  ║ ║╣ ╠╦╝  ╚╗╔╝╠═╣║  ║ ║║╣
# ╚═╝╚═╝ ╩   ╩  ╩ ╩╩╚═╩ ╩╩ ╩╚═╝ ╩ ╚═╝╩╚═   ╚╝ ╩ ╩╩═╝╚═╝╚═╝ SET PARAMETER VALUE
# ===========================================================================

# wall_comments  = wall.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
# wall_type_name = wall.LookupParameter('Option1')
#
#
# t = Transaction(doc, __title__)
# t.Start()
# wall_type_name.Set('That was terrible joke.')
# print(wall_comments.AsString())
# # changes here
# t.Commit()

# ╔═╗╦ ╦╔═╗╔╦╗╔═╗╔╦╗  ╔╦╗╔═╗╔═╗╦
# ║  ║ ║╚═╗ ║ ║ ║║║║   ║ ║ ║║ ║║
# ╚═╝╚═╝╚═╝ ╩ ╚═╝╩ ╩   ╩ ╚═╝╚═╝╩═╝ CUSTOM TOOL
# ===========================================================================

t = Transaction(doc,'Writing ElementID to Mark parameter of Walls.')
t.Start()
# SET WALL ELEMENT-ID TO MARK
all_walls = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()

for wall in all_walls:
    wall_mark = wall.get_Parameter(BuiltInParameter.ALL_MODEL_MARK)
    wall_mark.Set(str(wall.Id))
    print (wall.Id)

t.Commit()

print ("The script finished")