"""
Microservices Architecture-এ centralized logging implement করার জন্য কিছু নির্দিষ্ট coding practice অনুসরণ করতে হবে।

1. সাধারণ text লগের বদলে JSON format log generate করতে হবে, যাতে Log Aggregator সহজেই তা বুঝতে পারে।
2. প্রতিটি request-এর সাথে একটি ইউনিক ID বা Correlation ID যুক্ত করতে হবে।

Python-এ python-json-logger লাইব্রেরি ব্যবহার করে খুব সহজেই JSON logging setup করা যায়।
"""

import logging
import sys
import uuid
from pythonjsonlogger import jsonlogger

def setup_logger():
    logger = logging.getLogger("payment_microservice")   # set name
    logger.setLevel(logging.INFO)   # set levelname

    logHandler = logging.StreamHandler(sys.stdout)

    formatter = jsonlogger.JsonFormatter('%(asctime)s %(name)s %(levelname)s %(message)s %(correlation_id)s %(service_name)s')
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)

    return logger

logger = setup_logger()

def process_payment():
    correlation_id = str(uuid.uuid4())

    log_context = {
        "correlation_id": correlation_id,
        "service_name": "payment_service",
        "user_id": 105
    }

    logger.info("Payment Processing Started", extra=log_context)

    try:
         # other logic
        logger.info("Payment Successful", extra=log_context)
    except Exception as e:
        logger.error("Payment Failed", extra=log_context, exc_info=True)


if __name__ == '__main__':
    process_payment()

"""
- এই কোড রান করলে console-এ JSON format-এ log output আসবে।
- প্রতিটি লগের সাথে correlation_id এবং service_name যুক্ত থাকবে।
- production envrionment-এ, container-এর এই stdout আউটপুটগুলো Filebeat বা Fluentd স্বয়ংক্রিয়ভাবে সংগ্রহ করে Logstash বা Elasticsearch-এ পাঠিয়ে দেবে।
- অন্য কোনো সার্ভিসে request পাঠানোর সময় এই correlation_id টি HTTP হেডারে (যেমন: X-Correlation-ID) যুক্ত করে পাঠাতে হবে, যাতে পুরো system-এ রিকোয়েস্টটি track করা যায়।
"""
