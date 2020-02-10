#!/bin/bash 

sudo su 
sudo yum update -y
sudo wget https://d3pxv6yz143wms.cloudfront.net/11.0.5.10.1/java-11-amazon-corretto-devel-11.0.5.10-1.x86_64.rpm 
sudo yum install -y java-11-amazon-corretto-devel-11.0.5.10-1.x86_64.rpm 
sudo yum update -y
sudo java -version
sudo wget -O /etc/yum.repos.d/sonar.repo http://downloads.sourceforge.net/project/sonar-pkg/rpm/sonar.repo
sudo yum install -y sonar
sudo service sonar restart
