import sys, re, codecs
from handlers import *
from util import *
from rules import *

class Parser:
    """
    A Parser reads a text file, applying rules and controlling a handler.
    """
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []
    def addRule(self, rule):
        self.rules.append(rule)
    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block,
                           self.handler)
                    if last: break
        self.handler.end('document')

class BasicTextParser(Parser):
    """
    A specific Parser that adds rules and filters in its constructor.
    """
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())
        self.addRule(CodeRule())
        self.addRule(HtmlRule())

        self.addFilter(r'\*\*\$\$(.+?)\$\$\*\*', 'coloredform')
        self.addFilter(r'\$\$(.+?)\$\$', 'formula')
        #self.addFilter(r'\*(.+?)\*', 'emphasis')
        #self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        #self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')

class Logger(object):
    '''
    A Logger that both prints output to the terminal and saves the output to a log file.
    '''
    def __init__(self):
        self.terminal = sys.stdout
        self.log = codecs.open(sys.argv[2], 'w', 'utf-8')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        
    def flush(self):
        pass  

sys.stdout = Logger()
#handler = HTMLRenderer()
handler = CsdnRenderer()
parser = BasicTextParser(handler)

#parser.parse(sys.stdin)
parser.parse( codecs.open(sys.argv[1], 'r', 'utf-8'))