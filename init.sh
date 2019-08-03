#!/bin/sh

echo "Initializing the project, you will only need to run this once."

# Copy all the base files out here without overwriting
echo "Copying base files"
cp -n base/* .

# Copy over the nginx files
echo "Copying nginx site.conf"
cp -n services/nginx/site.conf volumes/nginx/conf.d/site.conf
