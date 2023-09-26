import time
from pprint import pprint
import pandas as pd
import numpy as np
import datetime,time
# For formatted dictionary printing>>>
import telegram

bot = telegram.Bot(token='6343206405:AAHkaKIXCMvif0yqkzvTYWasYPEIsTmImgQ')

date_now = datetime.datetime.utcnow()
date_date = str(date_now)[0:10]

pce_date = ['2023-09-26 20:30:00','2023-09-29 20:30:00','2023-10-27 20:30:00','2023-11-30 21:30:00','2023-12-22 21:30:00']
cpi_date = ['2023-09-26 20:30:00','2023-10-12 20:30:00','2023-11-14 21:30:00','2023-12-12 21:30:00']
feinong_date = ['2023-09-26 20:30:00','2023-10-06 20:30:00','2023-11-03 21:30:00','2023-12-01 21:30:00']

feinong_text = '美国非农数据通常关注两个值：非农业就业人数、失业率。顾名思义，就是反映美国非农业人口的就业状况的数据指标。在发布前后几分钟通常会影响大多数加密货币的价格，非农就业人数下降或者失业率增加，说明美国就业承压，美联储加息预期下降属于利好，通常会引起加密货币价格上涨，非农就业人数增加或者失业率降低，说明美国经济强韧，美联储加息预期上涨属于利空，通常会引起加密货币价格下跌。当您手中在发布时间时有高倍杠杆合约的时候，要注意风险把控。'

cpi_text = '消费者价格指数（CPI）：显示美国当前的通货膨胀率，会影响该国加息的联邦公开市场委员会（FOMC）会议，在发布前后几分钟通常会影响大多数加密货币的价格，当发布值小于预期说明通胀下降，美联储加息预期下降属于利好，通常会引起加密货币价格上涨，大于预期值属于利空，通常会引起加密货币价格下跌。当您手中在发布时间时有高倍杠杆合约的时候，要注意风险把控。'

pce_text = '个人消费支出指数（PCE）：核心PCE物价指数是衡量美国民间消费通胀的关键指标，会影响该国加息的联邦公开市场委员会（FOMC）会议，在发布前后几分钟通常会影响大多数加密货币的价格，当发布值小于预期预示CPI有可能下降，美联储加息预期下降属于利好，通常会引起加密货币价格上涨，大于预期值属于利空，通常会引起加密货币价格下跌。当您手中在发布时间时有高倍杠杆合约的时候，要注意风险把控。'

for ele in pce_date:
	sub_ele = ele[0:10]
	ele_time = ele[11:19]
	if ele == date_date:
		content = '\n \
%s今晚%s是美国公布PCE时间。\n \
%s'%(sub_ele,ele_time,pce_text)
		bot.sendMessage(chat_id='-1001975215255', text = text_4,message_thread_id=6) #链上数据分享
	else:
		continue

for ele in cpi_date:
	sub_ele = ele[0:10]
	ele_time = ele[11:19]
	if ele == date_date:
		content = '\n \
%s今晚%s是美国公布CPI时间。\n \
%s'%(sub_ele,ele_time,cpi_text)
		bot.sendMessage(chat_id='-1001975215255', text = text_4,message_thread_id=6) #链上数据分享
	else:
		continue

for ele in feinong_date:
	sub_ele = ele[0:10]
	ele_time = ele[11:19]
	if ele == date_date:
		content = '\n \
%s今晚%s是美国公布非农数据时间。\n \
%s'%(sub_ele,ele_time,feinong_text)
		bot.sendMessage(chat_id='-1001975215255', text = text_4,message_thread_id=6) #链上数据分享
	else:
		continue



