from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask_admin.form.upload import ImageUploadField
from flask import redirect,url_for

class AdminView(ModelView):
    def is_accessible(self): # Дія яка повертає True якщо є повноваження
                             # або False в іншому випадку
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # Що робити коли немає повноважень
        return redirect(url_for('auth_app.login'))



class ImageView(AdminView):
    form_extra_fields = {
        'img': ImageUploadField(base_path="static")
    }
