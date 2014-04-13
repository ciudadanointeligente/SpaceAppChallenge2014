# Read about factories at https://github.com/thoughtbot/factory_girl

FactoryGirl.define do
  factory :observation do
    source_object "MyText"
  end
end
