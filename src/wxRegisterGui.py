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
## Class RegisterFrame
###########################################################################

class RegisterFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		mainbody = wx.BoxSizer( wx.VERTICAL )

		up = wx.BoxSizer( wx.HORIZONTAL )


		up.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.usernameLabel = wx.StaticText( self, wx.ID_ANY, u"用户名", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.usernameLabel.Wrap( -1 )

		self.usernameLabel.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lucida Grande" ) )

		bSizer3.Add( self.usernameLabel, 0, wx.ALL, 5 )

		self.usernameInput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,25 ), 0 )
		bSizer3.Add( self.usernameInput, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.passwordLabel = wx.StaticText( self, wx.ID_ANY, u"密码   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.passwordLabel.Wrap( -1 )

		self.passwordLabel.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lucida Grande" ) )

		bSizer4.Add( self.passwordLabel, 0, wx.ALL, 5 )

		self.passwordInput1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,25 ), wx.TE_PASSWORD )
		bSizer4.Add( self.passwordInput1, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer38 = wx.BoxSizer( wx.HORIZONTAL )

		self.usernameLabel1 = wx.StaticText( self, wx.ID_ANY, u"确认   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.usernameLabel1.Wrap( -1 )

		self.usernameLabel1.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lucida Grande" ) )

		bSizer38.Add( self.usernameLabel1, 0, wx.ALL, 5 )

		self.passwordInput2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,25 ), wx.TE_PASSWORD )
		bSizer38.Add( self.passwordInput2, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer38, 1, wx.EXPAND, 5 )


		up.Add( bSizer2, 1, wx.EXPAND, 5 )


		up.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		mainbody.Add( up, 1, wx.EXPAND, 5 )

		down = wx.BoxSizer( wx.HORIZONTAL )


		down.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.login = wx.Button( self, wx.ID_ANY, u"注册", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )

		self.login.SetDefault()
		self.login.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lucida Grande" ) )

		down.Add( self.login, 0, wx.ALL, 5 )


		down.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lucida Grande" ) )

		down.Add( self.m_button2, 0, wx.ALL, 5 )


		down.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		mainbody.Add( down, 1, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.message = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.message.Wrap( -1 )

		self.message.SetForegroundColour( wx.Colour( 76, 76, 75 ) )

		bSizer22.Add( self.message, 0, wx.ALL, 5 )


		bSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		mainbody.Add( bSizer22, 1, wx.EXPAND, 5 )


		self.SetSizer( mainbody )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.login.Bind( wx.EVT_BUTTON, self.registerEvent )
		self.m_button2.Bind( wx.EVT_BUTTON, self.cancle )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def registerEvent( self, event ):
		event.Skip()

	def cancle( self, event ):
		event.Skip()


