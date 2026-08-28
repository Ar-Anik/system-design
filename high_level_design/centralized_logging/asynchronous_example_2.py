import logging
import logging.handlers
import queue
import sys
from pythonjsonlogger import jsonlogger


def setup_async_logger():
    # Infinite Queue
    log_queue = queue.Queue(-1)

    # Logger Define
    logger = logging.getLogger("advanced_microservice")
    logger.setLevel(logging.INFO)

    # JSON Formatter
    formatter = jsonlogger.JsonFormatter(
        '%(asctime)s %(name)s %(levelname)s %(message)s'
    )

    # Console Handler (যেটি প্রকৃত পক্ষে লগ আউটপুট দেবে)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # Queue Listener (এটি ব্যাকগ্রাউন্ড Thread-এ চলবে এবং Queue থেকে ডেটা নিয়ে Console Handler-এ পাঠাবে)
    queue_listener = logging.handlers.QueueListener(
        log_queue, console_handler, respect_handler_level=True
    )
    queue_listener.start()

    # Queue Handler (মূল Application এটি ব্যবহার করে Queue-তে লগ পাঠাবে)
    queue_handler = logging.handlers.QueueHandler(log_queue)
    logger.addHandler(queue_handler)

    return logger, queue_listener


logger, listener = setup_async_logger()

try:
    # other business logic
    logger.info("This is an asynchronous log Message")
finally:
    # Application Listener stop
    listener.stop()
