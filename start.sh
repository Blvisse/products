#!/bin/bash

uvicorn backend.app.main:app --reload --port 8080

