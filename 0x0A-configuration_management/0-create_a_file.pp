# A file that creates a new file in /tmp with the following requirements:
#	File path is /tmp/school
#	File permission is 0744
#	File owner is www-data
#	File group is www-data
#	File contains I love Puppet

file{ '/tmp/school':
  path    => '/tmp/school',
  group   => 'www-data',
  owner   => 'www-data',
  content => 'I love Puppet',
  mode    => '0744'
}
