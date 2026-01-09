#------------------------------------------------------------
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
#------------------------------------------------------------
# online selenium tutorial for python with all the element selection techniques:
# https://www.qatouch.com/blog/selenium-with-python-tutorial/
#------------------------------------------------------------
chromeOptions = Options()
chromeOptions.add_experimental_option("detach",True)
browser = webdriver.Chrome(options= chromeOptions)
browser.set_window_position(1000,40)
browser.set_window_size(900,926)
#------------------------------------------------------------
global tickspeed,currentUpgrade
tickspeed = 0
#------------------------------------------------------------

def main():
#------------------------------------------------------------
    #startup
    browser.get("https://cookieclicker.ee/")
    time.sleep(2)
    englishButton = browser.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
    englishButton.click()
    time.sleep(3)
#------------------------------------------------------------
    #get cookie for clicking
    cookie = browser.find_element(By.XPATH, '//*[@id="bigCookie"]')
    getEverything()
#------------------------------------------------------------
    #MAIN LOOP
    time.sleep(1)
    while True:
#------------------------------------------------------------
       # click cookie then do all the calculations
        try:
            cookie.click()
        except:
            print("cookie click error")
#------------------------------------------------------------
        time.sleep(tickspeed)
#------------------------------------------------------------
        cookies = browser.execute_script("return Game.cookies")
        cps = browser.execute_script("return Game.cookiesPs")
#------------------------------------------------------------
        #check stuff and buy stuff
        buyMain(cookies,cps)
#------------------------------------------------------------
        #MAIN LOOP EXIT
        #if cookies >= 10:
            #break
#------------------------------------------------------------

def buyMain(cookies,cps):
#------------------------------------------------------------
    #check if there are notes to close
    #notes = browser.find_element(By.XPATH, '//*[@id="notes"]/div[3]')
    #notesPresent = notes.is_displayed()
    notesPresent = checkExistsByXpath('//*[@id="notes"]/div[3]')
    if notesPresent:
        for i in range(3,5):
            try:
                notesX = browser.find_element(By.XPATH, f'//*[@id="notes"]/div[{i}]')
                notesX.click()
            except:
                print("<<< Notes Exception >>>")
#------------------------------------------------------------
    #checks if upgrades are available
    upgradePresent = checkExistsByXpath('//*[@id="upgrade0"]')
#------------------------------------------------------------
    if upgradePresent:
        upgrade = browser.find_element(By.ID, 'upgrade0')
        try:
            #only retrieving the specific attribute "basePrice" from the dict
            upgradePrice = browser.execute_script('return Game.UpgradesInStore[0]["basePrice"]')
            if "upgradePrice" in vars():
                if cookies >= upgradePrice:
                    try:
                        upgrade.click()
                    except:
                        print("UPGRADE CLICK ERROR")
#------------------------------------------------------------
            else:
                print("<<< upgradePrice not in vars() >>>")
#------------------------------------------------------------
        except:
            print("<<< Upgrade Error >>>")
#------------------------------------------------------------
    try:
        if int(cookies) % 10 == 0:
            print(f"Cookies: {cookies:.1f} CPS: {cps:.1f}")
#------------------------------------------------------------
        if "cursorPrice" in vars() or "cursorPrice" in globals():
            if cookies >= cursorPrice:
                cursor.click()
                getEverything()
#------------------------------------------------------------
        if "grandmaPrice" in vars() or "grandmaPrice" in globals():
            if cookies >= grandmaPrice:
                grandma.click()
                getEverything()
#------------------------------------------------------------
        if "farmPrice" in vars() or "farmPrice" in globals():
            if cookies >= farmPrice:
                farm.click()
                getEverything()
#------------------------------------------------------------
        if "minePrice" in vars() or "minePrice" in globals():
            if cookies >= minePrice:
                mine.click()
                getEverything()
#------------------------------------------------------------
        if "factoryPrice" in vars() or "factoryPrice" in globals():
            if cookies >= factoryPrice:
                factory.click()
                getEverything()
