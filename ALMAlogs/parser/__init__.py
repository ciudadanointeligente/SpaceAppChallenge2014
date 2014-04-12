from ..models import Line
from bs4 import BeautifulSoup
from bs4 import CData
import dateutil.parser

class LogsParser(object):
    def parse_line(self, line_raw):
        line = Line()
        line.raw = line_raw
        line_process = BeautifulSoup(line_raw)
        element = line_process.children.next()
        line.cdata = element.get_text()
        line.timestamp = dateutil.parser.parse(element['timestamp'])
        line.sourceobject = element['sourceobject']

        return line