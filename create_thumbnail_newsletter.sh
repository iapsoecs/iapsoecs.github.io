#! /bin/bash

# usage
# ./create_thumbnail_newsletter.sh file.pdf

# if convert is not happy, use and adapt depending on your imagemagick version
# Check before that gs --version is higher that 9.24
# sudo sed -i '/disable ghostscript format types/,+6d' /etc/ImageMagick-6/policy.xml

convert -thumbnail x400 -background white -alpha remove $1[0] ${1%.pdf}_thumbnail.png
