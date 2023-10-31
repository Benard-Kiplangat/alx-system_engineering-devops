#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=to:|flags:|from:).?[-:a-zA-Z0-9]*/).join(", ")

