# login_test.ps1
$account = "stanleyzhang@quasitek.info"
$password = "qqq112233"
$loginUrl = "http://127.0.0.1:8080/auth/login"

# 發送 POST 並接收回傳資料
$response =
Invoke-RestMethod -Uri $loginUrl `
-Method POST -ContentType "application/json" `
-Body (@{account = $account; password = $password} | ConvertTo-Json)

# 顯示結果
Write-Host "Successfully logged in" -ForegroundColor Green
Write-Host "Access Token: $($response.access_token)"
Write-Host "Token Type:   $($response.token_type)"
Write-Host "User ID:      $($response.user_id)"