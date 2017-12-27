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
      
a=int(sys.argv[1])
b=int(sys.argv[2])
x=NandGate(a,b)
x.logic()
print (x.output)
x=NorGate(a,b)
x.logic()
print (x.output)

#print (x.input)
