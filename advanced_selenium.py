# clicking by Enter instead of click()
from selenium.webdriver.common.keys import Keys # importing Keys
# find element as usual
login_btn.send_keys(Keys.RETURN) # simulate ENTER key

#get attribute of elements
image_element = self.browser.find_element(By.XPATH, "xpath") # находим элемент обычным образом
actual_text = image_element.get_attribute("src") # достаем то что находится в src
print(actual_text)

#scroll to element
from selenium.webdriver.common.action_chains import ActionChains # необходимый импорт
actions = ActionChains(driver) # создаем экземпляр класса, а driver - это экземпляр вебдрайвера.
element = driver.find_element(By.XPATH, "") # находим элемент
actions.move_to_element(element).perform() # скроллим до элемента


#css property (color)
elem = driver.find_element(By.ID, '') # находим элемент, а driver - это экземпляр вебдрайвера.
color = elem.value_of_css_property('background-color') # достаем css property
expected_color = '' # ожидаемый цвет
assert expected_color == color #сверяем


# hover
from selenium.webdriver import ActionChains # необходимый импорт
mouse = ActionChains(driver) # создаем экземпляр класса, а driver - это экземпляр вебдрайвера.
elem = driver.find_element(By.XX, 'XX') # находим элемент
mouse.move_to_element(elem).perform() # наводим курсор на элемент



# select class
from selenium.webdriver.support.select import Select # необходимый импорт

dropdown = находим элемент обычным способом и кладем сюда
select = Select(dropdown) # создаем экземпляр класса Select и с помощью него начинаем взаимодействовать с выпадающим списком
select.select_by_visible_text(сюда прописываем текст по которому будем выбирать элемент из списка) -> используя этот класс можно выбирать и по другим значениям, не только по тексту.


# list of elements
from selenium.webdriver.remote.webelement import WebElement # необходимый импорт
from selenium.webdriver.support import expected_conditions as ec # необходимый импорт
from typing import List # необходимый импорт

def are_visible(self, locator) -> List[WebElement]:
    return self.wait.until(ec.visibility_of_all_elements_located(locator)) # тут базовый метод я уже прописал, просто надо использовать его в том месте где это необходимо

# drag and drop
from selenium.webdriver import ActionChains # необходимый импорт
actions = ActionChains(driver) # создаем экземпляр класса, а driver - это экземпляр вебдрайвера.
to_drag_elem = driver.find_element(By.ID, 'draggable') # находим элемент который будем тянуть
to_drop_elem = driver.find_element(By.ID, 'droppable') # находим элемент куда будем тянуть первый элемент
actions.drag_and_drop(to_drag_elem, to_drop_elem).perform() # выполняем действие

# дополнительные методы работы с селеинумом

driver.switch_to.alert.accept() #accept alert
driver.switch_to.window(self.driver.window_handles[window_number]) #change window
driver.switch_to.frame(frame) #change frame
driver.current_url #get current url
driver.refresh() #refresh page
driver.close() #close tab (NOT quit driver)


