from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

user = input('Enter Username: ')
pasw = input('Enter password: ')


class InstaBot:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.bot = webdriver.Firefox()

	def login(self):
		bot = self.bot
		bot.get(https://www.instagram.com/)
		time.sleep(6)
		email = bot.find_element_by_name('username')
		password = bot.find_element_by_name('password')
		# submit = bot.find_element_by_id('submit')
		email.clear()
		password.clear()
		email.send_keys(self.username)
		password.send_keys(self.password)
		password.send_keys(Keys.RETURN)
		time.sleep(10)


log = InstaBot(user, pasw)
log.login()
