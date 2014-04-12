# coding=utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client
from .models import Line
from .parser import LogsParser
from datetime import datetime
from django.utils.timezone import now

# Create your tests here.
line_raw = '<Debug TimeStamp="2014-04-03T01:46:02.972" File="alma.Control.ObservingModes.LocalOscilatorThread"  Line="98" Routine="run" Host="gas01" Process="CONTROL/ACC/javaContainer" SourceObject="CONTROL/Array014" Thread="Thread-26724581" LogId="95269" Audience="Developer"><![CDATA[Waiting 0.964 seconds for subscan 19 to start.]]></Debug>'

class IndexTextCase(TestCase):
    def setUp(self):
        pass
    def test_get_home(self):
        '''gets home page'''
        url = reverse("home")
        self.assertTrue(url)
        client = Client()
        response = client.get(url)
        self.assertEquals(response.status_code, 200)

class LogParserCase(TestCase):
    def test_parser_line(self):
        '''get one line, one love'''
        parser = LogsParser()
        line = parser.parse_line(line_raw)
        self.assertIsInstance(line, Line)

    def test_raw_line(self):
        '''get a raw line'''
        parser = LogsParser()
        line = parser.parse_line(line_raw)
        self.assertEquals(line.raw, line_raw)
        self.assertEquals(line.cdata, 'Waiting 0.964 seconds for subscan 19 to start.')
        self.assertEquals(line.timestamp.year, 2014) # 2014-04-03T01:46:02.972
        self.assertEquals(line.timestamp.month, 4) # 2014-04-03T01:46:02.972
        self.assertEquals(line.timestamp.day, 3) # 2014-04-03T01:46:02.972
        self.assertEquals(line.timestamp.hour, 1) # 2014-04-03T01:46:02.972
        self.assertEquals(line.timestamp.minute, 46) # 2014-04-03T01:46:02.972
        self.assertEquals(line.timestamp.second, 02) # 2014-04-03T01:46:02.972


class LineCase(TestCase):
    def test_lineclass(self):
        '''instance a line'''
        line = Line()
        self.assertTrue(line)

    def test_line_attr(self):
        '''get attribute'''
        actualdate = now()
        line = Line.objects.create(raw=line_raw, timestamp=actualdate, cdata='Waiting 0.964 seconds for subscan 19 to start.', sourceobject='CONTROL/Array014')
        self.assertEquals(line.raw, line_raw)
        self.assertEquals(line.timestamp, actualdate)
        self.assertEquals(line.cdata, 'Waiting 0.964 seconds for subscan 19 to start.')
        self.assertEquals(line.sourceobject, 'CONTROL/Array014')