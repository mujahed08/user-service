"""
FastAPI
"""

from USER_SERVICE.pydantic.holders import Example, Status

logger = get_logger('main.py')
logger.info(Example.schema_json())

logger.info('   Initiliazing Fast API app')
app = FastAPI(title="FastAPI")
logger.info('   Initialized Fast API app')

@app.get("/example", response_model=Status)
async def get_example():
    logger.info('   get_example function is executing')
	message = 'Hello World!'
    return Status(message=f'Returning with message: {message}')

@app.post("/example/ops", response_model=Example,
responses={404: {"model": HTTPNotFoundError}})
async def example_ops(example:Example):
    logger.info('   example_ops function is executing')
    logger.info(example.json())
    return Example(id=1, name='Hellow World!')

logger.info('   End of the main file')
