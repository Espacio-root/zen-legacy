#!/bin/bash

function proxy_on() {
    local proxy="http://127.0.0.1:8080/"
    export http_proxy="$proxy" \
           https_proxy=$proxy \
           ftp_proxy=$proxy \
           rsync_proxy=$proxy \
           HTTP_PROXY=$proxy \
           HTTPS_PROXY=$proxy \
           FTP_PROXY=$proxy \
           RSYNC_PROXY=$proxy
    echo -e "Proxy environment variable added"
}

function proxy_off(){
    unset http_proxy https_proxy ftp_proxy rsync_proxy \
          HTTP_PROXY HTTPS_PROXY FTP_PROXY RSYNC_PROXY
    echo -e "Proxy environment variable removed."
}
proxy_on

VIRTUAL_ENV_PATH="/home/espacio/projects/zen/venv/bin/activate"
MITMPROXY_SCRIPT_PATH="/home/espacio/projects/zen/main.py"
if [ -f "$VIRTUAL_ENV_PATH" ]; then
    source "$VIRTUAL_ENV_PATH"
    mitmdump -s "$MITMPROXY_SCRIPT_PATH"
    deactivate
else
    echo "Virtual environment not found at: $VIRTUAL_ENV_PATH"
fi
