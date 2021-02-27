#!/bin/bash

# Do not ignore a 'Ctrl-C' force quit
# trap "exit" INT

while true; do

    # Wait for internet connection
    while ! ping -c 1 -W 3 127.0.0.1; do
        echo "Waiting for 1.2.3.4 - network interface might be down..."
        sleep 10
    done

    # Find our current directory
    LAUNCH_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
    cd $LAUNCH_DIR
    echo $LAUNCH_DIR

    echo "copying user background"
    BACKGROUND_DIR="$(gsettings get org.gnome.desktop.background picture-uri | cut -c 9- | sed 's/.$//')"
    echo $BACKGROUND_DIR
    cp $BACKGROUND_DIR $LAUNCH_DIR/back_texture.png

    cd $LAUNCH_DIR

    rm index.html*
    rm comic.png

    wget https://xkcd.com/archive/ 

    python3 XKCD_Background.py

    # Take the edited image and make it out background!
    gsettings set org.gnome.desktop.background picture-uri $LAUNCH_DIR/new_background.png

    ## Search again for a new comic every 30 minutes
    sleep 1800
done