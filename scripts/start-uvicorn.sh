#!/bin/bash
uvicorn --factory libranet_django.api:create_app --reload
