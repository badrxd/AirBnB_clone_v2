# Puppet script
exec { 'update':
  command => 'apt-get update',
  provider => shell,
}
-> exec { 'install_nginx':
  command => 'apt-get install -y nginx',
  provider => shell,
}
-> exec { 'create_test_folder':
  command => 'mkdir -p /data/web_static/releases/test/',
  provider => shell,
}
-> exec { 'create_shared_folder':
  command => 'mkdir -p /data/web_static/shared/',
  provider => shell,
}
-> exec { 'add_content':
  command => 'echo "hello badr" > /data/web_static/releases/test/index.html',
  provider => shell,
}
-> exec { 'smb_link':
  command => 'ln -sfn /data/web_static/releases/test /data/web_static/current',
  provider => shell,
}
-> exec { 'ch_permission':
  command => 'chown -R ubuntu:ubuntu /data/',
  provider => shell,
}
-> exec { 'add_lines':
  command => 'sudo sed -i "s|server_name _;|server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}|" /etc/nginx/sites-enabled/default',
  provider => shell,
}
-> exec { 'restart':
  command => 'sudo service nginx restart',
  provider => shell,
}
