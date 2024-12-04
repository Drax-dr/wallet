import json
import uuid
import secrets
from mnemonic import Mnemonic
from api import Api
from web3 import Web3
from eth_account import Account
from typing import NewType

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from labelbutton import LabelButton

Address = NewType('Address', 'str')
print("In module products __package__, __name__ ==", __package__, __name__)
class Wallet:
    def new(
            self,
            password: str
            ) -> None:
        self.w3 = Web3()
        gn = Mnemonic("english")
        words = gn.generate(160)
        self.id = uuid.uuid4()
        self.api = self.id.hex
        self.private = "0x"+secrets.token_hex(32)
        #acc = self.w3.eth.account.create()
        acc = Account.from_key(self.private)
        enc = acc.encrypt(password)
        self.data = {'id':self.id,'private-key':self.private,'eth': acc, 'encrypt':enc}

    def send(
            self,
            pk,
            to: Address
            ):
        pass

    def get_balance(self,address: Address):
        pass

    def receive(self,from_: Address) -> str:
        pass

    def buy(self,amount: int,cur: str):
        pass

class Home(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.add_widget(Label(text="Welcome to Bucky Wallet"))
        btn = LabelButton(text="Create a new wallet")
        self.add_widget(btn)

class CreateWallet(BoxLayout):
    def __init__(self):
        super().__init__()
        

class UI(App):
    def build(self):
        return Home()

if __name__ == '__main__':
    UI().run()