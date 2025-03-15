from django.forms import ModelForm
from django.core.exceptions import ValidationError

from catalog.models import Product


class ProductForm(ModelForm):

    restrictions = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    class Meta:
        model = Product
        # fields = "__all__"
        exclude = ("owner",)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        for restriction in self.restrictions:
            if restriction in name.lower():
                raise ValidationError(
                    "Вы используете запрещенные слова в названии продукта"
                )
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        for restriction in self.restrictions:
            if restriction in description.lower():
                raise ValidationError(
                    "Вы используете запрещенные слова в описании продукта"
                )
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена продукта не может быть отрицательной")
        if price == 0:
            raise ValidationError("Цена продукта не может быть нулевой")
        return price

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите наименование",
            }
        )

        self.fields["description"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите описание",
            }
        )

        self.fields["photo"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )

        self.fields["category"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Выберите категорию",
            }
        )

        self.fields["price"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите стоимость товара",
            }
        )

        # self.fields['owner'].widget.attrs.update({
        #     'class': 'form-control',
        #     'placeholder': 'Заполните автора товара',
        # })


class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            "is_published",
        ]

    def __init__(self, *args, **kwargs):
        super(ProductModeratorForm, self).__init__(*args, **kwargs)

        self.fields["is_published"].widget.attrs.update(
            {
                "class": "form-check-input",
                "placeholder": "Статус публикации",
            }
        )
