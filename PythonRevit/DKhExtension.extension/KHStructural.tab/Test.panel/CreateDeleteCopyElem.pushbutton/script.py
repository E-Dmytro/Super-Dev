# -*-coding: utf-8 -*-

__title__ = "Create Delete Copy Elements" #Name of the button displayed in Revit UI
__doc__   ="""This is simple tool to filter an element """ #Button Description shown in Revit UI
__version__ = "Version = 1.0"
__doc__ = """ Version = 1.0
Date    = 20.04.2022
_____________________________________________________________________
Description:

Test code about Creating/Deleting/Copying Elements 
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

active_view  = doc.ActiveView
active_level = doc.ActiveView.GenLevel

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
with Transaction(doc, __title__) as t:
    t.Start()
    #CHANGES HERE

    # ╔╦╗╔═╗═╗ ╦╔╦╗
    #  ║ ║╣ ╔╩╦╝ ║
    #  ╩ ╚═╝╩ ╚═ ╩  TEXT
    # ===========================================================================
    # ## ARGUMENTS
    # text_type_id = FilteredElementCollector(doc).OfClass(TextNoteType).FirstElementId()
    # pt           = XYZ(0,0,0)
    # text         = 'Random Point'
    # ## CREATE TEXT NOTE
    # TextNote.Create(doc, active_view.Id, pt, text, text_type_id)


    # ╦═╗╔═╗╔═╗╔╦╗
    # ╠╦╝║ ║║ ║║║║
    # ╩╚═╚═╝╚═╝╩ ╩  ROOM
    # ===========================================================================
    # # ARGUMENTS
    # pt = UV(100, 0)
    #
    #
    # # CREATE ROOM
    # room      = doc.Create.NewRoom(active_level,pt)
    #
    # # CREATE ROOM TAG
    # room_link = LinkElementId(room.Id)
    # doc.Create.NewRoomTag(room_link, pt, active_view.Id)


    # ╦  ╦╔╗╔╔═╗╔═╗
    # ║  ║║║║║╣ ╚═╗
    # ╩═╝╩╝╚╝╚═╝╚═╝ LINES
    # ===========================================================================
    # # ARGUMENTS
    # pt1   = XYZ(100,0,0)
    # pt2   = XYZ(100,50,0)
    #
    # # CREATE DETAIL LINE
    # curve = Line.CreateBound(pt1, pt2)
    # detail_line = doc.Create.NewDetailCurve(active_view, curve)

    # ╦ ╦╔═╗╦  ╦  ╔═╗
    # ║║║╠═╣║  ║  ╚═╗
    # ╚╩╝╩ ╩╩═╝╩═╝╚═╝ WALLS
    # ===========================================================================
    # # # ARGUMENTS
    # pt1   = XYZ(80, 0, 0)
    # pt2   = XYZ(80, 10, 0)
    #
    # # # CREATE WALL
    # curve = Line.CreateBound(pt1, pt2)
    # wall  = Wall.Create(doc, curve, active_level.Id, False)

    # ╦ ╦╦╔╗╔╔╦╗╔═╗╦ ╦╔═╗
    # ║║║║║║║ ║║║ ║║║║╚═╗
    # ╚╩╝╩╝╚╝═╩╝╚═╝╚╩╝╚═╝ WINDOWS
    # ===========================================================================
    # ARGUMENTS
    # with forms.WarningBar(title='Pick an element'):
    #     element = revit.pick_element()
    # element_type = type(element)
    # if element_type != Wall:
    #     forms.alert('You were supposed to pick a Wall', exitscript=True)
    # host_wall = doc.GetElement(element.Id)
    # pt1 = XYZ(80, 0, 0)
    # pt2 = XYZ(80, 10, 0)
    # pt_mid = (pt1 + pt2) / 2
    # window_type = FilteredElementCollector(doc). \
    #     OfCategory(BuiltInCategory.OST_Windows). \
    #     WhereElementIsElementType() \
    #     .FirstElement()
    #
    # # CREATE WINDOW
    # window = doc.Create.NewFamilyInstance(pt_mid, window_type, host_wall, StructuralType.NonStructural)

    # ╔═╗╔═╗╔╦╗╦╦ ╦ ╦  ╦╔╗╔╔═╗╔╦╗╔═╗╔╗╔╔═╗╔═╗
    # ╠╣ ╠═╣║║║║║ ╚╦╝  ║║║║╚═╗ ║ ╠═╣║║║║  ║╣
    # ╚  ╩ ╩╩ ╩╩╩═╝╩   ╩╝╚╝╚═╝ ╩ ╩ ╩╝╚╝╚═╝╚═╝ FAMILY INSTANCE
    # ===========================================================================
    # # EXTRA FUNCTION
    # def get_type_by_name(type_name):
    #     "Extra Function to get Family Type by name"
    #     # CREATE RULE
    #     param_type        = ElementId(BuiltInParameter.ALL_MODEL_TYPE_NAME)
    #     f_param           = ParameterValueProvider(param_type)
    #     evaluator         = FilterStringEquals()
    #     f_rule            = FilterStringRule(f_param, evaluator, type_name, True) #Revit 2023 doesn't need last argument!
    #
    #     # CREATE FILTER
    #     filter_type_name = ElementParameterFilter(f_rule)
    #
    #     # GET ELEMENTS
    #     return FilteredElementCollector(doc).WherePasses(filter_type_name).WhereElementIsElementType().FirstElement()
    #
    # # ARGUMENTS
    # pt =  XYZ(200,0,0)
    # symbol = get_type_by_name('WorkPlace')
    #
    # # CREATE AN ELEMENT
    # element = doc.Create.NewFamilyInstance(pt, symbol, StructuralType.NonStructural)

    # ╔═╗╦ ╦╔═╗╔═╗╔╦╗╔═╗
    # ╚═╗╠═╣║╣ ║╣  ║ ╚═╗
    # ╚═╝╩ ╩╚═╝╚═╝ ╩ ╚═╝ SHEETS
    # ===========================================================================
    # ARGUMENTS
    # title_block_id = FilteredElementCollector(doc)\
    #     .OfCategory(BuiltInCategory.OST_TitleBlocks)\
    #     .WhereElementIsNotElementType()\
    #     .FirstElementId()
    #
    # # CREATE A NEW SHEET
    #
    # new_sheet = ViewSheet.Create(doc, title_block_id)
    # new_sheet.SheetNumber = 'Random Sheet Number' #<- Unique !
    # new_sheet.Name        = 'Random Name'

    # ╦  ╦╦╔═╗╦ ╦╔═╗
    # ╚╗╔╝║║╣ ║║║╚═╗
    #  ╚╝ ╩╚═╝╚╩╝╚═╝ VIEWS
    # ===========================================================================
    # # ARGUMENTS
    # all_view_type = FilteredElementCollector(doc).OfClass(ViewFamilyType).ToElements()
    # view_3D_type  = [vt for vt in all_view_type if vt.ViewFamily == ViewFamily.ThreeDimensional][0]
    # #
    # # CREATE A NEW SHEET
    # #
    # new_3D        = View3D.CreateIsometric(doc, view_3D_type.Id)

    # ╦═╗╔═╗╔═╗╦╔═╗╔╗╔
    # ╠╦╝║╣ ║ ╦║║ ║║║║
    # ╩╚═╚═╝╚═╝╩╚═╝╝╚╝ REGION
    # ===========================================================================

    # # ARGUMENTS
    # region_type_id = doc.GetDefaultElementTypeId(ElementTypeGroup.FilledRegionType)
    #
    # # POINTS
    # pt_0 =  XYZ(50,0,0)
    # pt_1 =  XYZ(55,0,0)
    # pt_2 =  XYZ(55,5,0)
    # pt_3 =  XYZ(50,5,0)
    #
    # # LINES
    # l_0 = Line.CreateBound(pt_0, pt_1)
    # l_1 = Line.CreateBound(pt_1, pt_2)
    # l_2 = Line.CreateBound(pt_2, pt_3)
    # l_3 = Line.CreateBound(pt_3, pt_0)
    #
    # # BOUNDARY
    # boundary = CurveLoop()
    # boundary.Append(l_0)
    # boundary.Append(l_1)
    # boundary.Append(l_2)
    # boundary.Append(l_3)
    #
    # # LIST OF BOUNDARIES
    # list_boundaries = List[CurveLoop]()
    # list_boundaries.Add(boundary)
    #
    # # CREATE FILLED REGION
    # region = FilledRegion.Create(doc, region_type_id, active_view.Id, list_boundaries)

    # ╔═╗╦  ╔═╗╔═╗╦═╗
    # ╠╣ ║  ║ ║║ ║╠╦╝
    # ╚  ╩═╝╚═╝╚═╝╩╚═ FLOOR
    # ===========================================================================
    # # ARGUMENTS
    # floor_type_id = doc.GetDefaultElementTypeId(ElementTypeGroup.FloorType)
    # floor_type    = doc.GetElement(floor_type_id)
    #
    # # POINTS
    # pt_0 =  XYZ(60,0,0)
    # pt_1 =  XYZ(65,0,0)
    # pt_2 =  XYZ(65,5,0)
    # pt_3 =  XYZ(60,5,0)
    #
    # # LINES
    # l_0 = Line.CreateBound(pt_0, pt_1)
    # l_1 = Line.CreateBound(pt_1, pt_2)
    # l_2 = Line.CreateBound(pt_2, pt_3)
    # l_3 = Line.CreateBound(pt_3, pt_0)
    #
    # # BOUNDARY
    # boundary = CurveArray()
    # boundary.Append(l_0)
    # boundary.Append(l_1)
    # boundary.Append(l_2)
    # boundary.Append(l_3)
    #
    #
    # # CREATE FLOOR
    # new_floor = doc.Create.NewFloor(boundary, floor_type, active_level, False)


    # ╔═╗╔═╗╔═╗╦ ╦  ╔═╗╦  ╔═╗╔╦╗╔═╗╔╗╔╔╦╗╔═╗
    # ║  ║ ║╠═╝╚╦╝  ║╣ ║  ║╣ ║║║║╣ ║║║ ║ ╚═╗
    # ╚═╝╚═╝╩   ╩   ╚═╝╩═╝╚═╝╩ ╩╚═╝╝╚╝ ╩ ╚═╝ COPY ELEMENTS
    # ===========================================================================
    # # GET ELEMENTS TO COPY
    # all_floor_in_view = FilteredElementCollector(doc, active_view.Id)\
    #     .OfCategory(BuiltInCategory.OST_Floors)\
    #     .WhereElementIsNotElementType()\
    #     .ToElementIds()
    # element_to_copy = List[ElementId](all_floor_in_view)
    #
    # # COPY ELEMENTS (Multiple Times)
    # for i in range(1,6):
    #     vector = XYZ(0, 10*i, 0)
    #     ElementTransformUtils.CopyElements(doc, element_to_copy, vector)

    # ╔╦╗╔═╗╦  ╔═╗╔╦╗╔═╗  ╔═╗╦  ╔═╗╔╦╗╔═╗╔╗╔╔╦╗╔═╗
    #  ║║║╣ ║  ║╣  ║ ║╣   ║╣ ║  ║╣ ║║║║╣ ║║║ ║ ╚═╗
    # ═╩╝╚═╝╩═╝╚═╝ ╩ ╚═╝  ╚═╝╩═╝╚═╝╩ ╩╚═╝╝╚╝ ╩ ╚═╝ DELETE ELEMENTS
    # ===========================================================================
    # # GET ELEMENTS TO COPY
    # all_floor_in_view = FilteredElementCollector(doc, active_view.Id)\
    #     .OfCategory(BuiltInCategory.OST_Floors)\
    #     .WhereElementIsNotElementType()\
    #     .ToElementIds()
    # element_to_delete = List[ElementId](all_floor_in_view)
    #
    # # DELETE ELEMENTS
    # doc.Delete(element_to_delete)
    #
    #
    #
    # t.Commit()





# ===========================================================================
