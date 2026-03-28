import argparse
import logging

from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logging


setup_logging()


parser = argparse.ArgumentParser(description="Trading Bot CLI")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    validate_inputs(args)


    client = get_client()

    print("\n📌 Order Request:")
    print("Symbol:", args.symbol)
    print("Side:", args.side)
    print("Type:", args.type)
    print("Quantity:", args.quantity)
    if args.type.upper() == "LIMIT":
        print("Price:", args.price)

 
    order = place_order(client, args)


    print("\n📊 Order Response:")
    print("Order ID:", order['orderId'])
    print("Status:", order['status'])
    print("Executed Qty:", order['executedQty'])
    print("Avg Price:", order.get('avgPrice', 'N/A'))

    print("\n✅ Order executed successfully")

except Exception as e:
    logging.error(f"Error: {e}")
    print(f"\n❌ Error: {e}")