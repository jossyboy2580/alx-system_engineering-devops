#!/usr/bin/env ruby
# A script that ascertains the presence of h and b at the beginning and end
# of the string plus any other single character in-between
puts ARGV[0].scan(/^h[a-zA-Z0-9]n$/).join
