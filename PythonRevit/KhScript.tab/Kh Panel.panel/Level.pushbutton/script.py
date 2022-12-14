# -*- coding: UTF-8 -*-

# from logging import _Level
import Autodesk
from Autodesk.Revit.DB import *
doc = __revit__.ActiveUIDocument.Document

t = Transaction(doc, 'grid')
t.Start()
level_1 = Level.Create(doc, 3000/304.8)
level_2 = Level.Create(doc, 6000/304.8)

level_1_name = level_1.get_Parameter(BuiltInParameter.DATUM_TEXT)
level_1_name.Set('Second Floor')
t.Commit()
