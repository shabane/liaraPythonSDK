#!/usr/bin/env python
from mail import MailServer

# simple example
mailserver1 = MailServer("67193094cb34b917d17acd1d", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySUQiOiI2NDllOWVkNTdhZWIxMjE4OTI0ODdkMjIiLCJ0eXBlIjoiYXV0aCIsImlhdCI6MTc0MDE0NzE0Mn0._v_DcIOeuSOkZ02I4IlmqOgHXbgopkED94vx4-Wa50A")
mails = mailserver1.list_income()
i0 = mails[0].get_text();
