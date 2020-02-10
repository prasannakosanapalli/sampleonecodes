# Create a new load balancer
resource "aws_elb" "sonarelb" {
  security_groups = [ "sg-00ec57c74f9cf0cf7" ]
  availability_zones = var.azs 


  listener     {
      instance_port     = 9000
      instance_protocol = "HTTP"
      lb_port           = 9000
      lb_protocol       = "HTTP"
    }

  

  health_check  {
    target              = "HTTP:9000/"
    interval            = 30
    healthy_threshold   = 10
    unhealthy_threshold = 2
    timeout             = 20
  }

  instances                   = [for value in aws_instance.sonar: value.id]
  tags ={
    Name = "sonar-elb"
  }
  
}

output "elb-dns-name" {
  value = aws_elb.sonarelb.dns_name
}