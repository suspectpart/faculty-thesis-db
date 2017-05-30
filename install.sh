#!/bin/bash

echo "Installiere Thesispool..."
echo

# root check
if [[ $(id -u) -ne 0 ]]
then 
	echo "Please run as root";
	exit 1; 
fi

# upgrade system
apt-get update && apt-get upgrade -y

# install packages
apt-get install -y python3 apache2 python3-setuptools python3-pip libsasl2-dev libapache2-mod-wsgi-py3 libldap2-dev libssl-dev libapache2-mod-xsendfile libmysqlclient-dev mysql-client

# update pip
pip3 install -U pip

#install django, LDAP backend, xsendfile and datetutil
pip3 install pyldap django django_auth_ldap python-dateutil django_sendfile

# enable file sending in apache (to send pdfs)
a2enmod xsendfile

# make db and folder above it owned by www-data
python3 manage.py migrate
python3 manage.py collectstatic --no-input

cp conf/thesispool.conf /etc/apache2/sites-available/
cp conf/thesispool_ssl.conf /etc/apache2/sites-available/

chown wwwrun: /var/www/thesispool
chown wwwrun: /var/www/thesispool/db.sqlite3

systemctl restart apache2

# certificate ca-cert in /etc/ssl/certs/ca-certificats einfügen