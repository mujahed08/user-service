
.pylintrc has been created with following command
pylint --generate-rcfile > .pylintrc

pytest.ini is a configuration file for pytest having higest configuration precedence. -s argument says python print() function 
prints to the console.

To generate pydantic model for API

user-service>datamodel-codegen --url http://localhost:7001/openapi.json --output USER_SERVICE\pydantic_models\generated\user_svc_pcs\models.py


To Start applicationuse the following command
user-service>uvicorn USER_SERVICE.main:app --port 8002 --log-config log4py.yaml --reload --reload-dir USER_SERVICE