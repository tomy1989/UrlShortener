@echo off
ECHO curl with error
curl -X POST "http://localhost:8000/create" -H "Content-type: application/json"  -d "{\"url\": \"ravkavonline.co.il\"}"
PAUSE