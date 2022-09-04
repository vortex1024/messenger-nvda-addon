import api
import appModuleHandler
import tones
import ui
import winUser
import mouseHandler
import scriptHandler
from scriptHandler import getLastScriptRepeatCount, script

class AppModule(appModuleHandler.AppModule):
	def event_gainFocus(self, obj, nextHandler):
		focus=api.getFocusObject()
		#tones.beep(123,123)
		if focus.UIAAutomationId=="" and focus.childCount>0:
			ui.message(focus.getChild(0).name)
			focus.role=15
		nextHandler()
		
	@script(
	gesture="kb:applications",
	description=_("right click messenger"),
	category="Input")
	def script_rigtClick(self, gesture):
		focus=api.getFocusObject()
		setMousePosition(focus.location.center.x, focus.location.center.y, True)
			
def setMousePosition(x, y,  click):
	# Setter version of report mouse position function.
	# The new position announcement is to be used if needed.
	winUser.setCursorPos(x, y)
	mouseHandler.executeMouseMoveEvent(x, y)
	if click:
		winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTDOWN, 0, 0, None, None)
		winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTUP, 0, 0, None, None)
		