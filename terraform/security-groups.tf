# Look up the default VPC in the configured AWS region.
data "aws_vpc" "default" {
  default = true
}

# Create the security group in that VPC.
resource "aws_security_group" "allow_ssh" {
  name        = "allow_ssh"
  description = "Allow SSH, HTTP from a specified IP, and outbound IPv4 traffic"
  vpc_id      = data.aws_vpc.default.id

  tags = {
    Name = "allow_ssh"
  }
}

# Allow SSH on TCP port 22 from your current public IPv4 address.
resource "aws_vpc_security_group_ingress_rule" "allow_ssh_ingress" {
  security_group_id = aws_security_group.allow_ssh.id
  cidr_ipv4         = "217.74.151.68/32" # Your network's public IPv4 + /32. Find yours at https://checkip.amazonaws.com/
  ip_protocol       = "tcp"
  from_port         = 22
  to_port           = 22
}

# Allow HTTP on TCP port 80 from any IPv4 address.
resource "aws_vpc_security_group_ingress_rule" "allow_http_ingress" {
  security_group_id = aws_security_group.allow_ssh.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "tcp"
  from_port         = 80
  to_port           = 80
}

# Allow all outbound IPv4 traffic.
resource "aws_vpc_security_group_egress_rule" "allow_ssh_egress" {
  security_group_id = aws_security_group.allow_ssh.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1"
}

