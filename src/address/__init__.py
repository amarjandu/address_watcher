import datetime
from typing import Set, Dict

import attr


@attr.s(frozen=True, auto_attribs=True, kw_only=True)
class Address:
    address: str
    transactions: Set[Dict[str, str]]

    @property
    def balance(self):
        return

    @classmethod
    def from_ether_scan(cls, address, txn_by_address_response) -> 'Address':
        # See example response:
        # https://github.com/pcko1/etherscan-python/blob/master/logs/standard/get_internal_txs_by_address.json
        return Address(address=address,
                       transactions=txn_by_address_response)
