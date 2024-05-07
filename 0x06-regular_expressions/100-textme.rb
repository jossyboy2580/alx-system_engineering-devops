#!/usr/bin/env ruby
# A script to print sender, receiver and flags for a message
sender = ARGV[0].scan(/from:(\+?\w+)\]/).join
receiver = ARGV[0].scan(/to:(\+?\w+)/).join
flag = ARGV[0].scan(/flags:(-?\d:-?\d:-?\d:-?\d:-?\d)/).join
print sender, ",", receiver, ",", flag, "\n"
