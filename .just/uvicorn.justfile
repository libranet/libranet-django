# uvicorn

export PORT := env('PORT', '8000')
export HOST := env('HOST', '8000')

# show help for uvicorn
[group: 'uvicorn']
[unix]
uvicorn-help:
    .venv/bin/uvicorn --help

alias help-uvicorn := uvicorn-help


# start the app using uvicorn
[group: 'uvicorn']
[unix]
start-app-uvicorn host="0.0.0.0" port="8000":
    .venv/bin/uvicorn --factory libranet_django.api:create_app --host {{host}} --port {{port}}

alias run-app-uvicorn := start-app-uvicorn
alias run-app := start-app-uvicorn
alias start-app := start-app-uvicorn

alias uvicorn-start := start-app-uvicorn
alias start-uvicorn := start-app-uvicorn


# start the app using uvicorn with reload
[group: 'uvicorn']
[unix]
start-app-uvicorn-reload host="0.0.0.0" port="8000":
    .venv/bin/uvicorn --factory libranet_django.api:create_app --host {{host}} --port {{port}} --reload

alias run-app-reload := start-app-uvicorn-reload
alias start-app-reload := start-app-uvicorn-reload


# open the app in the browser
# [group: 'uvicorn']
# [unix]
# open-app host="0.0.0.0" port="8000":
#     @ xdg-open http://{{host}}:{{port}}

# open the app in the browser
[group: 'uvicorn']
[unix]
open-app:
    @ xdg-open http://${HOST}:${PORT}


# open the swagger-docs in the browser
[group: 'uvicorn']
[unix]
open-app-docs host="0.0.0.0" port="8000":
    @ xdg-open http://{{host}}:{{port}}/docs