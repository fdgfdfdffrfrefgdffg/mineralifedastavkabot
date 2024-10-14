from aiogram import Router, F
from . import start, orders
import states, filters


router = Router()

router.message.register(start.input_login, states.Login.login)
router.message.register(start.input_password, states.Login.parol)
router.message.register(start.start_no, filters.UserCheck())
router.message.register(start.start_yes, F.text == "/start")
router.message.register(orders.recent_orders_answer, F.text == "Buyurtmalarni ko'rish")
router.message.register(orders.get_order_answer)