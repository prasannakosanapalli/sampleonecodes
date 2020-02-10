# VPC
resource "aws_vpc" "sonar_vpc" {
  cidr_block       = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support = true
  tags = {
      Name = "sonar"
      }
}

# Internet Gateway
resource "aws_internet_gateway" "sonar_igw" {
  vpc_id = aws_vpc.sonar_vpc.id
  tags ={
    Name = "sonar"
  }
}

# Subnets : public
resource "aws_subnet" "sonar" {
  count = length(var.subnets_cidr)
  vpc_id = aws_vpc.sonar_vpc.id
  cidr_block = element(var.subnets_cidr,count.index)
  availability_zone = element(var.azs,count.index)
  map_public_ip_on_launch = true 
  tags ={
    Name = "sonar-${count.index}"
  }
}

resource "aws_route_table" "sonar" {
  vpc_id = aws_vpc.sonar_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.sonar_igw.id
  }
  tags = {
    Name = "main"
  }
}



