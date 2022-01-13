import datetime

from attrs import attr


@attr.s(frozen=True, auto_attribs=True, keyword_only=True)
class Address:
    hash: str
    transactions: str
    log_timestamp: datetime

    @property
    def balance(self):
        return

    @classmethod
    def from_ether_scan(cls, txn_by_address_response) -> 'Address':
        # See example response:
        # https://github.com/pcko1/etherscan-python/blob/master/logs/standard/get_internal_txs_by_address.json
        hash = txn_by_address_response['kwargs']['address']
        transactions = txn_by_address_response['res']
        log_timestamp = datetime.datetime(txn_by_address_response['log_timestamp'])
        return Address(hash=hash,
                       transactions=transactions,
                       log_timestamp=log_timestamp)
