#from mcp.server import MCPServer
from mcp.server.fastmcp import FastMCP

from products import products

mcp = FastMCP("RETAIL+")


@mcp.tool()
def buscar_producto(nombre: str) -> str:
    """
    Busca un producto en el catálogo de RETAIL+.
    """

    resultados = [
        producto
        for producto in products
        if nombre.lower() in producto["name"].lower()
    ]

    if not resultados:
        return f"No se encontró ningún producto con el nombre '{nombre}'."

    respuesta = []

    for producto in resultados:
        respuesta.append(
            f"ID: {producto['id']} | "
            f"Producto: {producto['name']} | "
            f"Categoría: {producto['category']} | "
            f"Precio: ${producto['price']:,} COP | "
            f"Stock: {producto['stock']}"
        )

    return "\n".join(respuesta)


@mcp.tool()
def consultar_stock(nombre: str) -> str:
    """
    Consulta la cantidad disponible de un producto.
    """

    for producto in products:
        if nombre.lower() in producto["name"].lower():
            return (
                f"El producto '{producto['name']}' "
                f"tiene {producto['stock']} unidades disponibles."
            )

    return f"No se encontró el producto '{nombre}'."


@mcp.tool()
def consultar_precio(nombre: str) -> str:
    """
    Consulta el precio actual de un producto.
    """

    for producto in products:
        if nombre.lower() in producto["name"].lower():
            return (
                f"El precio actual de '{producto['name']}' "
                f"es ${producto['price']:,} COP."
            )

    return f"No se encontró el producto '{nombre}'."


if __name__ == "__main__":
    mcp.run()
# pip install uv
# mcp dev server.py
# consultar_stock("iPhone 15")
# uv run --with "mcp[cli]" D:\code\retail_mcp\server.py

# uv run mcp dev server.py
# uv run --with mcp mcp run server.py