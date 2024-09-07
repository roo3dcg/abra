import os
import nuke
import sys
import webbrowser


#**********************************************
#*************** CUSTOM MENU ******************
#**********************************************



'''
REPLACE THE ICON FILE PATH WITH THE FILEPATH LOCATION OF WHERE YOU PLACED YOUR ABRA/icons folder.

Example:

Add the filepath location of downlaoded app (in my case C:/Users/user/Downloads/abra) to the existing text for each icon '/icons.roo_lgt.png'

# YOU MAY ALSO REPLACE THE HOTKEYS AS DESIRED
'''

def add_menu_toolbar():
	# MENU
	custom_menu = nuke.menu('Nuke').addMenu('BEAUTY REBUILD v.01', icon= '/icons/roo_lgt.png')
	custom_menu.addSeparator()
	custom_menu.addCommand('Create AOV node grpah', 'abra.template()', 'ctrl+shift+t', icon='C:/Users/i9-7900X & RTX 3080/Downloads/abra/icons/connect.png')
	custom_menu.addSeparator()
	custom_menu.addCommand('Create Backdrop', 'abra.backdrop()', 'ctrl+shift+q', icon='/icons/multiply.png')
	custom_menu.addSeparator()
	custom_menu.addCommand('Help','import webbrowser;webbrowser.open("https://github.com/roo3dcg")', icon= '/icons/help.png')

	# TOOLBAR
	custom_toolbar = nuke.menu('Nodes').addMenu('BEAUTY REBUILD v.01', icon= '/icons/roo_lgt.png')
	custom_toolbar.addSeparator()
	custom_toolbar.addCommand('Create AOV node grpah', 'abra.template()', 'ctrl+shift+t', icon='/icons/connect.png')
	custom_toolbar.addSeparator()
	custom_toolbar.addCommand('Create Backdrop', 'abra.backdrop()', 'ctrl+shift+q', icon='/icons/multiply.png')
	custom_toolbar.addSeparator()
	custom_toolbar.addCommand('Help','import webbrowser;webbrowser.open("https://github.com/roo3dcg")', icon= '/icons/help.png')

add_menu_toolbar()