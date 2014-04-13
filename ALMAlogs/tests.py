# coding=utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client
from .models import Line
from .models import ExecBlock
from .parser import LogsParser
from datetime import datetime
from django.utils.timezone import now
from bs4 import BeautifulSoup
import os

# Create your tests here.
line_raw = '<Debug TimeStamp="2014-04-03T01:46:02.972" File="alma.Control.ObservingModes.LocalOscilatorThread"  Line="98" Routine="run" Host="gas01" Process="CONTROL/ACC/javaContainer" SourceObject="CONTROL/Array014" Thread="Thread-26724581" LogId="95269" Audience="Developer"><![CDATA[Waiting 0.964 seconds for subscan 19 to start.]]></Debug>'

def read_template_as_string(path, file_source_path=__file__):
    script_dir = os.path.dirname(file_source_path)
    result = ''
    with open(os.path.join(script_dir, path), 'r') as f:
       result = f.read()

    return result

lines = read_template_as_string('fixtures/block.xml')

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
    def setUp(self):
        line_process = BeautifulSoup(line_raw)
        self.debug_line = line_process.children.next()

    def test_parser_line(self):
        '''get one line, one love'''
        parser = LogsParser()
        line = parser.parse_line(self.debug_line)
        self.assertIsInstance(line, Line)

    def test_raw_line(self):
        '''get a raw line'''
        parser = LogsParser()
        line = parser.parse_line(self.debug_line)
        self.assertEquals(line.raw, '<debug audience="Developer" file="alma.Control.ObservingModes.LocalOscilatorThread" host="gas01" line="98" logid="95269" process="CONTROL/ACC/javaContainer" routine="run" sourceobject="CONTROL/Array014" thread="Thread-26724581" timestamp="2014-04-03T01:46:02.972"><![CDATA[Waiting 0.964 seconds for subscan 19 to start.]]></debug>')
        self.assertEquals(line.cdata, 'Waiting 0.964 seconds for subscan 19 to start.')
        self.assertEquals(line.timestamp.year, 2014) # 2014-04-03T01:46:02.972
        self.assertEquals(line.timestamp.month, 4) # 2014-04-03T01:46:02.972
        self.assertEquals(line.timestamp.day, 3) # 2014-04-03T01:46:02.972
        self.assertEquals(line.timestamp.hour, 1) # 2014-04-03T01:46:02.972
        self.assertEquals(line.timestamp.minute, 46) # 2014-04-03T01:46:02.972
        self.assertEquals(line.timestamp.second, 02) # 2014-04-03T01:46:02.972
        self.assertEquals(line.sourceobject, 'CONTROL/Array014')
        self.assertEquals(line.routine, 'run')
        self.assertEquals(line.type, 'debug')


class LineCase(TestCase):
    def test_lineclass(self):
        '''instance a line'''
        line = Line()
        self.assertTrue(line)

    def test_line_attr(self):
        '''get attribute'''
        actualdate = now()
        line = Line.objects.create(raw=line_raw, timestamp=actualdate, cdata='Waiting 0.964 seconds for subscan 19 to start.', sourceobject='CONTROL/Array014', routine='run', type='debug')
        self.assertEquals(line.raw, line_raw)
        self.assertEquals(line.timestamp, actualdate)
        self.assertEquals(line.cdata, 'Waiting 0.964 seconds for subscan 19 to start.')
        self.assertEquals(line.sourceobject, 'CONTROL/Array014')
        self.assertEquals(line.routine, 'run')
        self.assertEquals(line.type, 'debug')

    def test_line_has_exec_block(self):
        ''' A line has an exec block'''
        obs = ExecBlock.objects.create(uid='wid_')
        actualdate = now()
        line = Line.objects.create(raw=line_raw, \
            timestamp=actualdate, \
            cdata='Waiting 0.964 seconds for subscan 19 to start.', sourceobject='CONTROL/Array014',\
            execblock = obs)
        self.assertTrue(line)
        self.assertEquals(line.execblock, obs)


class ExecBlockCaseTestCase(TestCase):
    def test_execblock_attr(self):
        '''get execblock attributes'''
        obs = ExecBlock.objects.create(uid='wid_')
        self.assertTrue(obs)
        self.assertEquals(obs.uid, 'wid_')

    def test_get_startEvent(self):
        #sendExecBlockStartedEvent
        soup = BeautifulSoup(lines)
        message_started_ev =  ''

        for message in soup.findAll(routine="sendExecBlockStartedEvent"):
            message_started_ev = message

        self.assertEquals(message_started_ev.__str__(), '<debug file="alma.Control.Array.ArrayStateBase" host="gas01" line="887" logid="113150" process="CONTROL/ACC/javaContainer" routine="sendExecBlockStartedEvent" sourceobject="CONTROL/Array016" thread="RequestProcessor-32200" timestamp="2014-04-03T03:01:41.969"><![CDATA[Sending ExecBlockStartedEvent]]></debug>')

    def test_get_endEvent(self):
        #sendExecBlockEndedEvent
        soup = BeautifulSoup(lines)
        # message_ended_ev =  ''

        for message in soup.findAll(routine="sendExecBlockEndedEvent"):
            message_ended_ev = message

        self.assertEquals(message_ended_ev.__str__(), '<debug file="alma.Control.Array.ArrayStateBase" host="gas01" line="964" logid="108664" process="CONTROL/ACC/javaContainer" routine="sendExecBlockEndedEvent" sourceobject="CONTROL/Array014" thread="CONTROL/Array014-1" timestamp="2014-04-03T02:40:25.369"><![CDATA[Sending ExecBlockEndedEvent]]></debug>')

