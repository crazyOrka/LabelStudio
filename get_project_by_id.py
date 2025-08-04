from label_studio_sdk import LabelStudio

URL = "http://localhost:8080"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6ODA2MTUwMTIzNSwiaWF0IjoxNzU0MzAxMjM1LCJqdGkiOiIyOTc1NWI0NzllYTQ0YWE4OTg2MDkyY2NiMTNjMzcxNiIsInVzZXJfaWQiOiIxIn0.EdOZJh_9KvVn-O1APXzHjdPUjm18c5lQBNPXdefl3sg"

client = LabelStudio(
    api_key=API_KEY,
)

response = client.projects.get(id=1)

print(f"\nProjekttitel: {response.title}")
print(f"\nLabelkonfiguration: \n{response.label_config}")
print(f"\nErstellt am {response.created_at} von {response.created_by.email}")