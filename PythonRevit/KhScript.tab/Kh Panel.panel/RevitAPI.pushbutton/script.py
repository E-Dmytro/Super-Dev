# -*- coding:utf-8 -*-
#
#TODO VARIABLES
#

__title__ = "05 - Create/Delete/Copy Elements"
__author__ = "Dmytro Khom"
__version__ = "Version 1.0"
__doc__ = """Version = 1.0
Date  =06-10-2022

Description:
Code from YouTube tutorial about Creating/Deleting/Copying Elements
using Revit API.

Author: Dmytro Khom"""



#* IMPORTS


import imp
from webbrowser import get
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import StructuralType

#* .NET IMPORTS


import clr
import symbol
clr.AddReference('System')
from System.Collections.Generic import List

#
#
# 
# 
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app =  __revit__.Application

active_view  = doc.ActiveView
active_level = doc.ActiveView.GenLevel


# 
#TODO MAIN
# 


with Transaction(doc, __title__) as t:
    t.Start()
    #* CHANGES HERE 

    
    #
    ##TODO TEXT
    #
    
    # C#
    # temp = """
    # public static TextNote Create(
	# Document document, - doc
	# ElementId viewId, - active_view.Id
	# XYZ position, - pt
	# string text, - text
	# ElementId typeId
    # )
    # """
    
    # #* ARGUMENTS
    
    # text_type_id = FilteredElementCollector(doc).OfClass(TextNoteType).FirstElementId()
    # pt      = XYZ(0,0,0)
    # text    = 'Hello BIM World'
    
    # # CREATE TEXT NOTE 
    
    # TextNote.Create(doc, active_view.Id, pt, text, text_type_id )


    # 
    ##TODO ROOM
    #
    
    # #*ARGUMENTS
    # pt = UV(10,0)
    
    # # CREATE ROOM
    # room = doc.Create.NewRoom(active_level, pt)
    
    # # CREATE ROOM TAG
    # room_link = LinkElementId(room.Id)
    # doc.Create.NewRoomTag( room_link, pt, active_view.Id ) 
    
    # # C#
    # temp = """RoomTag NewRoomTag(
    #                     LinkElementId roomId,
    #                     UV point,
    #                     ElementId viewId
    #                 )
    #                 """
    
    
    #    
    #TODO LINES
    #

    # pt_start = XYZ(20, 0, 0 )
    # pt_end = XYZ(20, 5, 0)
    # curve = Line.CreateBound(pt_start, pt_end)


    # detail_line = doc.Create.NewDetailCurve(active_view, curve)


    #    
    #TODO WALL
    #

    # temp = """public static Wall Create(
	# Document document,
	# Curve curve,
	# ElementId levelId,
	# bool structural
    # )"""
    
    # # ARGUMENTS 
    # pt_start = XYZ(100, 0, 0 )
    # pt_end = XYZ(100, 50, 0)
    # curve = Line.CreateBound(pt_start, pt_end)
    
    # # CREATE A WALL
    # wall = Wall.Create(doc,curve, active_level.Id, False)

    #    
    #TODO WINDOWS
    #
    
    # host_wall = doc.GetElement(ElementId(349252))
    
    # #
    # # temp = """ public FamilyInstance NewFamilyInstance(
	# # XYZ location,
	# # FamilySymbol symbol,
	# # Element host,
	# # StructuralType structuralType
    # # )
    # # """
    # pt_start = XYZ(100, 0, 0 )
    # pt_end = XYZ(100, 50, 0)
    # pt_mid = (pt_start + pt_end)/2
    # window_type = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Windows)\
    #                                         .WhereElementIsElementType().FirstElement()

    # # window_type = doc.GetElement(ElementId(349286))
    
    # # CREATE A WINDOW
    # window = doc.Create.NewFamilyInstance(pt_mid, window_type, host_wall, StructuralType.NonStructural )
    
    #    
    #TODO FAMILY INSTANCE
    #
    #EXTRA FUNCTION
    def get_type_by_name(type_name):
        """Extra Function to get Family Type by name"""
        # CREATE RULE
        param_type = ElementId(BuiltInParameter.ALL_MODEL_TYPE_NAME)
        f_param = ParameterValueProvider(param_type)
        evaluator = FilterStringEquals()
        f_rule = FilterStringRule(f_param, evaluator, type_name, True) #Revit 2023 does not need last argument!
    
        # CREATE FILTER
        filter_type_name = ElementParameterFilter(f_rule)
    
        # GET ELEMENTS 
        return FilteredElementCollector(doc).WherePasses(filter_type_name).WhereElementIsElementType().FirstElement()    
    
    # temp = """ NewFamilyInstance(
    #     XYZ location,
    #     FamilySymbol symbol, 
    #     StructuralType structuralType
    # )"""
    
    # ARGUMENTS
    pt = XYZ(40, 50, 0)
    symbol = get_type_by_name("1525 x 762mm")
    
    
    # CREATE AN ELEMENT
    element = doc.Create.NewFamilyInstance(pt, symbol, StructuralType.NonStructural)
    
    
    


















































#
##TODO DELETE ELEMENTS
#


    t.Commit()