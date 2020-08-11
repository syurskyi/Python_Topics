import logging

def foo(A, B, C):

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler("ex3_log.log.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    logger.info(f'args: ({A}, {B}, {C})')
    
    result = (A - B) * C

    logger.info(f'result: {result}')
    
    return result
