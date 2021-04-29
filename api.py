#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 13:48:09 2021

@author: abhishek
"""

from linkedin import linkedin

redirectURI = "https://www.google.com/"
URLENCODE = """https%3A%2F%2Fwww.google.com%2F"""
clientId = '861r5s6eu968jk'
clientSecret = 'E0LoDI9ShHoHCPOl'


access_token="AQW7X1e2kVsxuxt8JjEqh9F87MEDZHJwkrOBhOLtQrJnKUZQgkiHPO4KyEcqcLxPZ3cZPaAqBJUPSQRc4VoH7l5TjVs5R4igaGYVqztQmprIl-XHw4wUU9p0vN9Y4_RkSCRqjL4gNdMq67CUKl24X5RT-vCUkOs1SZgaSiKHJv-tr76Dt9mDpmQnP3W6PwwXVL9AZHHeiQYQmG9pVem81W-pqiE3meQFC5XBZo5kruyhLxdkAxxbQAI_DktxHRUPmCP8XJG_Xc-q05yCDvpEfpasFqI4bN0f4NibKo3BHoEazD7xKB1PcsIck1i8_tGHMj4rYqc5i2iSECoS29EaAkPeq54bKg"




application = linkedin.LinkedInApplication(token=access_token)

application.get_profile()
application.get_connections()
application.search_job(selectors=[{'jobs': ['id', 'customer-job-code', 'posting-date']}], params={'title': 'python', 'count': 2})
