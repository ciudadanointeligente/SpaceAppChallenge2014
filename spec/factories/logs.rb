# Read about factories at https://github.com/thoughtbot/factory_girl

FactoryGirl.define do
  factory :log do
    raw "MyText"
    timestamp "2014-04-13 07:32:50"
    cdata "MyText"
    source_object "MyText"
    routine "MyText"
    tag "MyText"
  end
end
