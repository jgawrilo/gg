
sudo apt-get install google-chrome-stable
sudo apt-get install xvfb
pip install Google-Search-API
pip install pyvirtualdisplay selenium
wget https://chromedriver.storage.googleapis.com/2.30/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
