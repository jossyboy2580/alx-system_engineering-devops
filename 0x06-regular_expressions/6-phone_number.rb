#!/usr/bin/env ruby
# A script to match a 10 digit phone number
puts ARGV[0].scan(/^\d{10,10}$/).join
