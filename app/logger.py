import logging
import sys
import os


def setup_logger(logger_name, log_file_path=None, level=logging.INFO):
    """
    Sets up a logger with a file handler and a stream handler.

    Args:
        logger_name (str): The name of the logger.  Use __name__
        log_file_path (str, optional): Path to the log file. If None, logs to console only.
        level (int, optional): The logging level. Defaults to logging.INFO.
            Use logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR,
            or logging.CRITICAL.

    Returns:
        logging.Logger: The configured logger.
    """
    # Create the logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)  # Set the logger's level

    # Create a formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Create handlers
    if log_file_path:
        # Ensure the directory exists
        log_dir = os.path.dirname(log_file_path)
        if log_dir:  # Check if directory is not empty
            os.makedirs(log_dir, exist_ok=True)
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler(sys.stdout)  # Output to console
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
