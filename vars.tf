variable "secret_key" {
    type = string
    default = "bvxBDg5Z4UNAH/3ZmDF77/cN9bkieLUwky+thR9s"
}
variable "access_key" {
    type = string
    default = "AKIAWUSYAZHIIVTVS7HC"
}
variable "region" {
    type = string
    default = "us-east-1"
}

variable "vpc_cidr" {
    type = string
    default= "10.0.0.0/16"
}

variable "subnet_cidr" {
    type = string
    default = "10.0.1.0/24"
  
}

variable "ami" {
    type = string
    default = "ami-00d4e9ff62bc40e03"
  
}

