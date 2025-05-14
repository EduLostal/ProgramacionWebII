¿Qué ventajas ofrece GraphQL sobre REST en este contexto?

- La ventaja mas clara en este caso  es que con GraphQL puedes pedir solo lo que necesitas y nada más, en un REST generalmente consumes toda la información del endpoint aunque no la vayas a usar entera. Con GraphQL con una sola peticion eliges que datos quieres obtener lo que te hace ganar tiempo y eficiencia.

¿Cómo se definen los tipos y resolvers en una API con GraphQL?

- Los tipos se definen creando clases en GraphQL que indican que campos tienen los objetos que maneja la API, son como plantillas. Los resolvers son funciones normales que se encargan de conseguir esos datos, son como metodos que devuelven exactamente la informacion que pide cada consulta.

¿Por qué es importante que el backend también actualice disponible y no depender solo del frontend?

- Si solo actualizas la disponibilidad desde el frontend corres el riesgo de tener incosistencias. Un ejemplo práctico sería por ejemplo que varias apps distintas utilicen el backend y que cada cliente gestione eso por su cuenta. Eso haría aparecer errores  o diferentes estados de disponibilidad, por eso lo correcto sería que fuera el backend siempre el que controle esos datos.

¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?

- La forma mas directa de garantizarlo es que la lógica la controle el backend ya que cada vez que se hace una modificacion en el stock el backend automáticamente comprueba si el stock es 0 o mayor a 0 para actualizar el campo de "disponible". Asi siempre hay consistencia y no hay posibilidad de errores desde la aplicacion del cliente.