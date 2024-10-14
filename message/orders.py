from aiogram.types import Message
from api_requests import get_recent_orders, get_order, get_customer

async def recent_orders_answer(message: Message):
    wait_msg = await message.answer("Sorov yuborilmoqda....")
    orders = await get_recent_orders()
    text = ""
    for i in orders: text += "➖" * 5 + "\n" + str(i["id"]) + "-raqamli buyurtma " + "maxsus nom: " + i["fio"] + "\n"
    text += "\nBuyurtma raqamini yuboring." if text else "Bugunga buyurtmalar yo'q!"
    await wait_msg.delete()
    await message.answer(text)

async def get_order_answer(message: Message):
    if not message.text.isdigit(): return 
    # try:
    wait_msg = await message.answer("Sorov yuborilmoqda....")
    order = await get_order(message.text)
    if order.get("detail"): 
        await wait_msg.delete()
        await message.answer("Buyurtma ma'luotlari topilmadi!")
        return
    customer = await get_customer(order["customer_id"])
    if customer.get("detail"): 
        await wait_msg.delete()
        await message.answer("Buyurtmachi ma'luotlari topilmadi!")
        return
    # except:
    #     await message.answer("Buyurtma ma\lumotlarni olishda qandaydir xatolik yuzaga keldi. Menga buyurtma raqamini yuboring.")
    #     return
    
    await wait_msg.delete()
    await message.answer_location(
        latitude=order["latitute"],
        longitude=order["longitute"],
    )

    await message.answer(
        f"{order['id']}-buyurtma\n\n"
        f"Buyurtmachi: {customer['customer_name']}\n"
        f"Telefon: {customer['telefon']}\n"
        f"Mahsulot: {order['product']}\n"
        f"Miqdori: {order['suv_miqdori']}\n"
        f"eslatma: {order['eslatma']}\n"
        # f"holat: {'faol' if order['status'] else 'bajarilgan'}"
    )