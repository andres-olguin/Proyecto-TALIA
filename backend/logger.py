import logging
import sys

def get_logger(name="TALIA APP", level=logging.INFO, output=sys.stdout):
    """
    Returns a configured logger instance. 
    Defaults to stdout. Can easily be extended.
    """
    logger = logging.getLogger(name)

    # Prevent duplicate logs if get_logger is called multiple times
    if not logger.handlers:
        logger.setLevel(level)

        # Configure output handler based on the provided argument
        handler = logging.StreamHandler(output)
        handler.setLevel(level)

        # Standard formatting
        formatter = logging.Formatter(
            '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)

        logger.addHandler(handler)

    return logger

if __name__ == '__main__':
    from sys import stdout
    log = get_logger(name="LOGGER EXAMPLE", output=stdout)

    log.info("Printing to stdout")