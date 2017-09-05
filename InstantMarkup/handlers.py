class Handler:
    """
    An object that handles method calls from the Parser.

    The Parser will call the start() and end() methods at the
    beginning of each block, with the proper block name as a
    parameter. The sub() method will be used in regular expression
    substitution. When called with a name such as 'emphasis', it will
    return a proper substitution function.
    """
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method): return method(*args)
    def start(self, name):
        self.callback('start_', name)
    def end(self, name):
        self.callback('end_', name)
    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None: match.group(0)
            return result
        return substitution

class HTMLRenderer(Handler):
    """
    A specific handler used for rendering HTML.

    The methods in HTMLRenderer are accessed from the superclass
    Handler's start(), end(), and sub() methods. They implement basic
    markup as used in HTML documents.
    """
    def start_document(self):
        print('<html><head><title>...</title></head><body>')
    def end_document(self):
        print('</body></html>')
    def start_paragraph(self):
        print('<p>')
    def end_paragraph(self):
        print('</p>')
    def start_heading(self):
        print('<h2>')
    def end_heading(self):
        print('</h2>')
    def start_list(self):
        print('<ul>')
    def end_list(self):
        print('</ul>')
    def start_listitem(self):
        print('<li>')
    def end_listitem(self):
        print('</li>')
    def start_title(self):
        print('<h1>')
    def end_title(self):
        print('</h1>')
    def sub_emphasis(self, match):
        return '<em>{}</em>'.format(match.group(1))
    def sub_url(self, match):
        return '<a href="{}">{}</a>'.format(match.group(1), match.group(1))
    def sub_mail(self, match):
        return '<a href="mailto:{}">{}</a>'.format(match.group(1), match.group(1))
    def feed(self, data):
        print(data)

class CsdnRenderer(Handler):
    """
    A specific handler used for rendering CSDN-Markdown.

    The methods in CsdnRenderer are accessed from the superclass
    Handler's start(), end(), and sub() methods. They implement basic
    markup as used in CSDN-Markdown documents.
    """
    def start_document(self):
        print('')
    def end_document(self):
        print('')
    def start_paragraph(self):
        print('<font face="微软雅黑" size=4>')
    def end_paragraph(self):
        print('</font>')
    def start_heading(self):
        print('<font face="微软雅黑" size=4>\n</font>')
    def end_heading(self):
        pass
    def start_code(self):
        pass
    def end_code(self):
        pass
    def start_html(self):
        pass
    def end_html(self):
        pass
    def sub_formula(self, match):
        return '<font face="微软雅黑" size=2>$${}$$</font>'.format(match.group(1))
    def sub_coloredform(self, match):
        return '<font face="微软雅黑" color=olive size=2>$${}$$</font>'.format(match.group(1))
    def feed(self, data):
        print(data)