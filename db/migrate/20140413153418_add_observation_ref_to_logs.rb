class AddObservationRefToLogs < ActiveRecord::Migration
  def change
    add_reference :logs, :observation, index: true
  end
end
