# Create a new load balancer
resource "aws_elb" "sonarelb" {
  subnets = [for value in aws_subnet.sonar: value.id]
  security_groups = [aws_security_group.sonarsg.id]

  listener     {
      instance_port     = 80
      instance_protocol = "tcp"
      lb_port           = 80
      lb_protocol       = "tcp"
    }
  listener    {
      instance_port     = 9000
      instance_protocol = "tcp"
      lb_port           = 9000
      lb_protocol       = "tcp"
    }
  

  health_check  {
    target              = "TCP:80"
    interval            = 30
    healthy_threshold   = 2
    unhealthy_threshold = 2
    timeout             = 2
  }

  instances                   = [for value in aws_instance.sonar: value.id]
  tags ={
    Name = "sonar-elb"
  }
  
}

output "elb-dns-name" {
  value = aws_elb.sonarelb.dns_name
}