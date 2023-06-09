# replace the mis-spelling of php (writtten as phpp) in wp-settings.php file

exec {'searchAndReplace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
