from aiogram.utils.keyboard import ReplyKeyboardBuilder


main_menu = ReplyKeyboardBuilder()
main_menu.button(text="Buyurtmalarni ko'rish")
main_menu = main_menu.as_markup()
main_menu.resize_keyboard = True
main_menu.is_persistent = True