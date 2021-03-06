from brownie import FundMe
from scripts.helpful_scripts1 import get_account


def deploy_fund_me():
    account = get_account()
    print(account)
    fund_me = FundMe.deploy({"from": account}, publish_source=True)
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
