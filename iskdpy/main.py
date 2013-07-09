from cocos.director import director
from cocos.scenes.transitions import *
from .scene.graphics import SlideScene

from .source_plugins import *
from . import types
from . import config
from . import presenter

def main():
	slide=presenter.Presenter().get_empty_slide()
	
	director.init(**config.window)
	if ( config.scale_down ):
		director.window.set_size(640, 360)
	if ( config.fullscreen ):
		director.window.set_fullscreen(True)
	director.window.set_mouse_visible(False)

	director.run(SlideScene(slide) )
