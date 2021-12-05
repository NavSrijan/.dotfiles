#!/bin/sh

URL="https://www.reddit.com/message/unread/.json?feed=39f25ca230b0a79e4d43530ed988ced8e772bff4&user=Monkee_monk"
USERAGENT="polybar-scripts/notification-reddit:v1.0 u/Monkee_monk"

notifications=$(curl -sf --user-agent "$USERAGENT" "$URL" | jq '.["data"]["children"] | length')

if [ -n "$notifications" ] && [ "$notifications" -gt 0 ]; then
    echo "#1 $notifications"
else
    echo "#2"
fi
