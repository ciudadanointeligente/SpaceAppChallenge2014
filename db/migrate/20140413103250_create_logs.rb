class CreateLogs < ActiveRecord::Migration
  def change
    create_table :logs do |t|
      t.text :raw
      t.datetime :timestamp
      t.text :cdata
      t.text :source_object
      t.text :routine
      t.text :tag

      t.timestamps
    end
  end
end
