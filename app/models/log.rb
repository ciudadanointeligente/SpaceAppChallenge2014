class Log < ActiveRecord::Base
  belongs_to :observation
  
  def self.import_data file
    file = File.open(file)
    xml = Nokogiri::XML file
    file.close
    ['Debug','Delouse','Info','Error','Warning'].each do |tag|
      xml.css(tag).each do |node|
        log = create_log_from_node node
      end
    end
    Observation.index_observations
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