#!/usr/bin/env ruby
# A script to match a 10 digit phone number
puts ARGV[0].scan(/^[0-9]{10, 10}$/).join
