sudo apt-get -y update
sudo add-apt-repository -y ppa:linuxuprising/java
sudo apt update
sudo apt install -y oracle-java13-installer
sudo apt install -y oracle-java13-set-default
java -version 
sudo apt-get -y update
sudo apt-get install -y unzip software-properties-common wget 
sudo apt-get install -y postgresql postgresql-contrib
sudo -u postgres psql -c " CREATE USER sonarqube WITH PASSWORD 'sonarqube' "
sudo -u postgres psql -c " CREATE DATABASE sonarqube OWNER sonarqube; "
sudo -u postgres psql -c " GRANT ALL PRIVILEGES ON DATABASE sonarqube TO sonarqube; "


sudo wget  https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-8.0.zip

sudo unzip sonarqube-6.0.zip
sudo mv -i sonarqube-6.0 /opt/sonarqube

sudo adduser --system --no-create-home --group --disabled-login sonarqube
sudo chown -R sonarqube:sonarqube /opt/sonarqube*

cd /opt/sonarqube*/bin/linu*

sudo cat sonar.sh | grep "#RUN_AS_USER" | sudo sed -i 's/#RUN_AS_USER=/RUN_AS_USER=sonarqube/g' /opt/sonar*/bin/linux-x86-64/sonar.sh

sudo echo "sonar.jdbc.username=sonarqube
sonar.jdbc.password=sonarqube
sonar.jdbc.url=jdbc:postgresql://localhost/sonarqube
sonar.web.javaAdditionalOpts=-server
sonar.web.host=0.0.0.0
" >> /opt/sonarqube/conf/sonar.properties    

sudo echo "
sonarqube   -   nofile   65536
sonarqube   -   nproc    4096
" >> /etc/security/limits.d/99-sonarqube.conf

sudo echo "
vm.max_map_count=262144
fs.file-max=65536
" >> /etc/sysctl.conf

sudo /opt/sonarqub*/bin/linux*/sonar.sh restart
