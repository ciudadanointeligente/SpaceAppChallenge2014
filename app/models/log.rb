class Log < ActiveRecord::Base
  def self.import_data file
    file = File.open(file)
    xml = Nokogiri::XML file
    file.close
    ['Debug','Delouse','Info'].each do |tag|
      xml.css(tag).each do |node|
        create_log_from_node node
      end
    end
  end
  def self.create_log_from_node node
      log = Log.new
      log.source_object = node['SourceObject']
      log.raw = node.to_s
      log.timestamp = node['TimeStamp']
      log.cdata = node.text
      log.routine = node['Routine']
      log.tag = node.name
      log.save
      return log
  end
end
