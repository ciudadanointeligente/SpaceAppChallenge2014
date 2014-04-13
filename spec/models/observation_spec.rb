require 'spec_helper'

describe Observation do
  describe "self.index_observations" do
    it 'asdf' do
      Log.import_data "./spec/fixtures/chico.xml"
      obs = Observation.first
      obs.logs.count.should eql 2

    end


  end
end
