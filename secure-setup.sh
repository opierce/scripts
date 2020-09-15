#!/usr/bin/env bash

# Update and upgrade apt-get
apt-get update
apt-get upgrade

# Install fail2ban
apt-get install fail2ban

# Setup login user
useradd appa
mkdir /home/appa
mkdir /home/appa/.ssh
chmod 700 /home/appa/.ssh

# Require public key auth
## vim /home/appa/.ssh/authorized_keys
## chmod 400 /home/appa/.ssh/authorized_keys
## chown appa:appa /home/appa -R

apt-get install unattended-upgrades

# Test The New User & Enable Sudo
passwd appa

# Add user to sudoers
## visudo
### root    ALL=(ALL) ALL
### deploy  ALL=(ALL) ALL

# Lock Down SSH
## vim /etc/ssh/sshd_config
### PermitRootLogin no
### PasswordAuthentication no
### AllowUsers deploy@(your-ip) deploy@(another-ip-if-any) 

# Reset SSH
## service ssh restart

# Automagical Updates
## vim /etc/apt/apt.conf.d/10periodic
### APT::Periodic::Update-Package-Lists "1";
### APT::Periodic::Download-Upgradeable-Packages "1";
### APT::Periodic::AutocleanInterval "7";
### APT::Periodic::Unattended-Upgrade "1";

# Secure Updates
## vim /etc/apt/apt.conf.d/50unattended-upgrades
### Unattended-Upgrade::Allowed-Origins {
###        "Ubuntu lucid-security";
###        "Ubuntu lucid-updates";
### };
