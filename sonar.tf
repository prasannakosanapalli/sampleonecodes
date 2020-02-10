provider "aws" {
  region     = var.region
  access_key = var.access_key
  secret_key = var.secret_key
}

terraform {
  backend "s3" {
    bucket = "terraformbackups3"
    key    = "v-1"
    region = "us-east-1"
  }
}
resource "aws_vpc" "sonar" {
    cidr_block = var.vpc_cidr
    tags = {
    Name = "sonar"
  }
}
resource "aws_subnet" "sonar" {
    vpc_id     = aws_vpc.sonar.id
    cidr_block = var.subnet_cidr
    tags = {
    Name = "sonar"
  }
}
resource "aws_internet_gateway" "sonar" {
  vpc_id = aws_vpc.sonar.id
  tags = {
    Name = "sonar"
  }
}

resource "aws_route_table" "sonar" {
  vpc_id = aws_vpc.sonar.id

  tags = {
    Name = "sonar"
  }
}

resource "aws_security_group" "sonar" {
  name        = "sonar"
  vpc_id      = aws_vpc.sonar.id
  ingress {
    from_port   = 9000
    to_port     = 9000
    protocol    = "tcp"
  }
  egress {
    from_port       = 9000
    to_port         = 9000
    protocol        = "tcp"
  }
}

data "aws_vpc" "sonar" {
    id = aws_vpc.sonar.id
}
data "aws_subnet" "sonar" {
    id = aws_subnet.sonar.id
}
data "aws_security_group" "sonar" {
    id = aws_security_group.sonar.id
}


resource "aws_instance" "sonar" {
    ami           = var.ami
    instance_type = "t2.micro"
    subnet_id     = aws_subnet.sonar.id
    vpc_security_group_ids = [ aws_security_group.sonar.id ]

  tags = {
    Name = "SONAR-QUBE"
  }
}
