from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


Link = r"E:\STAR\backend\voice.html"
chrome_driver_path = "E:\STAR\chromedriver-win64\chromedriver.exe"  # Specify the path to your ChromeDriver executable

# Define Chrome options
chrome_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.106 Safari/537.36"
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--use-fake-device-for-media-stream")
chrome_options.add_argument("--headless=new")

# Initialize the WebDriver with a Service object
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(Link)

def SpeechRecognitionModel():
      driver.find_element(by=By.ID,value="start").click()
      print("Listening...")
      while True:
            try:
                  Text = driver.find_element(by=By.ID,value="output").text
                  if Text:
                        driver.find_element(by=By.ID,value="end").click()
                        return Text

                  else:
                        sleep(0.333)

            except:
                  pass

# Example usage
while True:
      try:
            recognized_text = SpeechRecognitionModel()
            print(f"Recognized Text: {recognized_text}")
      except:
            pass