#------------------------------------------------------------
        if "bankPrice" in vars() or "bankPrice" in globals():
            if cookies >= bankPrice:
                bank.click()
                getEverything()
#------------------------------------------------------------
        if "templePrice" in vars() or "templePrice" in globals():
            if cookies >= templePrice:
                temple.click()
                getEverything()
#------------------------------------------------------------
        if "wizardTowerPrice" in vars() or "wizardTowerPrice" in globals():
            if cookies >= templePrice:
                wizardTower.click()
                getEverything()
#------------------------------------------------------------
        if "shipmentPrice" in vars() or "shipmentPrice" in globals():
            if cookies >= shipmentPrice:
                shipment.click()
                getEverything()
#------------------------------------------------------------
        if "alchemyLabPrice" in vars() or "alchemyLabPrice" in globals():
            if cookies >= alchemyLabPrice:
                alchemyLab.click()
                getEverything()
#------------------------------------------------------------
        if "portalPrice" in vars() or "portalPrice" in globals():
            if cookies >= portalPrice:
                portal.click()
                getEverything()
#------------------------------------------------------------
        if "timeMachinePrice" in vars() or "timeMachinePrice" in globals():
            if cookies >= timeMachinePrice:
                timeMachine.click()
                getEverything()
#------------------------------------------------------------
        if "antimCondenserPrice" in vars() or "antimCondenserPrice" in globals():
            if cookies >= antimCondenserPrice:
                antimCondenser.click()
                getEverything()
#------------------------------------------------------------
        if "prismPrice" in vars() or "prismPrice" in globals():
            if cookies >= prismPrice:
                prism.click()
                getEverything()
#------------------------------------------------------------
        if "chancemakerPrice" in vars() or "chancemakerPrice" in globals():
            if cookies >= chancemakerPrice:
                chancemaker.click()
                getEverything()
#------------------------------------------------------------
        if "fractalEnginePrice" in vars() or "fractalEnginePrice" in globals():
            if cookies >= fractalEnginePrice:
                fractalEngine.click()
                getEverything()
#------------------------------------------------------------
        if "javaConsolePrice" in vars() or "javaConsolePrice" in globals():
            if cookies >= javaConsolePrice:
                javaConsole.click()
                getEverything()
#------------------------------------------------------------
        if "idleVersePrice" in vars() or "idleVersePrice" in globals():
            if cookies >= idleVersePrice:
                idleVerse.click()
                getEverything()
#------------------------------------------------------------
        if "cortexBakerPrice" in vars() or "cortexBakerPrice" in globals():
            if cookies >= cortexBakerPrice:
                cortexBaker.click()
                getEverything()
#------------------------------------------------------------
        if "youPrice" in vars() or "youPrice" in globals():
            if cookies >= youPrice:
                you.click()
                getEverything()
#------------------------------------------------------------              
    except:
        print("<<< product error >>>")
#------------------------------------------------------------

def getEverything():
#------------------------------------------------------------
    global cursor,grandma,farm,mine,factory,bank,temple,wizardTower,shipment,alchemyLab,\
    portal,timeMachine,antimCondenser,prism,chancemaker,fractalEngine,javaConsole,idleVerse,\
    cortexBaker,you,\
    cursorPrice,grandmaPrice,farmPrice,minePrice,factoryPrice,bankPrice,templePrice,\
    wizardTowerPrice,shipmentPrice,alchemyLabPrice,portalPrice,timeMachinePrice,\
    antimCondenserPrice,prismPrice,chancemakerPrice,fractalEnginePrice,javaConsolePrice,\
    idleVersePrice,cortexBakerPrice,youPrice
