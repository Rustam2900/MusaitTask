all_languages = ['uz', 'ru']

message_history = {}

default_languages = {
    "language_not_found": "Siz to'g'ri tilni tanlamadingiz!\n"
                          "Сиз тўғри тилни танламадингиз!",
    "welcome_message": "Assalomu alaykum, xush kelibsiz!\n"
                       "Quyidagi tillardan birini tanlang!\n\n"
                       "Ассалому алайкум, хуш келибсиз!\n"
                       "Қуйидаги тиллардан бирини танланг!",

    "uz": {
        "not": "❌ You cannot use the bot, you are blacklisted.\n"
               "❗ To use the bot, contact the admin: @ruqiyasuv",
        "connection": "Currently, we only provide services for Fergana:\n"
                      "Looking for dealers in other regions:\n"
                      "For offers:\n"
                      "📞+998916694474 📩 @Ruqiyasuv",
        "name_update": "Update full name",
        "phone_update": "Update phone number",
        "lang_update": "Change language",
        "full_name_update": "Your full name has been successfully updated:",
        "admin_not": "👮🏻‍♂️ Sorry, you are not an Admin",
        "admin": "️Admin",
        "admin_welcome": "👮🏻‍♂️ Welcome, Admin",
        "back": "Back",
        "country": "Select district:",
        "state_": "Select region:",
        "order__": "Your order has been accepted, our couriers will contact you within 24 hours.",
        "min_order_required": "minimum order required",
        "min_order_error": "minimum order not met",
        "send_receipt": "send receipt",
        "order": "My Orders",
        "order_save": "Your order has been accepted and saved.",
        "send_location_order": "Send your location to confirm your order.",
        "product_add_cart": "Your products have been added to the cart, you can place an order from there:",
        "products_quantity_enter": "Enter the quantity of the product:",
        "invalid_quantity": "Please enter a value consisting of a number and 'pcs', e.g., 10 or 10 pcs",
        "send_location": "Send location",
        "product_shopping_cart": "Your cart:",
        "product_not_cart": "Your cart is empty.",
        "cart": "🛒Cart",
        "place_order": "Place Order",
        "delivery_time": "Delivery time",
        "products_price": "Price",
        "products_description": "Description",
        "products": "Products",
        "category_select": "Select products",
        "order_not_found": "Order not found!",
        "successful_changed": "Successfully changed",
        "select_language": "Select language!",
        "categories": "✅Place an order",
        "my_orders": "📦 My Orders",
        "contact_us": "📲 Contact Us",
        "settings": "⚙️ Settings",
        "ID": "ID",
        "contact": "Please enter your number, Example: +998 93 068 29 11",
        "contact_update": "Your phone number has been successfully updated:",
        "successful_registration": "Successfully registered",
        "sorry": "Sorry, try another number",
        'invalid_id': "Sorry, the ID you provided is incorrect. Please try again.",
    },

    "ru": {
        "not": "❌ Вы не можете использовать бот, вы в черном списке.\n"
               "❗ Для использования бота свяжитесь с администратором: @ruqiyasuv",
        "connection": "На данный момент у нас есть услуги только для Ферганы:\n"
                      "Для других регионов ищем дилеров:\n"
                      "Для предложений:\n"
                      "📞+998916694474 📩 @Ruqiyasuv",
        "name_update": "Изменить полное имя",
        "phone_update": "Изменить номер телефона",
        "lang_update": "Изменить язык",
        "full_name_update": "Ваше полное имя успешно обновлено:",
        "admin_not": "👮🏻‍♂️ Извините, вы не Админ",
        "admin": "️Админ",
        "admin_welcome": "👮🏻‍♂️ Добро пожаловать, Админ",
        "back": "Назад",
        "country": "Выберите район:",
        "state_": "Выберите область:",
        "order__": "Ваш заказ принят, наши курьеры свяжутся с вами в течение 24 часов.",
        "min_order_required": "требуется минимальный заказ",
        "min_order_error": "недостаточно минимального заказа",
        "send_receipt": "отправьте чек",
        "order": "Мои заказы",
        "order_save": "Ваш заказ принят и сохранен.",
        "send_location_order": "Отправьте ваше местоположение для подтверждения заказа.",
        "product_add_cart": "Ваши товары добавлены в корзину, заказывайте оттуда:",
        "products_quantity_enter": "Введите количество товара:",
        "invalid_quantity": "Пожалуйста, введите число и слово 'штук', например: 10 или 10 штук",
        "send_location": "Отправить местоположение",
        "product_shopping_cart": "Ваша корзина:",
        "product_not_cart": "Ваша корзина пуста.",
        "cart": "🛒Корзина",
        "place_order": "Оформить заказ",
        "delivery_time": "Время доставки",
        "products_price": "Цена",
        "products_description": "Описание",
        "products": "Товары",
        "category_select": "Выберите товары",
        "order_not_found": "Заказ не найден!",
        "successful_changed": "Успешно изменено",
        "select_language": "Выберите язык!",
        "categories": "✅Оформить заказ",
        "my_orders": "📦 Мои заказы",
        "contact_us": "📲 Свяжитесь с нами",
        "settings": "⚙️ Настройки",
        "ID": "ID",
        "contact": "Пожалуйста, введите номер, пример: +998 93 068 29 11",
        "contact_update": "Ваш номер телефона успешно обновлен:",
        "successful_registration": "Успешно зарегистрировано",
        "sorry": "Извините, попробуйте другой номер",
        "invalid_id": "Извините, указанный вами идентификатор неверен. Попробуйте еще раз."
    }

}

user_languages = {}
local_user = {}

introduction_template = {
    'uz': """
<b>💧 Ruqiya Shifo suvi</b>
Tanangiz va ruhingiz salomatligi uchun Ruqiya qilingan tabiiy toza ichimlik suvi.

<b>🚛 Yetkazib berish bepul</b>
""",
    'ru': """
<b>💧 Руқия Шифо суви</b>  
Танангиз ва руҳингиз саломатлиги учун Руқия қилинган табиий тоза ичимлик суви.  

<b>🚛 Етказиб бериш бепул</b>
"""
}

order_text = {
    "uz": "Order number {} \n order status {}",
    "ru": "Номер заказа {} \n Статус заказа {}"
}


def fix_phone(phone):
    if "+" not in phone:
        return f"+{phone}"
    return phone
