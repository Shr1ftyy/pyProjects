import os 
import bs4 
from bs4 import BeautifulSoup as soup 
import requests 

link = 'https://www.google.com/search?tbm=fin&sxsrf=ACYBGNSF_NrNmkSR99cGCm9zog6XGsRD1Q:1575672058465&q=NYSE:+GS&stick=H4sIAAAAAAAAAONgecRoyi3w8sc9YSmdSWtOXmNU4-IKzsgvd80rySypFJLgYoOy-KR4uLj0c_UNzKtyCiwNeRaxcvhFBrtaKbgHAwCUpmQ5RQAAAA&sa=X&ved=0ahUKEwjq48zqi6LmAhUJyDgGHeiTAioQlq4CCDgwAA#scso=_AdnqXfzzFPiE4-EPtt-PmA49:0'
source = requests.get()