#!/bin/bash 
java-version = sudo java -version

java_uninstall(){
  sudo apt-get purge -y openjdk-\* icedtea-\* icedtea6-\*
}

java_install() {
  sudo apt install -y openjdk-11-jre
  sudo echo " JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64/bin/" " >> /etc/environment 
  sudo source /etc/environment
  sudo echo $JAVA_HOME
  sudo java -version
}



sudo apt-get install -y unzip software-properties-common wget 
sudo apt-get install -y postgresql postgresql-contrib
sudo -u postgres psql -c " CREATE USER sonarqube WITH PASSWORD 'sonarqube' "
sudo -u postgres psql -c " CREATE DATABASE sonarqube OWNER sonarqube; "
sudo -u postgres psql -c " GRANT ALL PRIVILEGES ON DATABASE sonarqube TO sonarqube; "
pwd 
cd /home/ubuntu/

search_sonarfolder( {
    c= "sudo find /opt/ -name sonarqube -type d"
    a= "sudo find /home/ubuntu/ -name sonarqube-8.0 -type d " 
    b= "sudo find /home/ubuntu/ -name sonarqube-8.0.zip  "
    
    if [ $c == 0]
    then
    echo "sonar folder is present at $c"
    exit 
    else 
      if [ $a == 0]
      then 
      sudo mv -i sonarqube-6.0 /opt/sonarqube 
       elif [ $b == 0]
       then
       sudo wget  https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-8.0.zip
       sudo unzip sonarqube-8.0.zip
       sudo mv -i sonarqube-6.0 /opt/sonarqube
}
)

