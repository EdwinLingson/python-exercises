#!/usr/bin/env/python
import sys
class Gate(object):
    """ class representing a gate. It can be any gate. """

    def __init__(self, *args):
        """ initialise the class """
        self.input = args
        self.output = None

    def logic(self):
        """ the intelligence to be performed """
        raise NotImplementedError

    def output(self):
        """ the output of the gate """
        self.logic()
        return self.output


class AndGate(Gate):
    """ class representing AND gate """

    def logic(self):
        self.output = self.input[0] and self.input[1]


class OrGate(Gate):
    """ class representing OR gate """

    def logic(self):
        self.output = self.input[0] or self.input[1]


class NotGate(Gate):
    """ class representing NOT gate """

    def logic(self):
        self.output = not self.input[0]
        
class NandGate(AndGate,NotGate):
    """ class representing NOT gate """

    def logic(self):
       c = AndGate(self.input[0],self.input[1])
       c.logic()
       d =NotGate(c.output)
       d.logic()
       self.output =d.output
       
class NorGate(OrGate,NotGate):
    """ class representing NOT gate """

    def logic(self):
       c = OrGate(self.input[0],self.input[1])
       c.logic()
       d =NotGate(c.output)
       d.logic()
       self.output =d.output
      



	#gate=kwargs['Gates']
	#print (kwargs['Gates'])
	#print ("oper = ",oper)
	#a=kwargs['input1']
	#b=kwargs['input2']
d=sys.argv[3:][0].split('=')
b=d[1]
d=sys.argv[2:][0].split('=')
a=d[1]
d=sys.argv[1:][0].split('=')
gate=d[1]
	
if(gate=='not'):
	x=NotGate(a,b)
	x.logic()
	print ("Not Operation: of ",a," and ",b," is ",x.output)
if(gate=='and'):
	x=AndGate(a,b)
	x.logic()
	print ("And Operation: of ",a," and ",b," is ",x.output)
if(gate=='or'):
	x=OrGate(a,b)
	x.logic()
	print ("Or Operation: of ",a," and ",b," is ",x.output)
if(gate=='nor'):
	x=NorGate(a,b)
	x.logic()
	print ("Nor Operation: of ",a," and ",b," is ",x.output)
if(gate=='nand'):
	x=NandGate(a,b)
	x.logic()
	print ("Nand Operation: of ",a," and ",b," is ",x.output)	
