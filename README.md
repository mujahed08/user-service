
.pylintrc has been created with following command
pylint --generate-rcfile > .pylintrc

pytest.ini is a configuration file for pytest having higest configuration precedence. -s argument says python print() function 
prints to the console.


To Start applicationuse the following command
user-service-system>uvicorn USER_SERVICE.main:app --port 8002 --log-config log4py.yaml --reload --reload-dir USER_SERVICE