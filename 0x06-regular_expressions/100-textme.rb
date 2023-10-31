#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=to:|flags:|from:).+?(?=\])/).join(", ")

