class Log < ActiveRecord::Base
  belongs_to :observation
  
  def self.import_data file
    file = File.open(file)
    xml = Nokogiri::XML file
    file.close
    current_observations = Hash.new
    ['Debug','Delouse','Info','Error','Warning'].each do |tag|
      xml.css(tag).each do |node|
        log = create_log_from_node node
        if log.cdata.include? "observing mode starting up"
          observation = Observation.new
          observation.logs = []
          observation.save
          current_observations[log.source_object.to_s] = observation

        end
        current_key = log.source_object.to_s
        current_observations.keys.each do |key|
          if current_key != key
            if current_key.include? key
              current_key = key
            end
          end
        end

        if !current_observations[current_key].nil?
          current_observations[current_key].logs << log
          current_observations[current_key].save
          if log.cdata.include? "observing mode shutting down"
            current_observations.delete(current_key)
          end
        end

      end
    end
    # Observation.index_observations
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