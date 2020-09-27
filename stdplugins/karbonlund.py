"""Carbon Scraper Plugin for Userbot. //text in creative way.
usage: .car //as a reply to any text message

Thanks to @r4v4n4 for vars"""

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from telethon import events
from urllib.parse import quote_plus
from urllib.error import HTTPError
from time import sleep
from uniborg.util import admin_cmd
import asyncio
import os

@borg.on(admin_cmd(pattern="car ?(.*)", allow_sudo=True))
async def carbon_api(e):
 if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
   """ A Wrapper for carbon.now.sh """
   hmm = await e.reply("🔲🔲🔲🔲🔲")
   CARBON = 'https://carbon.now.sh/?bg=rgba(249%2C237%2C212%2C0)&t=synthwave-84&wt=none&l=application%2Fjson&ds=true&dsyoff=20px&dsblur=0px&wc=true&wa=true&pv=56px&ph=0px&ln=false&fl=1&fm=IBM%20Plex%20Mono&fs=14.5px&lh=153%25&si=false&es=4x&wm=false&code={code}'
   CARBONLANG = "en"
   textx = await e.get_reply_message()
   pcode = e.text
   if pcode[8:]:
         pcode = str(pcode[8:])
   elif textx:
         pcode = str(textx.message) # Importing message to module
   code = quote_plus(pcode) # Converting to urlencoded
   url = CARBON.format(code=code, lang=CARBONLANG)
   chrome_options = Options()
   chrome_options.add_argument("--headless")
   chrome_options.binary_location = Config.GOOGLE_CHROME_BIN
   chrome_options.add_argument("--window-size=1920x1080")
   chrome_options.add_argument("--disable-dev-shm-usage")
   chrome_options.add_argument("--no-sandbox")
   chrome_options.add_argument('--disable-gpu')
   prefs = {'download.default_directory' : './'}
   chrome_options.add_experimental_option('prefs', prefs)
   await hmm.edit("🔳🔳🔲🔲🔲")

   driver = webdriver.Chrome(executable_path=Config.CHROME_DRIVER, options=chrome_options)
   driver.get(url)
   download_path = './'
   driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
   params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_path}}
   command_result = driver.execute("send_command", params)

   driver.find_element_by_xpath('//*[@id="__next"]/main/div[3]/div[2]/div[1]/div[1]/div/span[2]').click()
   driver.find_element_by_id("export-menu").click()

   #removing below line coz seems no use now
   #driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()

   sleep(5) # this might take a bit.
   driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
   sleep(5)
   await hmm.edit("🔳🔳🔳🔲🔲")
   driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
   sleep(5) #Waiting for downloading

   await hmm.edit("🔳🔳🔳🔳🔳")
   file = './carbon.png'
   await hmm.edit("☣️Karbon1 Completed, Uploading Karbon☣️")
   await e.client.send_file(
         e.chat_id,
         file,
         caption="@R4V4N4 SAYS: Kya Comment Dakun Behenchod",
         force_document=False,
         reply_to=e.message.reply_to_msg_id,
         )

   os.remove('./carbon.png')
   # Removing carbon.png after uploading
   await hmm.delete() # Deleting msg
