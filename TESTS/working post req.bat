@echo off
ECHO working curl command with corrent output
curl -X POST "http://localhost:8000/create" -H "Content-type: application/json"  -d "{\"url\": \"https://ravkavonline.co.il\"}"
PAUSE