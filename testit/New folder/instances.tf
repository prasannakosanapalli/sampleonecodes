resource "aws_instance" "sonar" {
	count = length(var.subnets_cidr) 
	ami = var.webservers_ami
	instance_type = var.instance_type
	security_groups = [ aws_security_group.sonarsg.id ]
	subnet_id = element(aws_subnet.sonar.*.id,count.index)
	key_name = "prasanna"
	user_data = file("script.sh")
    tags ={
	  Name = "Sonar-${count.index}"
	}
}