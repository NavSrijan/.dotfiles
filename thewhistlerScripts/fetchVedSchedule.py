from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser as cfg
import pickle as pkl
import time
import pdb

def writeFile(file, to_write):
    with open(file, "wb") as f:
        pkl.dump(to_write, file)

def start_chrome():
    options = Options()
    options.headless = True
    options.binary_location = "/usr/bin/google-chrome-beta"
    driver = webdriver.Chrome(options=options)
    return driver

def vedantu_login(driver):
    parser = cfg.ConfigParser()
    parser.read("config.cfg")
    email = parser['Vedantu']['email']
    password = parser['Vedantu']['pswd']

    driver.get("https://vedantu.com")
    print("Vedantu Opened")
    #Before_Login
    ppk = 0
    while True:
        try:
            signIn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div")
            print("found signIn")
            break
        except:
            print("Finding....")
            ppk+=1
            time.sleep(0.01)
            if ppk==10000:
                return

    time.sleep(3)
    try:
        try:
            cross = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/div/div[1]")
            cross.click()
        except:
            pass
        signIn.click()
        time.sleep(1)
        emailField = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div[3]/div/form/div/div[2]/input")
        emailNext = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div[3]/div/form/input")
        emailField.send_keys(email)
        emailNext.click()
        while True:
            try:
                passwdField = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div[11]/div/form/div/div/input")
                passwdNext = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div[11]/div/form/input")
                passwdField.send_keys(password)
                passwdNext.click()
                break
            except:
                pass
        print("Logged in on Vedantu")
        is_chrome_open = True

    except:
        print("Error")
def vedantu_classes_info(driver):
    #Going into My Schedule
    while True:
        try:
            driver.get("https://www.vedantu.com/my-schedule?view=ALL")
            break
        except:
            pass
    time.sleep(3)
    pdb.set_trace()
    #Finding all the classes info
    while True:
        while True:
            try:
                #Loading the main class container from the website
                driver.get("https://www.vedantu.com/my-schedule?view=ALL")
                full_schedule_container = driver.find_element_by_class_name("mys-cards-view")
                print("LOADED")
                break
            except:
                print("LOADING")
        time.sleep(2)
        #Fetching only the schedule from the container
        full_schedule = full_schedule_container.find_elements_by_class_name("container")
        try:
            date = full_schedule[0].text
            break
        except IndexError:
            driver.refresh()
            continue
    try:
        f_ll= [] #This list will be sent to the user
        f_str="" #This is a temporary string to transfer the text into f_ll
        pdb.set_trace()
        for i in full_schedule[1:]:
            if len(i.text)==16:
                break
            if "PM" in i.text:
                f_ll.append(f_str)
                f_str=""
            f_str+=i.text+"\n"
        f_ll.append(f_str)
        writeFile("vedSchedule.pkl". f_ll) 
    except:
        print("Error")

driver=start_chrome()
vedantu_login(driver)
vedantu_classes_info(driver)
