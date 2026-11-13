resource "aws_default_vpc" "default" {
  tags = {
    Name = "Default VPC"
  }
}

resource "aws_instance" "ec2_instance" {
  ami                    = "ami-0bce970415466784a"
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.allow_ssh.id]
  key_name               = "ec2-northcoders-kp"

  tags = {
    Name = "ec2_instance"
  }
}

# Expose the EC2 instance ID, such as i-0123456789abcdef0.
output "instance_id" {
  value = aws_instance.ec2_instance.id
}

# Expose the display name shown in the EC2 console.
output "instance_name" {
  value = aws_instance.ec2_instance.tags["Name"]
}