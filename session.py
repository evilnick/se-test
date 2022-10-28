from selenium import webdriver
from PIL import Image
from Screenshot import Screenshot_clipping
import Screenshot
driver = webdriver.Chrome(executable_path = ‘path\to\chromedriver.exe’’)
url = "https://www.google.com/"’
driver = webdriver.Chrome(executable_path = '/usr/bin/google-chrome')
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
dt = driver.get("https://www.instagram.com")
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
dt = driver.get("https://www.instagram.com")
driver.get_screenshot_as_file("LambdaTestVisibleScreen.png") 
dt = driver.get("https://trello.com/b/Pfu4BlRO/demo-roadmap")
driver.get_screenshot_as_file("LambdaTestVisibleScreen.png") 
driver.set_window_size(900,720)
driver.set_window_size(900,600)
driver.set_window_size(880,600)
driver.set_window_size(890,600)
driver.set_window_size(1080,600)
driver.set_window_size(1120,600)
driver.set_window_size(1140,600)
driver.set_window_size(1160,600)
driver.set_window_size(1180,600)
driver.get_screenshot_as_file("roadmap.png") 
png = driver.get_screenshot_as_png() 
top = 30
left=0
im = Image.open(BytesIO(png))
im = Image.open(bytes(png))
png
im = Image.frombytes("L",(bytes(png))
)
im = Image.frombytes("L",(1180,600),png)
im.save("test2.png")
im = Image.frombytes("L",(1180,600),png,decoder_name='png')
image = Image.open(io.BytesIO(image_data))
import io
image = Image.open(io.BytesIO(png))
image.save("test2.png")
w,h = image.size()
w,h = image.size
image.crop((0,60,w,h-60))
image.save("test2.png")
i2 = image.crop((0,60,w,h-60))
i2.save("test2.png")
import readline; print('\n'.join([str(readline.get_history_item(i + 1)) for i in range(readline.get_current_history_length())]))
