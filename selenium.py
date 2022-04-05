from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import os

def extract_emails(input_files):
    """Extract an email address from a text file.
        Input files as list of strings.
        Returns a list of the emails."""

    f_emails = open("failed_emails.txt","w")
    emails_list = []
    for file_name in input_files:
        for i in os.listdir(file_name):
            with open(f"{file_name}\{i}","r") as f:
                email_line = f.readlines()
                ind_email = email_line[38].split(' ')[1]
                f_emails.write( ind_email) 
                emails_list.append(ind_email.strip('\n'))
    f_emails.close()

    return emails_list


def delete_failed_emails(emails_list):
    """Search for failed email in thecustomerfactor website
    and delete if found."""

    PATH = r"C:\Users\Charoula Kyriakides\Documents\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=PATH)
    driver.get("https://www.thecustomerfactor.com/home.php")

    #Login
    search = driver.find_element_by_name("username")
    search.send_keys(username)
    search = driver.find_element_by_name("password")
    search.send_keys(password)
    search.send_keys(Keys.RETURN)

    for item in emails_list:
        search = driver.find_element_by_name("s")
        search.send_keys(item)
        search.send_keys(Keys.RETURN)
        driver.find_element_by_id("cb-select-all-1").click() # tick
        sel = Select(driver.find_element_by_name("action2"))
        sel.select_by_visible_text("Delete")
        driver.find_element_by_id("doaction2").click()  # delete
        driver.find_element_by_name("s").clear()
        
    driver.quit()