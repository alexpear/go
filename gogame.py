#!/usr/bin/python

import app

class GoGame(App):
  # Go commands
  def drawGrid(self, params=[]):
  	pass

  def makeInputMap(self):
  	return {
  	  'ls': drawGrid
  	}

  def __init__(self):
  	App.__init__(self)
  	self.inputMap.update(makeInputMap())
