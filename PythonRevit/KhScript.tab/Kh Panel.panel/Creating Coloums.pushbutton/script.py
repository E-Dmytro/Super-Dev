# -*- coding: UTF-8 -*-
import Autodesk
from Autodesk.Revit.DB import *
doc = __revit__.ActiveUIDocument.Document

columns = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralColumns).WhereElementIsElementType().ToElements()
levels = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType().ToElements()

for level in levels:
	elevation = level.get_Parameter(BuiltInParameter.LEVEL_ELEV).AsDouble()
	if elevation:
		level_0 = level
for column in columns:
	column_name = column.get_Parameter(BuiltInParameter.ALL_MODEL_FAMILY_NAME).AsString()
	if column_name == 'CircleColumn':
		column_type = column



t = Transaction(doc, 'column')
t.Start()
column_type.Activate()
col = doc.Create.NewFamilyInstance(XYZ(0,0,level_0.Elevation), column_type, level_0, Structure.StructuralType.Column)
top_offset = col.get_Parameter(BuiltInParameter.FAMILY_TOP_LEVEL_OFFSET_PARAM)
top_offset.Set(6000/304.8)
t.Commit()
