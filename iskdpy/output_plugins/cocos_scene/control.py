import logging
logger = logging.getLogger(__name__)

from cocos.layer import Layer
from cocos.actions import Delay, CallFunc
from pyglet.window import key

from ...output import OutputPlugin

class _KeyboardControlLayer(Layer):

	is_event_handler = True  #: enable pyglet's events

	def __init__( self):
		super(_KeyboardControlLayer, self).__init__()
		self.push_all_handlers()

	def on_key_press( self, k , m ):
		if k == key.ENTER:
			self.parent.cancel_transition()
			RemoteControlLayer().callback.goto_next_slide()
			return True
		elif k == key.RIGHT:
			self.parent.cancel_transition()
			RemoteControlLayer().callback.goto_next_slide()
			return True
		elif k == key.LEFT:
			self.parent.cancel_transition()
			RemoteControlLayer().callback.goto_previous_slide()
			return True


class _RemoteControlLayer(Layer):
	def __init__(self, *args, **kwargs):
		super(_RemoteControlLayer, self).__init__(*args, **kwargs)
		self.schedule_interval(self.run, 0.1)
		self.task=None

	def set_callback(self, cb):
		self.callback=cb

	def set_task(self, task):
		self.task=task

	def run(self, *args):
		if self.task:
			self.task()

__rcl=None
def RemoteControlLayer():
	global __rcl
	if not __rcl:
		__rcl=_RemoteControlLayer()
	return __rcl

__kcl=None
def KeyboardControlLayer():
	global __kcl
	if not __kcl:
		__kcl=_KeyboardControlLayer()
	return __kcl