#------------------------------------------------------------
    cursor = browser.find_element(By.XPATH, '//*[@id="product0"]')
    grandma = browser.find_element(By.XPATH, '//*[@id="product1"]')
    farm = browser.find_element(By.XPATH, '//*[@id="product2"]')
    mine = browser.find_element(By.XPATH, '//*[@id="product3"]')
    factory = browser.find_element(By.XPATH, '//*[@id="product4"]')
    bank = browser.find_element(By.XPATH, '//*[@id="product5"]')
    temple = browser.find_element(By.XPATH, '//*[@id="product6"]')
    wizardTower = browser.find_element(By.XPATH, '//*[@id="product7"]')
    shipment = browser.find_element(By.XPATH, '//*[@id="product8"]')
    alchemyLab = browser.find_element(By.XPATH, '//*[@id="product9"]')
    portal = browser.find_element(By.XPATH, '//*[@id="product10"]')
    timeMachine = browser.find_element(By.XPATH, '//*[@id="product11"]')
    antimCondenser = browser.find_element(By.XPATH, '//*[@id="product12"]')
    prism = browser.find_element(By.XPATH, '//*[@id="product13"]')
    chancemaker = browser.find_element(By.XPATH, '//*[@id="product14"]')
    fractalEngine = browser.find_element(By.XPATH, '//*[@id="product15"]')
    javaConsole = browser.find_element(By.XPATH, '//*[@id="product16"]')
    idleVerse = browser.find_element(By.XPATH, '//*[@id="product17"]')
    cortexBaker = browser.find_element(By.XPATH, '//*[@id="product18"]')
    you = browser.find_element(By.XPATH, '//*[@id="product19"]')

#------------------------------------------------------------
    try:
        cursorPrice = float(((browser.find_element(By.ID, "productPrice0")).text).replace(",",""))
        grandmaPrice = float(((browser.find_element(By.ID, "productPrice1")).text).replace(",",""))
        farmPrice = float(((browser.find_element(By.ID, "productPrice2")).text).replace(",",""))
        minePrice = float(((browser.find_element(By.ID, "productPrice3")).text).replace(",",""))
        factoryPrice = float(((browser.find_element(By.ID, "productPrice4")).text).replace(",",""))
        bankPrice = float(((browser.find_element(By.ID, "productPrice5")).text).replace(",",""))
        templePrice = float(((browser.find_element(By.ID, "productPrice6")).text).replace(",",""))
        wizardTowerPrice = float(((browser.find_element(By.ID, "productPrice7")).text).replace(",",""))
        shipmentPrice = float(((browser.find_element(By.ID, "productPrice8")).text).replace(",",""))
        alchemyLabPrice = float(((browser.find_element(By.ID, "productPrice9")).text).replace(",",""))
        portalPrice = float(((browser.find_element(By.ID, "productPrice10")).text).replace(",",""))
        timeMachinePrice = float(((browser.find_element(By.ID, "productPrice11")).text).replace(",",""))
        antimCondenserPrice = float(((browser.find_element(By.ID, "productPrice12")).text).replace(",",""))
        prismPrice = float(((browser.find_element(By.ID, "productPrice13")).text).replace(",",""))
        chancemakerPrice = float(((browser.find_element(By.ID, "productPrice14")).text).replace(",",""))
        fractalEnginePrice = float(((browser.find_element(By.ID, "productPrice15")).text).replace(",",""))
        javaConsolePrice = float(((browser.find_element(By.ID, "productPrice16")).text).replace(",",""))
        idleVersePrice = float(((browser.find_element(By.ID, "productPrice17")).text).replace(",",""))
        cortexBakerPrice = float(((browser.find_element(By.ID, "productPrice18")).text).replace(",",""))
        youPrice = float(((browser.find_element(By.ID, "productPrice19")).text).replace(",",""))
#------------------------------------------------------------
    except:
        print("<<< future product exception >>>")
#------------------------------------------------------------

def checkExistsByXpath(xpath):
    try:
        browser.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True
#------------------------------------------------------------

def checkExistsByID(Id):
    try:
        browser.find_element(By.ID, Id)
    except NoSuchElementException:
        return False
    return True
#------------------------------------------------------------

main()