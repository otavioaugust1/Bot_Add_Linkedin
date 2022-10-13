
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(r"../Bot_Add_Linkedin/chromedriver.exe")
driver.get("https://linkedin.com")
time.sleep(15)


'''Acesse várias páginas de contatos, escolha quantos com "n_pages"
Selecione todos os botões "Mensagem"
keyword = escolha uma area que queira realizar a pesquisa
Gere uma mensagem personalizada com uma saudação pessoal e o primeiro nome do contato
Envie essas mensagens para quantos contatos quiser!'''

n_pages = 5
keyword = 'sisreg'




for n in range(1, n_pages + 1):

    driver.get(
        "https://www.linkedin.com/search/results/all/?keywords=" + str(n))
    time.sleep(5)

    all_buttons = driver.find_element_by_xpach(
        '/html/body/div[4]/div[3]/div[2]/section/div/nav/div/ul/li[1]/div/button/li-icon/svg').click()
    message_buttons = [btn for btn in all_buttons if btn.text == "Message"]

    for i in range(6, 7):
        # click on "Message" button
        driver.execute_script("arguments[0].click();", message_buttons[i])
        time.sleep(2)

        # activate main div
        main_div = driver.find_element_by_xpath(
            "//div[starts-with(@class, 'msg-form__msg-content-container')]")
        driver.execute_script("arguments[0].click();", main_div)

        # type message
        paragraphs = driver.find_elements_by_tag_name("p")

        all_span = driver.find_elements_by_tag_name("span")
        all_span = [s for s in all_span if s.get_attribute(
            "aria-hidden") == "true"]

        idx = [*range(3, 23, 2)]
        greetings = ["Olá", "Oi"]
        all_names = []

        for j in idx:
            name = all_span[j].text.split(" ")[0]
            all_names.append(name)

        greetings_idx = random.randint(0, len(greetings)-1)
        message = greetings[greetings_idx] + " " + all_names[i] + \
            ", tudo bem?\n Sou Otávio Augusto, atualmente como consultor técnico no Ministério da Saúde. Com 15 anos de experiência no Sistema Único de Saúde - SUS (sendo 9 anos em cooperação com o Sistema de Regulação - SISREG), contribuo na melhoria do processo de regulação em saúde no país. \n O motivo de me conectar é para expandir minhas conexões no LinkedIn. Busco pessoas da área de gestão em saúde e regulação.\n Obrigado."

        paragraphs[-5].send_keys(message)
        time.sleep(2)

        # send message
        submit = driver.find_element_by_xpath(
            "//button[@type='submit']").click()
        time.sleep(2)

        # close div
        close_button = driver.find_element_by_xpath(
            "//button[starts-with(@data-control-name, 'overlay.close_conversation_window')]")
        driver.execute_script("arguments[0].click();", close_button)
        time.sleep(2)
