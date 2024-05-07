#!/usr/bin/env ruby
# A ruby script to match a repetition with regex
puts ARGV[0].scan(/hbt{2,5}[^o]n/).join
