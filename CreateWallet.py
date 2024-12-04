import uuid
import secrets
from mnemonic import Mnemonic
from api import Api
from web3 import Web3
from eth_account import Account

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