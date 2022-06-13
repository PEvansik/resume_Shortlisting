from dateparser.search import search_dates
para = search_dates("Competition opens 1/03/19 and closes 17/05/19 Online meetingApplication(DiscordClone)FrshrTech 12//07/2021 - 01/06/2022 (04/2022 - 05/2022)", settings={'STRICT_PARSING': True, 'DATE_ORDER': 'DMY'})
for x in para:
    date_string =  x[0]
    print(date_string)