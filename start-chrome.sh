#!/bin/bash
# kill any existing google-chrome processes
pkill -f /usr/bin/google-chrome

mkdir -p /app/data/chrome_data 
sleep 8

# start google-chrome
google-chrome \
  --user-data-dir=/app/data/chrome_data \
  --window-position=0,0 \
  --window-size=${RESOLUTION_WIDTH},${RESOLUTION_HEIGHT} \
  --start-maximized \
  --no-sandbox \
  --disable-dev-shm-usage \
  --disable-software-rasterizer \
  --disable-setuid-sandbox \
  --no-first-run \
  --no-default-browser-check \
  --no-experiments \
  --ignore-certificate-errors \
  --remote-debugging-port=${CHROME_DEBUGGING_PORT} \
  --remote-debugging-address=${CHROME_DEBUGGING_HOST} \
  "https://outshift.com"
  # --disable-gpu \