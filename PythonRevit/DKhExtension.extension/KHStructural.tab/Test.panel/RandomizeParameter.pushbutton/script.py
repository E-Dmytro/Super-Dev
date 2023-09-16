# -*-coding: utf-8 -*-

__title__ = "Randomize Parameter" #Name of the button displayed in Revit UI
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
doc        = __revit__.ActiveUIDocument.Document   #type: UIDocument
uidoc      = __revit__.ActiveUIDocument            #type: Document
app        = __revit__.Application                 #type: UIApplication
rvt_year   = int(app.VersionNumber)

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
# ===========================================================================
def get_elements_by_type_name(type_name):
    """Function to get Elements by Type Name."""

    # CREATE RULE
    param_id    = ElementId(BuiltInParameter.ALL_MODEL_TYPE_NAME)
    f_param     = ParameterValueProvider(param_id)
    f_evaluator = FilterStringEquals()
    f_rule      = FilterStringRule(f_param, f_evaluator  , type_name, True)
    # Revit 2023 does not need last argument in f_rule!

    # CREATE FILTER
    filter_type_name = ElementParameterFilter(f_rule)

    # GET ELEMENTS
    return FilteredElementCollector(doc).WherePasses(filter_type_name)\
                          .WhereElementIsNotElementType().ToElements()


def get_elements_by_family_name(family_name):
    """Function to get Elements by Family Name."""

    # CREATE RULE
    param_id    = ElementId(BuiltInParameter.ALL_MODEL_TYPE_NAME)
    f_param     = ParameterValueProvider(param_id)
    f_evaluator = FilterStringEquals()
    f_rule      = FilterStringRule(f_param, f_evaluator  , family_name, True)
    # Revit 2023 does not need last argument in f_rule!

    # CREATE FILTER
    filter_family_name = ElementParameterFilter(f_rule)

    # GET ELEMENTS
    return FilteredElementCollector(doc).WherePasses(filter_family_name)\
                               .WhereElementIsNotElementType().ToElements()

def convert_internal_units (value, get_internal = True, units='m'):
    # type: (float, bool, str) -> float I
    """Function to convert Internal units to meters or vice versa.
    :param value: Value to convert
    :param get_internal: True to get internal units, False to get Meters
    :param units:  Select desired Units: ['m', 'm2']
    :return: Length in Internal units or Meters."""

    if rvt_year >= 2021:
        from Autodesk.Revit.DB import UnitTypeId
        if units == 'm'   : units = UnitTypeId.Meters
        elif units == 'm2': units = UnitTypeId.SquareMeters
        elif units == 'cm': units = UnitTypeId.Centimeters
    else:
        from Autodesk.Revit.DB import DisplayUnitType
        if units == 'm'   : units = DisplayUnitType.DUT_METERS
        elif units == 'm2': units = DisplayUnitType.DUT_SQUARE_METERS
        elif units == 'cm': units = DisplayUnitType.DUT_CENTIMETERS

    if get_internal:
        return UnitUtils.ConvertToInternalUnits(value, units)
    return UnitUtils.ConvertFromInternalUnits(value, units)

def random_step(_min, _max, _step):
    import random
    return random.randrange(_min, _max+1, _step)


# ╔═╗╦  ╔═╗╔═╗╔═╗╔═╗╔═╗
# ║  ║  ╠═╣╚═╗╚═╗║╣ ╚═╗
# ╚═╝╩═╝╩ ╩╚═╝╚═╝╚═╝╚═╝ CLASSES
# ===========================================================================


# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
# ===========================================================================



# 1️⃣ Variables
# family_name = 'Vertical Blade'
# type_name   = 'Vertical Blade'
# parma_name  = 'Tiefe'
# _min        = 40
# _max        = 250
# _step       = 10


# 1️⃣ Variables (Custom UI)

from rpw.ui.forms import (FlexForm, Label, ComboBox, TextBox, TextBox,Separator, Button, CheckBox)

components = [Label("Element's Type Name:"), TextBox('type_name', Text="Default Value"),
              Label('Parameter Name'), TextBox('param_name', Text="Default Value"),
              Separator(),
              Label('Min Value(in cm)'), TextBox('_min', Text="40"),
              Label('Max Value(in cm)'), TextBox('_max', Text="250"),
              Label('Step Value(in cm)'), TextBox('_step', Text="10"),
              Separator(),
              Button('Select')]

form = FlexForm('Title', components)
form.show()

value = form.values
type_name   = values ['type_name']
parma_name  = values ['param_name']
_min        = float(values ['_min'])
_max        = float(values ['_max'])
_step       = float(values ['_step'])

# User selects `Opt 1`, types 'Wood' in TextBox, and select Checkbox
# form.values
# {'combobox1': 10.0, 'textbox1': 'Wood', 'checkbox': True}




# 2️ Get Elements
elements = get_elements_by_family_name(type_name)
# elements = get_elements_by_family_name(family_name)


# 3️⃣ Write Random Parameter Values

t = Transaction(doc, __title__)
t.Start() # 🔓

for el in elements:
    p = el.LookupParameter(parma_name)

    if p:
        value_cm = random_step(_min, _max, _step)
        value_ft = convert_internal_units(value_cm, get_internal=True, units='cm')
        p.Set(value_ft)







t.Commit() #🔒







# 🔷 Bonus: Custom UI



