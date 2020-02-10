#!/bin/bash

# Do not ignore a 'Ctrl-C' force quit
trap "exit" INT

while true; do

    # Wait for internet connection
    while ! ping -c 1 -W 3 127.0.0.1; do
        echo "Waiting for 1.2.3.4 - network interface might be down..."
        sleep 1
    done

    cd /home/calvin/Coding_Projects/XKCD

    rm index.html*
    rm comic.png

    wget https://xkcd.com/archive/

    python3 XKCD_Background.py

    gsettings set org.gnome.desktop.background picture-uri file:///home/calvin/Coding_Projects/XKCD/new_background.png

    ## Search again for a new comic every 30 minutes
    sleep 1800
done