# -*-coding: utf-8 -*-

__title__ = "Add Levels Elevation" #Name of the button displayed in Revit UI
__doc__   ="""This tool will add/update your level name to have its elevation.""" #Button Description shown in Revit UI

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
# __helpurl__ = "www.youtube.com" #TO DO: Update URL
__highlight__ = "new"
__min_revit_ver__  = 2019
__max_revit_ver__  = 2022
# __context__ = ['Walls', 'Floors', 'Roofs'] # Make your button available only when certain categories are selected


# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# =======================================================================

# Regular + Autodesk
import os, sys, math, datetime, time
from Autodesk.Revit.DB import * #Import everything from DB (Very good for beginners and development)
from Autodesk.Revit.DB import Transaction, Element, ElementId, FilteredElementCollector, Level, BuiltInCategory

# pyRevit
from pyrevit import revit, forms

# Custom Imports
from Snippets._selection import get_selected_elements
from Snippets._convert import convert_internal_to_m


# .NET Import
import clr
clr.AddReference("System")
from System.Collections.Generic import List  #List<ElementType>() <- it's special type of kist that RevitAPI often requires.

# list_elements_ids = [ElementId(546771), ElementId(546771)] # Let's imagine these are real element Ids...
# List_element_ids= List[ElementId](list_elements_ids)
#
# uidoc.Selection.SetElementIds(List_element_ids)

# for e_id in list_elements_ids:
#     List_element_ids.Add(e_id)


# from System.Collections.Generic import List #List<Element() <- it's special type of list that RevitAPI often requires.

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ===========================================================================
# from pyrevit.revit import uidoc, doc, app #Alternative
doc    = __revit__.ActiveUIDocument.Document
uidoc  = __revit__.ActiveUIDocument
app    = __revit__.Application
PATHSCRIPT = os.path.dirname(__file__)

# Symbols

symbol_start = "."
symbol_end   = "."


# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
# ===========================================================================

def get_text_in_bracket(text, symbol_start, symbol_end):
    # type(str,str,str) -> str
    """Function to get content between 2 symbols
     :param text:           Initial Text
     :param symbol_start:   Start Symbol
     :param symbol_end:     End_Symbol
     :return:               Text between 2 symbols, if found.
     e.g. get_text_in_bracket('This is [not] very important message.', '[', ']') -> 'not'"""
    if symbol_start in text and symbol_end in text:
        start = text.find(symbol_start) + len(symbol_start)
        stop  = text.find(symbol_end)
        return text[start:stop]
    return ""

# ╔═╗╦  ╔═╗╔═╗╔═╗╔═╗╔═╗
# ║  ║  ╠═╣╚═╗╚═╗║╣ ╚═╗
# ╚═╝╩═╝╩ ╩╚═╝╚═╝╚═╝╚═╝ CLASSES
# ===========================================================================


# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN


# GET all Levels

all_levels = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType().ToElements()
t = Transaction(doc, __title__)
t.Start()
# Get Levels Eleveations
for lvl in all_levels:
    lvl_elevation = lvl.Elevation
    lvl_elevation_m = round(convert_internal_to_m(lvl.Elevation), 2)
    lvl_elevation_m_str = "+" + str(lvl_elevation_m) if lvl.Elevation > 0 else str(lvl_elevation_m)

    #ELEVATION EXISTS (update)
    if symbol_start in lvl.Name and symbol_end in lvl.Name:
        current_value = get_text_in_bracket(lvl.Name, symbol_start, symbol_end)
        new_name = lvl.Name.replace(current_value, lvl_elevation_m_str)
    #
    # # ELEVATION DOES NOT EXIST (new)
    # else:
    #     elevation_value = symbol_start + lvl_elevation_m_str + symbol_end
    #     new_name = lvl.Name + elevation_value

    elevation_value = symbol_start + lvl_elevation_m_str + symbol_end
    new_name = lvl.Name + elevation_value


    try:
        current_name = lvl.Name
        lvl.Name = new_name
        print ('Renamed: {} -> {}'.format(current_name, new_name))
    except:
        print ("Could not change Level's name... ")

t.Commit()

    # if lvl.Elevation > 0:
    #     var = '+' + str(lvl_elevation_m)
    # else:
    #     var = str(lvl_elevation_m)



