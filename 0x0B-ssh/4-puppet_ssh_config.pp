#Requirements, with Puppet:
# Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
# Your SSH client configuration must be configured to refuse to authenticate using a password
file_line { 'private_key':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
}
file_line { 'no_password':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}
