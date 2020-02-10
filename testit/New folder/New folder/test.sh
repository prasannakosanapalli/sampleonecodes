#! /bin/bash
sudo apt-get update
sudo apt-get install -y unzip wget
sudo apt-get install mysql-server 
service mysqld start 

mysql -u root –p password <<-EOF
mysql>SET PASSWORD FOR root@localhost = PASSWORD('password');
mysql>CREATE USER 'sonarqube'@'localhost' IDENTIFIED BY 'password';

mysql> CREATE DATABASE sonarqube ;

mysql>GRANT ALL PRIVILEGES ON sonarqube.* TO 'sonarqube'@'localhost' ;

EOF

cd /opt
pwd 
wget -y https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-8.0.zip

unzip sonarqube-6.0.zip

echo "sonar.jdbc.username=sonar

sonar.jdbc.password=password

sonar.jdbc.url=jdbc:mysql://localhost:3306/sonar?useUnicode=true&characterEncoding=utf8&rewriteBatchedStatements=true&useConfigs=maxPerformance&useSSL=false
" >> /opt/sonarqube-8.0/conf/sonar.properties 