# A puppet script to increase the limits of user holberton
exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }
