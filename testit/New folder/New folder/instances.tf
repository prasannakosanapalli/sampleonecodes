resource "aws_instance" "sonar" {
	count = length(var.subnets_cidr) 
	ami = var.webservers_ami
	instance_type = var.instance_type
	vpc_security_group_ids = [ "sg-00ec57c74f9cf0cf7" ]
	key_name = "prasanna"
	user_data = file("practiceshel.sh")
    tags ={
	  Name = "Sonar-${count.index}"
	}
}

