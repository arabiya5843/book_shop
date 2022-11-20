from models import User

us = User("Ahmad", "Shoxbozov" , "shox")
us.save()
us.set_password("shox_master")
