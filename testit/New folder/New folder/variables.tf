variable "aws_region" {
	default = "us-east-1"
}
variable "vpc_cidr" {
	default = "10.20.0.0/16"
}
variable "subnets_cidr" {
	type = list
	default = ["10.20.1.0/28", "10.20.2.0/28"]
}
variable "azs" {
	type = list
	default = ["us-east-1a", "us-east-1b","us-east-1c", "us-east-1d","us-east-1e", "us-east-1f"]
}
variable "secret_key" {
    type = string
    default = "25r4QLtr56EqfxCVzEk3eHwS1lxhn6bWWEsYH8Ms"
}
variable "access_key" {
    type = string
    default = "AKIAXZXIY4Q4OQX5IE5K"
}
variable "webservers_ami" {
    default = "ami-00eb20669e0990cb4"
}

variable "instance_type" {
    default = "t2.large"
}