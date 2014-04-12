from ..models import Line
from bs4 import BeautifulSoup
from bs4 import CData
import dateutil.parser

class LogsParser(object):
    def parse_line(self, line_raw):
        line = Line()
        line.raw = line_raw
        line_process = BeautifulSoup(line_raw)
        line.cdata = line_process.get_text()
        element = line_process.children.next()
        line.timestamp = dateutil.parser.parse(element['timestamp'])

        return line