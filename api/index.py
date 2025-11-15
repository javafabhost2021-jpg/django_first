from mangum import Mangum
from django.core.asgi import get_asgi_application

app = get_asgi_application()
handler = Mangum(app)
