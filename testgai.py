#import google.generativeai as generativeai

#generativeai.configure(api_key="AIzaSyDHEz77ybg7OG_HTO_smM-M_V5hKzWWJPg")
#model_id = "gemini-2.0-flash-exp"



import os
from dotenv import load_dotenv
import google.generativeai as generativeai

load_dotenv()


generativeai.configure(api_key=os.getenv('api_key'))
response = generativeai.GenerativeModel('gemini-2.0-flash-exp').generate_content('妳是誰 ?')
print(response.text)



as
fd
saf
sa
f
sa
f
assert