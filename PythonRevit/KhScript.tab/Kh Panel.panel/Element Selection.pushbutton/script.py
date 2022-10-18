# -*- coding: UTF-8 -*-
import Autodesk

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

# # 1 Select Element
#
# sel = uidoc.Selection.PickObject(Selection.ObjectType.Element, 'Choose element')
# el = doc.GetElement(sel)
#
# t= Transaction(doc, 'selection')
# t.Start()
# par1 = el.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
# par1.Set('Text_1')
# t.Commit()


#  # 2 Select Multiplate Elements
# sel = uidoc.Selection.PickObject(Selection.ObjectType.Element, 'Choose element')
# # el = []
# # for i in sel:
# #     el = doc.GetElement(i)
# #     els.append(el)
# els = [doc.GetElement(elId) for elId in sel]
# t = Transaction(doc, 'selection')
# t.Start()
# for i in els:
#     par1 = el.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
#     par1.Set('Text_1')
# t.Commit()

# 3 Single Category

sel = uidoc.Selection.PickObject(Selection.ObjectType.Element, Single_Category('Structural Columns'))

els = [doc.GetElement(elId) for elId in sel]
t = Transaction(doc, 'selection')
t.Start()
for i in els:
    par1 = el.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
    par1.Set('Text_1')
t.Commit()
