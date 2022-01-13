from datetime import datetime

from src.address import (
    Address,
)
from etherscan import (
    etherscan,
)

from rich.pretty import pprint
import os


class Config:
    def __init__(self):
        pass

    @property
    def etherscan_api_key(self) -> str:
        return os.environ['etherscan_api_key']


config = Config()


class Controller:
    def __init__(self):
        self.client = etherscan.Etherscan(api_key=config.etherscan_api_key)

    @classmethod
    def time_stamp_format(cls, datetime_: datetime):
        return int(datetime_.timestamp())


if __name__ == '__main__':
    ctrl = Controller()
    latest_block_number = ctrl.client.get_block_number_by_timestamp(timestamp=ctrl.time_stamp_format(datetime.now()),
                                                                    closest='before')

    addresses = [
        dict(address=Address.from_ether_scan(address=address,
                                             txn_by_address_response=ctrl.client.get_normal_txs_by_address(address,
                                                                                                           0,
                                                                                                           latest_block_number,
                                                                                                           1000)))
        for address in [
            ''  # make this configurable from env files
        ]
    ]
    for address in addresses:
        for k, v in address.items():
            pprint(v.__dict__)
