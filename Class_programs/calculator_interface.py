from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import math

class CalculatorApp(App):
    def calculate(self, instance):
        try:
            num1 = float(self.text_input1.text)
            num2 = float(self.text_input2.text)

            if self.operation == "Addition":
                result = num1 + num2
            elif self.operation == "Subtraction":
                result = num1 - num2
            elif self.operation == "Multiplication":
                result = num1 * num2
            elif self.operation == "Division":
                if num2 == 0:
                    result = "Cannot divide by zero"
                else:
                    result = num1 / num2
            elif self.operation == "Square Root":
                result = math.sqrt(num1)
            elif self.operation == "Power Of":
                result = num1 ** num2
            else:
                result = "Invalid operation"
        except ValueError:
            result = "Invalid input"

        self.output_label.text = f"Result: {result}"

    def build(self):
        self.operation = None
        layout = BoxLayout(orientation='vertical')

        self.text_input1 = TextInput(text='', hint_text='Enter first number')
        layout.add_widget(self.text_input1)

        self.text_input2 = TextInput(text='', hint_text='Enter second number')
        layout.add_widget(self.text_input2)

        operations = [
            "Addition",
            "Subtraction",
            "Multiplication",
            "Division",
            "Square Root",
            "Power Of"
        ]

        for operation in operations:
            button = Button(text=operation)
            button.bind(on_press=self.on_button_click)
            layout.add_widget(button)

        self.output_label = Label(text="Result: ")
        layout.add_widget(self.output_label)

        return layout

    def on_button_click(self, instance):
        self.operation = instance.text
        self.calculate(instance)


if __name__ == "__main__":
    CalculatorApp().run()