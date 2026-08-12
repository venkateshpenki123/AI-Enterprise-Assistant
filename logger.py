import logging
import os


os.makedirs("logs", exist_ok=True)


logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_question(question):

    logging.info(
        f"QUESTION: {question}"
    )


def log_answer(answer):

    logging.info(
        f"ANSWER: {answer}"
    )


def log_error(error):

    logging.error(
        f"ERROR: {error}"
    )


def log_warning(message):

    logging.warning(
        f"WARNING: {message}"
    )


def log_info(message):

    logging.info(
        f"INFO: {message}"
    )