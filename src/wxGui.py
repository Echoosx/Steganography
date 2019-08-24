# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class bodyFrame
###########################################################################

class bodyFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"图片隐写软件", pos = wx.DefaultPosition, size = wx.Size( 531,509 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bodyLayout = wx.BoxSizer( wx.VERTICAL )

		writeLayout = wx.BoxSizer( wx.VERTICAL )

		self.writeAbleChoice = wx.RadioButton( self, wx.ID_ANY, u"写入隐藏信息", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.writeAbleChoice.SetValue( True )
		self.writeAbleChoice.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		writeLayout.Add( self.writeAbleChoice, 0, wx.ALL, 5 )

		choseLayout = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"选择图片", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		choseLayout.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.choseFile = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.Point( -1,-1 ), wx.Size( 400,-1 ), wx.FLP_DEFAULT_STYLE )
		self.choseFile.SetMinSize( wx.Size( 400,-1 ) )
		self.choseFile.SetMaxSize( wx.Size( 400,-1 ) )

		choseLayout.Add( self.choseFile, 0, wx.ALL, 5 )


		writeLayout.Add( choseLayout, 1, wx.EXPAND, 5 )

		dataLayout = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"隐藏信息", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		dataLayout.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.dataInput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dataInput.SetMinSize( wx.Size( 400,50 ) )
		self.dataInput.SetMaxSize( wx.Size( 400,-1 ) )

		dataLayout.Add( self.dataInput, 0, wx.ALL, 5 )


		writeLayout.Add( dataLayout, 1, wx.EXPAND, 5 )

		saveLayout = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"保存为   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		saveLayout.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.saveName = wx.TextCtrl( self, wx.ID_ANY, u"encodeImage.png", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.saveName.SetMinSize( wx.Size( 210,-1 ) )

		saveLayout.Add( self.saveName, 0, wx.ALL, 5 )

		self.writeButton = wx.Button( self, wx.ID_ANY, u"写入", wx.DefaultPosition, wx.DefaultSize, 0 )
		saveLayout.Add( self.writeButton, 0, wx.ALL, 5 )

		self.cancleButton = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		saveLayout.Add( self.cancleButton, 0, wx.ALL, 5 )


		writeLayout.Add( saveLayout, 1, wx.EXPAND, 5 )

		self.messageLabel = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( -1,30 ), 0 )
		self.messageLabel.Wrap( -1 )

		self.messageLabel.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lucida Grande" ) )
		self.messageLabel.SetForegroundColour( wx.Colour( 76, 76, 75 ) )

		writeLayout.Add( self.messageLabel, 0, wx.ALL, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		writeLayout.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )


		bodyLayout.Add( writeLayout, 1, wx.EXPAND, 5 )

		readLayout = wx.BoxSizer( wx.VERTICAL )

		readLayout.SetMinSize( wx.Size( 400,-1 ) )
		self.readAbleChoice = wx.RadioButton( self, wx.ID_ANY, u"读取隐藏信息", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.readAbleChoice.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		readLayout.Add( self.readAbleChoice, 0, wx.ALL, 5 )

		choseLayout2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"选择图片", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		choseLayout2.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.choseFile2 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.choseFile2.Enable( False )
		self.choseFile2.SetMinSize( wx.Size( 400,-1 ) )
		self.choseFile2.SetMaxSize( wx.Size( 400,-1 ) )

		choseLayout2.Add( self.choseFile2, 0, wx.ALL, 5 )


		readLayout.Add( choseLayout2, 1, wx.EXPAND, 5 )

		dataLayout = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"隐藏信息" ), wx.VERTICAL )

		dataLayout.SetMinSize( wx.Size( -1,80 ) )
		self.dataOutput = wx.TextCtrl( dataLayout.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dataOutput.Enable( False )
		self.dataOutput.SetMinSize( wx.Size( 500,50 ) )

		dataLayout.Add( self.dataOutput, 0, wx.ALL, 5 )


		readLayout.Add( dataLayout, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.messageLabel2 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.messageLabel2.Wrap( -1 )

		self.messageLabel2.SetForegroundColour( wx.Colour( 76, 76, 75 ) )

		bSizer10.Add( self.messageLabel2, 0, wx.ALL, 5 )


		bSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.readButton = wx.Button( self, wx.ID_ANY, u"读取", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.readButton.Enable( False )

		bSizer10.Add( self.readButton, 0, wx.ALL, 5 )

		self.cancleButton2 = wx.Button( self, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cancleButton2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.cancleButton2.Enable( False )

		bSizer10.Add( self.cancleButton2, 0, wx.ALL, 5 )


		readLayout.Add( bSizer10, 1, wx.EXPAND, 5 )


		readLayout.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bodyLayout.Add( readLayout, 1, wx.EXPAND, 5 )


		bodyLayout.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bodyLayout )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.writeAbleChoice.Bind( wx.EVT_RADIOBUTTON, self.writeable )
		self.writeButton.Bind( wx.EVT_BUTTON, self.writeStart )
		self.cancleButton.Bind( wx.EVT_BUTTON, self.clearwrite )
		self.readAbleChoice.Bind( wx.EVT_RADIOBUTTON, self.readable )
		self.readButton.Bind( wx.EVT_BUTTON, self.readStart )
		self.cancleButton2.Bind( wx.EVT_BUTTON, self.clearread )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def writeable( self, event ):
		event.Skip()

	def writeStart( self, event ):
		event.Skip()

	def clearwrite( self, event ):
		event.Skip()

	def readable( self, event ):
		event.Skip()

	def readStart( self, event ):
		event.Skip()

	def clearread( self, event ):
		event.Skip()


