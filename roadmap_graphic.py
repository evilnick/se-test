from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import io


# element ids found by inspecting actual page; probably a cleverer way of doing this
elements= ["f75ad846","47fc9ee4","98236657"]
url ="https://github.com/users/evilnick/projects/1"
margin=26


def crop_centre(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
dt = driver.get(url)
driver.set_window_size(1180,900)
element_images=[]
for e in elements:
    image = driver.find_element(By.ID,e).screenshot_as_png 
    img = Image.open(io.BytesIO(image))
    element_images.append(img)

bg = Image.open("wallpaper.png")
width = (element_images[0].width+margin)*3 + margin
height = element_images[0].height + margin*2
bg = crop_centre(bg,width,height)

for i in range(len(element_images)):
    x_offset = margin + (margin*i) + (element_images[i].width*i)
    y_offset = margin
    bg.paste(element_images[i], (x_offset, y_offset))

bg.save("roadmap.png")

