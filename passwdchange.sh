#!/bin/bash

# Prompt the user for the MySQL root password
read -sp 'Enter the MySQL root password: ' mysql_root_password

# Prompt the user for the username and new password
read -p 'Enter the username for the MySQL user: ' mysql_username
read -sp 'Enter the new password for the MySQL user: ' mysql_new_password

# Change the MySQL user password
mysql -u root -p${mysql_root_password} <<EOF
USE mysql;
UPDATE user SET authentication_string=PASSWORD('${mysql_new_password}') WHERE User='${mysql_username}';
FLUSH PRIVILEGES;
EOF

# Check the exit code of the previous command to see if it was successful
if [ $? -eq 0 ]; then
  echo "Password changed successfully for user ${mysql_username}."
else
  echo "An error occurred while changing the password for user ${mysql_username}."
fi
