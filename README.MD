# INSTALLATION GUIDE (Linux)

1) Clone the repository:

`git clone https://github.com/Espacio-root/zen.git ~/`


2) Install dependencies:

```
python3 -m venv ~/zen/venv
source ~/zen/venv/activate
pip install mitmproxy
```


3)Replace [user] with your username in script.sh and zen.service file:


4) Execute the following code as super user:

```
sudo chmod +x ~/zen/startup.sh
sudo cp zen.service /etc/systemd/system/zen.service
sudo systemctl enable zen.service
sudo systemctl start zen.service
```


5) Configure the browser (firefox):

i)   Open firefox settings and search for `proxy`
ii)  Click on the settings button that shows up
iii) Select Manual Proxy Configuration
iv)  Set the proxy to be 127.0.0.1 and port to be 8080
v)   Click on Ok
