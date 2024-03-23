import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
import config


class YoutubeSearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_video_play(self):
        self.driver.get('https://www.youtube.com/watch?v=NpzTEVfUo_U&list=WL&index=4&t=1200s')
        time.sleep(3)
        play_button = self.driver.find_element('css selector', '.ytp-play-button')
        play_button.click()
        time.sleep(3)
        pause_button = play_button.get_attribute("data-title-no-tooltip")
        self.assertEqual(pause_button, "Пауза")

    def test_search_youtube(self):
        driver = self.driver
        driver.get("https://www.youtube.com")
        search_box = driver.find_element("name", "search_query")
        search_box.send_keys("Kuplinov")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "Kuplinov" in driver.page_source

    def test_authorization(self):
        driver = self.driver
        driver.get("https://www.youtube.com")
        login_button = driver.find_element("link text", "Войти")
        login_button.click()
        email_input = driver.find_element("id", "identifierId")
        email_input.send_keys(config.EMAIL)
        email_input.send_keys(Keys.RETURN)
        time.sleep(2)
        password_input = driver.find_element("id", "identifierId")
        password_input.send_keys(config.PASSWORD)
        password_input.send_keys(Keys.RETURN)
        time.sleep(2)
        assert "youtube.com" in driver.current_url

    def test_play_shorts(self):
        driver = self.driver
        driver.get("https://youtube.com")
        shorts = driver.find_element("link text", "Shorts")
        shorts.click()
        time.sleep(3)
        like = driver.find_element("class name", "yt-spec-button-shape-next--icon-button")
        like.click()
        is_liked = like.get_attribute("aria-pressed")
        self.assertEqual(is_liked, "true")

    def test_like_on_video(self):
        driver = self.driver
        driver.get("https://youtube.com")
        search_box = driver.find_element("name", "search_query")
        search_box.send_keys("Kuplinov")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        first_video = driver.find_element("id", "video-title")
        first_video.click()
        time.sleep(3)
        like = driver.find_element("class name", "yt-spec-button-view-model")
        like.click()
        time.sleep(3)
        button_like = driver.find_element("class name", "yt-spec-button-shape-next--segmented-start")
        is_liked = button_like.get_attribute("aria-pressed")
        self.assertEqual(is_liked, "true")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
