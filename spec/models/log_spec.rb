require 'spec_helper'

describe Log do
  it "saves correct info" do
    file = File.open("./spec/fixtures/log_data.xml")
    xml = Nokogiri::XML file
    file.close
    node =xml.at_css('Debug')
    log = Log.create_log_from_node node
    log.source_object.should eq "ACC/javaContainer"
    log.raw.should_not be_nil
    log.timestamp.should eq "2014-02-24T15:02:49.254"
    log.cdata.should eq "calling orb.resolve_initial_references"
    log.routine.should eq "initRootPoa"
    log.tag.should eq "Debug"
  end
  # describe "self.import_data" do
    it "saves the data to db" do
      Log.import_data "./spec/fixtures/log_data.xml"
      Log.count.should eq 91
    end
  # end
  # describe "self.create_log_from_node" do
    it "saves the node data into the new log" do
      file = File.open("./spec/fixtures/log_data.xml")
      xml = Nokogiri::XML file
      file.close
      node =xml.at_css('Debug')
      log = Log.create_log_from_node node
      log.source_object.should_not be_nil
    end
  # end
end
