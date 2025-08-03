from pydantic import BaseModel
from faker import Faker

faker = Faker()


class ItemDataModel(BaseModel):
    title: str
    description: str

    @staticmethod
    def create_item_data():
        return ItemDataModel(
            title=faker.word().capitalize(),
            description=faker.sentence(nb_words=10)
        )

    @staticmethod
    def creating_too_long_data():
        return ItemDataModel(
            title=faker.text(max_nb_chars=356),
            description=faker.text(max_nb_chars=356)
        )
