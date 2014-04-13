class Observation < ActiveRecord::Base
  has_many :logs
  def self.index_observations
    Log.select(:source_object).where("source_object like ?", "%Array%").distinct.map{|x| x.source_object}.each do |s|
      observation_logs = []
      in_between_logs = false
      Log.where(source_object: s).order(timestamp: :desc).each do |log|
        if log.cdata.include? "observing mode starting"
          in_between_logs = true
        elsif log.routine == "sendExecBlockStartedEvent"
          observation_logs << log
          observation = Observation.new
          observation.logs = observation_logs
          observation.save
          observation_logs = []
          in_between_logs = false
        end
        if in_between_logs
          observation_logs << log
        end
      end
    end
  end
end
