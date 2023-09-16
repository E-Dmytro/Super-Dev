# -*- coding: UTF-8 -*-
from module0 import *
import clr
import sys
import Autodesk

from Autodesk.Revit.DB import *
from Autodesk.Revit.Exceptions import *

from Autodesk.Revit.UI import *
#from Autodesk.Revit.UI.Selection import *

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

RS = Autodesk.Revit.DB.Structure
import math
curview = uidoc.ActiveGraphicalView
from operator import itemgetter
__doc__='Arm beam'
__author__ = 'Dmytro Khom'

from Autodesk.Revit.UI import IExternalEventHandler, IExternalApplication, Result, ExternalEvent, IExternalCommand
from Autodesk.Revit.DB import Transaction
from Autodesk.Revit.Exceptions import InvalidOperationException, OperationCanceledException, ArgumentException
import rpw
from rpw import revit, DB, UI
from pyrevit.forms import WPFWindow
import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from operator import itemgetter
import math
import sys
from Autodesk.Revit.UI.Selection import *
from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.Exceptions import *
RS = Autodesk.Revit.DB.Structure
import System
from System.Collections.Generic import List


#path=os.path.dirname(os.path.abspath(__file__))

class CustomISelectionFilter(ISelectionFilter):
	def __init__(self, nom_categorie):
		self.nom_categorie = nom_categorie
	def AllowElement(self, e):
		if e.Category.Name == self.nom_categorie:
			return True
		else:
			return False
	def AllowReference(self, ref, point):
		return true
def filter_sel(filter_name):
    filter=CustomISelectionFilter(filter_name)
    return filter

clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

import System.Drawing
import System.Windows.Forms
from System.Drawing import *
from System.Windows.Forms import *
import os
path=os.path.dirname(os.path.abspath(__file__))

all_rebar_types = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rebar).WhereElementIsElementType().ToElements()
rebar_bar_types = []
rebar_hook_types = []
rebar_shapes = []
for rebar_type in all_rebar_types:
	name = rebar_type.GetType().Name
	if name == "RebarBarType":
		rebar_bar_types.append(rebar_type)
	if name == "RebarHookType":
		rebar_hook_types.append(rebar_type)
list_r=[]
list_h=[]
for rebar in rebar_bar_types:
	#d = str(int(rebar.BarDiameter*304.8))
	list_r.append(rebar.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString())
for rebar in rebar_hook_types:
	#d = str(int(rebar.BarDiameter*304.8))
	list_h.append(rebar.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString())

import os
path=os.path.dirname(os.path.abspath(__file__))
MarginWidth = 2
MarginHeight = 2



class CustomizableEvent:
    def __init__(self):
        """ An instance of this class need to be created before any modeless operation.
        You can then call the raise_event method to perform any modeless operation.
        Any modification to Revit DB need to be performed inside a valid Transaction.
        This Transaction needs to be open inside the function_or_method, NOT before calling raise_event.
        >>> customizable_event = CustomizableEvent()
        >>> customizable_event.raise_event(rename_views, views_and_names)
        """
        # Create an handler instance and his associated ExternalEvent
        custom_handler = _CustomHandler()
        custom_handler.customizable_event = self
        self.custom_event = UI.ExternalEvent.Create(custom_handler)

        # Initialise raise_event variables
        self.function_or_method = None
        self.args = ()
        self.kwargs = {}

    def _raised_method(self):
        """ !!! DO NOT USE THIS METHOD IN YOUR SCRIPT !!!
        Method executed by IExternalEventHandler.Execute when ExternalEvent is raised by ExternalEvent.Raise.
        """
        self.function_or_method(*self.args, **self.kwargs)

    def raise_event(self, function_or_method, *args, **kwargs):
        """
        Method used to raise an external event with custom function and parameters
        Example :
        >>> customizable_event = CustomizableEvent()
        >>> customizable_event.raise_event(rename_views, views_and_names)
        """
        self.args = args
        self.kwargs = kwargs
        self.function_or_method = function_or_method
        self.custom_event.Raise()

class _CustomHandler(UI.IExternalEventHandler):
    """ Subclass of IExternalEventHandler intended to be used in CustomizableEvent class
    Input : function or method. Execute input in a IExternalEventHandler"""
    def __init__(self):
        self.customizable_event = None

    # Execute method run in Revit API environment.
    # noinspection PyPep8Naming, PyUnusedLocal
    def Execute(self, application):
        try:
            self.customizable_event._raised_method()
        except InvalidOperationException:
            # If you don't catch this exeption Revit may crash.
            print ("InvalidOperationException catched")

    # noinspection PyMethodMayBeStatic, PyPep8Naming
    def GetName(self):
        return "Execute an function or method in a IExternalHandler"


