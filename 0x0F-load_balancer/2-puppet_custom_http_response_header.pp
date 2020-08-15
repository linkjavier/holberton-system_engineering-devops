#Custom HTTP header response with Puppet.
#The name of the custom HTTP header is X-Served-By
#The value of the custom HTTP header is the hostname of the server Nginx is running on
exec {'update':
  command  => 'sudo apt-get update',
  path    => ['/usr/bin', '/bin'],
}

package {'nginx':
  ensure  => installed,
  require => Exec['update'],
}

file_line {'header':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => "add_header X-Served-By ${hostname};",
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => File_line['header'],
}
