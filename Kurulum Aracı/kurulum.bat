@echo off
chcp 65001 > nul
echo Unutmayın Python kurmadıysanız kurulum yapılmaz. Made by yıldırımlord
timeout /t 2 > nul
echo Python kurmak için klasördeki Python dosyasına çift tıklayın ve kurun sonrasında tekrar bu aracı çalıştırın.

timeout /t 7 > nul
cls
echo Kurulum başlatıldı.
echo ///////////////////////////
timeout /t 2 > nul
pip3 install -r requirements.txt

if %errorlevel% neq 0 (
    echo Kurulum sırasında bir hata oluştu!
    pause
    exit /b
)
cls
echo Kurulum tamamlandı. SMS Bomber programı çalıştırılıyor.
timeout /t 3 > nul
cd..
python smsbomber.py

pause