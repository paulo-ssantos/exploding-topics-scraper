import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Scrapper:
  
  BASE_URL = 'https://explodingtopics.com/'
  
  def __init__(self):
    options = webdriver.FirefoxOptions()
    options.headless = True
    self.driver = webdriver.Firefox(options=options)
    
  def get_trending_topics(self):
    self.driver.get(self.BASE_URL)
    time.sleep(5)
    trending_topics = self.driver.find_elements(By.CSS_SELECTOR, ".cardHover")
    
    trendsList = []
    
    for topic in trending_topics:
      isProtected = "blur" in topic.get_attribute("style")
      
      if isProtected:
        continue
      
      topicTitle = topic.find_element(By.CSS_SELECTOR, ".tileKeyword").get_attribute("innerHTML")
      topicVolume = topic.find_element(By.CSS_SELECTOR, ".scoreTag--volume > .scoreTagTop").get_attribute("innerHTML")
      topicGrotwh = topic.find_element(By.CSS_SELECTOR, ".growth").get_attribute("innerHTML")
      topicDescription = topic.find_element(By.CSS_SELECTOR, ".tileDescription").get_attribute("innerHTML")
      
      trendTopicProps = {
        "title": topicTitle,
        "volume": topicVolume,
        "growth": topicGrotwh,
        "description": topicDescription
      }
      
      trendsList.append(trendTopicProps)
      
    self.driver.quit()
    return trendsList
