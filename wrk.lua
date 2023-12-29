local wrk = wrk

counter = 1

request = function()
  local path = wrk.path .. "/" .. ((counter % 25) + 1)
  counter = counter + 1
  return wrk.format(nil, path)
end