customizable_event = CustomizableEvent()
class Form1(Form):
	def __init__(self):
		self.InitializeComponent()
		self._values_main=[]
		self._values_1=[]
		self._values_2=[]

	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		#resources = System.Resources.ResourceManager("Form1", System.Reflection.Assembly.GetEntryAssembly())
		self._tabControl1 = System.Windows.Forms.TabControl()
		self._tabPage1 = System.Windows.Forms.TabPage()
		self._button_Save = System.Windows.Forms.Button()
		self._button_Load = System.Windows.Forms.Button()
		self._button_saveAs = System.Windows.Forms.Button()
		self._textBox_saveAs = System.Windows.Forms.TextBox()
		self._tabPage4 = System.Windows.Forms.TabPage()
		self._button_Ok = System.Windows.Forms.Button()
		self._button_cancel = System.Windows.Forms.Button()
		self._comboBox_save = System.Windows.Forms.ComboBox()
		self._imageList1 = System.Windows.Forms.ImageList(self._components)
		self._vertRebar_M1_1 = System.Windows.Forms.ComboBox()
		self._vertRebar_M1_3 = System.Windows.Forms.ComboBox()
		self._vertRebar_M1_2 = System.Windows.Forms.ComboBox()
		self._vertRebar_M1_4 = System.Windows.Forms.ComboBox()
		self._textBox_M1_16 = System.Windows.Forms.TextBox()
		self._textBox_M1_12 = System.Windows.Forms.TextBox()
		self._textBox_M1_2 = System.Windows.Forms.TextBox()
		self._textBox_M1_1 = System.Windows.Forms.TextBox()
		self._textBox_M1_17 = System.Windows.Forms.TextBox()
		self._textBox_M1_18 = System.Windows.Forms.TextBox()
		self._comboBox_1_2 = System.Windows.Forms.ComboBox()
		self._label_1_2 = System.Windows.Forms.Label()
		self._label_1_1 = System.Windows.Forms.Label()
		self._comboBox_1_1 = System.Windows.Forms.ComboBox()
		self._textBox_4_1 = System.Windows.Forms.TextBox()
		self._textBox_4_2 = System.Windows.Forms.TextBox()
		self._textBox_4_3 = System.Windows.Forms.TextBox()
		self._textBox_4_5 = System.Windows.Forms.TextBox()
		self._textBox_4_7 = System.Windows.Forms.TextBox()
		self._textBox_4_8 = System.Windows.Forms.TextBox()
		self._textBox_4_10 = System.Windows.Forms.TextBox()
		self._textBox_4_4 = System.Windows.Forms.TextBox()
		self._textBox_4_6 = System.Windows.Forms.TextBox()
		self._textBox_4_9 = System.Windows.Forms.TextBox()
		self._textBox_4_11 = System.Windows.Forms.TextBox()
		self._label_4_1 = System.Windows.Forms.Label()
		self._label_4_2 = System.Windows.Forms.Label()
		self._comboBox_4_2 = System.Windows.Forms.ComboBox()
		self._textBox_4_12 = System.Windows.Forms.TextBox()
		self._gor_arm_4_1 = System.Windows.Forms.ComboBox()
		self._gor_arm_4_2 = System.Windows.Forms.ComboBox()
		self._gor_arm_4_3 = System.Windows.Forms.ComboBox()
		self._gor_arm_4_4 = System.Windows.Forms.ComboBox()
		self._gor_arm_4_5 = System.Windows.Forms.ComboBox()
		self._label_4_5 = System.Windows.Forms.Label()
		self._label_4_6 = System.Windows.Forms.Label()
		self._label_4_7 = System.Windows.Forms.Label()
		self._label_4_8 = System.Windows.Forms.Label()
		self._label_4_9 = System.Windows.Forms.Label()
		self._label_4_4 = System.Windows.Forms.Label()
		self._button_select = System.Windows.Forms.Button()
		self._pictureBox_1_1 = System.Windows.Forms.PictureBox()
		self._vertRebar_M1_5 = System.Windows.Forms.ComboBox()
		self._vertRebar_M1_6 = System.Windows.Forms.ComboBox()
		self._textBox_M1_9 = System.Windows.Forms.TextBox()
		self._textBox_M1_10 = System.Windows.Forms.TextBox()
		self._textBox_M1_11 = System.Windows.Forms.TextBox()
		self._textBox_M1_13 = System.Windows.Forms.TextBox()
		self._textBox_M1_14 = System.Windows.Forms.TextBox()
		self._textBox_M1_15 = System.Windows.Forms.TextBox()
		self._textBox_M1_4 = System.Windows.Forms.TextBox()
		self._textBox_M1_8 = System.Windows.Forms.TextBox()
		self._textBox_M1_7 = System.Windows.Forms.TextBox()
		self._textBox_M1_6 = System.Windows.Forms.TextBox()
		self._textBox_M1_5 = System.Windows.Forms.TextBox()
		self._vertRebar_M1_7 = System.Windows.Forms.ComboBox()
		self._pictureBox1 = System.Windows.Forms.PictureBox()
		self._textBox_4_13 = System.Windows.Forms.TextBox()
		self._textBox_4_14 = System.Windows.Forms.TextBox()
		self._tabControl1.SuspendLayout()
		self._tabPage1.SuspendLayout()
		self._tabPage4.SuspendLayout()
		self._pictureBox_1_1.BeginInit()
		self._pictureBox1.BeginInit()
		self.SuspendLayout()
		#
		# tabControl1
		#
		self._tabControl1.Controls.Add(self._tabPage1)
		self._tabControl1.Controls.Add(self._tabPage4)
		self._tabControl1.Location = System.Drawing.Point(3, 43)
		self._tabControl1.Name = "tabControl1"
		self._tabControl1.SelectedIndex = 0
		self._tabControl1.Size = System.Drawing.Size(680, 493)
		self._tabControl1.TabIndex = 0
		#
		# tabPage1
		#
		self._tabPage1.BackColor = System.Drawing.SystemColors.Control
		self._tabPage1.Controls.Add(self._comboBox_1_2)
		self._tabPage1.Controls.Add(self._textBox_M1_1)
		self._tabPage1.Controls.Add(self._comboBox_1_1)
		self._tabPage1.Controls.Add(self._textBox_M1_2)
		self._tabPage1.Controls.Add(self._textBox_M1_5)
		self._tabPage1.Controls.Add(self._textBox_M1_6)
		self._tabPage1.Controls.Add(self._textBox_M1_7)
		self._tabPage1.Controls.Add(self._textBox_M1_8)
		self._tabPage1.Controls.Add(self._textBox_M1_4)
		self._tabPage1.Controls.Add(self._textBox_M1_15)
		self._tabPage1.Controls.Add(self._textBox_M1_17)
		self._tabPage1.Controls.Add(self._textBox_M1_18)
		self._tabPage1.Controls.Add(self._label_1_2)
		self._tabPage1.Controls.Add(self._textBox_M1_14)
		self._tabPage1.Controls.Add(self._label_1_1)
		self._tabPage1.Controls.Add(self._textBox_M1_13)
		self._tabPage1.Controls.Add(self._textBox_M1_11)
		self._tabPage1.Controls.Add(self._textBox_M1_10)
		self._tabPage1.Controls.Add(self._textBox_M1_9)
		self._tabPage1.Controls.Add(self._textBox_M1_12)
		self._tabPage1.Controls.Add(self._textBox_M1_16)
		self._tabPage1.Controls.Add(self._pictureBox_1_1)
		self._tabPage1.Controls.Add(self._vertRebar_M1_6)
		self._tabPage1.Controls.Add(self._vertRebar_M1_5)
		self._tabPage1.Controls.Add(self._vertRebar_M1_7)
		self._tabPage1.Controls.Add(self._vertRebar_M1_4)
		self._tabPage1.Controls.Add(self._vertRebar_M1_2)
		self._tabPage1.Controls.Add(self._vertRebar_M1_3)
		self._tabPage1.Controls.Add(self._vertRebar_M1_1)
		self._tabPage1.Location = System.Drawing.Point(4, 22)
		self._tabPage1.Name = "tabPage1"
		self._tabPage1.Padding = System.Windows.Forms.Padding(3)
		self._tabPage1.Size = System.Drawing.Size(672, 467)
		self._tabPage1.TabIndex = 0
		self._tabPage1.Text = "Повздовжні стрижні"
		#
		# button_Save
		#
		self._button_Save.Location = System.Drawing.Point(12, 12)
		self._button_Save.Name = "button_Save"
		self._button_Save.Size = System.Drawing.Size(75, 23)
		self._button_Save.TabIndex = 1
		self._button_Save.Text = "Зберегти"
		self._button_Save.UseVisualStyleBackColor = True
		self._button_Save.Click += self.Button_SaveClick
		#
		# button_Load
		#
		self._button_Load.Location = System.Drawing.Point(93, 12)
		self._button_Load.Name = "button_Load"
		self._button_Load.Size = System.Drawing.Size(75, 23)
		self._button_Load.TabIndex = 1
		self._button_Load.Text = "Завантажити"
		self._button_Load.UseVisualStyleBackColor = True
		self._button_Load.Click += self.Button_LoadClick
		#
		# button_saveAs
		#
		self._button_saveAs.Location = System.Drawing.Point(427, 12)
		self._button_saveAs.Name = "button_saveAs"
		self._button_saveAs.Size = System.Drawing.Size(88, 23)
		self._button_saveAs.TabIndex = 1
		self._button_saveAs.Text = "Зберегти як"
		self._button_saveAs.UseVisualStyleBackColor = True
		self._button_saveAs.Click += self.Button_saveAsClick
		#
		# textBox_saveAs
		#
		self._textBox_saveAs.Location = System.Drawing.Point(521, 15)
		self._textBox_saveAs.Name = "textBox_saveAs"
		self._textBox_saveAs.Size = System.Drawing.Size(149, 20)
		self._textBox_saveAs.TabIndex = 2
		#
		# tabPage4
		#
		self._tabPage4.BackColor = System.Drawing.SystemColors.Control
		self._tabPage4.Controls.Add(self._gor_arm_4_5)
		self._tabPage4.Controls.Add(self._gor_arm_4_4)
		self._tabPage4.Controls.Add(self._gor_arm_4_3)
		self._tabPage4.Controls.Add(self._gor_arm_4_2)
		self._tabPage4.Controls.Add(self._gor_arm_4_1)
		self._tabPage4.Controls.Add(self._comboBox_4_2)
		self._tabPage4.Controls.Add(self._label_4_4)
		self._tabPage4.Controls.Add(self._label_4_2)
		self._tabPage4.Controls.Add(self._label_4_9)
		self._tabPage4.Controls.Add(self._label_4_8)
		self._tabPage4.Controls.Add(self._label_4_7)
		self._tabPage4.Controls.Add(self._label_4_6)
		self._tabPage4.Controls.Add(self._label_4_5)
		self._tabPage4.Controls.Add(self._label_4_1)
		self._tabPage4.Controls.Add(self._textBox_4_11)
		self._tabPage4.Controls.Add(self._textBox_4_10)
		self._tabPage4.Controls.Add(self._textBox_4_9)
		self._tabPage4.Controls.Add(self._textBox_4_8)
		self._tabPage4.Controls.Add(self._textBox_4_12)
		self._tabPage4.Controls.Add(self._textBox_4_7)
		self._tabPage4.Controls.Add(self._textBox_4_6)
		self._tabPage4.Controls.Add(self._textBox_4_4)
		self._tabPage4.Controls.Add(self._textBox_4_5)
		self._tabPage4.Controls.Add(self._textBox_4_3)
		self._tabPage4.Controls.Add(self._textBox_4_14)
		self._tabPage4.Controls.Add(self._textBox_4_2)
		self._tabPage4.Controls.Add(self._textBox_4_13)
		self._tabPage4.Controls.Add(self._textBox_4_1)
		self._tabPage4.Controls.Add(self._pictureBox1)
		self._tabPage4.Location = System.Drawing.Point(4, 22)
		self._tabPage4.Name = "tabPage4"
		self._tabPage4.Padding = System.Windows.Forms.Padding(3)
		self._tabPage4.Size = System.Drawing.Size(672, 467)
		self._tabPage4.TabIndex = 3
		self._tabPage4.Text = "Арматурні хомути"
		#
		# button_Ok
		#
		self._button_Ok.Location = System.Drawing.Point(261, 542)
		self._button_Ok.Name = "button_Ok"
		self._button_Ok.Size = System.Drawing.Size(75, 23)
		self._button_Ok.TabIndex = 1
		self._button_Ok.Text = "Ок"
		self._button_Ok.UseVisualStyleBackColor = True
		self._button_Ok.Click += self.Button_OkClick
		#
		# button_cancel
		#
		self._button_cancel.Location = System.Drawing.Point(365, 542)
		self._button_cancel.Name = "button_cancel"
		self._button_cancel.Size = System.Drawing.Size(75, 23)
		self._button_cancel.TabIndex = 1
		self._button_cancel.Text = "Скасувати"
		self._button_cancel.UseVisualStyleBackColor = True
		self._button_cancel.Click += self.Button_cancelClick
		#
		# comboBox_save
		#
		self._comboBox_save.FormattingEnabled = True
		self._comboBox_save.Location = System.Drawing.Point(174, 14)
		self._comboBox_save.Name = "comboBox_save"
		self._comboBox_save.Size = System.Drawing.Size(234, 21)
		self._comboBox_save.TabIndex = 3
		location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
		location_2 = os.path.realpath(os.path.join(location + '/options/'))
		for f in os.listdir(location_2):
			file_name, file_ext = os.path.splitext(f)
			self._comboBox_save.Items.Add(file_name)
		#
		# imageList1
		#
		self._imageList1.ColorDepth = System.Windows.Forms.ColorDepth.Depth32Bit
		self._imageList1.ImageSize = System.Drawing.Size(46, 25)
		self._imageList1.Images.Add(Image.FromFile(path+"\img\icon_3_5.PNG"))
		self._imageList1.Images.Add(Image.FromFile(path+"\img\icon_3_6.PNG"))
		self._list_6 = [0, 1]
		for idx, val in enumerate(self._imageList1.Images):
			if idx in self._list_6:
				self._comboBox_1_1.Items.Add(val)
				self._comboBox_1_2.Items.Add(val)
		#
		# vertRebar_M1_1
		#
		self._vertRebar_M1_1.FormattingEnabled = True
		self._vertRebar_M1_1.Location = System.Drawing.Point(328, 52)
		self._vertRebar_M1_1.Items.AddRange(System.Array[System.Object](list_r))
		self._vertRebar_M1_1.Name = "vertRebar_M1_1"
		self._vertRebar_M1_1.Size = System.Drawing.Size(121, 21)
		self._vertRebar_M1_1.TabIndex = 0
		self._vertRebar_M1_1.SelectedIndex = 0

		#
		# vertRebar_M1_3
		#
		self._vertRebar_M1_3.Enabled = True
		self._vertRebar_M1_3.FormattingEnabled = True
		self._vertRebar_M1_3.Location = System.Drawing.Point(328, 106)
		self._vertRebar_M1_3.Items.AddRange(System.Array[System.Object](list_r))
		self._vertRebar_M1_3.Name = "vertRebar_M1_3"
		self._vertRebar_M1_3.Size = System.Drawing.Size(121, 21)
		self._vertRebar_M1_3.TabIndex = 0
		self._vertRebar_M1_3.SelectedIndex = 0
		#
		# vertRebar_M1_2
		#
		self._vertRebar_M1_2.Enabled = True
		self._vertRebar_M1_2.FormattingEnabled = True
		self._vertRebar_M1_2.Location = System.Drawing.Point(328, 79)
		self._vertRebar_M1_2.Items.AddRange(System.Array[System.Object](list_r))
		self._vertRebar_M1_2.Name = "vertRebar_M1_2"
		self._vertRebar_M1_2.Size = System.Drawing.Size(121, 21)
		self._vertRebar_M1_2.TabIndex = 0
		self._vertRebar_M1_2.SelectedIndex = 0
		#
		# vertRebar_M1_4
		#
		self._vertRebar_M1_4.Enabled = True
		self._vertRebar_M1_4.FormattingEnabled = True
		self._vertRebar_M1_4.Location = System.Drawing.Point(328, 223)
		self._vertRebar_M1_4.Items.AddRange(System.Array[System.Object](list_r))
		self._vertRebar_M1_4.Name = "vertRebar_M1_4"
		self._vertRebar_M1_4.Size = System.Drawing.Size(121, 21)
		self._vertRebar_M1_4.TabIndex = 0
		self._vertRebar_M1_4.SelectedIndex = 0

		#
		# textBox_M1_16
		#
		self._textBox_M1_16.Location = System.Drawing.Point(266, 184)
		self._textBox_M1_16.Name = "textBox_M1_16"
		self._textBox_M1_16.Size = System.Drawing.Size(52, 20)
		self._textBox_M1_16.TabIndex = 2
		self._textBox_M1_16.Text = "0"
		#
		# textBox_M1_12
		#
		self._textBox_M1_12.Enabled = True
		self._textBox_M1_12.Location = System.Drawing.Point(266, 144)
		self._textBox_M1_12.Name = "textBox_M1_12"
		self._textBox_M1_12.Size = System.Drawing.Size(52, 20)
		self._textBox_M1_12.TabIndex = 2
		self._textBox_M1_12.Text = "30"
		#
		# textBox_M1_2
		#
		self._textBox_M1_2.Enabled = True
		self._textBox_M1_2.Location = System.Drawing.Point(27, 53)
		self._textBox_M1_2.Name = "textBox_M1_2"
		self._textBox_M1_2.Size = System.Drawing.Size(52, 20)
		self._textBox_M1_2.TabIndex = 2
		self._textBox_M1_2.Text = "30"
		#
		# textBox_M1_1
		#
		self._textBox_M1_1.Enabled = True
		self._textBox_M1_1.Location = System.Drawing.Point(27, 18)
		self._textBox_M1_1.Name = "textBox_M1_1"
		self._textBox_M1_1.Size = System.Drawing.Size(52, 20)
		self._textBox_M1_1.TabIndex = 2
		self._textBox_M1_1.Text = "30"
		#
		# textBox_M1_17
		#
		self._textBox_M1_17.Location = System.Drawing.Point(20, 425)
		self._textBox_M1_17.Name = "textBox_M1_17"
		self._textBox_M1_17.Size = System.Drawing.Size(136, 20)
		self._textBox_M1_17.TabIndex = 1
		self._textBox_M1_17.Text = "0"
		#
		# textBox_M1_18
		#
		self._textBox_M1_18.Location = System.Drawing.Point(236, 425)
		self._textBox_M1_18.Name = "textBox_M1_18"
		self._textBox_M1_18.Size = System.Drawing.Size(136, 20)
		self._textBox_M1_18.TabIndex = 1
		self._textBox_M1_18.Text = "0"
		#
		# comboBox_1_2
		#
		self._comboBox_1_2.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed
		self._comboBox_1_2.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._comboBox_1_2.FormattingEnabled = True
		self._comboBox_1_2.ItemHeight = 30
		self._comboBox_1_2.Location = System.Drawing.Point(236, 383)
		self._comboBox_1_2.Name = "comboBox_1_2"
		self._comboBox_1_2.Size = System.Drawing.Size(82, 36)
		self._comboBox_1_2.TabIndex = 8
		self._comboBox_1_2.DrawItem += self.cboDrawImage_DrawItem
		self._comboBox_1_2.SelectedIndex = 0
		#
		# label_1_2
		#
		self._label_1_2.Location = System.Drawing.Point(236, 357)
		self._label_1_2.Name = "label_1_2"
		self._label_1_2.Size = System.Drawing.Size(165, 23)
		self._label_1_2.TabIndex = 2
		self._label_1_2.Text = "Розміщення нижніх стрижнів"
		#
		# label_1_1
		#
		self._label_1_1.Location = System.Drawing.Point(20, 357)
		self._label_1_1.Name = "label_1_1"
		self._label_1_1.Size = System.Drawing.Size(169, 23)
		self._label_1_1.TabIndex = 2
		self._label_1_1.Text = "Розміщення верхніх стрижнів"
		#
		# comboBox_1_1
		#
		self._comboBox_1_1.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed
		self._comboBox_1_1.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._comboBox_1_1.FormattingEnabled = True
		self._comboBox_1_1.ItemHeight = 30
		self._comboBox_1_1.Location = System.Drawing.Point(20, 383)
		self._comboBox_1_1.Name = "comboBox_1_1"
		self._comboBox_1_1.Size = System.Drawing.Size(82, 36)
		self._comboBox_1_1.DrawItem += self.cboDrawImage_DrawItem
		self._comboBox_1_1.TabIndex = 8
		self._comboBox_1_1.SelectedIndex = 0
		#
		# textBox_4_1
		#
		self._textBox_4_1.Location = System.Drawing.Point(15, 136)
		self._textBox_4_1.Name = "textBox_4_1"
		self._textBox_4_1.Size = System.Drawing.Size(50, 20)
		self._textBox_4_1.TabIndex = 1
		self._textBox_4_1.Text = "50"
		#
		# textBox_4_2
		#
		self._textBox_4_2.Location = System.Drawing.Point(488, 136)
		self._textBox_4_2.Name = "textBox_4_2"
		self._textBox_4_2.Size = System.Drawing.Size(50, 20)
		self._textBox_4_2.TabIndex = 1
		self._textBox_4_2.Text = "50"
		#
		# textBox_4_3
		#
		self._textBox_4_3.Location = System.Drawing.Point(212, 240)
		self._textBox_4_3.Name = "textBox_4_3"
		self._textBox_4_3.Size = System.Drawing.Size(44, 20)
		self._textBox_4_3.TabIndex = 2
		self._textBox_4_3.Text = "100"
		#
		# textBox_4_5
		#
		self._textBox_4_5.Enabled = False
		self._textBox_4_5.Location = System.Drawing.Point(212, 266)
		self._textBox_4_5.Name = "textBox_4_5"
		self._textBox_4_5.Size = System.Drawing.Size(44, 20)
		self._textBox_4_5.TabIndex = 2
		#
		# textBox_4_7
		#
		self._textBox_4_7.Location = System.Drawing.Point(212, 292)
		self._textBox_4_7.Name = "textBox_4_7"
		self._textBox_4_7.Size = System.Drawing.Size(44, 20)
		self._textBox_4_7.TabIndex = 2
		self._textBox_4_7.Text = "200"
		#
		# textBox_4_8
		#
		self._textBox_4_8.Enabled = False
		self._textBox_4_8.Location = System.Drawing.Point(212, 318)
		self._textBox_4_8.Name = "textBox_4_8"
		self._textBox_4_8.Size = System.Drawing.Size(44, 20)
		self._textBox_4_8.TabIndex = 2
		#
		# textBox_4_10
		#
		self._textBox_4_10.Location = System.Drawing.Point(212, 344)
		self._textBox_4_10.Name = "textBox_4_10"
		self._textBox_4_10.Size = System.Drawing.Size(44, 20)
		self._textBox_4_10.TabIndex = 2
		self._textBox_4_10.Text = "100"
		#
		# textBox_4_4
		#
		self._textBox_4_4.Location = System.Drawing.Point(278, 240)
		self._textBox_4_4.Name = "textBox_4_4"
		self._textBox_4_4.Size = System.Drawing.Size(44, 20)
		self._textBox_4_4.TabIndex = 2
		self._textBox_4_4.Text = "10"
		#
		# textBox_4_6
		#
		self._textBox_4_6.Enabled = False
		self._textBox_4_6.Location = System.Drawing.Point(278, 266)
		self._textBox_4_6.Name = "textBox_4_6"
		self._textBox_4_6.Size = System.Drawing.Size(44, 20)
		self._textBox_4_6.TabIndex = 2
		#
		# textBox_4_9
		#
		self._textBox_4_9.Enabled = False
		self._textBox_4_9.Location = System.Drawing.Point(278, 318)
		self._textBox_4_9.Name = "textBox_4_9"
		self._textBox_4_9.Size = System.Drawing.Size(44, 20)
		self._textBox_4_9.TabIndex = 2
		#
		# textBox_4_11
		#
		self._textBox_4_11.Location = System.Drawing.Point(278, 344)
		self._textBox_4_11.Name = "textBox_4_11"
		self._textBox_4_11.Size = System.Drawing.Size(44, 20)
		self._textBox_4_11.TabIndex = 2
		self._textBox_4_11.Text = "10"
		#
		# label_4_1
		#
		self._label_4_1.Location = System.Drawing.Point(222, 214)
		self._label_4_1.Name = "label_4_1"
		self._label_4_1.Size = System.Drawing.Size(34, 23)
		self._label_4_1.TabIndex = 3
		self._label_4_1.Text = "Крок"
		#
		# label_4_2
		#
		self._label_4_2.Location = System.Drawing.Point(278, 214)
		self._label_4_2.Name = "label_4_2"
		self._label_4_2.Size = System.Drawing.Size(56, 23)
		self._label_4_2.TabIndex = 3
		self._label_4_2.Text = "Кількість"
		#
		# comboBox_4_2
		#
		self._comboBox_4_2.FormattingEnabled = True
		self._comboBox_4_2.Enabled = False
		self._comboBox_4_2.Items.AddRange(System.Array[System.Object](
			["Точна відстань",
			"Список відстаней"]))
		self._comboBox_4_2.Location = System.Drawing.Point(278, 292)
		self._comboBox_4_2.Name = "comboBox_4_2"
		self._comboBox_4_2.Size = System.Drawing.Size(186, 21)
		self._comboBox_4_2.TabIndex = 4
		#
		# textBox_4_12
		#
		self._textBox_4_12.Location = System.Drawing.Point(470, 293)
		self._textBox_4_12.Enabled = False
		self._textBox_4_12.Name = "textBox_4_12"
		self._textBox_4_12.Size = System.Drawing.Size(167, 20)
		self._textBox_4_12.TabIndex = 2
		#
		# gor_arm_4_1
		#
		self._gor_arm_4_1.Enabled = False
		self._gor_arm_4_1.FormattingEnabled = True
		self._gor_arm_4_1.Items.AddRange(System.Array[System.Object](list_r))
		self._gor_arm_4_1.Location = System.Drawing.Point(53, 236)
		self._gor_arm_4_1.Name = "gor_arm_4_1"
		self._gor_arm_4_1.Size = System.Drawing.Size(136, 21)
		self._gor_arm_4_1.TabIndex = 4
		#
		# gor_arm_4_2
		#
		self._gor_arm_4_2.Enabled = False
		self._gor_arm_4_2.FormattingEnabled = True
		self._gor_arm_4_2.Items.AddRange(System.Array[System.Object](list_r))
		self._gor_arm_4_2.Location = System.Drawing.Point(53, 263)
		self._gor_arm_4_2.Name = "gor_arm_4_2"
		self._gor_arm_4_2.Size = System.Drawing.Size(136, 21)
		self._gor_arm_4_2.TabIndex = 4
		#
		# gor_arm_4_3
		#
		self._gor_arm_4_3.FormattingEnabled = True
		self._gor_arm_4_3.Items.AddRange(System.Array[System.Object](list_r))
		self._gor_arm_4_3.Location = System.Drawing.Point(53, 290)
		self._gor_arm_4_3.Name = "gor_arm_4_3"
		self._gor_arm_4_3.Size = System.Drawing.Size(136, 21)
		self._gor_arm_4_3.TabIndex = 4
		self._gor_arm_4_3.SelectedIndex = 0
		#
		# gor_arm_4_4
		#
		self._gor_arm_4_4.Enabled = False
		self._gor_arm_4_4.FormattingEnabled = True
		self._gor_arm_4_4.Items.AddRange(System.Array[System.Object](list_r))
		self._gor_arm_4_4.Location = System.Drawing.Point(53, 317)
		self._gor_arm_4_4.Name = "gor_arm_4_4"
		self._gor_arm_4_4.Size = System.Drawing.Size(136, 21)
		self._gor_arm_4_4.TabIndex = 4
		#
		# gor_arm_4_5
		#
		self._gor_arm_4_5.Enabled = False
		self._gor_arm_4_5.FormattingEnabled = True
		self._gor_arm_4_5.Items.AddRange(System.Array[System.Object](list_r))
		self._gor_arm_4_5.Location = System.Drawing.Point(53, 344)
		self._gor_arm_4_5.Name = "gor_arm_4_5"
		self._gor_arm_4_5.Size = System.Drawing.Size(136, 21)
		self._gor_arm_4_5.TabIndex = 4
		#self._gor_arm_4_5.SelectedIndex = 0
		#
		# label_4_5
		#
		self._label_4_5.Location = System.Drawing.Point(23, 236)
		self._label_4_5.Name = "label_4_5"
		self._label_4_5.Size = System.Drawing.Size(22, 23)
		self._label_4_5.TabIndex = 3
		self._label_4_5.Text = "1"
		#
		# label_4_6
		#
		self._label_4_6.Location = System.Drawing.Point(23, 263)
		self._label_4_6.Name = "label_4_6"
		self._label_4_6.Size = System.Drawing.Size(22, 23)
		self._label_4_6.TabIndex = 3
		self._label_4_6.Text = "2"
		#
		# label_4_7
		#
		self._label_4_7.Location = System.Drawing.Point(23, 290)
		self._label_4_7.Name = "label_4_7"
		self._label_4_7.Size = System.Drawing.Size(22, 23)
		self._label_4_7.TabIndex = 3
		self._label_4_7.Text = "3"
		#
		# label_4_8
		#
		self._label_4_8.Location = System.Drawing.Point(23, 317)
		self._label_4_8.Name = "label_4_8"
		self._label_4_8.Size = System.Drawing.Size(22, 23)
		self._label_4_8.TabIndex = 3
		self._label_4_8.Text = "4"
		#
		# label_4_9
		#
		self._label_4_9.Location = System.Drawing.Point(23, 344)
		self._label_4_9.Name = "label_4_9"
		self._label_4_9.Size = System.Drawing.Size(22, 23)
		self._label_4_9.TabIndex = 3
		self._label_4_9.Text = "5"
		#
		# label_4_4
		#
		self._label_4_4.Location = System.Drawing.Point(77, 210)
		self._label_4_4.Name = "label_4_4"
		self._label_4_4.Size = System.Drawing.Size(95, 23)
		self._label_4_4.TabIndex = 3
		self._label_4_4.Text = "Тип арматури"
		#
		# button_select
		#
		self._button_select.Location = System.Drawing.Point(21, 542)
		self._button_select.Name = "button_select"
		self._button_select.Size = System.Drawing.Size(175, 23)
		self._button_select.TabIndex = 1
		self._button_select.Text = "Вибрати балки"
		self._button_select.UseVisualStyleBackColor = True
		self._button_select.Click += self.Button_selectClick
		#
		# pictureBox_1_1
		#
		self._pictureBox_1_1.Image = Image.FromFile(path+"\img\Main1_1.PNG")
		self._pictureBox_1_1.Location = System.Drawing.Point(86, 17)
		self._pictureBox_1_1.Name = "pictureBox_1_1"
		self._pictureBox_1_1.Size = System.Drawing.Size(184, 329)
		self._pictureBox_1_1.TabIndex = 1
		self._pictureBox_1_1.TabStop = False
		#
		# vertRebar_M1_5
		#
		self._vertRebar_M1_5.Enabled = True
		self._vertRebar_M1_5.FormattingEnabled = True
		self._vertRebar_M1_5.Location = System.Drawing.Point(328, 251)
		self._vertRebar_M1_5.Items.AddRange(System.Array[System.Object](list_r))
		self._vertRebar_M1_5.Name = "vertRebar_M1_5"
		self._vertRebar_M1_5.Size = System.Drawing.Size(121, 21)
		self._vertRebar_M1_5.TabIndex = 0
		self._vertRebar_M1_5.SelectedIndex = 0

		#
		# vertRebar_M1_6
		#
		self._vertRebar_M1_6.Enabled = True
		self._vertRebar_M1_6.FormattingEnabled = True
		self._vertRebar_M1_6.Location = System.Drawing.Point(328, 278)
		self._vertRebar_M1_6.Items.AddRange(System.Array[System.Object](list_r))
		self._vertRebar_M1_6.Name = "vertRebar_M1_6"
		self._vertRebar_M1_6.Size = System.Drawing.Size(121, 21)
		self._vertRebar_M1_6.TabIndex = 0
		self._vertRebar_M1_6.SelectedIndex = 0
		#
		# textBox_M1_9
		#
		self._textBox_M1_9.Enabled = True
		self._textBox_M1_9.Location = System.Drawing.Point(266, 53)
		self._textBox_M1_9.Name = "textBox_M1_9"
		self._textBox_M1_9.Size = System.Drawing.Size(52, 20)
		self._textBox_M1_9.TabIndex = 2
		self._textBox_M1_9.Text = "4"
		#
		# textBox_M1_10
		#
		self._textBox_M1_10.Enabled = True
		self._textBox_M1_10.Location = System.Drawing.Point(266, 80)
		self._textBox_M1_10.Name = "textBox_M1_10"
		self._textBox_M1_10.Size = System.Drawing.Size(52, 20)
		self._textBox_M1_10.TabIndex = 2
		self._textBox_M1_10.Text = "0"
		#
		# textBox_M1_11
		#
		self._textBox_M1_11.Enabled = True
		self._textBox_M1_11.Location = System.Drawing.Point(266, 106)
		self._textBox_M1_11.Name = "textBox_M1_11"
		self._textBox_M1_11.Size = System.Drawing.Size(52, 20)
		self._textBox_M1_11.TabIndex = 2
		self._textBox_M1_11.Text = "0"
		#
		# textBox_M1_13
		#
		self._textBox_M1_13.Enabled = True
		self._textBox_M1_13.Location = System.Drawing.Point(266, 224)
		self._textBox_M1_13.Name = "textBox_M1_13"
		self._textBox_M1_13.Size = System.Drawing.Size(52, 20)
		self._textBox_M1_13.TabIndex = 2
		self._textBox_M1_13.Text = "0"
		#
		# textBox_M1_14
		#
		self._textBox_M1_14.Enabled = True
		self._textBox_M1_14.Location = System.Drawing.Point(266, 251)
		self._textBox_M1_14.Name = "textBox_M1_14"
		self._textBox_M1_14.Size = System.Drawing.Size(52, 20)
		self._textBox_M1_14.TabIndex = 2
		self._textBox_M1_14.Text = "0"
		#
		# textBox_M1_15
		#
		self._textBox_M1_15.Enabled = True
		self._textBox_M1_15.Location = System.Drawing.Point(266, 279)
		self._textBox_M1_15.Name = "textBox_M1_15"
		self._textBox_M1_15.Size = System.Drawing.Size(52, 20)
		self._textBox_M1_15.TabIndex = 2
		self._textBox_M1_15.Text = "4"
		#
		# textBox_M1_4
		#
		self._textBox_M1_4.Enabled = True
		self._textBox_M1_4.Location = System.Drawing.Point(27, 308)
		self._textBox_M1_4.Name = "textBox_M1_4"
		self._textBox_M1_4.Size = System.Drawing.Size(52, 20)
		self._textBox_M1_4.TabIndex = 2
		self._textBox_M1_4.Text = "30"
		#
		# textBox_M1_8
		#
		self._textBox_M1_8.Enabled = True
		self._textBox_M1_8.Location = System.Drawing.Point(50, 278)
		self._textBox_M1_8.Name = "textBox_M1_8"
		self._textBox_M1_8.Size = System.Drawing.Size(52, 20)
		self._textBox_M1_8.TabIndex = 2
		self._textBox_M1_8.Text = "50"
		#
		# textBox_M1_7
		#
		self._textBox_M1_7.Enabled = True
		self._textBox_M1_7.Location = System.Drawing.Point(50, 251)
		self._textBox_M1_7.Name = "textBox_M1_7"
		self._textBox_M1_7.Size = System.Drawing.Size(52, 20)
		self._textBox_M1_7.TabIndex = 2
		self._textBox_M1_7.Text = "50"
		#
		# textBox_M1_6
		#
		self._textBox_M1_6.Enabled = True
		self._textBox_M1_6.Location = System.Drawing.Point(40, 132)
		self._textBox_M1_6.Name = "textBox_M1_6"
		self._textBox_M1_6.Size = System.Drawing.Size(52, 20)
		self._textBox_M1_6.TabIndex = 2
		self._textBox_M1_6.Text = "50"
		#
		# textBox_M1_5
		#
		self._textBox_M1_5.Enabled = True
		self._textBox_M1_5.Location = System.Drawing.Point(40, 106)
		self._textBox_M1_5.Name = "textBox_M1_5"
		self._textBox_M1_5.Size = System.Drawing.Size(52, 20)
		self._textBox_M1_5.TabIndex = 2
		self._textBox_M1_5.Text = "50"
		#
		# vertRebar_M1_7
		#
		self._vertRebar_M1_7.Enabled = True
		self._vertRebar_M1_7.FormattingEnabled = True
		self._vertRebar_M1_7.Location = System.Drawing.Point(328, 184)
		self._vertRebar_M1_7.Items.AddRange(System.Array[System.Object](list_r))
		self._vertRebar_M1_7.Name = "vertRebar_M1_7"
		self._vertRebar_M1_7.Size = System.Drawing.Size(121, 21)
		self._vertRebar_M1_7.TabIndex = 0
		self._vertRebar_M1_7.SelectedIndex = 0
		#
		# pictureBox1
		#
		self._pictureBox1.Image = Image.FromFile(path+"\img\Main2_1.PNG")
		self._pictureBox1.Location = System.Drawing.Point(30, 43)
		self._pictureBox1.Name = "pictureBox1"
		self._pictureBox1.Size = System.Drawing.Size(478, 135)
		self._pictureBox1.TabIndex = 5
		self._pictureBox1.TabStop = False
		#
		# textBox_4_13
		#
		self._textBox_4_13.Location = System.Drawing.Point(30, 17)
		self._textBox_4_13.Name = "textBox_4_13"
		self._textBox_4_13.Size = System.Drawing.Size(50, 20)
		self._textBox_4_13.TabIndex = 1
		self._textBox_4_13.Text = "0"
		#
		# textBox_4_14
		#
		self._textBox_4_14.Location = System.Drawing.Point(458, 17)
		self._textBox_4_14.Name = "textBox_4_14"
		self._textBox_4_14.Size = System.Drawing.Size(50, 20)
		self._textBox_4_14.TabIndex = 1
		self._textBox_4_14.Text = "0"
		#
		# Form1
		#
		self.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None
		self.ClientSize = System.Drawing.Size(707, 577)
		self.Controls.Add(self._comboBox_save)
		self.Controls.Add(self._textBox_saveAs)
		self.Controls.Add(self._button_saveAs)
		self.Controls.Add(self._button_Load)
		self.Controls.Add(self._button_select)
		self.Controls.Add(self._button_cancel)
		self.Controls.Add(self._button_Ok)
		self.Controls.Add(self._button_Save)
		self.Controls.Add(self._tabControl1)
		self.ImeMode = System.Windows.Forms.ImeMode.On
		self.KeyPreview = True
		self.MaximizeBox = False
		self.MinimizeBox = False
		self.Name = "Form1"
		self.ShowIcon = False
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
		self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Fixed3D
		self.Text = "Армування балки"
		self.TopMost = True
		self._tabControl1.ResumeLayout(False)
		self._tabPage1.ResumeLayout(False)
		self._tabPage1.PerformLayout()
		self._tabPage4.ResumeLayout(False)
		self._tabPage4.PerformLayout()
		self._pictureBox_1_1.EndInit()
		self._pictureBox1.EndInit()
		self.ResumeLayout(False)
		self.PerformLayout()

	def cboDrawImage_DrawItem(self, sender, e):
		e.DrawBackground()
		#img = Image.FromFile(path+'\Vupysk.png')
		if e.Index<0:
			return
		img = sender.Items[e.Index]
		hgt = e.Bounds.Height - 2 * MarginHeight
		scale = float(hgt / img.Height)
		#print([e.Bounds.Height, img.Height, hgt, scale, 52/60])
		wid = img.Width * scale
		rect = RectangleF(e.Bounds.X + MarginWidth, e.Bounds.Y + MarginHeight, img.Width, img.Height)#wid, hgt)
		#print([e.Bounds.X + MarginWidth, e.Bounds.Y + MarginHeight, wid, hgt, scale])
		e.Graphics.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBilinear
		e.Graphics.DrawImage(img, rect);
		e.DrawFocusRectangle();
	def cboDrawImage_MeasureItem(self, sender, e):
		if e.Index < 0:
			return
		img = sender.Items[e.Index]
		e.ItemHeight = img.Height + 2 * MarginHeight
		e.ItemWidth = img.Width + 2 * MarginWidth

	#def label_create(self, tabPage, p1, p2, name, s1, s2, tab, text):
	#	label = System.Windows.Forms.Label()
	#
	#	tabPage.Controls.Add(self._label)
	#	label.Location = System.Drawing.Point(p1, p2)
	#	label.Name = name
	#	label.Size = System.Drawing.Size(s1, s2)
	#	label.TabIndex = tab
	#	label.Text = text

	def Button_selectClick(self, sender, e):
		out_list = []
		self.TopMost = False
		doc = __revit__.ActiveUIDocument.Document
		uidoc = __revit__.ActiveUIDocument
		try:
			sel = uidoc.Selection.PickObjects(ObjectType.Element, 'Виберіть елементи у бажаному порядку і натисніть Esc по завершенню')#Несущие колонны filter_sel('Несущие колонны')
			for i in sel:
				selelem = doc.GetElement(i.ElementId)
				out_list.append(selelem)
		except:
			0

		sender.Tag = out_list
		self.TopMost = True
		Form1.Focus(self)

	def Button_OkClick(self, sender, e):
		self._values_main=[]
		self._values_1=[]
		self._values_2=[]

		self._values_main.append(self._button_select.Tag)#0
		self._values_1.append(self._comboBox_1_1.SelectedIndex)#0
		self._values_1.append(self._comboBox_1_2.SelectedIndex)#1
		self._values_1.append(self.arm(self._vertRebar_M1_1))#2
		self._values_1.append(self.arm(self._vertRebar_M1_2))#3
		self._values_1.append(self.arm(self._vertRebar_M1_3))#4
		self._values_1.append(self.arm(self._vertRebar_M1_4))#5
		self._values_1.append(self.arm(self._vertRebar_M1_5))#6
		self._values_1.append(self.arm(self._vertRebar_M1_6))#7
		self._values_1.append(self.arm(self._vertRebar_M1_7))#8
		self._values_1.append([self._textBox_M1_1.Text, self._textBox_M1_12.Text, self._textBox_M1_4.Text, self._textBox_M1_2.Text])#9
		self._values_1.append([self._textBox_M1_9.Text, self._textBox_M1_10.Text, self._textBox_M1_11.Text, self._textBox_M1_13.Text, self._textBox_M1_14.Text, self._textBox_M1_15.Text, self._textBox_M1_16.Text])#10
		self._values_1.append([self._textBox_M1_5.Text, self._textBox_M1_6.Text, self._textBox_M1_7.Text, self._textBox_M1_8.Text])#11
		self._values_1.append([self._textBox_M1_17.Text, self._textBox_M1_18.Text])#12

		self._values_2.append(self.arm(self._gor_arm_4_1))#0
		self._values_2.append(self.arm(self._gor_arm_4_2))#1
		self._values_2.append(self.arm(self._gor_arm_4_3))#2
		self._values_2.append(self.arm(self._gor_arm_4_4))#3
		self._values_2.append(self.arm(self._gor_arm_4_5))#4
		self._values_2.append(self._textBox_4_1.Text)#5
		self._values_2.append(self._textBox_4_2.Text)#6

		self._values_2.append(self._textBox_4_3.Text)#7
		self._values_2.append(self._textBox_4_4.Text)#8

		self._values_2.append(self._textBox_4_5.Text)#9
		self._values_2.append(self._textBox_4_6.Text)#10

		self._values_2.append(self._textBox_4_7.Text)#11

		self._values_2.append(self._textBox_4_8.Text)#12
		self._values_2.append(self._textBox_4_9.Text)#13

		self._values_2.append(self._textBox_4_10.Text)#14
		self._values_2.append(self._textBox_4_11.Text)#15

		self._values_2.append(self._textBox_4_12.Text)#16

		self._values_2.append(self._textBox_4_13.Text)#17
		self._values_2.append(self._textBox_4_14.Text)#18
		#create_rebar(self._values_main, self._values_1, self._values_2)
		try:
			customizable_event.raise_event(create_rebar, [self._values_main, self._values_1, self._values_2])
		except:
			TaskDialog.Show('error', 'error')

	def Button_cancelClick(self, sender, e):
		self.Close()

	def Button_SaveClick(self, sender, e):
		location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
		name = self._comboBox_save.SelectedItem
		if name:
			file = os.path.realpath(os.path.join(location + '/options/'+name+'.txt'))
			location_2 = os.path.realpath(os.path.join(location + '/options/'))
			options_list = [self._vertRebar_M1_1.SelectedIndex,self._vertRebar_M1_2.SelectedIndex, self._vertRebar_M1_3.SelectedIndex, self._vertRebar_M1_4.SelectedIndex, self._vertRebar_M1_5.SelectedIndex,
							self._vertRebar_M1_6.SelectedIndex, self._vertRebar_M1_7.SelectedIndex, self._textBox_M1_1.Text, self._textBox_M1_12.Text, self._textBox_M1_4.Text, self._textBox_M1_2.Text,
							self._textBox_M1_9.Text, self._textBox_M1_10.Text, self._textBox_M1_11.Text, self._textBox_M1_13.Text, self._textBox_M1_14.Text, self._textBox_M1_15.Text, self._textBox_M1_16.Text,
							self._textBox_M1_5.Text, self._textBox_M1_6.Text, self._textBox_M1_7.Text, self._textBox_M1_8.Text, self._gor_arm_4_1.SelectedIndex, self._gor_arm_4_2.SelectedIndex,
							self._gor_arm_4_3.SelectedIndex, self._gor_arm_4_4.SelectedIndex, self._gor_arm_4_5.SelectedIndex, self._textBox_4_1.Text, self._textBox_4_2.Text, self._textBox_4_3.Text,
							self._textBox_4_4.Text, self._textBox_4_5.Text, self._textBox_4_6.Text, self._textBox_4_7.Text, self._textBox_4_8.Text, self._textBox_4_9.Text, self._textBox_4_10.Text,
							self._textBox_4_11.Text, self._textBox_4_12.Text, self._textBox_4_13.Text, self._textBox_4_14.Text, self._comboBox_1_1.SelectedIndex, self._comboBox_1_2.SelectedIndex]
			with open(file, mode='w') as csv_file:
				for i in options_list:
					if isinstance(i, int):
						csv_file.writelines('int ' + str(i)+'\n')
					else:
						csv_file.writelines('str ' + i + '\n')
			self._comboBox_save.Items.Clear()
			for f in os.listdir(location_2):
				file_name, file_ext = os.path.splitext(f)
				self._comboBox_save.Items.Add(file_name)

			for idx, val in enumerate(self._comboBox_save.Items):
				if val == name:
					self._comboBox_save.SelectedIndex = idx

	def Button_LoadClick(self, sender, e):

		location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
		#print(self._comboBox_save.SelectedItem)
		file = os.path.realpath(os.path.join(location + '/options/'+self._comboBox_save.SelectedItem + '.txt'))
		#print(file)
		with open(file, mode='r') as csv_file:
			line = csv_file.readlines()
		fin_list=[]
		for i in line:
			a = i.replace('\n', '')
			char = a.split(' ')
			if char[0] == 'int':
				fin_list.append(int(char[1]))
			else:
				fin_list.append(char[1])
		self._vertRebar_M1_1.SelectedIndex = fin_list[0]
		self._vertRebar_M1_2.SelectedIndex = fin_list[1]
		self._vertRebar_M1_3.SelectedIndex = fin_list[2]
		self._vertRebar_M1_4.SelectedIndex = fin_list[3]
		self._vertRebar_M1_5.SelectedIndex = fin_list[4]
		self._vertRebar_M1_6.SelectedIndex = fin_list[5]
		self._vertRebar_M1_7.SelectedIndex = fin_list[6]
		self._textBox_M1_1.Text = fin_list[7]
		self._textBox_M1_12.Text = fin_list[8]
		self._textBox_M1_4.Text = fin_list[9]
		self._textBox_M1_2.Text = fin_list[10]
		self._textBox_M1_9.Text = fin_list[11]
		self._textBox_M1_10.Text = fin_list[12]
		self._textBox_M1_11.Text = fin_list[13]
		self._textBox_M1_13.Text = fin_list[14]
		self._textBox_M1_14.Text = fin_list[15]
		self._textBox_M1_15.Text = fin_list[16]
		self._textBox_M1_16.Text = fin_list[17]
		self._textBox_M1_5.Text = fin_list[18]
		self._textBox_M1_6.Text = fin_list[19]
		self._textBox_M1_7.Text = fin_list[20]
		self._textBox_M1_8.Text = fin_list[21]
		self._gor_arm_4_1.SelectedIndex = fin_list[22]
		self._gor_arm_4_2.SelectedIndex = fin_list[23]
		self._gor_arm_4_3.SelectedIndex = fin_list[24]
		self._gor_arm_4_4.SelectedIndex = fin_list[25]
		self._gor_arm_4_5.SelectedIndex = fin_list[26]
		self._textBox_4_1.Text = fin_list[27]
		self._textBox_4_2.Text = fin_list[28]
		self._textBox_4_3.Text = fin_list[29]
		self._textBox_4_4.Text = fin_list[30]
		self._textBox_4_5.Text = fin_list[31]
		self._textBox_4_6.Text = fin_list[32]
		self._textBox_4_7.Text = fin_list[33]
		self._textBox_4_8.Text = fin_list[34]
		self._textBox_4_9.Text = fin_list[35]
		self._textBox_4_10.Text = fin_list[36]
		self._textBox_4_11.Text = fin_list[37]
		self._textBox_4_12.Text = fin_list[38]
		self._textBox_4_13.Text = fin_list[39]
		self._textBox_4_14.Text = fin_list[40]
		self._comboBox_1_1.SelectedIndex = fin_list[41]
		self._comboBox_1_2.SelectedIndex = fin_list[42]
	def Button_saveAsClick(self, sender, e):
		name = self._comboBox_save.SelectedItem
		location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
		file = os.path.realpath(os.path.join(location + '/options/' + self._textBox_saveAs.Text+'.txt'))
		location_2 = os.path.realpath(os.path.join(location + '/options/'))
		options_list = [self._vertRebar_M1_1.SelectedIndex,self._vertRebar_M1_2.SelectedIndex, self._vertRebar_M1_3.SelectedIndex, self._vertRebar_M1_4.SelectedIndex, self._vertRebar_M1_5.SelectedIndex,
						self._vertRebar_M1_6.SelectedIndex, self._vertRebar_M1_7.SelectedIndex, self._textBox_M1_1.Text, self._textBox_M1_12.Text, self._textBox_M1_4.Text, self._textBox_M1_2.Text,
						self._textBox_M1_9.Text, self._textBox_M1_10.Text, self._textBox_M1_11.Text, self._textBox_M1_13.Text, self._textBox_M1_14.Text, self._textBox_M1_15.Text, self._textBox_M1_16.Text,
						self._textBox_M1_5.Text, self._textBox_M1_6.Text, self._textBox_M1_7.Text, self._textBox_M1_8.Text, self._gor_arm_4_1.SelectedIndex, self._gor_arm_4_2.SelectedIndex,
						self._gor_arm_4_3.SelectedIndex, self._gor_arm_4_4.SelectedIndex, self._gor_arm_4_5.SelectedIndex, self._textBox_4_1.Text, self._textBox_4_2.Text, self._textBox_4_3.Text,
						self._textBox_4_4.Text, self._textBox_4_5.Text, self._textBox_4_6.Text, self._textBox_4_7.Text, self._textBox_4_8.Text, self._textBox_4_9.Text, self._textBox_4_10.Text,
						self._textBox_4_11.Text, self._textBox_4_12.Text, self._textBox_4_13.Text, self._textBox_4_14.Text, self._comboBox_1_1.SelectedIndex, self._comboBox_1_2.SelectedIndex]
		#print(options_list)
		if self._textBox_saveAs.Text != '':
			with open(file, mode='w') as csv_file:
				for i in options_list:
					if isinstance(i, int):
						csv_file.writelines('int ' + str(i)+'\n')
					else:
						csv_file.writelines('str ' + i + '\n')
			self._comboBox_save.Items.Clear()
			for f in os.listdir(location_2):
				file_name, file_ext = os.path.splitext(f)
				self._comboBox_save.Items.Add(file_name)

			for idx, val in enumerate(self._comboBox_save.Items):
				if val == name:
					self._comboBox_save.SelectedIndex = idx
	def arm(self, e):
		sel_name = e.SelectedItem
		for i in rebar_bar_types:
			name = i.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString()
			if name == sel_name:
				rebar = i
				break
			else:
				rebar=None
		return rebar
form = Form1()
try:
	form.Show()
except:
	0
