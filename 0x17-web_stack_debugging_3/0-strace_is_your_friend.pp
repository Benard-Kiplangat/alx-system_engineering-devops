# A puppet script to fix a mispelling in a file in a server

$file = '/var/www/html/wp-settings.php'

#replace wp-settings.php file containing "phpp" with "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file}",
  path    => ['/bin','/usr/bin']
}
