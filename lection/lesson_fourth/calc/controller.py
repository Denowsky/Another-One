# Python - от простого к сложному

import model_sub as model
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.action()
    view.view_data(result, "result")