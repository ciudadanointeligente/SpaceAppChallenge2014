json.array!(@logs) do |log|
  json.extract! log, :id, :raw, :timestamp, :cdata, :source_object, :routine, :tag
  json.url log_url(log, format: :json)
end
