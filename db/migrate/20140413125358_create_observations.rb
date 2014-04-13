class CreateObservations < ActiveRecord::Migration
  def change
    create_table :observations do |t|
      t.text :source_object

      t.timestamps
    end
  end
end
