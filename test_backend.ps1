Write-Host "=== Testing Backend APIs ===" -ForegroundColor Green


Write-Host "`n1) Testing /weather endpoint..." -ForegroundColor Cyan
Invoke-WebRequest `
    -Uri "http://127.0.0.1:5000/weather" `
    -Method POST `
    -Body '{"city":"Pune"}' `
    -ContentType "application/json" `
| Select-Object -ExpandProperty Content


Write-Host "`n2) Testing /predict_with_weather endpoint..." -ForegroundColor Cyan
Invoke-WebRequest `
    -Uri "http://127.0.0.1:5000/predict_with_weather" `
    -Method POST `
    -Body '{"crop":"rice","city":"Pune"}' `
    -ContentType "application/json" `
| Select-Object -ExpandProperty Content

Write-Host "`n=== Testing Complete ===" -ForegroundColor Green
