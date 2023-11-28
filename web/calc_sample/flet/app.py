import flet as ft
from flet import Page, TextField


def main(page: Page):
    global operation
    page.title = "Simple Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    operation = "add"  # Global variable for the operation

    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        theme_switch.label = (
            "Light theme" if page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        page.update()

    def toggle_switches_states(prev_dict):
        """
        Toggles the switches states and returns the operation string
        """
        curr_dict = {k: v.value for k, v in switches.items()}

        # Set 'add' to True if all values are False
        if not any(curr_dict.values()):
            curr_dict['add'] = True

        # Find keys that have changed from False to True
        new_true_keys = [k for k, v in curr_dict.items() if v and not prev_dict.get(k, False)]

        # If no keys have changed to True, set 'add' to True
        if not new_true_keys:
            new_true_keys = ['add']

        # Update previous dictionary and reset all switches to False
        prev_dict.update(curr_dict)
        for switch in switches.values():
            switch.value = False

        # Set the new true switches to True
        for new_key in new_true_keys:
            switches[new_key].value = True

        return "".join(new_true_keys)

    def input_handler(e):
        calculate(operation)

    def switch_handler(e):
        global operation
        operation = toggle_switches_states(switches_state)
        calculate(operation)

    def calculate(operation):
        try:
            try:
                first_number_value = float(first_number.value)
                second_number_value = float(second_number.value)
            except ValueError:
                pass
            match operation:
                case "add":
                    result = first_number_value + second_number_value
                case "sub":
                    result = first_number_value - second_number_value
                case "mul":
                    result = first_number_value * second_number_value
                case "div":
                    result = first_number_value / second_number_value
                case _:
                    result = 0
            output_field.value = str(result)

        except UnboundLocalError as e:
            if "first_number_value" in str(e):
                output_field.value = "Please enter a valid first number"
            elif "second_number_value" in str(e):
                output_field.value = "Please enter a valid second number"
            else:
                output_field.value = e

        except ZeroDivisionError as e:
            output_field.value = e
        finally:
            page.update()

    theme_switch = ft.Switch(label="Light theme", on_change=theme_changed)

    first_number = TextField(
        label="First Number",
        on_change=input_handler)
    second_number = TextField(
        label="Second Number",
        on_change=input_handler)

    switches_state = {
        "add": True,
        "sub": False,
        "mul": False,
        "div": False,
    }
    switches = {
        "add": ft.Switch(
            label="Add",
            on_change=switch_handler,
            value=True),
        "sub": ft.Switch(
            label="Subtract",
            on_change=switch_handler),
        "mul": ft.Switch(
            label="Multiply",
            on_change=switch_handler),
        "div": ft.Switch(
            label="Divide",
            on_change=switch_handler),
    }
    switch_icons = {
        "add": ft.Icon(name=ft.icons.ADD_OUTLINED),
        "sub": ft.Icon(name=ft.icons.HORIZONTAL_RULE_OUTLINED),
        "mul": ft.Icon(name=ft.icons.DISABLED_BY_DEFAULT_OUTLINED),
        "div": ft.Icon(name=ft.icons.SAFETY_DIVIDER_OUTLINED),
    }
    output_field = TextField(
        label="Result",
        min_lines=2,
        max_lines=3,
        multiline=True,
        keyboard_type=ft.KeyboardType.MULTILINE
    )
    page.add(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(
                                content=first_number,
                                margin=10,
                                padding=10,
                                alignment=ft.alignment.center,
                                width=150,
                                height=150,
                                border_radius=10
                            ),
                            ft.Column(
                                [
                                    ft.Row([switch_icons["add"], switches["add"]]),
                                    ft.Row([switch_icons["sub"], switches["sub"]]),
                                    ft.Row([switch_icons["mul"], switches["mul"]]),
                                    ft.Row([switch_icons["div"], switches["div"]]),
                                ]
                            ),
                            ft.Container(
                                content=second_number,
                                margin=10,
                                padding=10,
                                alignment=ft.alignment.center,
                                width=150,
                                height=150,
                                border_radius=10
                            ),

                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                content=output_field,
                                margin=10,
                                padding=10,
                                alignment=ft.alignment.top_center,
                                width=350,
                                height=100,
                                border_radius=10
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                content=theme_switch,
                                margin=10,
                                padding=10,
                                alignment=ft.alignment.center,
                                width=150,
                                height=50,
                                border_radius=10
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START
                    )
                ]
            ),
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
