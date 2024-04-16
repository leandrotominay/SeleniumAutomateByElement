from selenium import webdriver

# Set options to make browsing easier
options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")
options.add_argument("start-maximized")
options.add_argument("disable-dev-shm-usage")
options.add_argument("no-sandbox")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)
driver.get(
      "https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/558/saopaulo-sp"
)

minima = driver.find_element(
      by="xpath",
      value=
      "/html/body/div[2]/div[5]/div[4]/div[1]/div/div[4]/section[1]/div[3]/div/div[3]/div[1]/div/div/span[1]"
  )

maxima = driver.find_element(
      by="xpath",
      value=
      "/html/body/div[2]/div[5]/div[4]/div[1]/div/div[4]/section[1]/div[3]/div/div[3]/div[1]/div/div/span[2]"
  )

title = driver.find_element(
      by="xpath",
      value="/html/body/div[2]/div[5]/div[4]/div[1]/div/div[1]/div[1]/h1")

# Prints -------------------=================--------------================

print("O Titulo é: " + title.text + " , Minima de: " + minima.text + " , Maxima de: " 
      + maxima.text)




