from selenium import webdriver
from config import keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


def order(k):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #driver = webdriver.Chrome('./chromedriver')
    driver.get(k['product_url'])

    # Add to cart
    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    sleep(1)
    # Checkout
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    # Billing name
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k["name"])
    # email
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k["email"])
    # phone number
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k["phone"])
    # address
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k["address"])

    # apt number

    driver.find_element_by_xpath('//*[@id="oba3"]').send_keys(k["apt"])
    # postal code
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k["po"])
    # city
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(k["city"])
    # Province
    driver.find_element_by_xpath('//*[@id="order_billing_state"]/option[1]').click()
    # Country
    driver.find_element_by_xpath('//*[@id="order_billing_country"]/option[2]').click()
    # card
    driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(k["card"])
    # card expiry month
    driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[{}]'.format(k['exp_month'])).click()
    # card expiry year
    driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[{}]'.format(k['exp_year'])).click()
    # cvv
    #driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(k["cvv"])

    # terms and conditions
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()


    # process payment
    #driver.find_element_by_xpath('//*[@id="pay"]/input').click()
    sleep(20)


if __name__ == '__main__':
    order(keys)
