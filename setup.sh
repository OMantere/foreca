#!/bin/bash -e

# setup virtualenv
sudo pip install virtualenv
virtualenv venv -p python2.7
source venv/bin/activate
pip install --upgrade -r requirements.txt


# symlink?

echo
read -p "Add symlink to /usr/local/bin (y/n)?" -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
	sudo ln -sf $(pwd)/foreca /usr/local/bin/foreca
fi

