# -*- coding: UTF-8 -*-
from ctypes import Structure
from math import floor
import Autodesk
from Autodesk.Revit.DB import *
doc = __revit__.ActiveUIDocument.Document


levels = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType().ToElements()
slabs = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsElementType().ToElements()

p_1 = XYZ(0, 0, 0)
p_2 = XYZ(0, 100, 0)
p_3 = XYZ(100, 100, 0)
p_4 = XYZ(100, 0, 0)


line_1 = Line.CreateBound(p_1, p_2)
line_2 = Line.CreateBound(p_2, p_3)
line_3 = Line.CreateBound(p_3, p_4)
line_4 = Line.CreateBound(p_4, p_1)
 





for level in levels:
	elevation = level.get_Parameter(BuiltInParameter.LEVEL_ELEV).AsDouble()
	if elevation:
		level_0 = level

for slab in slabs:
	name = slab.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString()
	if name == 'C20/25 200мм':
		floorType = slab	

curveArray = CurveArray()
curveArray.Append(line_1)
curveArray.Append(line_2)
curveArray.Append(line_3)
curveArray.Append(line_4)
t = Transaction(doc, 'column')
t.Start()
slab_new = doc.Create.NewFloor(curveArray, floorType, level_0, Structure.StructuralType.Footing)
offset = slab_new.get_Parameter(BuiltInParameter.FLOOR_HEIGHTABOVELEVEL_PARAM)
offset.Set(0)
t.Commit()