# INSTALLATION GUIDE (Linux)

Clone the repository:

`git clone https://github.com/Espacio-root/zen.git ~/`


Install dependencies:

```
python3 -m venv ~/zen/venv
source ~/zen/venv/activate
pip install mitmproxy
```


Replace [user] with your username and add the following lines of code to your ~/.bashrc file:

```
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

VIRTUAL_ENV_PATH="/home/[user]/zen/venv/bin/activate"
MITMPROXY_SCRIPT_PATH="/home/[user]/zen/main.py"
if [ -f "$VIRTUAL_ENV_PATH" ]; then
    source "$VIRTUAL_ENV_PATH"
    mitmdump -s "$MITMPROXY_SCRIPT_PATH"
    deactivate
else
    echo "Virtual environment not found at: $VIRTUAL_ENV_PATH"
fi
```


Configure the browser (firefox):

1) Open firefox settings and search for `proxy`
2) Click on the settings button that shows up
3) Select Manual Proxy Configuration
4) Set the proxy to be 127.0.0.1 and port to be 8080
5) Click on Ok
