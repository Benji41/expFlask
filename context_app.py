#importo mi app de mi archivo
from hello import app
from flask import current_app
current_app.name
#asi se obtiene el contexto de la aplicacion
app_ctx = app.app_context()
#corro el contexto de la aplicacion haciendola activa y ya puedo usar la instancia de current_app 
app_ctx.push()
current_app.name
app_ctx.pop()
