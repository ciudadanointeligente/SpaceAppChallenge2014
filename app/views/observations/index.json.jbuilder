json.array!(@observations) do |observation|
  json.extract! observation, :id, :source_object
  json.url observation_url(observation, format: :json)
end
