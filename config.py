import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
      API_ID = int(os.environ.get("APP_ID", "23833905463")
      API_HASH = os.environ.get("API_HASH", "4956e23833905463efb588eb806f9804")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "CHOUDHARY_JI_AK47")
      ADMIN_ID = int(os.environ.get("ADMIN_ID", "902551614") 
      DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://crchoudharyji1122:<Chenaram@2003>@cluster0.cuje2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
